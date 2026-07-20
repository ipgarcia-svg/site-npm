# Roadmap Executivo – Novo Site NPM

## Objetivo

Transformar a base atual do novo site NPM em um site institucional publicável, elegante, consistente e sustentável, com direção editorial clara, expansão controlada e baixo risco de drift visual, técnico ou de conteúdo.

## Princípios do Projeto

- o site novo deve evoluir a partir da base oficial já publicada no repositório
- o escopo da v1 deve ser suficiente para publicação, sem inflar páginas por ansiedade de completude
- conteúdo institucional deve ser sóbrio, verificável e compatível com o perfil de um escritório de advocacia
- novos elementos só entram se melhorarem clareza, navegação ou consistência institucional
- toda expansão deve respeitar as regras de governança do projeto

## Base Oficial Atual

### Páginas já consolidadas

- `index.html`
- `areas/societario.html`
- `areas/_template-area.html`
- `profissionais/index.html`
- `profissionais/luiz-novaes.html`
- `politica-de-privacidade.html`
- `aviso-de-cookies.html`

### Estrutura técnica já consolidada

- `assets/css/home.css`
- `assets/css/area-societario.css`
- `assets/css/profissionais.css`
- `assets/js/site.js`
- `assets/js/image-slot.js`
- `assets/img/*`

### Estado atual

- repositório Git criado e publicado
- branch principal: `main`
- raiz do projeto limpa
- legado separado da base ativa
- materiais brutos fora do núcleo versionado

## Regras de Governança

As regras para evitar drift estão consolidadas em:

- `REGRAS-ANTIDRIFT.md`
- `CHECKLIST-ETICO-COPY.md`

Esses documentos devem ser tratados como referência obrigatória para decisões de conteúdo, estrutura, estilo, copy institucional e versionamento.

---

## Sprint 1 – Base Oficial e Governança

### Objetivo

Fechar a base canônica do projeto, estruturar o repositório corretamente e estabelecer regras para impedir retrabalho.

### Escopo

- definir a base oficial do site novo
- organizar assets, áreas e profissionais
- separar legado e materiais de apoio
- publicar o projeto no Git
- criar regras anti-drift

### Entregáveis

- repositório publicado
- base de páginas oficial
- `.gitignore` funcional
- estrutura limpa de projeto
- regra de governança do site

### Status

`Concluído`

---

## Sprint 2 – Escopo Final e Conteúdo-Matriz

### Objetivo

Congelar o escopo institucional da v1 e consolidar o conteúdo-base que alimentará as páginas reais.

### Escopo

- validar o sitemap da v1
- decidir o que fica na home e o que vai para páginas internas
- consolidar o texto institucional do escritório
- fechar a lista definitiva de áreas
- fechar a lista definitiva de profissionais da v1
- definir os blocos obrigatórios por página

### Entregáveis

- sitemap validado
- matriz de conteúdo institucional
- lista final de páginas da v1
- regra clara de distribuição de conteúdo entre home, escritório, áreas e perfis

### Critério de pronto

- nenhuma página essencial depende mais de hipótese estrutural
- fica decidido o que entra agora e o que vai para backlog

### Status

`Concluído`

---

## Sprint 3 – Áreas de Atuação Completas

### Objetivo

Transformar o template validado em um conjunto completo de páginas de áreas.

### Escopo

- finalizar o molde editorial das páginas de área
- criar as demais páginas de áreas de atuação
- revisar consistência entre títulos, serviços, equipe associada e CTA
- padronizar nomenclatura, URLs e estrutura interna

### Entregáveis

- `areas/tributario.html`
- `areas/contratual.html`
- `areas/arbitragem.html`
- `areas/imobiliario.html`
- `areas/patrimonial-sucessorio.html`
- `areas/contencioso-civel.html`
- `areas/familia-sucessoes.html`

### Critério de pronto

- todas as áreas da v1 existem e seguem o mesmo padrão estrutural
- nenhuma área depende de texto genérico ou placeholder evidente

### Status

`Em execução`

---

## Sprint 4 – Equipe Completa

### Objetivo

Dar corpo institucional à página de equipe e aos perfis individuais.

### Escopo

- padronizar bios curtas, médias e longas
- criar páginas individuais para os sócios restantes
- criar páginas individuais para os demais advogados da v1
- revisar cargos, idiomas, áreas e associações
- revisar consistência entre perfis e páginas de área

### Entregáveis

- páginas individuais completas dos sócios
- páginas individuais dos demais profissionais aprovados para a v1
- padronização editorial da seção de equipe

### Critério de pronto

- a equipe deixa de ser apenas uma listagem e passa a funcionar como ativo institucional

---

## Sprint 5 – Escritório, Posicionamento e Publicações

### Objetivo

Expandir a camada institucional do site sem inflar a home.

### Escopo

- criar a página `escritorio.html`
- redistribuir corretamente história, posicionamento, diferenciais e entidades
- estruturar a área de publicações
- criar a página geral de publicações
- definir o molde de página individual de publicação

### Entregáveis

- `escritorio.html`
- `publicacoes/index.html`
- modelo de publicação institucional
- home revisada com menos densidade e mais hierarquia

### Critério de pronto

- a home deixa de carregar tudo sozinha
- o site passa a ter camada institucional e camada editorial distintas

---

## Sprint 6 – Componentização e Arquitetura Sustentável

### Objetivo

Reduzir repetição estrutural e preparar o projeto para crescer sem bagunça.

### Escopo

- decidir se a base HTML permanece estática nesta fase ou migra para framework
- consolidar componentes recorrentes
- centralizar header, footer, breadcrumbs, CTA e blocos repetidos
- revisar convenção de arquivos

### Decisão técnica recomendada

Se a expansão do site se confirmar, a migração para `Astro` passa a ser recomendada nesta sprint, e não antes.

### Entregáveis

- arquitetura definida para continuidade
- redução de repetição de markup
- plano de manutenção mais seguro

### Critério de pronto

- atualizações recorrentes deixam de exigir edição manual em múltiplas páginas

---

## Sprint 7 – Refinamento Premium, SEO e Publicação

### Objetivo

Fechar a v1 com acabamento de escritório de alto nível e padrão mínimo de publicação.

### Escopo

- refinar hierarquia visual
- revisar mobile e ritmo vertical
- suavizar hover e microinterações
- fechar titles, descriptions e headings
- revisar alt text, links, favicon e sitemap
- validar páginas jurídicas
- preparar hospedagem e publicação

### Entregáveis

- site refinado visualmente
- checklist de SEO básico concluído
- checklist jurídico concluído
- site apto para deploy

### Critério de pronto

- o site pode ser publicado sem pendências centrais de conteúdo, estrutura, UX ou conformidade básica

---

## Sitemap Proposto da V1

- `index.html`
- `escritorio.html`
- `areas/`
- `profissionais/index.html`
- páginas individuais de profissionais
- `publicacoes/index.html`
- páginas individuais de publicações
- `politica-de-privacidade.html`
- `aviso-de-cookies.html`

## Backlog Pós-V1

- versão em inglês
- filtros ou taxonomia de publicações
- analytics e eventos
- melhorias de performance avançadas
- automação editorial
- migração completa para arquitetura componentizada

## Critério de Gestão do Projeto

Este roadmap deve ser usado para priorização. Qualquer mudança relevante de escopo, estrutura, posicionamento ou linguagem deve ser validada contra:

- `SITE-ESTRUTURA.md`
- `REGRAS-ANTIDRIFT.md`
- base oficial já publicada no repositório

## Próxima Ação Recomendada

Executar a `Sprint 3 – Áreas de Atuação Completas` até fechar todas as páginas de área previstas na v1. Em seguida, avançar diretamente para a `Sprint 4 – Equipe Completa`.
