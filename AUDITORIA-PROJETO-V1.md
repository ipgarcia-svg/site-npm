# Auditoria do Projeto – V1

## Referência Externa Usada

Esta revisão considera, como base externa de comparação:

- a documentação do GitHub Pages, que confirma a prática comum de publicar sites diretamente a partir de um repositório Git com `README` e deploy a partir de branch
- o padrão `Keep a Changelog`, que reforça a utilidade de manter um histórico legível das mudanças relevantes do projeto

Fontes:

- [GitHub Pages Quickstart](https://docs.github.com/en/pages/quickstart)
- [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/)

## Leitura Executiva

O projeto já está com cara de base oficial de site: possui repositório publicado, estrutura ativa separada do legado, documentos de governança, home, página institucional, páginas jurídicas, seção de profissionais e páginas de área iniciadas.

O que falta agora não é reorganizar tudo de novo. O que falta é concluir a camada publicável da v1 com disciplina: completar páginas essenciais, fechar a navegação real, eliminar links provisórios e adicionar os artefatos técnicos mínimos de publicação.

## O Que Já Está Certo

- repositório Git publicado e com histórico já iniciado
- `README.md` e `CHANGELOG.md` presentes
- estrutura principal simples e compatível com site estático
- ativos organizados em `assets/css`, `assets/js` e `assets/img`
- separação entre base ativa, legado e materiais brutos
- documento de roadmap
- regras anti-drift
- escopo v1 e matriz de conteúdo já definidos
- home, `escritorio.html`, `profissionais/index.html` e documentos jurídicos mínimos já existentes

## Estrutura Comum de Repositórios de Sites

Em repositórios institucionais simples, a estrutura mais comum é:

- páginas HTML na raiz e em subpastas temáticas
- `assets/` para CSS, JS, imagens e ícones
- `README.md` para onboarding e visão do projeto
- `CHANGELOG.md` para histórico
- arquivos técnicos de publicação na raiz, como `robots.txt`, `sitemap.xml`, `404.html` e eventualmente `CNAME`

Por inferência técnica, a base atual da NPM já conversa bem com esse padrão. O principal gap está menos na forma do repositório e mais na conclusão do conteúdo e dos artefatos de deploy.

## O Que Ainda Falta Para a V1

### Crítico

- criar as páginas restantes de áreas previstas no escopo v1
- criar os perfis individuais restantes dos profissionais previstos
- substituir links da home que ainda apontam para páginas genéricas ou provisórias
- revisar coerência entre áreas, equipe associada e CTAs

### Importante

- adicionar `meta description` real em cada página
- definir metadados de compartilhamento social (`og:title`, `og:description`, `og:image`)
- preparar favicon
- criar `robots.txt`
- criar `sitemap.xml` quando o domínio final estiver definido
- revisar `h1`, títulos e consistência de nomenclatura
- revisar mobile com foco em ritmo vertical, cards e blocos de equipe

### Recomendado

- criar `404.html`
- definir imagem institucional padrão para compartilhamento
- revisar alt text e acessibilidade básica
- fazer auditoria final de links internos
- padronizar melhor as microcopies de CTA

## O Que Está Parcial

- `Sprint 2`: a governança e a matriz já existem, mas a tradução completa disso em todas as páginas da v1 ainda está em curso
- `Sprint 3`: já começou com `societario.html`, `tributario.html` e `contratual.html`, mas ainda não fechou o conjunto completo
- `Sprint 4`: a listagem de profissionais está forte, mas os perfis individuais ainda estão incompletos

## O Que Não Falta Para Publicar a Primeira Versão

Itens abaixo são valiosos, mas não precisam travar a publicação da v1:

- migração para `Astro`
- área formal de publicações
- versão em inglês
- filtros, taxonomias ou busca interna
- analytics avançado
- automação editorial

## Dependências de Decisão

Alguns itens dependem de decisão externa antes de fechamento técnico:

- domínio final do site
- forma de hospedagem
- eventual uso de GitHub Pages ou outro provedor
- imagem institucional principal para Open Graph

## Próxima Frente Recomendada

A melhor sequência, a partir daqui, é:

1. concluir todas as páginas de áreas da v1
2. concluir todos os perfis individuais da v1
3. revisar navegação interna e links provisórios
4. adicionar a camada técnica mínima de publicação
5. fazer uma rodada final de refinamento visual premium
