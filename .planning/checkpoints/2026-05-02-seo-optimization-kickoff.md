# Checkpoint - SEO optimization kickoff (additive over Grãos baseline)

Date: 2026-05-02
Owner: Claude (Opus 4.7)
Phase: SEO breadth — Fase A (Foundation)

## Why this exists

Usuario abriu uma sessão pedindo otimização SEO avançada. O problema concreto:
o site ranqueia bem em pesquisa exata ("manzanilla flor" → aparece) mas não
ranqueia em queries genéricas ("manzanilla" → não aparece). Cada produto
tem nome ultra-específico, e o SEO inteiro (title, h1, JSON-LD) espelha
apenas essa variação literal, sem sinônimos, nomes científicos ou variações
de busca.

Este checkpoint marca a abertura do bloco e registra a decisão estratégica
de fazer otimização **additive**: nada do que ranqueia hoje muda, só
empilhamos camadas de keyword breadth.

## Strategic lock

Decidido na conversa atual com o usuario:

- Domínio `graos.com.py` permanece (não há plano de migração agora).
- Marca SEO `Grãos S.A.` permanece (Organization schema, OG, titles, meta).
- Marca visível `Especias del Paraguay` permanece (front público já rebrand).
- Slugs e canonicals NÃO mudam — preservar URLs já indexadas.
- Sitemap NÃO muda na estrutura.

Isto **NÃO** é uma quebra do freeze definido em AGENT_RULES.md Regra 7:
o freeze proibia "mexer em titles, meta, canonical, JSON-LD, sitemap,
robots ou slugs". Aqui:
- canonicals: intocados.
- sitemap: intocado.
- robots: intocado.
- slugs: intocados.
- titles, meta, JSON-LD: ENRIQUECIDOS, mas mantendo o conteúdo `Grãos S.A.`
  que ranqueia hoje. Brand SEO continua na frente, breadth vem por trás.

A diferença prática: hoje uma página de produto tem `<title>Manzanilla Flor |
El Mayor...</title>`. Depois fica algo como `<title>Manzanilla Flor —
Manzanilla en Flor (Camomila) | El Mayor...</title>`. O brand continua
intacto, só ganhou keyword breadth.

## What was done in this checkpoint

- Análise técnica completa de:
  - `templates/base.html` (head, schema Organization, hreflang, OG, geo)
  - `templates/productos.html` (listing + categoria)
  - `templates/producto.html` (detalhe)
  - `app.py` (rotas, sitemap, robots)
  - `models.py` (Product, Category, SiteSetting)
  - `seed_data.json` (112 produtos × 9 categorias mapeados)
- Identificado o gap de breadth como causa raiz das queries genéricas
  não ranquearem.
- Plano de 4 fases construído:
  - Fase A (hoje): Foundation — campos novos no Product, aliases curados,
    JSON-LD enriquecido, title/meta com breadth.
  - Fase B: Search server-side com normalização e match alias-aware.
  - Fase C: FAQPage + HowTo schema + intro enriquecido em categorias.
  - Fase D: `/guias/` editorial com Article schema.
- Decisão registrada na tabela Key Decisions de PROJECT.md.

## Decisions made

1. SEO optimization é **additive**, nunca destrutiva. Nada que ranqueia
   hoje sai do site.
2. Cada produto recebe quatro campos novos (`aliases`, `scientific_name`,
   `seo_title_override`, `seo_description_override`).
3. Aliases ficam curados em `seed_data.json` para serem seedados em
   ambientes novos e revisáveis em PR.
4. Brand SEO segue `Grãos S.A.` em title pattern, OG, schema. Nenhuma
   substituição.
5. `/buscar` vai existir como rota server-side própria; o filter JS atual
   no productos.html vira fallback ou redirect.

## What was rejected

- Migrar marca SEO para `Especias del Paraguay`: rejeitado nesta fase por
  causar dip de ranking sem ganho compensatório imediato.
- Trocar slugs (ex: `/producto/manzanilla` em vez de `/producto/manzanilla-flor`):
  rejeitado, quebra URLs indexadas. Em vez disso, aliases entram no SEO
  da mesma URL.
- Adicionar AggregateRating com dados sintéticos: rejeitado, schema sem
  base real é anti-pattern e pode levar a manual action no GSC.

## Next step

Iniciar FASE A1: adicionar colunas ao Product model e migration script
idempotente. Em seguida A2 (curadoria de aliases no seed_data.json) e
A4 (rewrite de templates). Smoke test local antes de commit.
