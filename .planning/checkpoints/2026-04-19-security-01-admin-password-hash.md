# Checkpoint - Security 01: Admin Password Hash

Date: 2026-04-19
Owner: Claude (Opus 4.7)
Phase: Security basics (item 1 de 6)

## Why this exists

Item 1 do plano de seguranca basica que o usuario aprovou. Objetivo
unico: eliminar senha de admin em plaintext (env var + default
`graos2026` em `config.py`), trocando por hash PBKDF2-SHA256 na DB.

Checkpoints separados por item a pedido do usuario — ele valida cada
um antes de avancar pro proximo.

## What was done

### `config.py`
- Removida a linha `ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'graos2026')`
- O `ADMIN_USERNAME` continua em config.py como antes
- A env var `ADMIN_PASSWORD` ainda e lida pela app, mas *apenas* pelo
  bootstrap em `ensure_admin_password_hash`, nunca para autenticacao
  direta

### `app.py`
- Import de `werkzeug.security.generate_password_hash` e
  `check_password_hash`
- Nova funcao `ensure_admin_password_hash()`:
  - Se ja existe `admin_password_hash` em `SiteSetting` → no-op
  - Se nao existe e `ADMIN_PASSWORD` env var esta setado → hasha com
    `pbkdf2:sha256:600000` (600k iteracoes, recomendacao OWASP 2023+)
    e salva na DB
  - Se nao existe e env var vazio → log warning, admin login fica
    indisponivel (fail closed)
- Chamada dentro de `init_db()`, fora do bloco de seed, roda em todo
  boot (idempotente)
- `admin_login` agora compara `check_password_hash(stored_hash, password)`

### Porque PBKDF2-SHA256 e nao scrypt/argon2

- Werkzeug moderno usa scrypt por default, mas o ambiente local do
  usuario tem Python 3.9 com LibreSSL, que nao expoe `hashlib.scrypt`.
  Forcar scrypt quebraria dev local.
- PBKDF2 esta na stdlib de qualquer Python, e 100% portable.
- Com 600k iteracoes + rate limit no login (proximo item do plano),
  a resistencia a brute force online e suficiente para um admin de
  site B2B de pequeno porte.
- Se no futuro quisermos upgrade, werkzeug permite regenerar hash no
  proximo login sem migracao — basta trocar o parametro e checar
  `hash.startswith('pbkdf2:...')` para regerar.

## Migration path (sem downtime)

Primeira Railway deploy apos este commit:

1. App sobe com nova versao do codigo
2. `init_db()` → `ensure_admin_password_hash()` roda
3. Le `ADMIN_PASSWORD` da env var Railway (que ainda esta la)
4. Gera hash PBKDF2 e salva em `SiteSetting('admin_password_hash')`
5. Log de INFO: "Admin password hashed and persisted; ADMIN_PASSWORD
   env var may now be removed"
6. Usuario faz login normalmente com a mesma senha — agora via hash
7. Depois do login confirmado, usuario REMOVE `ADMIN_PASSWORD` da
   Railway (nao e mais necessario)

Se a DB for resetada no futuro e a env var `ADMIN_PASSWORD` ainda
estiver la, o bootstrap reseed cuida sozinho. Se ambos forem perdidos,
admin fica trancado com warning no log — e o modo seguro de falhar.

## Testing

Smoke test local (python3 script in bash):

- Bootstrap com env var → hash gerado e salvo → senha valida
- Senha errada rejeitada
- Hash nao contem plaintext
- Formato `pbkdf2:sha256:600000$...`
- Idempotencia: segundo call nao altera hash
- Lockout: sem env var + sem hash → nao seeda plaintext, loga warning

Todos os 3 casos passaram.

## What is NOT in this checkpoint

Intencional — esperar aprovacao do usuario antes de cada item seguinte:

- Item 2: SECRET_KEY sem default
- Item 3: rate limit no /admin/login
- Item 4: upload descarta arquivos que nao sao imagens validas
- Item 5: CSRF em todos os forms
- Item 6: honeypot + rate limit no /contacto

## User action required (pos-deploy)

1. Esperar Railway build ficar SUCCESS
2. Fazer login no admin (`/admin/login`) com as credenciais atuais
3. Confirmar que funciona
4. **Remover** `ADMIN_PASSWORD` das variaveis da Railway (Variables →
   deletar). A aplicacao nao precisa mais dela.
5. Opcionalmente, trocar a senha: como nao temos UI de troca ainda, o
   caminho e: setar `ADMIN_PASSWORD` nova, ir na Railway shell e rodar
   `from app import SiteSetting, db; SiteSetting.query.filter_by(key='admin_password_hash').delete(); db.session.commit()`,
   reiniciar o service — o bootstrap vai re-hashear a nova senha.
