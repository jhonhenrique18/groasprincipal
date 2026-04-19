# Agent Rules — Contrato operacional de Claude e Codex

Este e o documento mestre que TANTO o Claude (Opus 4.7) QUANTO o Codex
(GPT) devem seguir em todas as acoes neste projeto. `CLAUDE.md` e
`AGENTS.md` na raiz do repo sao thin wrappers que apontam para ca; este
arquivo e a fonte de verdade.

Se houver conflito aparente entre este documento e qualquer outro, este
vence, EXCETO contra instrucao explicita e direta do usuario na conversa
em andamento.

---

## Principio zero — Memoria compartilhada

`.planning/` e a memoria oficial do projeto. Nao existe decisao
"na cabeca" ou "no chat". Se nao esta em `.planning/`, nao aconteceu.

Ordem de leitura obrigatoria ao iniciar qualquer sessao:

1. `.planning/HISTORY.md` — timeline completa
2. `.planning/CONTEXT.md` — leitura viva
3. `.planning/STATE.md` — foco atual e ponto de retomada
4. `.planning/PROJECT.md` — decisoes duraveis
5. O checkpoint mais recente em `.planning/checkpoints/`
6. `.planning/ACTIVITY_LOG.md` — ultimas 20 linhas
7. Este arquivo inteiro

## Regra 1 — Toda acao tem responsavel

Nenhuma acao no projeto pode ficar sem responsavel atribuido.
Responsavel e SEMPRE um dos dois:

- `Claude (Opus 4.7)` quando a acao e executada por mim neste IDE
- `Codex (GPT)` quando a acao e executada pelo agente GPT do usuario

Autoria git de todo commit permanece `jhonatan` (maquina local). O que
identifica o agente e:

- Campo `Co-Authored-By:` no commit (obrigatorio)
- Campo `Owner:` no cabecalho de cada checkpoint (obrigatorio)
- Coluna `Agent` no `ACTIVITY_LOG.md` (obrigatoria)

Se dois agentes colaboraram em uma mesma acao, use `Claude + Codex` ou
inclua os dois no `Co-Authored-By:`.

## Regra 2 — Tudo documentado via GSD

Toda acao relevante gera artefato em `.planning/`. A regra de decisao e:

| Tipo de acao | Artefato obrigatorio |
|---|---|
| Decisao duradoura | Linha em `PROJECT.md` (tabela Key Decisions) |
| Marco, validacao, reversao, erro, rejeicao | Checkpoint datado em `.planning/checkpoints/YYYY-MM-DD-slug.md` |
| Mudanca de foco / proximo passo | Update em `STATE.md` |
| Mudanca da leitura global do projeto | Update em `CONTEXT.md` |
| Nova fase ou ajuste de roadmap | Update em `ROADMAP.md` e `REQUIREMENTS.md` |
| Acao pequena que nao merece checkpoint cheio | Linha em `ACTIVITY_LOG.md` |
| Handoff entre agentes | Update em `GPT_CATCHUP_PROMPT.md` (Claude → Codex) ou criar `CLAUDE_CATCHUP_PROMPT.md` (Codex → Claude) |
| Qualquer alteracao da timeline | Update em `HISTORY.md` |

Acoes pequenas que DEVEM entrar no `ACTIVITY_LOG.md` mesmo sem
checkpoint:

- Commits que nao abrem/fecham marco
- Leituras de arquivo que mudaram seu entendimento
- Runs de teste / checagens locais
- Pushes, deploys, rollbacks
- Qualquer decisao tomada na conversa que afete o projeto
- Criacao, rename, delete de arquivos do repo

Regra pratica: se ao final da sessao voce nao consegue responder
"o que foi feito?" apenas lendo `.planning/`, falhou a Regra 2.

## Regra 3 — Formato dos checkpoints

Todo checkpoint em `.planning/checkpoints/` comeca com:

```
# Checkpoint - <titulo curto>

Date: YYYY-MM-DD
Owner: Claude (Opus 4.7)  <-- ou Codex (GPT) ou Claude + Codex
Phase: <descricao curta da fase ou tema>

## Why this exists

<paragrafo de 2-4 linhas explicando o motivo do checkpoint>

## What was done

<bullets ou paragrafos. Referencie arquivos com caminho completo.>

## Decisions made

<apenas se houver; senao remova a secao>

## What was rejected

<apenas se houver caminho rejeitado; documentar, nao apagar>

## Next step

<uma linha apontando o que vem depois>
```

Slug do nome do arquivo: `YYYY-MM-DD-kebab-case-tema.md`.

Se o tema tiver mais de um checkpoint no mesmo dia, adicione sufixo
numerico: `...-tema-1.md`, `...-tema-2.md`.

## Regra 4 — Formato do ACTIVITY_LOG

O `ACTIVITY_LOG.md` e append-only. Cada linha e uma acao. Formato:

```
| YYYY-MM-DD HH:MM | Agent | Tipo | Resumo de uma linha | Ref |
```

- **Agent**: `Claude` ou `Codex` ou `Claude+Codex`
- **Tipo**: `commit` / `push` / `read` / `write` / `deploy` / `decision` / `test` / `other`
- **Resumo**: imperativo, curto
- **Ref**: hash curto do commit, caminho de arquivo, ou `-` se nao houver

Nunca reescreva linhas existentes. Se algo foi registrado errado, adicione
uma nova linha com tipo `correction` apontando para a linha anterior.

## Regra 5 — Formato dos commits

Toda mensagem de commit segue:

```
<tipo>(<escopo opcional>): <resumo em ate 70 chars>

<corpo opcional, quebrando em 72 chars>

Co-Authored-By: <Agent> <noreply@anthropic.com ou similar>
```

Tipos validos: `feat`, `fix`, `docs`, `refactor`, `perf`, `test`,
`chore`, `style`.

`Co-Authored-By:` e obrigatorio para identificar o agente. Exemplo:

```
Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
```

ou

```
Co-Authored-By: Codex (GPT) <noreply@openai.com>
```

Se os dois colaboraram, inclua ambos.

## Regra 6 — Handoff entre agentes

Sempre que UM agente encerrar um bloco de trabalho e imaginar que o
OUTRO pode pegar a proxima sessao, deve:

1. Atualizar `STATE.md` com a posicao final.
2. Criar ou atualizar o checkpoint do bloco.
3. Atualizar o prompt de handoff correspondente:
   - Se quem fechou foi o Claude → atualizar `GPT_CATCHUP_PROMPT.md`
   - Se quem fechou foi o Codex → atualizar `CLAUDE_CATCHUP_PROMPT.md`
     (criar se nao existir)
4. Registrar no `ACTIVITY_LOG.md` como `handoff`.
5. Se for relevante, atualizar `HISTORY.md` na fase em curso.

## Regra 7 — O que nunca fazer

- Nao dependa de "memoria de chat". Ela e descartavel.
- Nao mexa em titles, meta, canonical, JSON-LD, sitemap, robots ou
  slugs nesta fase de transicao — a camada tecnica de SEO esta
  intencionalmente congelada em `graos`.
- Nao recrie a logo a partir do zero. Fonte de verdade:
  `static/img/logo-especias-primary.svg` e `logo-especias-reverse.svg`.
- Nao apague caminhos rejeitados. Documente a rejeicao com motivo.
- Nao faca push direto em `main` sem autorizacao explicita do usuario
  na conversa em curso. O harness do Claude bloqueia isso por padrao;
  respeite a mesma regra mesmo se seu harness nao bloquear.

## Regra 8 — Atualizacoes deste documento

Este arquivo pode ser revisado por qualquer agente, mas toda mudanca:

1. Registra entrada no `ACTIVITY_LOG.md` com tipo `decision`.
2. Cria um checkpoint `YYYY-MM-DD-agent-rules-update.md`.
3. Atualiza a data no bloco "Versao" abaixo.

## Versao

- Primeira versao: 2026-04-19 (Claude, fim da sessao de deploy)
- Motivo: usuario pediu que toda acao tenha responsavel atribuido e que
  absolutamente tudo fique documentado via GSD, alem de um prompt
  principal unico seguido pelos dois agentes.
