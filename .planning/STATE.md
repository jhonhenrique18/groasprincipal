# Project State

## Project Reference

See: .planning/PROJECT.md (updated 2026-04-05)
See also: .planning/CONTEXT.md

**Core value:** Catálogo de produtos atualizado e acessível que converte visitantes em contatos de WhatsApp para vendas B2B ao por mayor.
**Current focus:** ⛔ SITE OFFLINE — Modo deindex ativo. Wipe total de "Grãos S.A." do código (templates, schemas, configs, assets) + 410 Gone em todas as rotas públicas + robots.txt Disallow: / + X-Robots-Tag noindex globais. Maintenance page neutra no /. Admin permanece acessível. Toggle via env var `MAINTENANCE_MODE=0` na Railway para reativar. Reativação aguarda "barra limpa" no Google (~60-120 dias de quarentena). Decisões pendentes para reativação: domínio final (manter graos.com.py vs migrar para especiasdelparaguay.com.py), schema Organization novo, disclosure de razão social, higiene Compliance (logs Railway/Meta token).

## Current Position

Phase: 1 of 4 (Catálogo Confiável)
Plan: 0 of 2 in current phase
Status: In review
Last activity: 2026-04-19 - Codex refez a auditoria de seguranca apos as mudancas recentes e confirmou que o pacote basico (hash admin, SECRET_KEY fail-loud, rate limit login, CSRF, validacao real de upload, XSS modal e antispam no contacto) esta refletido no codigo atual. Nota consolidada desta reavaliacao: seguranca 7.5/10; exposicao a vulnerabilidades 3/10. Riscos residuais priorizados: cookies de sessao sem flags explicitas, ausencia de CSP, endpoint /api/meta-capi-event ainda abusavel para poluir analytics e rate limiting dependente do comportamento de proxy.

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

- Fixar flags explicitas para cookie de sessao em producao (`SESSION_COOKIE_SECURE`, `SESSION_COOKIE_SAMESITE`, opcionalmente nome propio e lifetime).
- Adicionar Content-Security-Policy compativel com os scripts inline atuais de GA4 e Meta.
- Tornar o rate limit realmente proxy-aware em Railway em vez de depender de `request.remote_addr`.
- Endurecer `/api/meta-capi-event` com validacao adicional de origem/esquema para reduzir pollution de analytics.
- Fazer a higiene operacional pendente em prod: remover `ADMIN_PASSWORD` da Railway apos login validado e rotacionar o token da Meta/CAPI se ainda nao foi feito.

### Blockers/Concerns

- O runtime atual ainda nao define flags explicitas para o cookie de sessao do Flask; no check local, `SESSION_COOKIE_SECURE=False` e `SESSION_COOKIE_SAMESITE=None`.
- `add_security_headers()` ainda nao envia `Content-Security-Policy`, entao o site segue sem uma camada forte de mitigacao caso um XSS futuro reapareca.
- O endpoint `/api/meta-capi-event` esta CSRF-exempt por necessidade funcional e tem rate limit, mas continua publico e pode ser usado para poluir sinais da Meta.
- O comentario em `app.py` diz que `get_remote_address` e X-Forwarded-For-aware, mas a funcao instalada le apenas `request.remote_addr`; em Railway isso pode colapsar o rate limit por IP se a app estiver atras de proxy sem ajuste adicional.
- `/admin/logout` continua em GET, entao logout forcado cross-site segue possivel (baixo impacto).

## Deferred Items

| Category | Item | Status | Deferred At |
|----------|------|--------|-------------|
| Expansion | Importação em lote de produtos | Deferred | 2026-04-19 |
| Analytics | Dashboard de métricas no admin | Deferred | 2026-04-19 |
| Integrations | Webhook/e-mail transacional para leads | Deferred | 2026-04-19 |

## Session Continuity

Last session: 2026-05-11 (Claude)
Stopped at: Wipe total de "Grãos S.A." + modo deindex deployado em produção. Conselho de 4 especialistas (Arquiteto/SEO/Cético/Compliance) consultado em paralelo antes da execução; tensão "sem rastros vs autoridade SEO" nomeada e usuário escolheu corte total (autoridade descartada porque site fica offline mesmo). Site retorna 410 Gone em todas rotas públicas, robots Disallow, X-Robots-Tag noindex globais. Próximo natural: validar deploy Railway em produção, submeter URL Removal no GSC, monitorar deindex orgânico via Pages report, decidir domínio de reativação após quarentena.
Resume file: .planning/checkpoints/2026-05-11-graos-wipe-and-deindex.md

Sessão anterior (SEO Fase A+D, hoje descartada):
- 2026-05-03 (Claude). 26 guias editoriais + topic clusters + 112 produtos com FAQPage/HowTo. Toda a autoridade SEO construída nesse trabalho está sendo intencionalmente descartada pela decisão do usuário de wipe total + offline. Resume file legado: .planning/checkpoints/2026-05-03-seo-fase-d-guias-editoriales.md

Pacote anterior (security defense in depth, ainda pendente):
- Última sessão: 2026-04-19 (Codex). Reaudit confirmou hardening básico (items 1-7) refletido no código. Riscos residuais: cookie flags, CSP, proxy-aware rate limit, tightening de /api/meta-capi-event.
- Resume file alternativo: .planning/checkpoints/2026-04-19-security-reaudit-post-hardening.md
