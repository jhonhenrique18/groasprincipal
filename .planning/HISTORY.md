# Project History — Authored Timeline

Este arquivo registra, em ordem cronologica, tudo o que foi feito no projeto
e quem fez cada coisa. Ele existe para que qualquer agente (Codex/GPT,
Claude, ou o proprio usuario) consiga recuperar o contexto completo sem
depender da memoria volatil de chat.

A divisao de autoria segue estas convencoes:

- **User (jhonatan)**: trabalho direto, codigo escrito a mao, commits
  autorais sem assistencia automatizada registrada.
- **Codex (GPT)**: trabalho feito pelo agente OpenAI Codex/GPT em sessoes
  anteriores. Identificavel pelo campo `Owner: Codex` nos checkpoints e
  por blocos inteiros de `.planning/` escritos de uma vez.
- **Claude (Opus 4.7)**: trabalho feito por mim nesta IDE. Identificavel
  por commits com `Co-Authored-By: Claude Opus 4.7`, por alteracoes
  rastreadas nesta sessao atual e pelo proprio fato de ter sido eu quem
  gerou este arquivo.

Quando ha ambiguidade real sobre quem fez, o item vai marcado como `?`.

---

## Fase 0 — Bootstrap do produto (2026-02-07 a 2026-03-24)

Trabalho primario do **User**, sem GSD, sem agentes documentados.

### 2026-02-07
- `d570222` Grãos S.A. — Site institucional inicial para Railway (User)
- `1158a1e` Produtos, imagens e seed automatico para Railway (User)

### 2026-02-14
- `626642e` SEO: dominio canonico `www.graos.com.py` em todas as URLs (User)
- `84beaa0` SEO: otimizacao completa para ranking no Paraguai (User)
- `0878237` Favicon e app icons com a flor da Graos (User)

### 2026-03-23 / 2026-03-24
- `a5c4c79` SEO completo + GA4 + melhorias visuais (User)
- `a923c4f` Cadastro de 55 produtos + 9 categorias reorganizadas + GSC (User)
- `e125f50` Redesign da pagina de produtos: busca, filtros, layout premium (User)
- `f00291d` Cards mobile mais largos na home + cache busting (User)

## Fase 1 — Entrada do GSD e mapeamento da codebase (2026-04-04 a 2026-04-05)

Aqui comeca o uso do GSD local.

### 2026-04-04
- `10e747c` docs: map existing codebase (?)
  - Sao os arquivos em `.planning/codebase/`: ARCHITECTURE, STRUCTURE,
    CONVENTIONS, INTEGRATIONS, CONCERNS, STACK, TESTING.
  - Estes documentos deram a primeira base viva do projeto.
  - Atribuicao: provavelmente Codex (padrao de escrita combina com outros
    documentos Codex), mas sem `Owner` explicito.

### 2026-04-05
- `0827fbe` Catalogo 112 produtos + sidebar categorias + UI redesign (User)
- `550028d` docs: GSD project documentation + codebase mapping (?)
  - Criou REQUIREMENTS.md e ROADMAP.md iniciais.
  - Atribuicao: Codex (padrao de escrita GSD).
- `50ceb9a` feat: admin migrate-images route para Railway volume (User)
- `55a52bd` fix: sync product images to production (User)
- `ffb2db5` perf: WebP images + srcset responsivo (126MB -> 4.9MB) (User)
- `205f710` fix: complete image migration, PNG->WebP paths + volume sync (User)
- `51beb5a` fix: remove offers from Product schema (GSC price errors) (User)
- `9dc5f24` fix: broken images in production, definitive fix (User)

## Fase 2 — Rebrand de superficie (2026-04-19, manha/tarde, via Codex)

Sessao inteira documentada por Codex/GPT. Cada passo tem um checkpoint
dedicado em `.planning/checkpoints/`.

### Decisao estrategica
- **Rebrand de superficie** aprovado como estrategia de transicao.
- Dominio `graos.com.py` e SEO tecnico ficam congelados.
- Marca visivel passa a ser `Especias del Paraguay`.
- Checkpoint: `2026-04-19-rebrand-kickoff.md` (Owner: Codex)

### Estudo cromatico
- Catalogo analisado: predominio de especiarias e condimentos.
- Paleta recomendada: paprika + clove + sand.
- Cores finais: `#3F2A24` (clove), `#B14E2E` (paprika), `#E8D8C2` (sand),
  `#2B2623` (charcoal suave).
- Checkpoint: `2026-04-19-logo-color-study.md` (Owner: Codex)

### Rebrand aplicado no front publico
- Alteracoes em `templates/base.html`, `index.html`, `nosotros.html`,
  `static/css/style.css`, `static/manifest.json`, `app.py`.
- Logos publicas criadas:
  - `static/img/logo-especias-primary.svg`
  - `static/img/logo-especias-reverse.svg`
- Checkpoint: `2026-04-19-surface-rebrand-applied.md` (Owner: Codex)

### Caminho rejeitado (documentado, nao apagado)
- Foi criado um kit de marca paralelo com manual proprio.
- Foi rejeitado por nao bater com a logo aprovada.
- Regra consolidada: variacoes futuras so a partir dos SVGs aprovados.
- Checkpoint: `2026-04-19-approved-logo-exports.md` (Owner: Codex)

### Pacote de variacoes fieis gerado
- Diretorio `static/img/brand/especias-del-paraguay/` com:
  - `logo-especias-primary.svg`
  - `logo-especias-reverse.svg`
  - `logo-especias-black.svg`
  - `logo-especias-stacked.svg`
  - `logo-especias-stacked-black.svg`
  - `logo-especias-mark.svg`
- Cada SVG tambem exportado em PNG no mesmo diretorio.
- Checkpoint: `2026-04-19-approved-logo-exports.md` (Owner: Codex)

### Browser surface atualizada
- Title da home agora: `El Mayor Proveedor de Productos Naturales del
  Paraguay` (sem `Grãos S.A.` na aba).
- Favicon refeito varias vezes ate o monograma `EP` ficar legivel em
  16x16.
- Icones PWA novos:
  - `static/favicon-especias-16x16.png`
  - `static/favicon-especias-32x32.png`
  - `static/apple-touch-icon-especias.png`
  - `static/android-chrome-especias-192x192.png`
  - `static/android-chrome-especias-512x512.png`
- Checkpoint: `2026-04-19-browser-brand-surface.md` (Owner: Codex)

### Consolidacao da memoria do projeto
- Criado `CONTEXT.md` como leitura viva do projeto.
- Formalizado o protocolo de documentacao
  (PROJECT/STATE/CONTEXT/checkpoints).
- Checkpoint: `2026-04-19-context-consolidation.md` (Owner: Codex)

### Commit consolidado pelo Codex
- `50e7732` feat: rebrand de superficie para Especias del Paraguay
  - Criado localmente ainda nao pushed no fim da sessao do Codex.

## Fase 3 — Deploy de producao e onboarding do Claude (2026-04-19, noite)

Nesta fase, o usuario abriu o projeto na IDE com **Claude (esta sessao)**.
A pasta foi movida para `EP-Institucional`, o que criou uma nova pasta
de historico em `~/.claude/projects/` e orfanou a anterior.

Trabalho feito por **Claude** nesta sessao:

### Recuperacao de contexto
- Leitura completa de `.planning/`: PROJECT, STATE, CONTEXT, ROADMAP,
  REQUIREMENTS, config, todos os checkpoints e `.planning/codebase/`.
- Explicacao ao usuario de como o Claude Code persiste historico por
  caminho absoluto (motivo pelo qual mover a pasta orfanou o chat).

### Regra de memoria persistente salva
- `~/.claude/projects/-Users-jhonatan-Desktop-EP-Institucional/memory/feedback_gsd_planning_always.md`
- Conteudo: em todo projeto, `.planning/` e fonte de verdade; nunca
  depender apenas da memoria de chat.
- Motivo: usuario perdeu contexto ao mover a pasta e pediu para que essa
  regra fosse aplicada em todo projeto dai em diante.

### Deploy para producao
- Commits pushed para `origin/main`:
  - `50e7732` feat: rebrand de superficie (criado pelo Codex)
  - `147c97f` docs(planning): consolida memoria viva do rebrand (Claude)
  - `e3d23b8` docs(planning): registra deploy de producao (Claude)
- Mecanismo: Railway faz auto-deploy em todo push para `main`.
- Autorizacao: o push direto em main foi bloqueado por policy do harness
  e exigiu frase explicita do usuario (`Sim, autorizo git push origin
  main`) para ser executado.
- Checkpoint: `2026-04-19-production-deploy.md` (Owner: Codex no
  cabecalho porque herdou o template; na pratica foi escrito por Claude)

### Documentation pass
- Criado este `HISTORY.md` com atribuicao de autoria completa.
- Atualizado `CONTEXT.md` com leitura final pos-deploy.
- Atualizado `STATE.md` com posicao final.
- Criado checkpoint `2026-04-19-full-documentation-pass.md`.
- Criado `GPT_CATCHUP_PROMPT.md` como handoff formal para o Codex
  reassumir em paridade de contexto.

### Adocao do contrato unico de agentes (este momento)
- Criado `.planning/AGENT_RULES.md` como contrato compartilhado com 8
  regras operacionais.
- Criado `CLAUDE.md` na raiz do repo (auto-lido pelo Claude Code), thin
  wrapper apontando para `AGENT_RULES.md`.
- Criado `AGENTS.md` na raiz do repo (auto-lido pelo Codex CLI), thin
  wrapper apontando para `AGENT_RULES.md`.
- Criado `.planning/ACTIVITY_LOG.md` append-only com log retroativo
  das acoes da sessao.
- Atualizado `GPT_CATCHUP_PROMPT.md` para a versao 2, incluindo leitura
  obrigatoria do AGENT_RULES.md e AGENTS.md.
- Criado checkpoint `2026-04-19-agent-rules-adopted.md`.
- Motivacao: usuario pediu que toda acao tenha responsavel atribuido
  (Claude ou Codex), que absolutamente tudo seja documentado via GSD e
  que exista um prompt principal seguido pelos dois agentes.

## Estado atual ao fechar esta sessao

### O que esta em producao agora (Railway)

- Marca visivel: `Especias del Paraguay`.
- Paleta aplicada: paprika + clove + sand.
- Favicon e icones PWA: monograma `EP` (variante refinada sem moldura).
- Dominio: continua `graos.com.py`.
- SEO tecnico: continua ligado a `Grãos S.A.` (intencional, parte da
  transicao aprovada).

### O que e fonte de verdade da marca

- `static/img/logo-especias-primary.svg`
- `static/img/logo-especias-reverse.svg`
- Qualquer variacao futura deve partir desses arquivos, nao de
  reinterpretacoes.

### Roadmap nao iniciado

- Phase 1: Catalogo Confiavel (0/2 plans)
- Phase 2: Midia e SEO Resilientes (0/2 plans)
- Phase 3: Captacao Auditavel (0/2 plans)
- Phase 4: Admin Endurecido (0/3 plans)

### Bloqueios conhecidos (nao resolvidos)

- `config.py`: SECRET_KEY e ADMIN_PASSWORD com defaults inseguros.
- Formulario `/contacto`: aceita POST mas nao entrega em lugar nenhum.
- Sem CSRF, sem rate limit no `/admin/login`.
- Potencial XSS no modal de produto em `static/js/app.js`.

## Como reconciliar Codex e Claude daqui para frente

1. Ambos os agentes leem `.planning/` antes de qualquer acao.
2. O agente que executa uma acao cria/atualiza o checkpoint dessa acao e
   coloca o proprio nome no campo `Owner` do checkpoint.
3. Quando o usuario alternar de agente, aponta para `HISTORY.md` + o
   ultimo checkpoint + `STATE.md` como ponto de retomada.
4. Decisao que afete ambos os agentes entra em `PROJECT.md` na tabela de
   Key Decisions.
5. `GPT_CATCHUP_PROMPT.md` e atualizado sempre que o Claude fechar um
   bloco grande de trabalho, para o Codex reentrar em paridade.
