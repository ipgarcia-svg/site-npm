# Novo Site NPM

Base ativa do novo site institucional de Novaes, Plantulli e Manzoli Advogados.

## Objetivo

Organizar, versionar e evoluir o site novo do escritório com uma estrutura clara de páginas, assets e governança, reduzindo drift editorial, visual e técnico.

## Estado Atual

O projeto já possui:

- home institucional
- primeira página de área
- página geral de profissionais
- primeira página individual de profissional
- páginas jurídicas mínimas
- roadmap executivo
- regras anti-drift
- escopo congelado da v1
- changelog

## Estrutura Principal

```text
index.html
escritorio.html
areas/
profissionais/
assets/
politica-de-privacidade.html
aviso-de-cookies.html
```

## Documentos de Gestão

- `ROADMAP-PROJETO-SITE.md`
- `REGRAS-ANTIDRIFT.md`
- `SPRINT-2-ESCOPO-V1.md`
- `MATRIZ-DE-CONTEUDO-V1.md`
- `CHANGELOG.md`
- `SITE-ESTRUTURA.md`

## Pastas Fora da Base Ativa

- `legacy/`: arquivos históricos preservados como referência
- `source-assets/`: materiais brutos, rascunhos e insumos locais

Essas pastas não fazem parte do núcleo versionado do site publicado.

## Como Visualizar

Como o projeto é estático nesta fase, basta abrir `index.html` localmente no navegador ou servir a pasta com um servidor estático simples.

## Convenções

- páginas de áreas ficam em `areas/`
- páginas de profissionais ficam em `profissionais/`
- CSS, JS e imagens ficam em `assets/`
- mudanças de escopo e governança devem respeitar `REGRAS-ANTIDRIFT.md`

## Próxima Sprint Recomendada

`Sprint 3 — Áreas de Atuação Completas`

Prioridades:

1. criar as demais páginas de áreas
2. criar `escritorio.html`
3. criar os perfis individuais restantes
4. revisar navegação e coerência interna
