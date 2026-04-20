# Checkpoint - Security 06: XSS fix no modal de produto

Date: 2026-04-19
Owner: Claude (Opus 4.7)
Phase: Security basics (item 6 de 7)

## Why this exists

Vuln V4: `openProductModal` em `static/js/app.js` montava o conteudo do
modal via concatenacao de strings em `box.innerHTML`, com dados do
produto (nome, descricao, origem, apresentacao, categoria, imagem)
vindos da API sem escape. Se um produto fosse criado com `<script>` no
nome ou descricao (deliberadamente pelo admin ou por erro), o script
executava pra todo visitante que abrisse o modal.

## What was done

Reescrita completa da funcao `openProductModal` usando DOM API:

- `document.createElement(...)` pra cada elemento
- `.textContent = p.xxx` pra todo dado vindo do servidor (escape automatico)
- `.src = p.image` e `.alt = p.name` via attribute setters (safe contra
  injecao de HTML)
- `encodeURIComponent(slug)` na URL do fetch (defense em depth)
- `isSafeImageUrl()` so aceita URLs comecando com `/` ou `https://`
  (rejeita `javascript:`, `data:`, etc — embora img tags nao executem JS
  URLs, e melhor ter filtro explicito)
- `target="_blank"` no WhatsApp link ganha `rel="noopener noreferrer"`
  (fix de tabnabbing)
- Unica parte com `innerHTML` e um SVG estatico em um span isolado, sem
  concatenacao com dado do servidor — marcado com comentario alertando
  contra regressao

Dois helpers adicionais:
- `setLoading(box, text)` pra estado de carregando
- `buildDetailRow(label, value)` pra as linhas de detalhe

## Testing

Sintaxe validada com `node -e "new Function(...)"`.

Validacao visual pos-deploy:
1. Abrir produto normal no modal → deve renderizar identico ao antes
2. Criar produto temporario com `<img src=x onerror=alert(1)>` no nome
   → modal deve mostrar o texto literal, sem executar script
3. WhatsApp link deve abrir com o nome corretamente

## What still uses innerHTML (and why it's safe)

- `icon.innerHTML = '<svg...>'` — SVG estatico, sem concatenacao com dado
  dinamico; segue pratica de keeping HTML inline apenas quando 100%
  trusted.

## Next step

Avanca pro item 7 (rate limits adicionais + honeypot).
