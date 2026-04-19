# Claude Instructions

Voce e o agente Claude trabalhando neste projeto.

## Antes de qualquer acao

Leia, nesta ordem, sem excecao:

1. `.planning/AGENT_RULES.md` — contrato operacional compartilhado com o Codex
2. `.planning/HISTORY.md` — timeline completa com atribuicao de autoria
3. `.planning/CONTEXT.md` — leitura viva do projeto
4. `.planning/STATE.md` — foco atual e ponto de retomada
5. `.planning/PROJECT.md` — decisoes duraveis
6. O checkpoint mais recente em `.planning/checkpoints/`
7. As ultimas 20 linhas de `.planning/ACTIVITY_LOG.md`

## Enquanto trabalha

- Toda acao e executada com autoria `Claude (Opus 4.7)`.
- Todo commit leva `Co-Authored-By: Claude Opus 4.7 (1M context)`.
- Todo checkpoint escrito por voce leva `Owner: Claude (Opus 4.7)`.
- Toda acao pequena (commit, push, decisao, leitura relevante,
  deploy, teste) entra como nova linha em `ACTIVITY_LOG.md`.
- Acoes grandes, marcos, reversoes e rejeicoes ganham checkpoint
  completo em `.planning/checkpoints/`.
- Push direto em `main` SO com autorizacao explicita do usuario na
  conversa atual. Nao reutilizar autorizacao de turnos anteriores.

## Ao encerrar uma sessao ou handoff para o Codex

- Atualize `STATE.md` com a posicao final.
- Crie/atualize o checkpoint do bloco.
- Atualize `.planning/GPT_CATCHUP_PROMPT.md`.
- Registre o handoff no `ACTIVITY_LOG.md`.
- Se a timeline mudou, atualize `HISTORY.md`.

## Fonte de verdade

`.planning/AGENT_RULES.md` e a fonte de verdade das regras. Se houver
conflito com esta pagina, `AGENT_RULES.md` vence.
