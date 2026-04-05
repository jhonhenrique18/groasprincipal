# Grãos Institucional

## What This Is

Site institucional e catálogo B2B da Grãos S.A., importadora e distribuidora de produtos naturais no Paraguai. Apresenta o catálogo de 112+ produtos organizados em 9 categorias, com integração WhatsApp para pedidos. Flask + PostgreSQL, deploy na Railway.

## Core Value

Catálogo de produtos atualizado e acessível que converte visitantes em contatos de WhatsApp para vendas B2B ao por mayor.

## Requirements

### Validated

- ✓ Catálogo de 112 produtos com 9 categorias — existente
- ✓ Painel admin CRUD (produtos, categorias, configurações) — existente
- ✓ SEO completo (sitemaps, Schema.org, Open Graph, GA4) — existente
- ✓ Integração WhatsApp para contato/pedidos — existente
- ✓ Upload de imagens com cache otimizado — existente
- ✓ Design responsivo (desktop + mobile) — existente
- ✓ Sidebar de categorias no desktop com contagem — existente
- ✓ Filtros mobile com chips horizontais scrolláveis — existente
- ✓ Busca de produtos por nome — existente

### Active

- [ ] Completar imagens e presentations dos 57 novos produtos
- [ ] Otimizar imagens de produto (WebP, lazy loading)
- [ ] Adicionar produtos restantes da Curva ABC

### Out of Scope

- E-commerce / carrinho de compras — modelo é B2B via WhatsApp
- Sistema de usuários/login público — admin-only
- Blog / conteúdo — foco é catálogo

## Context

- Deploy automático via Railway (push to main = deploy)
- PostgreSQL em produção, SQLite em desenvolvimento
- Produtos baseados na Curva ABC de vendas reais
- Site em espanhol (público paraguaio)
- Importação direta de 16+ países

## Constraints

- **Tech stack**: Flask/Python — manter simplicidade, sem SPA
- **Hosting**: Railway — volume persistente para uploads
- **Idioma**: Espanhol para todo conteúdo público

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Sidebar categorias no desktop | 9 categorias não cabem em chips horizontais; sidebar mostra todas com contagem | ✓ Good |
| Chips mobile horizontais | Scroll horizontal é padrão mobile; nomes curtos para caber | ✓ Good |
| Seed inline no init_db | Evita import circular seed.py/app.py | ✓ Good |
| Produtos da Curva ABC | Priorizar produtos de maior valor de venda real | ✓ Good |
| Presentations pesquisadas | Cada produto com embalagem real do mercado atacadista | ✓ Good |

---
*Last updated: 2026-04-05 after catalog expansion + UI redesign*
