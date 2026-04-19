# Prompt de Handoff — Claude → Codex/GPT

Uso: cole o bloco abaixo (entre `---`) em uma nova sessao do Codex/GPT
para que ele recupere paridade total de contexto com o que o Claude fez.

Atualize este prompt sempre que o Claude fechar um bloco grande de
trabalho. A data no topo do bloco deve refletir a ultima atualizacao.

---

# CONTEXTO DO PROJETO — HANDOFF PARA CODEX/GPT

Atualizado: 2026-04-19, fim da sessao do Claude.
Fonte de verdade permanente: a pasta `.planning/` deste repositorio.

## O que voce precisa assumir ao comecar

1. Voce esta retomando um projeto Flask + PostgreSQL hospedado na Railway
   chamado internamente de "EP-Institucional" (pasta local), cujo negocio
   e um catalogo B2B de produtos naturais no Paraguai com conversao via
   WhatsApp.

2. O projeto usa GSD local. A pasta `.planning/` e a memoria oficial do
   projeto. Antes de qualquer decisao, leia nesta ordem:
   - `.planning/HISTORY.md` (timeline completa com atribuicao de autoria)
   - `.planning/CONTEXT.md` (leitura viva)
   - `.planning/STATE.md` (foco atual e proximo passo)
   - `.planning/PROJECT.md` (decisoes duraveis)
   - `.planning/ROADMAP.md` e `.planning/REQUIREMENTS.md`
   - O checkpoint mais recente em `.planning/checkpoints/`

3. O projeto esta em rebrand de superficie. A marca visivel virou
   `Especias del Paraguay`, mas o dominio `graos.com.py` e toda a camada
   de SEO tecnico continuam intencionalmente ligados a `Grãos S.A.`. Isso
   e intencional e temporario. Nao "arrume" isso.

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
  tres commits abaixo, o que disparou o deploy automatico na Railway:
  - `50e7732` feat: rebrand de superficie (criado pelo Codex, pushed pelo
    Claude)
  - `147c97f` docs(planning): consolida memoria viva do rebrand (Claude)
  - `e3d23b8` docs(planning): registra deploy de producao (Claude)
- Criou o checkpoint `2026-04-19-production-deploy.md`.
- Criou `HISTORY.md` com a linha do tempo completa e atribuicao de
  autoria por fase.
- Criou este proprio `GPT_CATCHUP_PROMPT.md`.
- Criou checkpoint `2026-04-19-full-documentation-pass.md` para marcar
  este momento.
- Atualizou `STATE.md` e `CONTEXT.md` para refletir o estado
  pos-deploy.

## Estado atual do projeto (ao retomar)

- Fase ativa: rebrand de superficie em **revisao visual pos-deploy**.
- Nao foi iniciada nenhuma Phase do ROADMAP (Phase 1: Catalogo
  Confiavel) ainda.
- O usuario acabou de validar em producao. Proximo passo logico e
  decidir entre (a) continuar refinamentos visuais se algum asset ficou
  estranho em producao ou (b) comecar a Phase 1 do roadmap.

## Regras duraveis que voce NAO deve violar

1. `.planning/` e fonte de verdade. Toda decisao relevante vai para la.
2. A logo aprovada e `static/img/logo-especias-primary.svg` e
   `logo-especias-reverse.svg`. Qualquer variacao futura sai dali, nao
   de reinterpretacao.
3. Nao mexa em titles, meta, canonical, JSON-LD, sitemap, robots ou
   slugs nesta fase. A camada tecnica de SEO segue congelada em `graos`.
4. Favicon e browser title da home SAO excecoes aprovadas que ja foram
   atualizadas. Respeite esse estado.
5. Caminho rejeitado e documentado, nao apagado: manual de marca proprio
   paralelo foi descartado. Nao recrie.
6. Ao terminar qualquer bloco de trabalho, atualize `STATE.md`, crie um
   checkpoint dated em `.planning/checkpoints/` com seu nome no campo
   `Owner`, e se for relevante atualize tambem `CONTEXT.md` e este
   `GPT_CATCHUP_PROMPT.md`.
7. Commits com mudancas no `.planning/` podem ser feitos livremente.
   Push direto em `main` requer autorizacao explicita do usuario (o
   harness do Claude bloqueou isso ate o usuario autorizar com frase
   literal, e provavelmente o seu ambiente respeita politica similar).

## Como responder ao usuario na primeira mensagem

Confirme em uma linha que voce leu o HISTORY, CONTEXT, STATE e o ultimo
checkpoint. Liste em bullets curtos:
- qual o estado atual
- qual o proximo passo logico
- o que voce esta esperando como input do usuario para seguir

Nao repita toda a timeline. Nao gere plano novo sem pedir confirmacao.

---

Fim do prompt de handoff.
