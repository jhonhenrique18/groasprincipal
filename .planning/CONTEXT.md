# Current Context

## Purpose

Este arquivo existe para concentrar o contexto vivo do projeto sem depender de memoria de chat.
Ele deve responder rapidamente:

- onde estamos
- o que foi decidido
- o que foi tentado e rejeitado
- qual arquivo hoje e a fonte de verdade
- como retomar sem perder contexto

## Project Snapshot

- Projeto: site institucional/catalogo B2B em Flask para Paraguay
- Negocio: importadora/distribuidora de produtos naturais com conversao para WhatsApp
- Dominio atual: `graos.com.py`
- Regra atual: a marca visivel ao usuario mudou, mas a base tecnica de SEO continua em transicao
- Marca visivel atual aprovada: `Especias del Paraguay`

## Brand Transition Rules

### What stays from the legacy layer

- dominio `graos`
- maior parte da camada SEO tecnica ligada a `Grãos S.A.`
- estrutura de URLs e slugs
- sitemap, robots, canonical e dados estruturados principais

### What changed in the visible layer

- logo publica
- nome exibido ao usuario
- paleta visual publica
- textos visiveis principais do front
- browser surface solicitada pelo usuario: titulo da home na aba e favicon

### Important nuance

A regra inicial era congelar tudo que fosse invisivel ao usuario.
Depois, o usuario pediu explicitamente para remover `Grãos S.A.` da aba do navegador e trocar o favicon.
Essa excecao foi aprovada e documentada.

## What Happened On 2026-04-19

### 1. GSD local was initialized

- O projeto passou a usar a pasta `.planning/` como memoria operacional
- `PROJECT.md`, `STATE.md`, `REQUIREMENTS.md`, `ROADMAP.md` e checkpoints foram criados/atualizados

### 2. Rebrand strategy was defined

- A marca `Grãos S.A.` nao pode seguir exposta no site publico nesta fase
- O nome visivel aprovado foi `Especias del Paraguay`
- O rebrand desta etapa foi definido como **surface rebrand**

### 3. Color direction was studied

- O catalogo mostrou predominio de especiarias e condimentos
- Isso puxou a marca para uma paleta mais quente e terrosa
- A direcao aprovada ficou proxima de clove/paprika/sand

### 4. Public surface rebrand was applied

- navbar
- footer
- home
- `Nosotros`
- sistema cromatico do front publico

### 5. Wrong approach was created and rejected

Foi criado um pacote de marca paralelo que nao batia com a logo aprovada pelo usuario.
Esse caminho foi rejeitado e removido.

Rejected approach:

- manual novo de identidade visual
- familia floral propria que nao correspondia ao que estava no site
- assets que reinterpretavam a marca em vez de partir do aprovado

### 6. Source-of-truth logo workflow was restored

Depois da rejeicao, ficou decidido que qualquer variacao deve partir apenas destes arquivos:

- `static/img/logo-especias-primary.svg`
- `static/img/logo-especias-reverse.svg`

Variacoes fiéis geradas:

- `static/img/brand/especias-del-paraguay/`

### 7. Browser surface was updated

- titulo da home na aba ficou apenas `El Mayor Proveedor de Productos Naturales del Paraguay`
- favicon passou por varias iteracoes ate ganhar leitura real em tamanhos pequenos

### 8. Logo itself was refined

Pedido do usuario:

- remover a barra inferior
- deixar o `EP` maior
- alinhar melhor com `Especias del Paraguay`
- tirar a sensacao de logo gerada por IA

Resultado:

- sem sublinhado
- `EP` mais dominante
- cores mais firmes
- composicao mais editorial/institucional

## Source Of Truth Right Now

### Public logo used by the site

- `static/img/logo-especias-primary.svg`
- `static/img/logo-especias-reverse.svg`

### Export bundle derived from the approved logo

- `static/img/brand/especias-del-paraguay/logo-especias-primary.svg`
- `static/img/brand/especias-del-paraguay/logo-especias-reverse.svg`
- `static/img/brand/especias-del-paraguay/logo-especias-black.svg`
- `static/img/brand/especias-del-paraguay/logo-especias-stacked.svg`
- `static/img/brand/especias-del-paraguay/logo-especias-stacked-black.svg`
- `static/img/brand/especias-del-paraguay/logo-especias-mark.svg`

### Browser/app icons

- `static/favicon.ico`
- `static/favicon-especias-16x16.png`
- `static/favicon-especias-32x32.png`
- `static/apple-touch-icon-especias.png`
- `static/android-chrome-especias-192x192.png`
- `static/android-chrome-especias-512x512.png`

## Files Most Touched In This Rebrand Track

- `templates/base.html`
- `templates/index.html`
- `templates/nosotros.html`
- `static/css/style.css`
- `static/manifest.json`
- `app.py`

## What Must Not Be Forgotten

- Nem toda camada "invisivel" ficou congelada: favicon e browser title da home mudaram por pedido expresso
- A tentativa de criar uma familia visual diferente foi rejeitada
- O usuario quer continuidade e memoria forte na `.planning/`
- A logo nao deve parecer "AI slop"; refinamento manual e parte do criterio de qualidade
- Qualquer nova variacao de marca deve nascer da logo aprovada, nao de reinterpretacao criativa

## Resume Guidance

Se outro agente retomar o trabalho, deve assumir:

1. O projeto esta em rebrand de superficie, nao em migracao completa de SEO/dominio.
2. `Especias del Paraguay` e a marca visivel atual.
3. `static/img/logo-especias-primary.svg` e `static/img/logo-especias-reverse.svg` sao a verdade atual da marca.
4. Qualquer nova mudanca visual deve ser validada no localhost.
5. Toda tentativa rejeitada deve ser documentada, nao apagada da memoria do projeto.

## Documentation Protocol

Daqui para frente, toda mudanca relevante deve atualizar:

- `PROJECT.md` para decisoes duraveis
- `STATE.md` para foco atual e ponto de retomada
- `checkpoints/YYYY-MM-DD-*.md` para milestones, erros, reversoes e validacoes
- este `CONTEXT.md` quando a leitura global do projeto mudar
