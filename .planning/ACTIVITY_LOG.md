# Activity Log

Append-only. Cada linha e uma acao. Nao reescrever linhas antigas.
Formato: `| YYYY-MM-DD HH:MM | Agent | Tipo | Resumo | Ref |`

Ver `.planning/AGENT_RULES.md` secao "Regra 4" para formato completo.

| Data/Hora | Agent | Tipo | Resumo | Ref |
|-----------|-------|------|--------|-----|
| 2026-04-19 17:19 | Codex | commit | feat: rebrand de superficie para Especias del Paraguay | 50e7732 |
| 2026-04-19 17:35 | Claude | commit | docs(planning): consolida memoria viva do rebrand | 147c97f |
| 2026-04-19 17:36 | Claude | push | push de 9dc5f24..147c97f em origin/main; Railway auto-deploy disparado | - |
| 2026-04-19 17:37 | Claude | commit | docs(planning): registra deploy de producao | e3d23b8 |
| 2026-04-19 17:37 | Claude | push | push de 147c97f..e3d23b8 em origin/main | - |
| 2026-04-19 18:00 | Claude | write | cria HISTORY.md, GPT_CATCHUP_PROMPT.md e checkpoint full-documentation-pass | .planning/ |
| 2026-04-19 18:05 | Claude | commit | docs(planning): documentation pass, atribui autoria Codex vs Claude | dfd24f4 |
| 2026-04-19 18:05 | Claude | push | push de e3d23b8..dfd24f4 em origin/main | - |
| 2026-04-19 18:20 | Claude | decision | adota contrato unico de agentes: .planning/AGENT_RULES.md + CLAUDE.md + AGENTS.md na raiz + ACTIVITY_LOG.md append-only | AGENT_RULES.md |
| 2026-04-19 18:20 | Claude | write | cria .planning/AGENT_RULES.md (contrato compartilhado) | .planning/AGENT_RULES.md |
| 2026-04-19 18:20 | Claude | write | cria CLAUDE.md na raiz (entrypoint Claude Code) | CLAUDE.md |
| 2026-04-19 18:20 | Claude | write | cria AGENTS.md na raiz (entrypoint Codex CLI) | AGENTS.md |
| 2026-04-19 18:20 | Claude | write | cria .planning/ACTIVITY_LOG.md com log historico ate aqui | .planning/ACTIVITY_LOG.md |
| 2026-04-19 18:25 | Claude | commit | docs: adota contrato unico de agentes (Claude + Codex) | ac2944b |
| 2026-04-19 18:25 | Claude | push | push de dfd24f4..ac2944b em origin/main, autorizado pelo usuario | - |
| 2026-04-19 19:00 | Claude | decision | adota Meta Pixel + CAPI hybrid (Nivel 2) com dedup por event_id e advanced matching hashado | checkpoint meta-pixel-capi-hybrid |
| 2026-04-19 19:00 | Claude | write | cria meta_capi.py com send_capi_event, user_data_from_request, sha256_hash, normalize_phone | meta_capi.py |
| 2026-04-19 19:00 | Claude | write | config.py ganha META_PIXEL_ID, META_CAPI_ACCESS_TOKEN, META_TEST_EVENT_CODE, META_DOMAIN_VERIFICATION | config.py |
| 2026-04-19 19:00 | Claude | write | requirements.txt ganha requests==2.32.3 | requirements.txt |
| 2026-04-19 19:00 | Claude | write | base.html ganha facebook-domain-verification meta + Meta Pixel base script condicionais | templates/base.html |
| 2026-04-19 19:00 | Claude | write | app.py ganha context processor meta, cookie _ep_eid, /api/meta-capi-event e CAPI no /contacto POST | app.py |
| 2026-04-19 19:00 | Claude | write | app.js ganha epMetaEventId + epMetaTrack + eventos Contact/Lead/ViewContent | static/js/app.js |
| 2026-04-19 19:00 | Claude | write | contacto.html ganha hidden meta_event_id; index/productos ganham data-name nos cards | templates/ |
| 2026-04-19 19:05 | Claude | test | ast.parse + node Function + jinja2 parse confirmam sintaxe OK em todos os arquivos modificados | - |
| 2026-04-19 19:10 | Claude | commit | feat(tracking): Meta Pixel + Conversions API hybrid (Nivel 2) | 4cc002c |
| 2026-04-19 19:20 | Claude | decision | adota permission rules Bash(curl *backboard.railway.*) em .claude/settings.local.json com autorizacao literal do usuario | .claude/settings.local.json |
| 2026-04-19 19:20 | Claude | write | .gitignore ganha .claude/settings.local.json para nao vazar preferencias locais | .gitignore |
| 2026-04-19 19:22 | Claude | deploy | variableUpsert Railway: META_PIXEL_ID, META_CAPI_ACCESS_TOKEN, META_DOMAIN_VERIFICATION no service web env production, via Project-Access-Token scoped | Railway API |
| 2026-04-19 19:22 | Claude | test | query variables confirma META_* vars persistidas no service | Railway API |
| 2026-04-19 19:30 | Claude | commit | chore: gitignore .claude/settings.local.json + ACTIVITY_LOG | f8e4dca |
| 2026-04-19 19:30 | Claude | push | push de ac2944b..f8e4dca em origin/main; Railway iniciou deployment 5709914e (BUILDING) | - |
| 2026-04-19 19:45 | Claude | decision | aprovado plano de seguranca basica em 6 itens; usuario pediu ship por checkpoint (1 por vez) | - |
| 2026-04-19 19:50 | Claude | write | Security item 1: hash do admin password via werkzeug pbkdf2:sha256:600000, bootstrap idempotente em ensure_admin_password_hash | config.py, app.py |
| 2026-04-19 19:52 | Claude | test | smoke test cobre bootstrap + idempotencia + lockout fail-closed; 3/3 passaram | - |
| 2026-04-19 20:00 | Claude | deploy | Railway variableUpsert SECRET_KEY=<random 64 hex> + ADMIN_PASSWORD=graos2026 (prep para item 2, evita lock de admin) | Railway API |
| 2026-04-19 20:02 | Claude | write | Security item 2 (V1): config.py sem default inseguro; app.py levanta RuntimeError se vazio em prod | config.py, app.py |
| 2026-04-19 20:03 | Claude | test | 3 cenarios passaram: prod fail-loud, dev auto-gen, explicit env var | - |
| 2026-04-19 20:05 | Claude | commit | feat(security-02): SECRET_KEY sem default inseguro, fail-loud em prod | 285978b |
| 2026-04-19 20:05 | Claude | push | push 27ef978..285978b origin/main; Railway build | - |
| 2026-04-19 20:10 | Claude | write | Security item 3 (V3): Flask-Limiter + rate limit 5/15min em POST /admin/login | requirements.txt, app.py |
| 2026-04-19 20:12 | Claude | commit | feat(security-03): rate limit em /admin/login | 52230df |
| 2026-04-19 20:12 | Claude | push | push 285978b..52230df origin/main | - |
| 2026-04-19 20:20 | Claude | write | Security item 4 (V2): Flask-WTF CSRFProtect global + csrf_token em 7 forms + exempt em /api/meta-capi-event (rate-limited 60/min) | app.py, templates/ |
| 2026-04-19 20:25 | Claude | commit | feat(security-04): CSRF protection global via Flask-WTF | 8806e89 |
| 2026-04-19 20:25 | Claude | push | push 52230df..8806e89 origin/main | - |
| 2026-04-19 20:35 | Claude | write | Security item 5 (V5): save_image agora forca img.load() e descarta arquivo em falha sem fallback de escrita bruta | app.py |
| 2026-04-19 20:36 | Claude | test | 4 cenarios smoke-tested: fake binary / real PNG / .exe / truncated PNG — comportamento correto em todos | - |
| 2026-04-19 18:00 | Codex | read | confirma SVGs oficiais da marca antes de derivar avatar social | static/img/logo-especias-primary.svg |
| 2026-04-19 18:00 | Codex | write | cria avatars PNG oficiais para WhatsApp e Instagram a partir da logo aprovada | static/img/brand/especias-del-paraguay/ |
| 2026-04-19 18:06 | Codex | read | usa monograma oficial do bundle da marca para refazer avatar social centralizado | static/img/brand/especias-del-paraguay/logo-especias-mark.svg |
| 2026-04-19 18:06 | Codex | write | cria avatar social centralizado em alta definicao a partir da marca oficial | static/img/brand/especias-del-paraguay/profile-avatar-ep-centered-hd.png |
| 2026-04-19 18:06 | Codex | write | remove avatar quadrado antigo com logo horizontal por pedido do usuario | static/img/brand/especias-del-paraguay/profile-avatar-logo-oficial.png |
| 2026-04-19 18:08 | Codex | read | usa lockup oficial completo para derivar avatar com escrita em alta definicao | static/img/logo-especias-primary.svg |
| 2026-04-19 18:08 | Codex | write | cria avatar quadrado com logo completa centralizada em alta definicao | static/img/brand/especias-del-paraguay/profile-avatar-logo-centered-hd.png |
