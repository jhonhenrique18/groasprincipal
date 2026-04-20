# Checkpoint - Security 03: Rate limit em /admin/login

Date: 2026-04-19
Owner: Claude (Opus 4.7)
Phase: Security basics (item 3 de 7)

## Why this exists

Vuln V3: `/admin/login` aceitava tentativas infinitas. Mesmo com hash
PBKDF2 (item 1) + SECRET_KEY (item 2), um atacante com tempo suficiente
consegue brute-force de dicionario pra senhas fracas.

## What was done

### `requirements.txt`
- `+ Flask-Limiter==3.8.0`

### `app.py`
- Import `Limiter`, `get_remote_address`
- Inicializacao do `limiter` com `default_limits=[]` (sem limite global,
  so per-route explicito), storage `memory://`
- `/admin/login` decorado com `@limiter.limit('5 per 15 minutes', methods=['POST'])`
  - GET (carregar form) nao e limitado — UX intacta
  - POST limitado a 5 tentativas por IP em janela de 15 minutos
  - Excedeu: HTTP 429 Too Many Requests

## Trade-offs conhecidos

- **Storage em memoria**: funciona em single-instance. Se no futuro
  escalar pra multi-worker/multi-instance, cada replica tem seu proprio
  contador. Fix: trocar para Redis (`storage_uri='redis://...'`).
- **Por IP**: atacante com botnet distribuido passa do limite. Mitigacao
  de ataque basico (90%+ dos cases), nao de APT.
- **Nao limita por usuario**: atacante pode tentar usuarios diferentes
  ilimitadamente. Aceitavel porque nosso admin tem apenas 1 usuario.

## Testing

Syntax OK (flask-limiter nao instalado local mas sintaxe e padrao).
Smoke test real so roda apos Railway build (pip install resolve
Flask-Limiter).

Post-deploy, validacao manual:
- 5 logins errados seguidos → na 6a tentativa deve vir 429

## Next step

Avanca pro item 4 (CSRF via Flask-WTF).
