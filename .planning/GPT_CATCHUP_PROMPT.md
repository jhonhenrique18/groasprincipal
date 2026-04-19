# Prompt de Handoff — Claude → Codex/GPT

Uso: cole o bloco abaixo (entre `---`) em uma nova sessao do Codex/GPT
para que ele recupere paridade total de contexto com o que o Claude fez.

Atualize este prompt sempre que o Claude fechar um bloco grande de
trabalho. A data no topo do bloco deve refletir a ultima atualizacao.

Versao atual: 2 (2026-04-19, pos-adocao do AGENT_RULES.md)

---

# CONTEXTO DO PROJETO — HANDOFF PARA CODEX/GPT

Atualizado: 2026-04-19, pos-adocao do contrato de agentes.
Fonte de verdade permanente: a pasta `.planning/` deste repositorio.

## O que voce precisa assumir ao comecar

1. Voce esta retomando um projeto Flask + PostgreSQL hospedado na Railway
   chamado internamente de "EP-Institucional" (pasta local), cujo negocio
   e um catalogo B2B de produtos naturais no Paraguai com conversao via
   WhatsApp.

2. O projeto agora usa um CONTRATO UNICO de agentes. Antes de qualquer
   acao, leia nesta ordem:
   - `AGENTS.md` (raiz do repo) — entrypoint oficial do Codex
   - `.planning/AGENT_RULES.md` — contrato operacional completo
   - `.planning/HISTORY.md` — timeline com atribuicao de autoria
   - `.planning/CONTEXT.md` — leitura viva
   - `.planning/STATE.md` — foco atual e proximo passo
   - `.planning/PROJECT.md` — decisoes duraveis
   - `.planning/ROADMAP.md` e `.planning/REQUIREMENTS.md`
   - O checkpoint mais recente em `.planning/checkpoints/`
   - As ultimas 20 linhas de `.planning/ACTIVITY_LOG.md`

3. O projeto esta em rebrand de superficie. A marca visivel virou
   `Especias del Paraguay`, mas o dominio `graos.com.py` e toda a camada
   de SEO tecnico continuam intencionalmente ligados a `Grãos S.A.`. Isso
   e intencional e temporario. Nao "arrume" isso.

4. Regra zero de autoria: toda acao que voce fizer e executada com
   responsavel `Codex (GPT)`. Nunca aja anonimamente. Todo commit seu
   leva `Co-Authored-By: Codex (GPT) <noreply@openai.com>`, todo
   checkpoint seu leva `Owner: Codex (GPT)` e toda acao pequena sua
   entra como nova linha em `ACTIVITY_LOG.md` com `Agent=Codex`.

## O que o Codex/GPT (voce, em sessoes anteriores) ja fez

- Definiu a estrategia de rebrand de superficie.
- Conduziu o estudo cromatico e chegou na paleta paprika + clove + sand.
- Aplicou o rebrand no front publico (navbar, footer, home, nosotros,
  sistema cromatico em CSS).
- Gerou e rejeitou um kit de marca paralelo que nao batia com a logo
  aprovada, e documentou essa rejeicao como aprendizado.
- Gerou o pacote de variacoes fieis em
  `static/img/brand/especias-del-paraguay/`.
- Atualizou favicon e icones PWA para o monograma `EP`.
- Refinou a logo principal (sem barra inferior, `EP` maior, paleta mais
  firme, menos cara de "AI slop").
- Consolidou a memoria viva em `.planning/` e escreveu todos os
  checkpoints do dia (veja `Owner: Codex` em cada um).

## O que o Claude (Opus 4.7) fez na sessao mais recente

- Leu o GSD inteiro para recuperar contexto depois que o usuario moveu a
  pasta e perdeu o historico do Claude Code.
- Salvou uma regra de memoria persistente dizendo que `.planning/` e
  fonte de verdade em todo projeto, nao so neste.
- Commitou as atualizacoes de `.planning/` que estavam apenas no working
  tree (consolidacao de contexto e update de CONVENTIONS/PROJECT/STATE).
- Fez push em `origin/main` (com autorizacao explicita do usuario) dos
  quatro commits abaixo, o que disparou o deploy automatico na Railway:
  - `50e7732` feat: rebrand de superficie (criado pelo Codex, pushed
    pelo Claude)
  - `147c97f` docs(planning): consolida memoria viva do rebrand (Claude)
  - `e3d23b8` docs(planning): registra deploy de producao (Claude)
  - `dfd24f4` docs(planning): documentation pass, atribui autoria
    (Claude)
  - Mais um commit de agent rules sera feito apos esta atualizacao.
- Criou checkpoint `2026-04-19-production-deploy.md`.
- Criou `HISTORY.md` com a linha do tempo completa e atribuicao de
  autoria por fase.
- Criou checkpoint `2026-04-19-full-documentation-pass.md`.
- Atualizou `STATE.md` e `CONTEXT.md` para refletir o estado pos-deploy.
- **Adotou o contrato unico de agentes**:
  - Criou `.planning/AGENT_RULES.md` (contrato compartilhado, 8 regras).
  - Criou `CLAUDE.md` na raiz (entrypoint Claude Code).
  - Criou `AGENTS.md` na raiz (entrypoint Codex CLI — voce deve ler
    primeiro).
  - Criou `.planning/ACTIVITY_LOG.md` append-only com log retroativo.
  - Criou checkpoint `2026-04-19-agent-rules-adopted.md`.
  - Atualizou este proprio `GPT_CATCHUP_PROMPT.md` para refletir o
    contrato.

## Estado atual do projeto (ao retomar)

- Fase ativa: rebrand de superficie em **revisao visual pos-deploy**.
- Nao foi iniciada nenhuma Phase do ROADMAP (Phase 1: Catalogo
  Confiavel) ainda.
- O usuario acabou de validar em producao. Proximo passo logico e
  decidir entre (a) continuar refinamentos visuais se algum asset ficou
  estranho em producao ou (b) comecar a Phase 1 do roadmap.

## Regras duraveis que voce NAO deve violar

Regra zero: seguir `.planning/AGENT_RULES.md` em todas as acoes. Aquele
arquivo tem o contrato completo. O que segue abaixo e o subset minimo:

1. `.planning/` e fonte de verdade. Toda decisao relevante vai para la.
2. Toda acao sua tem autoria `Codex (GPT)`. Commits com
   `Co-Authored-By: Codex (GPT)`, checkpoints com `Owner: Codex (GPT)`,
   log com `Agent=Codex`.
3. A logo aprovada e `static/img/logo-especias-primary.svg` e
   `logo-especias-reverse.svg`. Qualquer variacao futura sai dali, nao
   de reinterpretacao.
4. Nao mexa em titles, meta, canonical, JSON-LD, sitemap, robots ou
   slugs nesta fase. A camada tecnica de SEO segue congelada em `graos`.
5. Favicon e browser title da home SAO excecoes aprovadas que ja foram
   atualizadas. Respeite esse estado.
6. Caminho rejeitado e documentado, nao apagado: manual de marca proprio
   paralelo foi descartado. Nao recrie.
7. Ao terminar qualquer bloco de trabalho, siga a Regra 6 do
   `AGENT_RULES.md`: atualize STATE.md, crie checkpoint, atualize
   `CLAUDE_CATCHUP_PROMPT.md` (voce — Codex — escreve para o Claude
   retomar), registre em ACTIVITY_LOG.md, atualize HISTORY.md se for
   mudanca de timeline.
8. Acoes pequenas (commit, push, leitura relevante, decisao, teste)
   entram como uma linha no `ACTIVITY_LOG.md`. Acoes grandes geram
   checkpoint completo.
9. Push direto em `main` requer autorizacao explicita do usuario na
   conversa em curso. Nao reutilizar autorizacao anterior.

## Como responder ao usuario na primeira mensagem

Confirme em uma linha que voce leu:

- `AGENTS.md`
- `.planning/AGENT_RULES.md`
- `.planning/HISTORY.md`
- `.planning/CONTEXT.md`
- `.planning/STATE.md`
- `.planning/PROJECT.md`
- ultimo checkpoint em `.planning/checkpoints/`
- ultimas 20 linhas de `.planning/ACTIVITY_LOG.md`

Depois liste em bullets curtos:
- qual o estado atual
- qual o proximo passo logico
- o que voce esta esperando como input do usuario para seguir
- uma unica linha confirmando que voce entendeu que toda acao sua sera
  atribuida a `Codex (GPT)` e registrada em ACTIVITY_LOG

Nao repita toda a timeline. Nao gere plano novo sem pedir confirmacao.

---

Fim do prompt de handoff.
