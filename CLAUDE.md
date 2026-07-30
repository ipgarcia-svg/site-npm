# CLAUDE.md — Manual do site NPM (para LLMs)

Este repositório é o site institucional estático do Novaes, Plantulli e
Manzoli (npmadvogados.com.br), hospedado no Netlify. **Leia primeiro o
manual de voz**: `templates-npm/CLAUDE.md` — tom, ban-list de linguagem e
ética OAB valem aqui integralmente. Este overlay soma as regras próprias do
site. Em conflito, os ADRs do `templates-npm` (docs/adr/) prevalecem.

## 1. Identidade visual (ADR-006/007/008)

- **Tokens**: `assets/css/tokens.css` é a única origem de cor, família e
  parâmetro de display. Nunca escreva hex ou família fora dele; consumo
  sempre por `var()`. Divergência local é defeito.
- **Paleta**: tinta `--ink`, marca navy `--accent`/`--blue`, superfícies de
  papel `--paper → --ivory-3`, linhas `--rule`. Acento quente e gradiente
  decorativo são proibidos.
- **Tipografia**: Newsreader display com os parâmetros do sistema (peso
  ~360/~670, tracking −0.045em, entrelinha 0.96); Hanken no texto;
  JetBrains Mono **só** em metadado factual curto (OAB, data, endereço,
  protocolo) — nunca em prosa, título ou CTA.
- Componentes de identidade vivem em `assets/css/identidade.css`.

## 2. Linha de autuação (ADR-011 — elemento-assinatura)

Régua única em mono, caps, sobre filete, imediatamente acima do h1
(`<div class="autuacao">`). Regras duras:

- Conteúdo = dados verificáveis da própria página, separados por `·`,
  fecho constante `DESDE 1989`.
- Sem dado próprio verificável, a página fica **sem** linha; linha só com o
  fecho é proibida. Nunca prosa, slogan ou qualificação.
- A linha substitui marcadores decorativos; não coexiste com numeração
  ornamental, monograma repetido ou eyebrow redundante (ADR-010).

## 3. Registro por tipo de página

- **Área de atuação**: lead abre com o recorte e a operação do cliente,
  fecha com consequência objetiva quando houver. CTA final é **descrição
  sóbria dos serviços reais da área** — nunca pergunta interpelativa
  dirigida a problema atual do leitor (risco de captação; em contencioso,
  indução à litigiosidade).
- **Perfil de profissional**: abre com a pessoa (foto real + fato
  biográfico verificável). Credencial sempre checável: entidade, comissão,
  período.
- **Institucional (escritório/index)**: abre com história e fatos (1989,
  condução pelos sócios, participações institucionais nomeadas).
- Imagens: somente fotografia própria (ADR-009). Imagem gerada por IA é
  proibida sem exceção; sem foto adequada, layout tipográfico — nunca
  placeholder.

## 4. Preflight (obrigatório antes de qualquer commit)

```bash
python3 scripts/preflight.py
```

- Exit ≠ 0 bloqueia o commit. Nenhum PR mergeia fazendo o preflight
  regredir em relação à sua base.
- Não há tolerância genérica vigente. Exceções pontuais de `F4`, já aprovadas
  pela regra do ADR-010, ficam justificadas dentro do próprio preflight.
- W6 (triagem ética) é apoio mecânico; a revisão final de copy é sempre pela
  régua do `06_agente_revisor_etico_oab` do templates-npm, com registro
  componente → risco → norma no PR.

## 5. Fluxo de trabalho

- Roadmap vigente: `ROADMAP-ANTI-IA.md` (fases, evidências, aceites).
  1 fase = 1 PR; PRs empilham na ordem declarada na fila.
- Branch por entrega; commits em português, verbo no infinitivo, prefixo
  semântico (`feat:`, `fix:`, `docs:`), sem Co-Authored-By.
- PR sempre com seção **"A confirmar"** para fato sem lastro ou decisão
  pendente dos sócios — nunca invente dado para fechar pendência.
- Copy público novo ou alterado exige aprovação humana registrada no PR
  (regra transversal 5 do roadmap).
- Dados sensíveis a confirmar com os sócios antes de alterar: e-mail e
  telefone oficiais (produção e repo divergem).

## 6. Estrutura do repositório

- Páginas na raiz, `areas/` e `profissionais/`; `_template-area.html` é
  molde interno (não servido, excluído do preflight).
- `_redirects` guarda o mapa 301 da migração Wix — slugs antigos são
  fatos conferidos em produção; não altere sem verificar.
- `sitemap.xml` e `CHANGELOG.md` acompanham toda mudança de páginas.
