# Checkpoint - Meta Pixel + Conversions API (Hybrid Setup)

Date: 2026-04-19
Owner: Claude (Opus 4.7)
Phase: Tracking / Ads infra

## Why this exists

Usuario pediu trackeamento avancado de Meta com o maximo possivel de
capture. Pesquisa confirmou que em 2026 o padrao profissional e o
hybrid setup (Pixel + Conversions API com event deduplication). Este
checkpoint documenta o que foi implementado e como testar.

## Scope implemented (Nivel 2 — hybrid recomendado)

| Evento | Pixel (client) | CAPI (server) | Trigger |
|---|---|---|---|
| PageView | ✓ auto | — | Toda pagina |
| ViewContent | ✓ | — | Click em product-card (abre modal) |
| Contact | ✓ | ✓ | Click em link `wa.me` / botao flutuante |
| Lead | ✓ | ✓ | Submit do formulario `/contacto` |

Dedup via `event_id` compartilhado entre pixel e CAPI (janela de 48h).

## Advanced Matching

Em toda request CAPI sao enviados:

- `client_ip_address` (normalizado pelo primeiro item de `X-Forwarded-For`)
- `client_user_agent`
- `fbp` e `fbc` (cookies setados pelo Pixel)
- `external_id` (cookie first-party `_ep_eid`, UUID de 1 ano, setado pelo
  proprio backend)

No evento `Lead` (form de contato) sao adicionalmente hashados:

- `em` (email, opcional no form)
- `ph` (phone, obrigatorio — apenas digitos, hashado SHA-256)
- `fn` (name/empresa, obrigatorio)

## Files changed

### New
- `meta_capi.py` — helper modular com `send_capi_event`,
  `user_data_from_request`, `sha256_hash`, `normalize_phone`

### Modified
- `config.py` — novas env vars `META_PIXEL_ID`,
  `META_CAPI_ACCESS_TOKEN`, `META_TEST_EVENT_CODE`,
  `META_DOMAIN_VERIFICATION` (default `vxgeoxsdul1vqi8dkaws3db2fcplfp`)
- `requirements.txt` — adicionado `requests==2.32.3`
- `app.py`:
  - import de `meta_capi`
  - context processor `inject_meta_tracking` expoe pixel_id,
    domain_verification e `meta_page_event_id` (uuid hex por request)
  - `ensure_external_id_cookie` seta cookie `_ep_eid` em respostas HTML
  - `/contacto` POST agora dispara `Lead` via CAPI com dados do form
  - `/api/meta-capi-event` (POST JSON) endpoint companion para eventos
    client-side (Contact e outros)
- `templates/base.html` — meta tag `facebook-domain-verification` e bloco
  Meta Pixel base no `<head>`, condicionais a env var existir
- `templates/contacto.html` — hidden input `meta_event_id` no form
- `templates/index.html` e `templates/productos.html` — `data-name` no
  product card pra alimentar `content_name` do ViewContent
- `static/js/app.js`:
  - helpers top-level `epMetaEventId()` e `epMetaTrack(name, data, opts)`
  - WhatsApp click dispara `Contact` (pixel + CAPI via sendBeacon)
  - Form submit gera event_id, popula hidden input, dispara pixel
    `Lead` com `capi: false` (o server faz a parte CAPI via form POST
    com mesmo event_id)
  - Product card click dispara `ViewContent` (pixel only)

## Env vars que o usuario precisa setar na Railway

Railway Dashboard → Variables:

```
META_PIXEL_ID=615912274768763
META_CAPI_ACCESS_TOKEN=<access token recebido do usuario no chat>
META_DOMAIN_VERIFICATION=vxgeoxsdul1vqi8dkaws3db2fcplfp
```

Opcional (para debug inicial em Events Manager → Test Events):

```
META_TEST_EVENT_CODE=TEST12345
```

## Como testar

1. Apos deploy, em Events Manager → "Test Events", setar
   `META_TEST_EVENT_CODE=TEST12345` na Railway, abrir o site publico e
   interagir; eventos devem aparecer em tempo real.
2. Remover `META_TEST_EVENT_CODE` depois para entrar em producao.
3. Verificar "Events Overview" e "Event Match Quality" apos 24-48h.
4. Target EMQ: 6-8 com o form de contato preenchido (email+phone
   hashados entram); 3-5 sem form (so IP+UA+external_id+fbp+fbc).

## Privacidade

Paraguay nao tem GDPR, mas:
- Todos os PII (email, phone, name) sao hashados SHA-256 antes de sair
  do servidor
- Nunca enviamos raw PII para Meta
- Cookie `_ep_eid` e first-party, SameSite=Lax, max_age 1 ano
- Recomenda-se atualizar a politica de privacidade do site mencionando
  Meta Pixel + CAPI (nao bloqueador pra producao, mas boa pratica)

## Security note

O access token foi colado pelo usuario no chat desta sessao. Esta
gravado no transcript local em
`~/.claude/projects/.../*.jsonl`. Recomendacao:
rotacionar o token em Events Manager apos validar que o setup funciona.
O valor nao foi commitado em arquivo nenhum do repo.

## Decisoes tomadas

- Usar `requests` em vez de `facebook-business` SDK (mais leve, menos
  deps transitivas)
- Nao fazer CAPI PageView (low value; pixel ja captura PageView bem)
- CAPI so para Contact e Lead (eventos criticos de conversao)
- ViewContent pixel-only (suficiente pra remarketing audiences)
- Token via env var na Railway; nunca em codigo
- `sendBeacon` para evento WhatsApp (link abre aba nova, nao bloqueia)

## Next step

1. Usuario seta as 3 env vars na Railway.
2. Push + deploy automatico da Railway.
3. Verificar eventos no Events Manager.
4. Verificar dominio em Business Manager → Domains.
