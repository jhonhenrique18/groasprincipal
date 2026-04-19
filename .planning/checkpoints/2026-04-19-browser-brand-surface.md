# Checkpoint - Browser Brand Surface

Date: 2026-04-19
Owner: Codex
Phase: Surface rebrand approval

## Goal

Atualizar a camada visível do navegador para a nova marca sem mexer no restante do SEO técnico.

## Changes

- Título da home no navegador agora fica apenas `El Mayor Proveedor de Productos Naturales del Paraguay`
- `Grãos S.A.` foi removido do texto da aba na página inicial
- Favicon passou a usar o monograma aprovado `EP`
- Ícones derivados criados para navegador e app:
  - `static/favicon-especias-16x16.png`
  - `static/favicon-especias-32x32.png`
  - `static/apple-touch-icon-especias.png`
  - `static/android-chrome-especias-192x192.png`
  - `static/android-chrome-especias-512x512.png`

## Files Touched

- `templates/base.html`
- `templates/index.html`
- `app.py`
- `static/manifest.json`

## Notes

- O restante da camada SEO antiga continua preservado.
- Foi usado versionamento no `href` dos favicons para reduzir efeito de cache no navegador local.
- O primeiro favicon aprovado tecnicamente carregava, mas perdia leitura por ser um reaproveitamento do lockup horizontal.
- A versão final passou a usar um selo claro com `EP` ampliado para destaque imediato em abas e bookmarks.
- Depois disso, a logo principal também foi refinada para remover a barra inferior, aumentar o `EP` e endurecer a paleta, mantendo a mesma identidade aprovada.
- Em seguida, o favicon foi refinado mais uma vez para uma composição ainda mais limpa, sem moldura e com melhor espaçamento, porque a versão anterior ainda parecia apertada na aba.
