# Project State

## Project Reference

See: .planning/PROJECT.md (updated 2026-04-05)
See also: .planning/CONTEXT.md

**Core value:** Catálogo de produtos atualizado e acessível que converte visitantes em contatos de WhatsApp para vendas B2B ao por mayor.
**Current focus:** Manter a memoria do rebrand consolidada e seguir refinando a camada visual publica sem perder contexto

## Current Position

Phase: 1 of 4 (Catálogo Confiável)
Plan: 0 of 2 in current phase
Status: In review
Last activity: 2026-04-19 - Documentation pass completa por Claude apos o deploy: HISTORY.md criado com atribuicao de autoria Codex vs Claude, GPT_CATCHUP_PROMPT.md gerado como handoff, CONTEXT.md atualizado pos-deploy, checkpoint de documentation pass criado.

Progress: [░░░░░░░░░░] 0%

## Performance Metrics

**Velocity:**
- Total plans completed: 0
- Average duration: -
- Total execution time: 0.0 hours

**By Phase:**

| Phase | Plans | Total | Avg/Plan |
|-------|-------|-------|----------|
| - | - | - | - |

**Recent Trend:**
- Last 5 plans: -
- Trend: Stable

## Accumulated Context

### Decisions

Decisions are logged in PROJECT.md Key Decisions table.
Recent decisions affecting current work:

- Brownfield init: tratar este repositório como projeto GSD local em Codex.
- Planning scope: usar a codebase atual como baseline e roadmapear o próximo ciclo, não reescrever o produto do zero.
- Rebrand first: nenhuma alteração visual grande será executada antes da aprovação da nova marca.
- Transitional SEO rule: manter domínio e sinais SEO atuais ligados a `graos` nesta fase; trocar apenas a marca visível no site.
- Invisible layer freeze: não alterar titles/meta/schema/sitemap/robots/canonical/slugs nesta etapa.
- Visible brand chosen: usar `Especias del Paraguay` como nome visível da nova marca nesta fase.
- Logo direction chosen: a fonte de verdade da marca é a logo já aprovada e aplicada no site (`static/img/logo-especias-primary.svg` e `static/img/logo-especias-reverse.svg`).
- Asset bundle updated: variações fiéis da logo aprovada agora ficam em `static/img/brand/especias-del-paraguay/`.
- Browser surface updated: favicon e título da aba da home agora seguem a marca visível, sem manter `Grãos S.A.` no texto do navegador.
- Favicon-specific rule: o ícone da aba usa uma versão otimizada da marca, com fundo claro e monograma ampliado, porque o lockup horizontal original perdia leitura em tamanhos pequenos.
- Favicon refinement: a melhor leitura veio de um monograma `EP` mais limpo, sem moldura, com menos aperto e mais respiro nas bordas.
- Logo refinement rule: a marca pública deve parecer editorial e institucional, não “gerada”; por isso a composição foi endurecida com cores mais fortes, sem sublinhado e com melhor equilíbrio entre `EP` e wordmark.
- Public rebrand applied: navbar, footer, home, nosotros e sistema cromático já refletem `Especias del Paraguay`.

### Pending Todos

- Consolidar no front os exports finais da logo ja aprovada.
- Revisar visualmente o favicon e a logo no localhost apos cache refresh completo.
- Seguir refinamentos visuais apenas a partir da fonte de verdade atual da marca.

### Blockers/Concerns

- `config.py` usa defaults inseguros para segredo e admin.
- Formulário de contato ainda não tem integração real de entrega.
- `robots.txt` e serving de imagens podem conflitar na Railway.
- A marca pública atual precisa ser substituída sem perder SEO nem coerência institucional.
- Haverá um período intencional em que SEO/domínio continuam `graos`, mas a marca exibida ao usuário será outra.

## Deferred Items

| Category | Item | Status | Deferred At |
|----------|------|--------|-------------|
| Expansion | Importação em lote de produtos | Deferred | 2026-04-19 |
| Analytics | Dashboard de métricas no admin | Deferred | 2026-04-19 |
| Integrations | Webhook/e-mail transacional para leads | Deferred | 2026-04-19 |

## Session Continuity

Last session: 2026-04-19 final (Claude)
Stopped at: documentation pass completa; rebrand em producao; proximo agente (Codex ou Claude) deve ler HISTORY.md + CONTEXT.md + STATE.md + ultimo checkpoint antes de agir. Prompt de handoff para o Codex em .planning/GPT_CATCHUP_PROMPT.md.
Resume file: .planning/checkpoints/2026-04-19-full-documentation-pass.md
