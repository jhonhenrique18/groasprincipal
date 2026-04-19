# Checkpoint - Agent Rules Adopted

Date: 2026-04-19
Owner: Claude (Opus 4.7)
Phase: Multi-agent governance setup

## Why this exists

O usuario pediu que toda acao no projeto tenha responsavel atribuido
(Claude ou Codex), que absolutamente tudo seja documentado via GSD e
que exista um prompt principal seguido pelos dois agentes. Este
checkpoint marca a adocao formal do contrato.

## What was done

- Criado `.planning/AGENT_RULES.md` como contrato operacional
  compartilhado pelos dois agentes. Contem 8 regras: memoria
  compartilhada, autoria obrigatoria, documentacao via GSD, formato
  de checkpoints, formato do activity log, formato dos commits,
  handoff entre agentes, regras proibitivas e protocolo de atualizacao
  do proprio documento.
- Criado `CLAUDE.md` na raiz do repo como entrypoint auto-lido pelo
  Claude Code. Thin wrapper que manda ler `AGENT_RULES.md`.
- Criado `AGENTS.md` na raiz do repo como entrypoint auto-lido pelo
  Codex CLI. Thin wrapper que manda ler `AGENT_RULES.md`.
- Criado `.planning/ACTIVITY_LOG.md` append-only com o log retroativo
  das acoes ja feitas nesta sessao. Formato tabular com colunas
  Data/Hora, Agent, Tipo, Resumo e Ref.

## Decisions made

- Fonte unica de regras: `.planning/AGENT_RULES.md`. CLAUDE.md e
  AGENTS.md sao thin wrappers que sempre apontam para la. Em conflito,
  AGENT_RULES.md vence, exceto contra instrucao direta do usuario na
  conversa em curso.
- Autoria git continua sempre `jhonatan` (maquina local). O agente e
  identificado por `Co-Authored-By:` no commit, `Owner:` no checkpoint
  e coluna `Agent` no activity log.
- Acoes pequenas entram no ACTIVITY_LOG (uma linha); acoes grandes
  geram checkpoint completo.
- Handoff Claude → Codex usa `GPT_CATCHUP_PROMPT.md`; Codex → Claude
  usa `CLAUDE_CATCHUP_PROMPT.md` (a ser criado quando o Codex fechar
  proxima sessao).

## What was NOT done

- Nao atualizei ainda `GPT_CATCHUP_PROMPT.md` para refletir as novas
  regras — sera feito no proximo passo desta mesma sessao.
- Nao exigi que commits passados sejam retroativamente rotulados; o
  ACTIVITY_LOG cobre a rastreabilidade daqui para frente.

## Next step

1. Atualizar `GPT_CATCHUP_PROMPT.md` mencionando AGENT_RULES.md e a
   nova obrigacao de ler a raiz AGENTS.md.
2. Atualizar `STATE.md` e `CONTEXT.md`.
3. Atualizar `HISTORY.md` adicionando este bloco na Fase 3.
4. Commitar tudo com `Co-Authored-By: Claude Opus 4.7` e pushar com
   autorizacao explicita do usuario.
5. Entregar ao usuario o novo prompt de handoff atualizado.
