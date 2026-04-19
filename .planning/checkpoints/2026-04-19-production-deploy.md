# Checkpoint - Production Deploy (Surface Rebrand)

Date: 2026-04-19
Owner: Codex
Phase: Surface rebrand shipping

## Goal

Enviar para producao o rebrand de superficie `Especias del Paraguay` junto com a memoria consolidada do projeto.

## Commits shipped to main

- `50e7732` feat: rebrand de superficie para Especias del Paraguay
- `147c97f` docs(planning): consolida memoria viva do rebrand em .planning/

## Remote

- Repo: https://github.com/jhonhenrique18/groasprincipal
- Range pushed: `9dc5f24..147c97f`
- Branch: `main`

## Deploy mechanism

Railway faz deploy automatico em todo push para `main`.
Nao ha pipeline intermediario: push para main = novo deploy.

## What went to production

- Marca visivel trocada no front publico para `Especias del Paraguay`
- Nova paleta (paprika + clove + sand) no CSS publico
- Logos aprovadas e pacote de variacoes fieis
- Favicon e icones PWA renovados com monograma `EP`
- Browser title da home atualizado (sem `Grãos S.A.` na aba)
- SEO tecnico continua intencionalmente ligado a `graos` nesta fase

## What stayed frozen on purpose

- Dominio `graos.com.py`
- Titles, meta, canonical, JSON-LD, sitemap, robots
- Slugs e estrutura de URL
- Camada invisivel de indexacao

## Next validation

- Confirmar que o deploy na Railway terminou sem erro
- Acessar o dominio publico e validar:
  - navbar mostra `Especias del Paraguay`
  - favicon com monograma `EP` aparece na aba
  - paleta nova aplicada
  - titles/meta continuam `Grãos S.A.` (intencional)
- Rodar um purge de cache do navegador se algum asset antigo ficar preso

## Notes

- Deploy autorizado explicitamente pelo usuario (push direto em main).
- Nenhum asset antigo foi removido; ambas as marcas coexistem nos arquivos
  enquanto a transicao de SEO nao entrar.
