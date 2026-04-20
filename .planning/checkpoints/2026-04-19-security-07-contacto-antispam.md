# Checkpoint - Security 07: Anti-spam no /contacto (rate limit + honeypot)

Date: 2026-04-19
Owner: Claude (Opus 4.7)
Phase: Security basics (item 7 de 7 — fecha o bloco)

## Why this exists

Vulns V6 e V7: `/contacto` nao tinha rate limit nem honeypot. Quando o
form comecar a entregar de verdade (futuro item — email/webhook), bots
enchem trivialmente. Tambem, o `/api/meta-capi-event` sem rate limit
permitiria flood que polui EMQ da Meta.

O item 4 (CSRF) ja adicionou `@limiter.limit('60 per minute')` no
`/api/meta-capi-event`. Este checkpoint fecha o `/contacto`.

## What was done

### `app.py`
- `/contacto` decorado com `@limiter.limit('3 per 10 minutes', methods=['POST'])`
  - GET (carregar pagina) nao e limitado
  - POST: 3 submissoes por IP a cada 10 min
- Honeypot check dentro do POST:
  ```python
  if request.form.get('website'):
      app.logger.info('contacto: honeypot tripped from %s', request.remote_addr)
      flash('Mensaje enviado con éxito...', 'success')
      return redirect(url_for('contacto'))
  ```
  Acao silenciosa — bots recebem resposta normal, nao aprendem que
  foram detectados.

### `templates/contacto.html`
- Campo honeypot invisivel adicionado ao form:
  ```html
  <div aria-hidden="true" style="position:absolute;left:-10000px;...">
      <label for="website">No llenar este campo</label>
      <input type="text" id="website" name="website" tabindex="-1" autocomplete="off">
  </div>
  ```
  - `position:absolute;left:-10000px` em vez de `display:none` (bots
    sofisticados detectam display:none)
  - `tabindex="-1"` pra nao aparecer na navegacao por tab do usuario
  - `aria-hidden="true"` pra leitores de tela ignorarem
  - `autocomplete="off"` pra o navegador nao preencher automaticamente

## Expected behavior

- Humano: nao ve o campo, nao preenche, passa no check
- Bot simples: preenche todos os campos incluindo `website`, e silenciosamente
  descartado
- Bot sofisticado: preenche so campos visiveis, passa no honeypot, mas cai
  no rate limit (3/10min) depois de poucos submits

## Testing

Sintaxe OK.

Pos-deploy manual:
1. Submit normal do form → chega como Lead na Meta
2. Submit com `website=anything` → retorna sucesso (UI), mas log mostra
   "honeypot tripped" e nenhum Lead e enviado pra Meta
3. 4 submits em 10 min do mesmo IP → 4o retorna HTTP 429

## Status do pacote de seguranca basica (itens 1-7)

| # | Vuln | Status |
|---|---|---|
| V1 | SECRET_KEY default | ✅ Fixed (checkpoint 02) |
| V2 | CSRF ausente | ✅ Fixed (checkpoint 04) |
| V3 | Brute force login | ✅ Fixed (checkpoint 03) |
| V4 | XSS modal produto | ✅ Fixed (checkpoint 06) |
| V5 | Upload fallback inseguro | ✅ Fixed (checkpoint 05) |
| V6 | Rate limit /api/meta-capi-event | ✅ Fixed (checkpoint 04, dentro do CSRF) |
| V7 | /contacto sem anti-spam | ✅ Fixed (este checkpoint) |

Bonus ja fechado em sessao anterior:
- Admin password plaintext → hash PBKDF2 (checkpoint 01)

## User action required

1. Validar deploy final na Railway (ultimo commit ship)
2. Testar login admin (graos2026 continua valido; hash persistido pelo
   bootstrap do item 1 deve permitir)
3. Remover `ADMIN_PASSWORD` da Railway Variables (nao e mais necessario)
4. Rotar o CAPI access token + deletar o "token claude" do Railway
   (higiene de credenciais expostas no transcript)
5. **Limpar** as imagens nao usadas em `static/img/brand/` que nao
   foram commitadas (arquivos `?? ` no git status — `.DS_Store` e
   profile avatars)

## Next

Se quiser mais seguranca alem dos basicos, proximos candidatos:
- Content-Security-Policy header (V9 do audit original)
- Dependabot / Sentry (V11/V12)
- Session cookies explicitos (V8)
- Flask-Migrate para schema changes (futuro)
