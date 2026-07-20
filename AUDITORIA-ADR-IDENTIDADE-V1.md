# AUDITORIA-ADR-IDENTIDADE-V1

**Data:** 2026-07-17
**Escopo:** conformidade do site institucional com os ADRs 006–011 (`templates-npm/docs/adr/`) e com a ban-list de linguagem do manual de voz (CLAUDE.md do templates-npm).
**Método:** varredura de todos os HTML públicos (exceto `legacy/` e `source-assets/`) e dos 3 CSS de `assets/css/`.
**Resultado:** 9 não-conformidades. Nenhum ADR de identidade está aplicado no site.

---

## NC-01 — Cor de marca sem lastro (ADR-006, crítico)

O marrom `#663C1F` é usado como `--accent` e documentado no código como "cor de marca NPM" — exatamente o defeito que motivou o ADR-006. A cor de marca oficial (navy `#1b2942` / blue `#284c72`) não aparece em nenhum arquivo do site.

- `assets/css/home.css:10` — `--accent: #663C1F; /* cor de marca NPM */`
- `assets/css/area-societario.css` e `assets/css/profissionais.css` — mesma definição
- Derivados: `--accent-soft` via `color-mix` nos 3 arquivos

**Correção:** substituir pela escala oficial do ADR-006 (via tokens, ver NC-03).

## NC-02 — Gradientes decorativos de fundo (ADR-006, crítico)

Fundos devem ser planos. Ocorrências:

- `home.css:31-32` — radial + linear gradient no `body`
- `home.css:118` — gradient decorativo em seção; `home.css:545` — shimmer
- `area-societario.css:26-27, 102, 382` — idem
- `profissionais.css:27-28` — idem

**Correção:** fundos planos com a escala de papel (`areia #e8dfd2` como chão; `ivory`/`panel`/`paper` para elevação).

## NC-03 — Paleta redefinida localmente, sem artefato de tokens (ADR-006 + ADR-008, crítico)

Cada CSS traz seu próprio `:root` com paleta em oklch sem correspondência com a escala oficial em hex. `aviso-de-cookies.html` e `politica-de-privacidade.html` têm `<style>` embutido com redefinições próprias. Não existe arquivo único de tokens no repo.

**Correção:** criar `assets/css/tokens.css` derivado do template system (fonte de verdade: `src/current/npm_template_system.html`), consumir por variável em todos os CSS/HTML e eliminar redefinições locais.

## NC-04 — Display tipográfico "de fábrica" (ADR-007, alto)

`.hero h1` (`home.css:136-144`): peso 300, tracking −0.018em, entrelinha 1.02, sem controle de eixo óptico.

Parâmetros vinculantes: peso ~360 (claro) / ~670 (ênfase), tracking −0.045 a −0.058em, entrelinha 0.96, opsz ~72. O mesmo vale para todos os displays das demais páginas.

## NC-05 — JetBrains Mono como peso morto (ADR-007, médio)

A família é carregada no `<head>` de 11 páginas (index, escritório, 9 de áreas) e tem **zero uso** nos CSS. Regra: mono só carrega se houver metadado factual na superfície. A correção natural converge com a NC-07: a linha de autuação passa a ser o uso legítimo da mono.

## NC-06 — Numeração decorativa 01–08 (ADR-010, alto)

Os cards de áreas do `index.html` são numerados `01`–`08` (`home.css:360 .area .num`) e os heros das páginas de área repetem o numeral (`area-societario.css:105 .page-hero .num`). Áreas de atuação não são sequência; a ordem não informa nada. Remover.

## NC-07 — Elemento-assinatura ausente; kicker redundante (ADR-010 + ADR-011, alto)

Nenhuma página exibe a linha de autuação. No lugar, o hero da home traz kicker "Novaes, Plantulli e Manzoli Advogados" — redundante com o logo no topbar (eyebrow que não nomeia categoria nova).

**Correção:** substituir kickers/numerações do bloco de título pela linha de autuação (JetBrains Mono, caixa alta, dado verificável da página + fecho "DESDE 1989", filete superior na cor `line`). Eyebrows de seção ("O escritório", "Áreas de atuação", "Profissionais") nomeiam categorias reais e podem permanecer; reavaliar "Destaques institucionais".

## NC-08 — Componente de preenchimento servido ao público (ADR-009, alto)

`<image-slot ... placeholder="Foto – arraste aqui">` está presente em **22 páginas** públicas, dependente de `assets/js/image-slot.js` (ferramenta de operador com estado em sidecar). Se o JS falhar, o público vê placeholder. As fotos reais já existem em `assets/img/`.

**Correção:** substituir todos os `<image-slot>` por `<img>` estáticos com as fotos reais; mover `image-slot.js` para tooling interno.

## NC-09 — Ban-list de linguagem (manual de voz, médio)

- `contencioso-civel.html:79` — "não apenas a tese, mas também..." (antítese-andaime)
- `contratual.html:79` — "não apenas como texto jurídico, mas como peça central..." (antítese-andaime; "peça central" tangencia "peça-chave")
- `escritorio.html:74` — "não só da prontidão..., mas também..." (antítese-andaime) e "altamente qualificados" (vocabulário banido)
- `index.html:80` — "altamente qualificados e personalizados" (vocabulário banido)

Sem violações OAB detectadas (nenhuma promessa de resultado, preço, superlativo comparativo ou autoatribuição de especialista).

---

## Ordem de correção sugerida

1. **Tokens + paleta + fundos planos** (NC-01, NC-02, NC-03) — cria a base; tudo o mais consome dela.
2. **Tipografia** (NC-04, NC-05) — parâmetros de display; mono condicionada à linha de autuação.
3. **Estrutura e assinatura** (NC-06, NC-07) — remover numeração/kicker, implantar linha de autuação em todas as páginas.
4. **Imagem** (NC-08) — `<img>` estáticos.
5. **Copy** (NC-09) — reescrita pontual das 4 ocorrências.

## Critério de encerramento

Auditoria de reverificação sem ocorrências: nenhum hex fora da escala oficial, nenhum `gradient` decorativo, displays nos parâmetros do ADR-007, mono apenas em metadado, linha de autuação em toda página pública, zero `<image-slot>` público, zero padrão de ban-list em texto público.
