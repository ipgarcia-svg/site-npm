# Proposta de modernização — rationale

**Protótipo completo:** abrir `proposta-redesign/index.html` no navegador — o
site inteiro navega: home, escritório, 8 áreas, 8 perfis + índice, políticas
e 404, todos consumindo `assets/proposta.css` (artefato único de tokens,
conforme ADR-008). `home.html` e `home-tonal.html` são as variantes
intermediárias apresentadas durante a exploração, mantidas como registro.
A variante aprovada (tonal) é a base de tudo.
**Base normativa:** ADRs 006–011 (`templates-npm/docs/adr/`) + manual de voz NPM
**Auditoria que motivou:** `AUDITORIA-ADR-IDENTIDADE-V1.md`

## A tese

O site como **autos bem organizados**: capa formal em navy, miolo em folhas
de papel sobre chão areia. A metáfora vem da cultura material do ofício
(capa de processo, autuação, sumário) — não de tendência visual. É o
caminho apontado pelo ADR-011 levado à estrutura da página inteira.

## O que muda em relação ao site atual

1. **Cor.** O marrom `#663C1F` (sem lastro no logotipo) sai; entra a paleta
   oficial do ADR-006 com navy `#1b2942` como cor de marca. Fundos planos,
   sem gradientes.
2. **Capa em navy.** O hero deixa de ser "landing page clara com headline"
   e vira capa de autos: linha de autuação, título display e ficha com três
   dados verificáveis (fundação, atuação, sede). Impacto de apresentação
   com lastro factual.
3. **Áreas como sumário, não cards.** A numeração decorativa 01–08 sai.
   As oito áreas viram índice em três naturezas reais — Empresarial,
   Patrimonial e família, Resolução de disputas — com pesos desiguais
   (4/2/2). Agrupamento é informação; grid simétrico era decoração.
4. **Display sans, alinhado aos tokens do template system.** O protótipo
   usa Hanken Grotesk 670, tracking −0.058em, entrelinha 0.96 — os valores
   exatos do `--display` em `src/current/npm_template_system.html`. A serifa
   editorial com itálico de ênfase foi descartada também por coincidir com
   a estética corrente de material gerado. Nota: o ADR-007 ainda descreve a
   Newsreader como voz de display; se esta direção for aprovada, o ADR deve
   ser revisado para refletir os tokens vigentes. JetBrains Mono permanece
   só onde há dado factual: linha de autuação, ficha da capa, endereço.
5. **Fotografia real no lugar de image-slot.** `<img>` estáticos com as
   fotos existentes do escritório e da equipe (ADR-009). A foto do
   escritório comanda a dobra "O escritório", com legenda de endereço real.
6. **Copy conforme.** Sai "altamente qualificados e personalizados" e as
   antíteses-andaime; entram fatos: 1989, condução direta, oito áreas,
   entidades nomeadas. Sem promessa, preço, superlativo ou interpelação
   (Provimento CFOAB 205/2021).

## O que fica `a confirmar`

- Número de inscrição da sociedade na OAB/SP (para eventual uso na linha de
  autuação do rodapé ou da página Escritório).
- Papéis formais de cada profissional (sócio/associado) — o protótipo
  lista apenas nomes para não afirmar o não confirmado.
- Foto do escritório em resolução final e direitos de uso confirmados.

## Se aprovado

Propagar a linguagem do protótipo às demais páginas (escritório, 8 áreas,
8 perfis, políticas) consumindo um `assets/css/tokens.css` único, conforme
ADR-008, e registrar a decisão de layout em ADR próprio no `templates-npm`.
