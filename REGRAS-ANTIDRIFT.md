# Regras Anti-Drift — Novo Site NPM

## Objetivo

Evitar drift de escopo, conteúdo, visual, estrutura e versionamento durante a evolução do site novo.

## 1. Regra de Base Oficial

- a base oficial é a estrutura atualmente publicada no repositório
- arquivos em `legacy/` não são base de evolução
- arquivos em `source-assets/` são apenas insumo bruto ou referência local
- nenhuma nova página deve nascer fora da estrutura principal do projeto

## 2. Regra de Escopo

- a v1 deve conter apenas páginas com função institucional clara
- toda nova página deve responder a uma pergunta: ela melhora posicionamento, clareza ou conversão?
- se a resposta for não, ela entra em backlog e não em execução

## 3. Regra Editorial

- não usar texto genérico de IA como versão final
- toda afirmação institucional deve ser verificável ou validada internamente
- o tom deve ser sóbrio, técnico e seguro
- evitar adjetivação inflada, autopromoção vaga e promessas indiretas de resultado
- a home não deve absorver todo o conteúdo do site

## 4. Regra de Distribuição de Conteúdo

- home: síntese, posicionamento, navegação e confiança
- escritório: história, diferenciais, entidades e visão institucional
- áreas: escopo, forma de atuação, equipe relacionada e CTA
- profissionais: formação, atuação, entidades, idiomas e contato
- publicações: autoridade, atualidade e aprofundamento técnico

## 5. Regra de Estrutura

- páginas novas devem seguir convenção de nomes simples, estáveis e sem improviso
- páginas de área pertencem a `areas/`
- páginas de profissionais pertencem a `profissionais/`
- assets visuais e técnicos pertencem a `assets/`
- documentos de decisão pertencem à raiz apenas se forem ativos de gestão do projeto

## 6. Regra Visual

- preservar a linguagem boutique editorial já definida
- evitar layouts mais chamativos do que o posicionamento institucional suporta
- novos blocos devem seguir a mesma lógica de tipografia, ritmo e contraste
- hovers, animações e CTAs devem ser discretos
- consistência vale mais do que novidade visual isolada

## 7. Regra de Imagens

- usar apenas imagens realmente incorporadas à base ativa do site
- não referenciar imagens brutas de `source-assets/` nas páginas oficiais
- retratos devem manter padrão de recorte e presença visual coerente
- logos intermediários e previews não entram na base ativa

## 8. Regra de Conteúdo de Profissionais

- nomes, cargos, idiomas e áreas devem ser padronizados
- bios devem manter proporcionalidade editorial, mesmo quando alguns profissionais tiverem mais material público
- participações institucionais relevantes podem ser usadas, mas com linguagem objetiva
- não usar estatísticas processuais de agregadores como credencial pública

## 9. Regra Jurídica e de Conformidade

- conteúdo institucional deve respeitar o perfil ético da advocacia
- políticas jurídicas não devem ficar com placeholder ao final da v1
- dados de contato, endereço e identidade institucional devem ser revisados antes de publicação

## 10. Regra de Git e Versionamento

- o repositório principal deve refletir apenas a base ativa
- `legacy/` e `source-assets/` permanecem fora do versionamento principal, salvo decisão expressa
- cada commit deve representar uma unidade clara de progresso
- mudanças estruturais grandes não devem ser misturadas com microajustes irrelevantes

## 11. Regra de Aprovação

Antes de considerar uma sprint concluída, revisar:

- coerência com o roadmap
- aderência à estrutura oficial
- aderência ao tom editorial
- aderência à linguagem visual
- ausência de placeholder crítico

## 12. Regra de Exceção

Qualquer quebra deliberada destas regras deve ser tratada como decisão explícita de projeto, e não como improviso silencioso.
