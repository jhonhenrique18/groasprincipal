# Grãos Institucional

See also: `.planning/CONTEXT.md`

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

- [ ] Rebrand completo da marca pública, substituindo “Grãos S.A.” por nova identidade aprovada
- [ ] Executar primeiro um rebrand de superfície, mudando apenas a marca visível e preservando toda a camada SEO atual ligada a “Grãos”
- [ ] Consolidar no front os exports finais da logo já aprovada de `Especias del Paraguay`
- [ ] Ajustar refinamentos finais da identidade visual pública de `Especias del Paraguay` após revisão no localhost
- [ ] Planejar migração de marca, domínio, assets e dados estruturados sem perder contexto do projeto
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
- A marca “Grãos S.A.” não poderá seguir no site; será necessário rebrand controlado
- O objetivo do rebrand é trocar a marca sem quebrar SEO, catálogo nem operação comercial
- Fase atual: manter o domínio `graos` e os sinais SEO já funcionando; trocar apenas a marca visível no site
- Nesta fase, tudo o que é invisível para o usuário final deve permanecer intacto para não afetar indexação e continuidade comercial
- Migração de domínio e SEO para a nova marca será tratada depois, em uma etapa separada
- A pasta `.planning/` e a memoria oficial do projeto; nenhuma decisão relevante deve depender apenas do chat

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
| Rebrand antes de novas mudanças visuais | Evita retrabalho e garante que SEO/ativos sejam ajustados uma vez só | ✓ Good |
| Rebrand de superfície sem tocar no invisível | Minimiza risco operacional agora; a nova marca aparece visualmente, enquanto domínio/SEO/slugs continuam intactos | ✓ Good |
| Nome visível aprovado: Especias del Paraguay | Remove dependência imediata de `Grãos S.A.` na interface sem tocar ainda na camada técnica invisível | ✓ Good |
| A logo já aprovada no site vira a fonte de verdade da marca | Evita retrabalho e impede desvio visual em relação ao que o usuário validou | ✓ Good |
| Variações devem sair do asset aprovado, não de uma reinterpretação | O pacote anterior foi rejeitado por fugir da identidade escolhida | ✓ Good |
| Browser title e favicon podem acompanhar a marca visível | O usuário pediu remover `Grãos S.A.` da aba e trocar o ícone para a identidade aprovada | ✓ Good |
| Favicon precisa ser tratado como asset de legibilidade, não só um export do logo | O monograma horizontal original ficava escuro e pequeno demais em 16x16 | ✓ Good |
| A logo principal pode ser refinada manualmente sem mudar de linguagem | O usuário aprovou a base, mas pediu menos cara de IA e mais presença institucional | ✓ Good |
| A pasta `.planning/` deve guardar o contexto operacional do projeto | O usuário quer continuidade entre agentes e retomada sem perda de memória | ✓ Good |
| Meta tracking em hybrid setup (Pixel + Conversions API) com dedup por event_id | Pixel puro perde 20-40% em 2026; hybrid é o padrão profissional | ✓ Good |
| Credenciais Meta (CAPI token) vivem apenas em env var na Railway | Token foi exposto no chat; não pode ir pro repo; rotação recomendada | ✓ Good |
| CAPI apenas em eventos críticos (Contact, Lead); ViewContent pixel-only | Foco em conversão; minimiza latência e ruído de sinais | ✓ Good |
| Advanced matching hasheia email/phone/name via SHA-256 antes do envio | Requisito Meta + privacidade; target EMQ 6-8 no form de contato | ✓ Good |

---
*Last updated: 2026-04-19 after Meta Pixel + CAPI implementation*
