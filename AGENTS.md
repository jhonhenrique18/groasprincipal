# Codex / Agent Instructions

Voce e o agente Codex (GPT) trabalhando neste projeto.

## Antes de qualquer acao

Leia, nesta ordem, sem excecao:

1. `.planning/AGENT_RULES.md` — contrato operacional compartilhado com o Claude
2. `.planning/HISTORY.md` — timeline completa com atribuicao de autoria
3. `.planning/CONTEXT.md` — leitura viva do projeto
4. `.planning/STATE.md` — foco atual e ponto de retomada
5. `.planning/PROJECT.md` — decisoes duraveis
6. O checkpoint mais recente em `.planning/checkpoints/`
7. As ultimas 20 linhas de `.planning/ACTIVITY_LOG.md`
8. `.planning/GPT_CATCHUP_PROMPT.md` — handoff mais recente do Claude

## Enquanto trabalha

- Toda acao e executada com autoria `Codex (GPT)`.
- Todo commit leva `Co-Authored-By: Codex (GPT) <noreply@openai.com>`.
- Todo checkpoint escrito por voce leva `Owner: Codex (GPT)`.
- Toda acao pequena (commit, push, decisao, leitura relevante,
  deploy, teste) entra como nova linha em `ACTIVITY_LOG.md`.
- Acoes grandes, marcos, reversoes e rejeicoes ganham checkpoint
  completo em `.planning/checkpoints/`.
- Push direto em `main` SO com autorizacao explicita do usuario na
  conversa atual. Nao reutilizar autorizacao de sessoes anteriores.

## Ao encerrar uma sessao ou handoff para o Claude

- Atualize `STATE.md` com a posicao final.
- Crie/atualize o checkpoint do bloco.
- Crie/atualize `.planning/CLAUDE_CATCHUP_PROMPT.md` com o handoff.
- Registre o handoff no `ACTIVITY_LOG.md`.
- Se a timeline mudou, atualize `HISTORY.md`.

## Fonte de verdade

`.planning/AGENT_RULES.md` e a fonte de verdade das regras. Se houver
conflito com esta pagina, `AGENT_RULES.md` vence.
