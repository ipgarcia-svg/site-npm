# Roadmap Executável — Novo Site NPM

## Objetivo

Transformar a base atual do novo site NPM em um site institucional publicável, elegante, consistente e fácil de manter, preservando a direção editorial já definida e evoluindo a implementação para um padrão de produção.

## Estado Atual

### Base canônica já existente

- `index.html`
- `areas/societario.html`
- `areas/_template-area.html`
- `profissionais/index.html`
- `profissionais/luiz-novaes.html`
- `politica-de-privacidade.html`
- `aviso-de-cookies.html`

### Assets e estrutura já organizados

- `assets/css/home.css`
- `assets/css/area-societario.css`
- `assets/css/profissionais.css`
- `assets/js/site.js`
- `assets/js/image-slot.js`
- `assets/img/*.jpg`
- `assets/img/logo-npm.png`

### O que já está resolvido

- Direção visual principal definida
- Fotos dos sócios incorporadas
- Navegação básica entre páginas
- Separação inicial entre HTML, CSS e JS
- Estrutura editorial de home, área e equipe já estabelecida

### O que ainda falta

- Conteúdo institucional final
- Expansão das demais áreas
- Padronização de páginas internas
- Estrutura mais reaproveitável
- Revisão completa de UX, SEO e publicação

---

## Fase 1 — Definição Final do Escopo

### Objetivo

Congelar o escopo institucional e impedir retrabalho estrutural.

### Entregáveis

- mapa final do site
- lista definitiva de páginas
- definição do idioma inicial do site
- definição dos dados obrigatórios por página

### Estrutura sugerida

- Home
- Escritório
- Áreas de atuação
- 8 páginas de áreas
- Profissionais
- página individual por profissional
- Publicações
- página individual por publicação
- Contato
- Política de privacidade
- Aviso de cookies

### Critério de pronto

O projeto passa a ter um sitemap fixo e uma lista objetiva do que entra na primeira versão publicada.

---

## Fase 2 — Consolidação de Conteúdo

### Objetivo

Trocar textos provisórios e exemplos por conteúdo real e validado.

### Entregáveis

- texto institucional final do escritório
- descrição final das 8 áreas
- nomes, cargos, minibios e contatos oficiais
- publicações reais selecionadas
- dados jurídicos e institucionais obrigatórios

### Pacotes de conteúdo

#### Escritório

- história
- posicionamento
- diferenciais
- entidades e associações

#### Áreas

- resumo estratégico
- escopo de atuação
- exemplos de trabalhos
- profissionais relacionados

#### Profissionais

- nome completo
- cargo
- e-mail
- telefone
- formação
- associações
- idiomas
- áreas de atuação

### Critério de pronto

Nenhum bloco essencial do site depende mais de placeholder, texto genérico ou hipótese.

---

## Fase 3 — Organização Técnica de Produção

### Objetivo

Sair de páginas soltas e preparar uma estrutura sustentável.

### Entregáveis

- convenção definitiva de nomes de arquivos
- separação clara entre conteúdo, layout e comportamento
- estrutura reaproveitável para páginas internas

### Estrutura recomendada

```text
/index.html
/escritorio.html
/areas/
  societario.html
  tributario.html
  contratual.html
  arbitragem.html
  imobiliario.html
  patrimonial-sucessorio.html
  contencioso-civel.html
  familia-sucessoes.html
/profissionais/
  index.html
  luiz-novaes.html
  fabio-plantulli.html
  andre-manzoli.html
  thais-vilhena.html
  tathiana-fiuza.html
/publicacoes/
  index.html
/assets/
  /css
  /js
  /img
/docs/
  roadmap
  conteúdo
```

### Decisão técnica recomendada

#### Opção ideal

Migrar para `Astro`.

### Por quê

- mantém performance alta
- ótimo para site institucional
- facilita componentes e layouts
- facilita SEO
- permite crescer para publicações sem virar bagunça

### Critério de pronto

A base deixa de ser um conjunto de arquivos independentes e passa a seguir uma arquitetura clara de projeto.

---

## Fase 4 — Criação de Componentes

### Objetivo

Eliminar repetição estrutural e facilitar manutenção.

### Componentes prioritários

- header
- footer
- hero institucional
- hero de área
- breadcrumbs
- card de área
- card de profissional
- card de publicação
- bloco de CTA
- bloco de texto em duas colunas

### Entregáveis

- padrão visual consistente entre páginas
- redução de código repetido
- atualização centralizada de navegação e rodapé

### Critério de pronto

Header, footer e seções recorrentes não precisam mais ser editados página por página.

---

## Fase 5 — Expansão das Páginas

### Objetivo

Completar o site real com base no molde já validado.

### Entregáveis

- 8 páginas de áreas
- página geral de profissionais
- páginas individuais dos sócios
- páginas individuais dos advogados
- página geral de publicações

### Ordem de implementação recomendada

1. finalizar molde de área
2. duplicar e adaptar para as 8 áreas
3. finalizar molde de profissional
4. criar páginas individuais dos 5 sócios
5. criar páginas individuais dos demais profissionais
6. montar listagem de publicações

### Critério de pronto

O site deixa de ser demonstrativo e passa a ter corpo institucional completo.

---

## Fase 6 — Refinamento Premium

### Objetivo

Dar acabamento de escritório de alto nível.

### Ajustes prioritários

- reduzir blocos longos demais na home
- aumentar respiro entre seções estratégicas
- revisar recorte e padronização dos retratos
- tornar os estados de hover mais discretos
- reforçar consistência tipográfica
- ajustar ritmo vertical no mobile

### Itens de percepção premium

- menos ruído visual
- mais silêncio na composição
- melhor hierarquia entre títulos, texto e meta-informação
- imagens com tratamento consistente
- CTAs mais discretos e seguros

### Critério de pronto

O site transmite sobriedade, clareza e precisão sem parecer template genérico.

---

## Fase 7 — SEO, Performance e Confiabilidade

### Objetivo

Preparar a publicação com qualidade técnica.

### Entregáveis

- title e meta description por página
- Open Graph
- favicon
- sitemap
- URLs limpas
- headings consistentes
- alt text em imagens
- revisão de links
- compressão de imagens

### Critério de pronto

O site pode ser publicado sem pendências básicas de indexação e apresentação.

---

## Fase 8 — Jurídico e Publicação

### Objetivo

Fechar conformidade mínima e subir a primeira versão.

### Entregáveis

- política de privacidade final
- aviso de cookies final
- revisão de dados institucionais
- domínio e SSL
- analytics, se aprovado
- ambiente de hospedagem

### Critério de pronto

O site está apto para publicação pública.

---

## Ordem de Execução Recomendada

### Sprint 1

- fechar sitemap
- fechar conteúdo institucional essencial
- validar lista completa de áreas e profissionais

### Sprint 2

- reorganizar estrutura técnica
- criar componentes
- definir modelo final das páginas internas

### Sprint 3

- criar as 8 páginas de áreas
- consolidar página de profissionais
- criar páginas individuais dos sócios

### Sprint 4

- criar páginas individuais restantes
- estruturar publicações
- revisar links, rodapé e navegação

### Sprint 5

- polish visual
- revisão mobile
- SEO
- páginas jurídicas finais

### Sprint 6

- testes finais
- publicação

---

## Backlog Prioritário Imediato

### Próximas tarefas práticas

1. mover `assets/home.css`, `assets/area-societario.css` e `assets/profissionais.css` para subpastas como `assets/css`
2. mover `assets/site.js` para `assets/js`
3. mover imagens para `assets/img`
4. criar estrutura `/areas` e `/profissionais`
5. transformar `area-societario.html` em template-base
6. criar primeira página individual de sócio
7. revisar a home para reduzir placeholders de publicações

---

## Recomendação Estratégica

Se a ideia é publicar com qualidade e continuar evoluindo sem retrabalho, a próxima etapa ideal não é “mais design solto”. É:

1. consolidar a estrutura técnica
2. padronizar os componentes
3. expandir as páginas reais

Essa é a virada de mockup institucional para produto web publicável.
