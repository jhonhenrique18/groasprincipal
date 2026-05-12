# Checkpoint — Wipe de Grãos S.A. + Modo Deindex (Fase 1 + Fase 2)

Date: 2026-05-11
Owner: Claude (Opus 4.7)
Phase: Brand wipe — site offline com 410 Gone

## Why this exists

Usuário solicitou remoção urgente de "Grãos S.A." da rede de pesquisa,
com desativação do site e reativação posterior "quando a barra estiver
limpa". Mudança de fase: a regra anterior (transitional SEO ligada a
graos, freeze da camada invisível) foi explicitamente sobrescrita pelo
usuário na conversa atual. Esta sessão executou Fase 1 (cleanup total
do código) + Fase 2 (modo deindex com 410 Gone) num único commit
atômico, conforme autorizado.

## Conselho consultado antes da execução

Antes de qualquer linha de código, foi convocado um conselho de 4
vozes paralelas para debate genuíno:

1. **Arquiteto de Migração** — defendeu hard cutover sem `sameAs`
   ("a tese de marca pesa mais que o delta de tráfego recuperável")
2. **SEO Specialist** — defendeu Caminho A (cirurgia interna, manter
   domínio, adiar decisão de domínio 6 meses)
3. **Cético/Realista** — destruiu a premissa "sem rastros" nomeando o
   que é imutável (Wayback, Ahrefs/SEMRush, Common Crawl, SET/RUC).
   Forçou a pergunta "POR QUÊ sem rastros?"
4. **Compliance Reviewer** — alertou que o estado anterior já era "ato
   enganoso" sob Ley 1334/98 PY e exigiu disclosure de razão social
   antes do plano técnico rodar

Tensão central nomeada: "sem rastros" e "preservar autoridade SEO" são
antagônicos. Só se escolhe um.

## What was done

### Fase 1 — Cleanup total do código

**Templates limpos** (sed bulk + verificação grep):
- `templates/base.html` — epicentro: removido JSON-LD Organization
  (`@id: graos.com.py/#organization`, `name: "Grãos S.A."`,
  alternateName, logo logo-verde.png), WebSite schema, hreflang
  hardcoded; meta robots default trocado para `noindex, nofollow,
  noarchive`; canonical agora dinâmico via `request.url_root`
- `templates/index.html` — FAQ schema sem menções a Grãos S.A.
- `templates/producto.html` — Product/BreadcrumbList/WebPage/FAQPage/
  HowTo schemas com brand "Especias del Paraguay" e
  `@id: /#especias-organization` (corte de continuidade no grafo)
- `templates/productos.html` — CollectionPage/BreadcrumbList/ItemList
  limpos
- `templates/nosotros.html` — AboutPage + Organization @id reset
- `templates/contacto.html` — ContactPage limpo
- `templates/guias/index.html` — CollectionPage limpo
- `templates/guias/article.html` — Article publisher/author Organization
  limpos
- `templates/admin/login.html` + `admin/base.html` — títulos e h1/h2
- `templates/admin/settings.html` — placeholder email `contacto@graossa.com`
  trocado para `contacto@especiasdelparaguay.com`

**Python/configs:**
- `config.py` — SQLite fallback `graos.db` → `epy.db`
- `models.py` — comentário "additive over the existing graos.com.py /
  Grãos S.A." trocado por "alias-aware product schema"
- `app.py` — base URL hardcoded `https://www.graos.com.py` trocada para
  `https://especiasdelparaguay.com.py` (no caminho post-MAINTENANCE_MODE)
- `.gitignore` — `lp-graos-foz/` → `lp-legacy-foz/`

**Assets removidos:**
- `graos flor.png` (raiz do repo, 691KB)
- `static/img/logo-verde.png` (referenciado no JSON-LD legado)

### Fase 2 — Modo deindex (site offline)

**Novo template:** `templates/maintenance.html` — HTML neutro, sem
nenhum branding (sem "Especias del Paraguay" também, para não vincular
o histórico Grãos S.A. à marca nova durante a quarentena). Mensagem:
"Sitio en mantenimiento. Volveremos pronto."

**`app.py` — gate global:**
- Constante `MAINTENANCE_MODE = os.environ.get('MAINTENANCE_MODE', '1') != '0'`
  (default ON; setar `MAINTENANCE_MODE=0` na Railway para reativar)
- `@app.before_request` `_maintenance_gate()`: intercepta todas as
  requisições e retorna `410 Gone` com `maintenance.html` para
  qualquer path que NÃO seja `/admin/*`, `/static/*`, `/uploads/*`,
  `/robots.txt`. Admin continua acessível para gestão.
- `@app.after_request` `add_security_headers`: agora também envia
  `X-Robots-Tag: noindex, nofollow, noarchive, nosnippet` em modo
  manutenção (belt-and-suspenders deindex signal)
- `/robots.txt`: em maintenance, retorna `User-agent: *\nDisallow: /\n`
  (sem sitemap referenciado)
- `/sitemap.xml` e `/sitemap-products.xml`: em maintenance, retornam
  `410 Gone` (não sitemap vazio — sitemap vazio re-registra URLs como
  "known but empty"; 410 diz "permanently gone")
- `errorhandler(404)`: em maintenance, vira `410` com `maintenance.html`

### Smoke test local (passou cleanly)

```
GET /                        status=410  maintenance=True  has_graos=False
GET /productos               status=410  maintenance=True  has_graos=False
GET /producto/manzanilla-flor status=410 maintenance=True has_graos=False
GET /guias                   status=410  maintenance=True  has_graos=False
GET /guias/manzanilla-flor   status=410  maintenance=True  has_graos=False
GET /nosotros                status=410  maintenance=True  has_graos=False
GET /contacto                status=410  maintenance=True  has_graos=False
GET /robots.txt              status=200  body="User-agent: *\nDisallow: /\n"
GET /sitemap.xml             status=410
GET /sitemap-products.xml    status=410
GET /admin/login             status=200  has_graos=False
GET /api/producto/x          status=410
GET /random-page             status=410
X-Robots-Tag header presente em todas as respostas
```

### Push autorizado

Usuário autorizou explicitamente Fase 1+2 num commit + push para main
via prompt: "executa Fase 1+2 agora". Railway auto-deploy on push.

## Decisions made

1. **Hard cutover, não soft transition.** O `@id` da Organization foi
   migrado de `graos.com.py/#organization` para `/#especias-organization`
   sem `sameAs` apontando pra entidade antiga. Corta a continuidade
   no Knowledge Graph propositalmente — o requisito "sem rastros"
   vence sobre "preservar autoridade SEO".
2. **Domínio NÃO migrado nesta sessão.** Mantido `graos.com.py`. O
   próprio host ainda contém "graos" — decisão de mudar de domínio
   fica para fase de reativação.
3. **410 Gone em vez de 404 ou 503.** Sinal mais forte de deindex
   permanente para o Googlebot. Sitemap também 410 (não vazio).
4. **`/` também retorna 410** (não 200 com noindex). Maximiza signal
   de "site permanently gone" para o crawler.
5. **Admin permanece acessível.** Usuário ainda precisa gerenciar
   conteúdo do banco enquanto site está dark.
6. **Maintenance page é neutra** — sem "Especias del Paraguay" no
   body. Não vincular a nova marca ao domínio enquanto Google está
   reindexando.
7. **Variável de ambiente `MAINTENANCE_MODE`** para toggle sem code
   change na reativação.

## What was rejected

- **Soft transition com `sameAs`** (proposta inicial do consenso SEO).
  Mantém rastro auditável no JSON-LD público. Vetado pelo "sem rastros".
- **Migrar para domínio novo `especiasdelparaguay.com.py` agora.**
  Decisão de domínio fica para reativação. Trocar agora + desativar
  é trabalho duplicado.
- **`git filter-repo` para reescrever história de commits.** GitHub
  mantém orphan commits 90 dias + quebra qualquer clone/fork. Cético
  apontou que o esforço não compensa porque Wayback/Ahrefs já têm
  snapshots.
- **Sitemap vazio em vez de 410.** Sitemap vazio re-registra URLs
  como "known but empty". 410 corta permanentemente.
- **Takedown agressivo do Wayback Machine.** Cético: requer
  justificativa legal formal (DMCA / disputa de marca) e tende a
  disparar Streisand Effect. Não vale o esforço.

## Riscos colaterais aceitos

- Perda de 100% da autoridade SEO acumulada (26 guias + 112 produtos
  + 9 hubs deployados em maio/2026). Aceito porque o site vai ficar
  offline mesmo.
- Citações externas (Ahrefs, SEMRush, Common Crawl, registros públicos
  Paraguay) preservam "Grãos S.A." indefinidamente — imutável. "Sem
  rastros" é só do Google Search público; resto é fora do controle.
- Backlinks externos que apontavam pra graos.com.py agora retornam
  410 — quebra silenciosa. Aceito.
- Cliente B2B que busca "Grãos S.A." e não acha vai assumir falência,
  não rebrand. Risco reputacional aceito por decisão do usuário.

## Pendências para fase de reativação (decisões adiadas)

1. **Domínio final**: manter `graos.com.py` ou migrar para
   `especiasdelparaguay.com.py`? Ambos os caminhos suportados — o
   código já usa `request.url_root` dinâmico onde possível.
2. **Disclosure de razão social** (apontado pelo Compliance Reviewer):
   adicionar no rodapé e em `/nosotros` algo como "Especias del
   Paraguay es la marca comercial de [Razón Social legal] — RUC X".
   Sem isso, reativação tem risco de "ato enganoso" sob Ley 1334/98.
3. **Higiene operacional do Compliance** (BLOCKER antes de reativar):
   - Purgar logs Railway que tenham `ADMIN_PASSWORD` em texto
   - Rotacionar token Meta/CAPI
   - Cookie de sessão flags (`SECURE`, `SAMESITE`, `HttpOnly`)
   - CSP completo no `add_security_headers`
4. **Schema Organization novo** — ao reativar, criar JSON-LD
   Organization com `@id` baseado no domínio final escolhido,
   sem referência a Grãos S.A.
5. **GSC** (manual, fora do código):
   - Submeter Removal Tool com prefixo `https://www.graos.com.py/`
     (90 dias, dá tempo do deindex orgânico via 410 acontecer)
   - Monitorar `Pages > Not Indexed` semanalmente
   - Quando GSC reportar `0` páginas indexadas por 4 semanas, considerar
     "barra limpa" no Google
6. **Plataformas externas** (manual):
   - Pausar Meta Pixel/CAPI no Business Manager
   - Suspender (não deletar) Google Business Profile se existir como
     "Grãos S.A."
   - Bing Webmaster: Removal Tool equivalente
   - Arquivar páginas Facebook/Instagram/LinkedIn como "Grãos S.A."

## Next step

Aguardar Railway auto-deploy (~5min após push to main). Validar em
produção:
```
curl -I https://www.graos.com.py/
# Esperado: HTTP/2 410, X-Robots-Tag: noindex, nofollow, noarchive, nosnippet
curl https://www.graos.com.py/robots.txt
# Esperado: User-agent: * / Disallow: /
```

Após validação em produção, abrir GSC e submeter URL Removal Tool
para `https://www.graos.com.py/` (prefix). A partir daí, fase 4
(quarentena 60-120 dias) começa.
