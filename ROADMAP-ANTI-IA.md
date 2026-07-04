# ROADMAP – Descaracterização de "site gerado por IA" – V1.2

Objetivo: eliminar do site público todos os sinais — de texto, design, estrutura e
tooling — que o identificam como produção assistida por IA ou template genérico.
Régua editorial de referência: `templates-npm/12_fonte_aberturas_e_linguagem_npm.md`
(ban-list de andaimes de antítese, tríades decorativas, pontuação de efeito e
vocabulário-clichê), aplicada aqui ao meio "site institucional".

Calibração externa: regras mecânicas do taste-skill (tasteskill.dev)
incorporadas na V1.1; protocolo de upgrade do redesign-skill incorporado na
V1.2. Em conflito, os ADRs de identidade do `templates-npm` prevalecem —
skill é calibração, ADR é autoridade.

Critério geral de pronto: um leitor atento (advogado concorrente, jornalista,
cliente sofisticado) não encontra nenhum padrão listado abaixo em nenhuma página
pública. Cada item traz evidência verificada no repositório, ação e critério de
aceite. Itens sem evidência confirmada estão marcados "a confirmar".

---

## Fase 0 – Bloqueadores: artefatos de mockup em produção

Estes itens não são "cara de IA" por estilo — são scaffolding de protótipo
embarcado no site publicado. Prioridade máxima.

### 0.1 Remover o componente `<image-slot>` de todas as páginas
- **Evidência**: 74 ocorrências de `<image-slot>` em 19 páginas.
  `assets/js/image-slot.js` é um componente de canvas de design
  ("user-fillable image placeholder", persistência via sidecar JSON, texto
  visível `placeholder="Foto – arraste aqui"`).
- **Problema**: em produção, slots sem `src` exibem o placeholder de arrasto;
  o JS de mockup inteiro é servido ao público.
- **Ação**: substituir todo `<image-slot src="...">` por `<img>` com `alt`
  descritivo, `width`/`height` e `loading="lazy"`; remover slots sem imagem
  correspondente; excluir `assets/js/image-slot.js` e sua carga nos HTML.
- **Aceite**: `grep -r "image-slot"` retorna vazio; nenhuma página exibe
  placeholder; Lighthouse sem JS não utilizado referente ao componente.

### 0.2 Resolver o toggle PT/EN decorativo
- **Evidência**: todas as páginas exibem `PT / EN` no topbar; não existe
  diretório `/en/` nem página `lang="en"`.
- **Problema**: controle visível que não faz nada = assinatura de mockup.
- **Ação**: decisão binária — (a) remover o toggle até existir versão EN; ou
  (b) produzir a versão EN (projeto próprio, não entra nesta V1).
- **Aceite**: nenhum controle sem função em página pública.

### 0.3 Fotografia real para os slots de área e escritório
- **Evidência**: `assets/img/` contém apenas as 7 fotos de equipe e o logo.
  Páginas de área têm 4–6 slots de imagem cada, sem arquivo correspondente;
  `escritorio.html` tem 1.
- **Ação**: sessão fotográfica própria (fachada, recepção, salas de reunião,
  biblioteca, detalhes do escritório na Cristiano Viana). Proibido banco de
  imagem e proibida imagem gerada — a fotografia própria é a âncora mais
  forte de autenticidade. Enquanto não houver foto, a seção vive sem imagem
  (layout tipográfico), nunca com placeholder.
- **Aceite**: toda imagem publicada é fotografia própria identificável do
  escritório ou da equipe; zero stock, zero geração.

---

## Fase 1 – Texto: aplicar a ban-list do 12_fonte às 22 páginas

### 1.1 Eliminar tríades decorativas
- **Evidência** (amostra): "sobriedade, clareza e aderência";
  "empresariais, patrimoniais e contenciosas" (index e escritorio);
  "societário, arbitragem e organização"; "consultiva, contenciosa e
  atendimento" (2×). Padrão presente na maioria dos leads.
- **Ação**: reescrever cada lead com uma ideia por frase. Enumerações só
  quando os itens forem fatos distintos e verificáveis (ex.: "tributos
  federais, estaduais e municipais" é enumeração real — mantém).
- **Aceite**: nenhuma tríade de abstrações em título, lead ou CTA; tríades
  factuais justificadas caso a caso na revisão.

### 1.2 Eliminar andaimes de antítese ("não é X, mas Y")
- **Evidência**: `escritorio.html` — "Essa presença não é tratada aqui como
  currículo extenso, mas como sinal concreto de repertório técnico, diálogo
  com debates relevantes da profissão e contato permanente com temas
  estruturais" (antítese + tríade na mesma frase).
- **Ação**: reescrever afirmativo e direto, dizendo o que a coisa É.
- **Aceite**: zero ocorrências do padrão em página pública.

### 1.3 Remover meta-discurso editorial vazado para o público
- **Evidência**: h2 da seção Publicações do index — "Conteúdo que fortalece a
  autoridade do escritório deve nascer de fatos verificáveis." Isto é regra
  interna de produção de conteúdo, não mensagem ao cliente.
- **Ação**: substituir por título que apresente as publicações em si.
- **Aceite**: nenhum texto público descreve o próprio método de escrita.

### 1.4 Desformular os CTAs por área
- **Evidência**: todas as páginas de área usam a mesma matriz "Discutir uma
  demanda em [área]." (societário, tributário, contratual, imobiliário,
  família, patrimonial...).
- **Ação**: um CTA específico por área, ancorado no problema típico do
  cliente daquela área (ex.: tributário → autuação/parcelamento;
  societário → conflito entre sócios/reorganização).
- **Aceite**: nenhum par de páginas com CTA de estrutura idêntica.
- **Regra intra-página (V1.1)**: uma intenção = um rótulo. CTAs com a mesma
  intenção (contato/conversa) usam o mesmo texto em toda a página — nav,
  meio e rodapé não podem alternar "Fale conosco" / "Entre em contato" /
  "Discutir uma demanda".

### 1.5 Substituir qualificação por fato
- **Evidência**: "altamente" (2×); leads que qualificam sem informar.
- **Ação**: passar cada afirmação pelo filtro "isso é verificável?". Ativos
  já existentes a explorar: 1989, atendimento direto pelos sócios, CESA,
  CBAr, Câmara Ítalo-Brasileira, IBDFAM, revisão do Código Civil. Onde
  couber, número (anos de atuação por sócio, câmaras arbitrais em que
  atuam, varas/tribunais recorrentes).
- **Aceite**: todo adjetivo de intensidade removido ou lastreado em fato na
  mesma frase.

### 1.6 Revisão de pontuação e cadência
- **Evidência**: em-dashes já foram trocados por en-dash (changelog) — ok.
  Restam padrões de cadência simétrica frase-a-frase típicos de geração.
- **Ação**: leitura em voz alta página a página; variar comprimento de
  frase; cortar frases-eco (segunda frase que reafirma a primeira).
- **Aceite**: aprovação humana (Iago ou sócio) por página, registrada no PR.

---

## Fase 2 – Estrutura e design: quebrar o molde único

### 2.1 Variar o molde de abertura das páginas internas
- **Evidência**: 12 páginas usam o mesmo bloco `page-hero` com `num` ("NPM"),
  h1 e `page-hero-lead` com `label`; 11 repetem o mesmo lead estruturado.
- **Ação**: manter o molde como base, mas diferenciar por tipo de página:
  áreas abrem com o problema do cliente; perfis abrem com a pessoa (foto +
  fato biográfico); escritório abre com a história (1989). O conteúdo dita a
  abertura, não o template.
- **Aceite**: nenhum par de tipos de página (área × perfil × institucional)
  com abertura estruturalmente idêntica.
- **Adendos mensuráveis (V1.1)**:
  - página com N seções usa ao menos 4 famílias de layout distintas quando
    N ≥ 8; nenhuma família se repete em seções consecutivas além de 2;
  - hero com no máximo 4 elementos de texto (eyebrow OU marca; título ≤ 2
    linhas; subtexto ≤ 20 palavras; até 2 CTAs), tudo visível sem rolagem.

### 2.2 Remover numeração decorativa de seções
- **Evidência**: `section-label` com numerais romanos ("iv") + eyebrow em
  caps no index. A ordem das seções não carrega informação — numeração é
  decoração, padrão clássico de layout gerado.
- **Ação**: remover os numerais; manter eyebrow apenas onde nomeia de fato a
  seção.
- **Aceite**: nenhum marcador numérico sem função informativa.
- **Adendo mensurável (V1.1) — cota de eyebrows**: máximo 1 eyebrow/label a
  cada 3 seções por página (teto = ⌈seções/3⌉). Checagem mecânica: contar
  rótulos em caps com tracking acima de títulos; acima do teto, reprova.

### 2.3 Hierarquizar o grid de áreas
- **Evidência**: 8 cards idênticos em grid regular no index.
- **Ação**: dar peso distinto às 2–3 áreas-âncora do escritório (definir com
  os sócios — a confirmar) e agrupar as demais; quebra de simetria
  intencional.
- **Aceite**: o grid comunica prioridade real do escritório, não uniformidade.

### 2.4 Assinatura tipográfica própria nos metadados
- **Evidência**: JetBrains Mono carregado e não utilizado; metadados (datas,
  OAB, tags de publicação) hoje em Hanken com tracking largo — tratamento
  genérico.
- **Ação**: aplicar `var(--mono)` a metadados: OAB nos perfis, datas e
  origem nas publicações, endereço no rodapé. Uma textura editorial
  específica e consistente.
- **Aceite**: mono aplicado ao conjunto definido; nenhum outro uso.

### 2.5 Um elemento-assinatura único do site
- **Evidência**: nenhum elemento atual é exclusivo da NPM; tudo deriva de
  padrões correntes (eyebrow, cards, CTA em faixa).
- **Ação**: definir e executar UMA assinatura memorável — candidatas:
  tratamento gráfico próprio do "desde 1989" como marca de tempo recorrente;
  monograma NPM tipográfico em Newsreader nos heros; régua de metadados em
  mono abrindo cada página. Escolher uma, aplicar com disciplina, cortar o
  resto.
- **Aceite**: um elemento identificável que não existe em template algum;
  demais decorações removidas.

---

## Fase 3 – Conteúdo-âncora: o que só a NPM pode publicar

### 3.1 Publicações reais em vez de vitrine institucional
- **Evidência**: a seção Publicações do index lista participações
  institucionais genéricas ("Participação de profissionais do NPM em
  debates...") sem data, sem link, sem autoria.
- **Ação**: cada item com autor nomeado, data, veículo/entidade e link
  verificável. Se `/blog` do Wix tiver posts aproveitáveis, migrar os que
  passarem na régua do 12_fonte (decisão pendente do PR #1 — a confirmar).
- **Aceite**: zero itens de publicação sem (autor + data + fonte linkável).

### 3.2 Prova social verificável
- **Evidência**: CESA, CBAr, Câmara Ítalo-Brasileira e IBDFAM citados como
  texto solto.
- **Ação**: vincular cada menção à participação concreta (comissão, cargo,
  ano) e, quando existir, à página da entidade.
- **Aceite**: toda credencial institucional é checável em um clique ou traz
  o dado concreto (comissão/ano).

### 3.3 Especificidade por área
- **Ação**: em cada página de área, uma subseção "como o trabalho acontece"
  com 3–5 situações reais e anonimizadas de atuação (tipo de cliente, tipo
  de disputa, foro/câmara) — sem violar sigilo. É o conteúdo que nenhum
  gerador produz porque exige conhecimento do caso.
- **Aceite**: cada área tem ao menos 3 situações concretas próprias; revisão
  de sigilo pelos sócios (a confirmar).

---

## Fase 4 – Acabamento funcional

### 4.1 Microcopy funcional no formulário de contato
- **Ação**: validação client-side (e-mail, obrigatórios) antes do envio;
  mensagens de erro específicas por campo, abaixo do campo; página/estado
  de sucesso após envio ("Mensagem recebida. Retornamos em até X dia útil"
  — prazo a confirmar com o escritório), sem tom de desculpas; nunca
  placeholder no lugar de label.
- **Aceite**: fluxo completo enviar → validar → confirmar testado em
  produção, com erros simulados.

### 4.2 Estados vazios e 404 com voz própria
- **Evidência**: 404.html existe (conteúdo a auditar); seções que dependem
  de conteúdo futuro (publicações) precisam de estado vazio digno.
- **Ação**: 404 orienta (busca áreas/contato); nada de humor genérico.
- **Aceite**: nenhum beco sem saída sem orientação.

### 4.3 Higiene técnica que denuncia geração
- **Ação**: revisar comentários de código servidos ao público (ex.: banners
  `─────────── Footer ───────────`), atributos vazios, `style` inline
  remanescentes; HTML semântico (`nav`, `main`, `section`, `footer`); zero
  código morto servido (JS órfão, blocos comentados); escala de z-index
  definida (nada de `9999`); `title`, `meta description` e og:tags
  completos por página.
- **Aceite**: view-source não revela scaffolding nem comentários de molde;
  checagens W4/W5 do preflight limpas.

### 4.4 Acessibilidade estrutural (V1.2)
- **Ação**: link "pular para o conteúdo" no topo de cada página;
  `:focus-visible` legível em todo elemento interativo; `alt` descritivo
  real em toda imagem com significado (nunca vazio ou "imagem/foto");
  `prefers-reduced-motion` respeitado onde houver transição/animação;
  contraste AA em textos, botões e formulário.
- **Aceite**: navegação completa por teclado sem beco; checagem W3 limpa;
  auditoria de contraste sem reprovação.

### 4.5 Estados de interação sóbrios (V1.2)
- **Ação**: hover/active/focus consistentes e discretos em links, cards e
  botões (ex.: deslocamento de 1px no `:active`); nenhum efeito de
  vocabulário de site de prêmio (parallax, spotlight, grain, scroll
  cinemático, máscaras de vídeo) — registrados como considerados e
  rejeitados por incompatibilidade de registro com o escritório.
- **Aceite**: todo elemento interativo responde a hover/focus/active; zero
  motion chamativo; um único elemento-assinatura (ADR-010) preservado.

---

## Métricas mecânicas — pre-flight (V1.1)

`scripts/preflight.py` audita o repositório contra as regras mecanizáveis
deste roadmap e dos ADRs de identidade:

```text
FALHA  F1  <image-slot> ou image-slot.js referenciado em página pública (0.1)
FALHA  F2  toggle PT/EN sem versão EN existente (0.2)
FALHA  F3  hex literal fora do(s) arquivo(s) de tokens (ADR-008)
FALHA  F4  cota de eyebrows estourada: rótulos > ⌈seções/3⌉ (2.2)
FALHA  F5  mais de um rótulo para a mesma intenção de CTA na página (1.4)
FALHA  F6  linha de autuação só com o fecho constante, ou page-hero com
           marcador decorativo remanescente (ADR-010/011)
AVISO  W1  padrões da ban-list no copy (tríade suspeita, "não é X, mas",
           adjetivo de intensidade, travessão longo)
AVISO  W2  input com placeholder sem label associado (4.1)
AVISO  W3  alt vazio ou genérico em imagem significativa (4.4)
AVISO  W4  higiene: z-index arbitrário, JS órfão, transição sem
           prefers-reduced-motion (4.3/4.4)
AVISO  W5  title/meta description/og ausentes na página (4.3)
AVISO  W6  risco ético OAB no copy — preço, promessa, especialista,
           urgência (regra transversal 7)
```

Uso local: `python3 scripts/preflight.py` (exit ≠ 0 se houver FALHA).
Ativação em CI (GitHub Actions) ocorre no PR da Fase 0 — antes disso o
repositório reprova por definição, pois os bloqueadores existem.

## Regras transversais (valem para todo PR deste roadmap)

1. Nenhum texto novo entra sem passar pela ban-list do 12_fonte.
2. Nenhuma imagem gerada por IA, em nenhuma hipótese; stock só se
   temporário e sinalizado internamente — nunca em produção final.
3. Nenhum componente de mockup/protótipo é servido em produção.
4. Fato sem evidência não entra: marcar "a confirmar" e resolver antes do
   merge (método Passo Atrás aplicado ao site).
5. Cada fase = um PR; aprovação humana de copy registrada no PR.
6. Nenhum PR das Fases 1–4 mergeia fazendo o `preflight.py` regredir
   (novas falhas em relação à base do PR).
7. Todo copy público do site — CTA, lead, título, microcopy — passa pela
   revisão ética do `06_agente_revisor_etico_oab` (Provimento 205/2021 e
   CED) antes do merge, com registro componente → risco → norma no PR.
   A triagem W6 do preflight é apoio mecânico, não substitui a revisão.

## Sequenciamento sugerido

| Ordem | Fase | Dependências |
|-------|------|--------------|
| 1 | Fase 0 (0.1, 0.2) | nenhuma — pode sair já |
| 2 | Fase 1 completa | 12_fonte como régua |
| 3 | Fase 0.3 + 3.x | sessão fotográfica; decisão /blog do PR #1 |
| 4 | Fase 2 | Fases 0–1 mergeadas (evita retrabalho de layout sobre copy velha) |
| 5 | Fase 4 | formulário do PR #1 em produção |
