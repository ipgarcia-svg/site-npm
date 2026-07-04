#!/usr/bin/env python3
"""Pre-flight do site NPM.

Audita as páginas públicas contra as regras mecanizáveis do
ROADMAP-ANTI-IA e dos ADRs de identidade do templates-npm
(ADR-006/007/008/010/011).

Uso:  python3 scripts/preflight.py [--tolerar F4,F5]
Saída: relatório por página; exit code = nº de categorias com FALHA
       (categorias toleradas são rebaixadas a AVISO no exit code,
       para débito conhecido de fase ainda não executada).
"""

import glob
import html
import math
import os
import re
import sys
from collections import defaultdict

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ARQUIVOS_TOKENS = {"assets/css/tokens.css", "assets/css/identidade.css"}
FECHO_AUTUACAO = "DESDE 1989"
INTENCAO_CONTATO = re.compile(
    r"discutir uma demanda|fale conosco|entre em contato|agende|converse|"
    r"contate|vamos conversar", re.I)

falhas = defaultdict(list)   # código -> [mensagens]
avisos = defaultdict(list)


def paginas_publicas():
    pgs = []
    for pad in ("*.html", "areas/*.html", "profissionais/*.html"):
        pgs += glob.glob(os.path.join(RAIZ, pad))
    return sorted(p for p in pgs if "_template" not in p)


def rel(p):
    return os.path.relpath(p, RAIZ)


def texto_visivel(fonte_html):
    s = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", fonte_html, flags=re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    return html.unescape(re.sub(r"\s+", " ", s))


def main():
    pgs = paginas_publicas()

    # ── F1: componente de mockup servido ao público (roadmap 0.1 / ADR-009)
    for p in pgs:
        s = open(p, encoding="utf-8").read()
        if "<image-slot" in s or "image-slot.js" in s:
            falhas["F1"].append(rel(p))
    if os.path.exists(os.path.join(RAIZ, "assets/js/image-slot.js")):
        falhas["F1"].append("assets/js/image-slot.js existe no repositório")

    # ── F2: toggle PT/EN sem versão EN (roadmap 0.2)
    tem_en = os.path.isdir(os.path.join(RAIZ, "en"))
    if not tem_en:
        for p in pgs:
            s = open(p, encoding="utf-8").read()
            if re.search(r">\s*EN\s*<", s) and 'class="lang"' in s:
                falhas["F2"].append(rel(p))

    # ── F3: hex fora dos arquivos de tokens (ADR-006/008)
    for css in glob.glob(os.path.join(RAIZ, "assets/css/*.css")):
        if rel(css) in ARQUIVOS_TOKENS:
            continue
        for i, ln in enumerate(open(css, encoding="utf-8"), 1):
            for hx in re.findall(r"#[0-9a-fA-F]{3,8}\b", ln):
                falhas["F3"].append(f"{rel(css)}:{i} {hx}")
    for p in pgs:
        s = open(p, encoding="utf-8").read()
        for hx in re.findall(r'style="[^"]*(#[0-9a-fA-F]{3,8})', s):
            falhas["F3"].append(f"{rel(p)} style inline {hx}")

    # ── F4: cota de eyebrows/labels por página (roadmap 2.2)
    # Nota: "section-label"/"group-label" é o bloco visual; "eyebrow" é o
    # span interno do mesmo bloco — contar os dois somaria a mesma
    # instância duas vezes.
    EXCECOES_F4 = {
        "index.html": (
            "4 blocos de conteúdo genuinamente distintos na página única "
            "(institucional, áreas, pessoas, publicações); eyebrow nomeia "
            "a categoria e o h2 é uma tese editorial própria — não "
            "redundantes entre si (teste do ADR-010 aplicado, aprovado)."
        ),
        "profissionais/index.html": (
            "2 grupos de pessoas sem heading próprio (Sócios / Sócias e "
            "equipe); o eyebrow é a única forma de distinguir quem é "
            "sócio na grade — removê-lo apagaria informação, não "
            "decoração (teste do ADR-010 aplicado, aprovado)."
        ),
    }
    for p in pgs:
        s = open(p, encoding="utf-8").read()
        secoes = max(1, len(re.findall(r"<section\b", s)))
        rotulos = len(re.findall(
            r'class="(?:section|group)-label"', s))
        rotulos += len(re.findall(
            r'class="label"(?![^>]*(?:section|group)-label)', s))
        teto = math.ceil(secoes / 3)
        if rotulos > teto and rel(p) not in EXCECOES_F4:
            falhas["F4"].append(f"{rel(p)}: {rotulos} rótulos / teto {teto} "
                                f"({secoes} seções)")
        elif rotulos > teto:
            avisos["F4-exceção"] = avisos.get("F4-exceção", [])
            avisos["F4-exceção"].append(
                f"{rel(p)}: {rotulos}/{teto} — {EXCECOES_F4[rel(p)]}")

    # ── F5: mais de um rótulo para a mesma intenção de CTA (roadmap 1.4)
    for p in pgs:
        s = open(p, encoding="utf-8").read()
        textos = re.findall(r"<a[^>]*>(.*?)</a>|<button[^>]*>(.*?)</button>",
                            s, re.S)
        rotulos = set()
        for a, b in textos:
            t = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", a or b)).strip()
            if t and INTENCAO_CONTATO.search(t):
                rotulos.add(t.lower())
        if len(rotulos) > 1:
            falhas["F5"].append(f"{rel(p)}: {sorted(rotulos)}")

    # ── F6: autuação/decoração nos blocos de título (ADR-010/011)
    for p in pgs:
        s = open(p, encoding="utf-8").read()
        for m in re.findall(r'<div class="autuacao">(.*?)</div>', s, re.S):
            conteudo = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", m)).strip()
            if conteudo.upper().replace("·", "").strip() == FECHO_AUTUACAO:
                falhas["F6"].append(f"{rel(p)}: linha só com o fecho constante")
        if re.search(r'class="num"', s):
            falhas["F6"].append(f"{rel(p)}: marcador decorativo 'num' remanescente")
        if re.search(r'class="number">[ivx]+<', s):
            falhas["F6"].append(f"{rel(p)}: numeral romano decorativo remanescente")

    # ── W1: ban-list de copy (roadmap Fase 1 / 12_fonte)
    pad_banlist = [
        (r"\baltamente\b", "adjetivo de intensidade"),
        (r"não (?:é|são|se trata)\b[^.]{5,80}\bmas\b", "andaime de antítese"),
        (r"\bexcelência\b", "vocabulário-clichê"),
        (r"soluções (?:personalizadas|sob medida|jurídicas)", "vocabulário-clichê"),
        (r"—", "travessão longo (usar –)"),
    ]
    for p in pgs:
        txt = texto_visivel(open(p, encoding="utf-8").read())
        for rx, nome in pad_banlist:
            for m in re.finditer(rx, txt, re.I):
                trecho = txt[max(0, m.start() - 20):m.end() + 20].strip()
                avisos["W1"].append(f"{rel(p)}: [{nome}] …{trecho}…")

    # ── W2: placeholder sem label associado (roadmap 4.1)
    for p in pgs:
        s = open(p, encoding="utf-8").read()
        for m in re.finditer(r"<input[^>]*placeholder=", s):
            tag = m.group(0)
            mid = re.search(r'id="([^"]+)"', tag)
            if not (mid and f'for="{mid.group(1)}"' in s):
                avisos["W2"].append(f"{rel(p)}: {tag[:70]}…")

    # ── W3: alt vazio/genérico em imagem significativa (roadmap 4.4)
    for p in pgs:
        s = open(p, encoding="utf-8").read()
        for m in re.finditer(r"<img\b[^>]*>", s):
            tag = m.group(0)
            malt = re.search(r'alt="([^"]*)"', tag)
            alt = (malt.group(1).strip().lower() if malt else None)
            if alt is None or alt in {"", "imagem", "foto", "image", "logo"}:
                avisos["W3"].append(f"{rel(p)}: {tag[:70]}…")

    # ── W4: higiene — z-index arbitrário, JS órfão, motion sem reduced-motion
    for css in glob.glob(os.path.join(RAIZ, "assets/css/*.css")):
        conteudo = open(css, encoding="utf-8").read()
        for z in re.findall(r"z-index:\s*(\d{3,})", conteudo):
            if int(z) >= 999:
                avisos["W4"].append(f"{rel(css)}: z-index {z}")
        if re.search(r"\b(transition|animation)\s*:", conteudo) and \
                "prefers-reduced-motion" not in conteudo:
            avisos["W4"].append(f"{rel(css)}: transição/animação sem "
                                "prefers-reduced-motion")
    for p in pgs:
        s = open(p, encoding="utf-8").read()
        for src in re.findall(r'<script[^>]*src="([^"]+)"', s):
            alvo = os.path.normpath(os.path.join(os.path.dirname(p), src))
            if not src.startswith("http") and not os.path.exists(alvo):
                avisos["W4"].append(f"{rel(p)}: script órfão {src}")

    # ── W5: title/meta description/og ausentes (roadmap 4.3)
    for p in pgs:
        s = open(p, encoding="utf-8").read()
        faltas = [t for t, rx in [
            ("title", r"<title>[^<]+</title>"),
            ("meta description", r'<meta name="description"'),
            ("og:title", r'property="og:title"'),
        ] if not re.search(rx, s)]
        if faltas:
            avisos["W5"].append(f"{rel(p)}: falta {', '.join(faltas)}")

    # ── W6: triagem de risco ético OAB (Prov. 205/2021) — padrões estreitos
    rx_etica = [
        (r"custos?\s+competitiv", "apelo de preço (mercantilização)"),
        (r"resultados?\s+(tang[íi]ve|comprovad|garantid)", "promessa de resultado"),
        (r"garantimos|[êe]xito\s+garantido|sucesso\s+garantido", "promessa de resultado"),
        (r"consulta\s+gratuita|sem\s+custo|or[çc]amento", "mercantilização"),
        (r"especialistas?\s+em|contencioso\s+especializado", "título de especialista sem lastro"),
        (r"melhor\s+(desfecho|resultado)|l[íi]der(es)?\s+(de|em|no)", "superlativo/comparação"),
        (r"agora\s+mesmo|n[ãa]o\s+perca|[úu]ltima\s+chance", "urgência/pressão"),
    ]
    for p in pgs:
        t = texto_visivel(open(p, encoding="utf-8").read())
        for rx, nome in rx_etica:
            for m in re.finditer(rx, t, re.I):
                trecho = t[max(0, m.start() - 25):m.end() + 25].strip()
                avisos["W6"].append(f"{rel(p)}: [{nome}] …{trecho}…")

    # ── Relatório
    print(f"Pre-flight — {len(pgs)} páginas públicas auditadas\n")
    nomes = {
        "F1": "componente de mockup em produção (0.1/ADR-009)",
        "F2": "toggle PT/EN sem versão EN (0.2)",
        "F3": "hex fora dos tokens (ADR-006/008)",
        "F4": "cota de eyebrows estourada (2.2)",
        "F5": "rótulos múltiplos para a mesma intenção de CTA (1.4)",
        "F6": "autuação/decoração irregular (ADR-010/011)",
        "W1": "ban-list de copy (Fase 1)",
        "W2": "placeholder sem label (4.1)",
        "W3": "alt vazio ou genérico em imagem significativa (4.4)",
        "W4": "higiene: z-index/JS órfão/motion sem reduced-motion (4.3/4.4)",
        "W5": "title/meta description/og ausentes (4.3)",
        "W6": "risco ético OAB no copy (Prov. 205/2021; revisar pelo 06_fonte)",
    }
    for cod in sorted(nomes):
        itens = falhas.get(cod) if cod.startswith("F") else avisos.get(cod)
        if not itens:
            if cod.startswith("F"):
                print(f"  OK    {cod}  {nomes[cod]}")
            continue
        rot = "FALHA" if cod.startswith("F") else "AVISO"
        print(f"  {rot} {cod}  {nomes[cod]} — {len(itens)} ocorrência(s)")
        for it in itens[:8]:
            print(f"          · {it}")
        if len(itens) > 8:
            print(f"          · … e mais {len(itens) - 8}")

    if avisos.get("F4-exceção"):
        print("  NOTA  F4  exceção documentada (ADR-010 aplicado, aprovado):")
        for it in avisos["F4-exceção"]:
            print(f"          · {it}")

    tolerar = set()
    for i, a in enumerate(sys.argv):
        if a == "--tolerar" and i + 1 < len(sys.argv):
            tolerar = set(x.strip() for x in sys.argv[i + 1].split(","))
    if tolerar & set(falhas):
        print(f"\nToleradas nesta execução (débito de fase): "
              f"{sorted(tolerar & set(falhas))}")
    n_falhas = len(set(falhas) - tolerar)
    print(f"\nResultado: {n_falhas} categoria(s) com FALHA, "
          f"{sum(len(v) for v in avisos.values())} aviso(s).")
    sys.exit(n_falhas)


if __name__ == "__main__":
    main()
