# Checkpoint - Context Consolidation

Date: 2026-04-19
Owner: Codex
Phase: Rebrand memory hardening

## Why this checkpoint exists

O usuario pediu que o projeto nunca perca contexto.
Este checkpoint consolida a memoria da sessao de rebrand e formaliza como a pasta `.planning/` deve ser usada daqui para frente.

## Session Summary

### Business rule approved

- A marca visivel do site mudou para `Especias del Paraguay`
- O dominio `graos` e a maior parte da camada SEO tecnica continuam em transicao

### Rebrand path approved

- Esta fase e um **surface rebrand**
- O usuario pode encontrar o site por `Grãos S.A.`, mas ao entrar deve ver a nova marca

### Brand execution summary

- logo publica aplicada
- paleta publica aplicada
- textos visiveis principais ajustados
- browser title da home ajustado por pedido do usuario
- favicon ajustado em iteracoes para legibilidade real

### Rejected path that must remain documented

- criacao de um kit de marca paralelo que nao batia com a logo aprovada
- criacao de manual proprio fora do que o usuario aprovou

## Final source of truth after correction

- `static/img/logo-especias-primary.svg`
- `static/img/logo-especias-reverse.svg`

Todas as variacoes futuras devem partir desses arquivos.

## Documentation rules agreed

Toda mudanca relevante deve atualizar:

- `PROJECT.md`
- `STATE.md`
- pelo menos um checkpoint em `.planning/checkpoints/`
- `CONTEXT.md` quando a leitura global do projeto mudar

## Outcome

A memoria do projeto agora ficou dividida assim:

- `PROJECT.md`: regras e decisoes duraveis
- `STATE.md`: foco atual e ponto de retomada
- `CONTEXT.md`: leitura viva do projeto e do rebrand
- `checkpoints/`: linha do tempo e evidencias de decisao
