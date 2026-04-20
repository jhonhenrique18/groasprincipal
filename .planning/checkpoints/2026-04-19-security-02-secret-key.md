# Checkpoint - Security 02: SECRET_KEY sem default

Date: 2026-04-19
Owner: Claude (Opus 4.7)
Phase: Security basics (item 2 de 7)

## Why this exists

Vuln V1 do audit: `config.py:4` tinha
`SECRET_KEY = os.environ.get('SECRET_KEY', 'graos-sa-secret-key-change-in-production')`.

Railway NAO tinha SECRET_KEY setada, entao producao rodou com esse
default desde sempre. Quem leia o repo (open source) pode forjar cookie
de sessao de admin e entrar sem saber a senha.

## Pre-step: fechou vuln ativa antes do commit

Setei via Railway API:
- `SECRET_KEY=<64 hex random>` (256 bits de entropia)
- `ADMIN_PASSWORD=graos2026` (restaura o comportamento do default
  anterior, evitando lock do admin quando o deploy do item 1 terminar)

## What was done

### `config.py`
- Removido default inseguro
- Adicionado fallback seguro **apenas para dev local** (sem DATABASE_URL
  → gera `secrets.token_hex(32)` por processo)
- Em prod (DATABASE_URL setado via Railway reference), sem SECRET_KEY
  retorna string vazia — pra ser rejeitado no proximo passo

### `app.py`
- Logo apos `app.config.from_object(Config)`: raise `RuntimeError`
  se `SECRET_KEY` estiver vazio
- App nao sobe em prod sem SECRET_KEY; logs de Railway mostram erro
  claro e acao obvia

## Testing

3 casos testados via subprocess:
1. Prod-like (DATABASE_URL set, SECRET_KEY missing) → config retorna ''
   e app.py levanta `RuntimeError: SECRET_KEY environment variable is
   required in production`
2. Dev (no DATABASE_URL, no SECRET_KEY) → auto-gerado 64 hex
3. SECRET_KEY explicito → usa o valor

## Impacto imediato em producao

- Sessoes de admin existentes foram invalidadas no momento em que setei
  a nova SECRET_KEY (cookie antigo nao valida com chave nova).
- Proximo login do admin usa a nova chave + hash PBKDF2 do item 1.

## Next step

Avanca pro item 3 (CSRF via Flask-WTF).
