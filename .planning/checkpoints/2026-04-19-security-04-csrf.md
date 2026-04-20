# Checkpoint - Security 04: CSRF em todos os forms

Date: 2026-04-19
Owner: Claude (Opus 4.7)
Phase: Security basics (item 4 de 7)

## Why this exists

Vuln V2: nenhum form tinha CSRF token. Admin logado em outra aba poderia
ser induzido a executar acoes (deletar produto, mudar settings, enviar
form fake) atraves de site externo malicioso.

## What was done

### `requirements.txt`
- `+ Flask-WTF==1.2.1`

### `app.py`
- Import de `CSRFProtect`
- `csrf = CSRFProtect(app)` ativa protecao global em todo POST/PUT/PATCH/DELETE
- `/api/meta-capi-event` marcado com `@csrf.exempt` (chamado via
  `navigator.sendBeacon`, que nao suporta headers custom e nao tem sessao
  admin envolvida; rate limit de 60/min cobre abuse)

### Templates patched (7 forms)
Cada `<form method="POST">` ganhou logo na primeira linha:
```
<input type="hidden" name="csrf_token" value="{{ csrf_token() }}">
```

- `templates/admin/login.html`
- `templates/admin/product_form.html`
- `templates/admin/category_form.html`
- `templates/admin/products.html` (form inline de delete)
- `templates/admin/categories.html` (form inline de delete)
- `templates/admin/settings.html`
- `templates/contacto.html`

## Routes não-POST (sem CSRF necessário)

- `/admin/migrate-images` → GET, idempotente na pratica (re-seed safe)
- `/admin/logout` → GET. Baixo risco (CSRF logout so causa inconveniencia).
  Melhorar pra POST com CSRF e um item futuro.

## Testing

- Sintaxe Python OK
- Jinja parse OK em todos os 7 templates
- Smoke test funcional (roundtrip GET form → POST com token → 200)
  requer Flask-WTF instalado, que so resolve no build Railway

Post-deploy sanity check:
1. Tentar POST em `/admin/login` com token valido → login normal
2. Tentar POST sem token → HTTP 400 "The CSRF token is missing"
3. Tentar `curl` direto em `/contacto` com form data sem token → 400
4. Modal de produto / WhatsApp click / form submit continuam funcionando
   (todos ja tem token server-rendered via template)

## Trade-offs conhecidos

- CSRF token tem TTL = tempo da sessao. Se usuario deixar aba aberta
  por 1 dia, pode receber 400. Reload do form resolve.
- Form de contato publico: token fica em HTML cached. Se o navegador
  cachear a pagina por muito tempo, token velho expira. Com
  `Cache-Control: public, max-age=300` (5 min) do app, nao vai ser
  problema.

## Next step

Avanca pro item 5 (upload verify image).
