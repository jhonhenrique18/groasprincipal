# Checkpoint - SEO Fase D: 10 guías editoriales para topic clusters

Date: 2026-05-03
Owner: Claude (Opus 4.7)
Phase: SEO breadth — Fase D (Long-form editorial content)

## Why this exists

Usuario pediu "criar páginas tipo blog para os 10 produtos principais"
para dominar SEO de Paraguay. Decisão estratégica do dev: cada guia
funciona como hub editorial que internamente linka para a página de
produto canônica (/producto/<slug>), criando topic clusters que elevam
toda a categoria saudável do site.

Este é o PHASE D do plano de 4 fases originalmente desenhado:
- Fase A (feita): keyword breadth nas páginas de produto.
- Fase B (pendente): search server-side com normalização.
- Fase C (pendente): FAQPage + HowTo nas páginas de produto.
- **Fase D (esta): 10 guias editoriais long-form.**

## Strategic lock

- 10 produtos selecionados pela combinação de volume de busca + valor B2B:
  Manzanilla, Canela, Cúrcuma, Hibisco, Spirulina, Quinoa, Chía, Cacao
  Alcalino, Anís Estrellado, Clavo de Olor.
- Cada guia ~1100-1500 palavras (atingido: 1304 palavras médias).
- Cada guia rankeia para QUERIES INFORMACIONAIS ("para qué sirve la X",
  "cómo preparar X") E B2B ("X al por mayor", "comprar X paraguay"),
  capturando ambos intents na mesma URL.
- Sales funnel embutido: cada guia termina com CTA pro produto canônico
  + WhatsApp.
- Marca SEO `Grãos S.A.` preservada como autor/publisher em todo Article
  schema. Nenhuma quebra de freeze.

## What was done

### Conteúdo (guias_data.py — 1325 linhas, 12k palavras curadas)

Cada uma das 10 guides tem:
- Título editorial longo (50-75 chars no H1, otimizado para featured
  snippets e content depth).
- Dek (subtítulo descritivo com keyword secundária).
- meta_title curto (50-60 chars) e meta_description (155-160 chars).
- Intro com lead paragraph (~250 palavras, drop-cap visual).
- 5 sections HTML estruturadas (¿Qué es?, Beneficios, Usos industria,
  Cómo preparar, Presentaciones).
- HowTo schema embutido em "Cómo preparar" com steps numerados.
- 6-7 FAQ entries (alimentam FAQPage schema).
- Lista de related_slugs para internal linking de topic cluster.

### Infraestrutura (app.py)

- Routes: GET /guias (listing), GET /guias/<slug> (detail).
- Sitemap.xml inclui as 10 guides com priority 0.85, changefreq monthly.
- Hidratação eager: cada guide carrega seu Product relacionado para
  imagem, aliases e CTA. Se o produto está inativo, gera 404 grácil.

### Templates (templates/guias/)

- `index.html`: hero editorial com gradient brand, grid de cards com
  treatment visual por categoria (warm/berry/green/earth), CTA band
  para WhatsApp.
- `article.html`: hero dramatic com produto image em mix-blend-mode,
  sticky TOC desktop com CTA produto inline, drop-cap intro, sections
  com section-heading + paprika underline, HowTo box com numbered steps,
  inline product CTA com gradient brand, FAQ accordion (details/summary),
  related guides feed, closing CTA band.
- Schema stack por página: Article + FAQPage + HowTo + BreadcrumbList,
  além dos 2 do base.html (Organization + WebSite). Total 6 por página.

### CSS editorial (static/css/style.css +420 linhas)

- Reading progress bar fixed top.
- Drop cap 5.6em paprika no primeiro parágrafo do intro.
- Hero treatments: warm (clove→paprika), berry (4A0E1A→7A1F2E),
  green (1F2F1F→4A6B3F), earth (3F2A24→8C6B3A).
- Mix-blend-mode luminosity nas imagens para integração com gradient.
- TOC sidebar sticky com border-left paprika.
- HowTo box com card ivory + step circles paprika.
- FAQ accordion com summary::after rotativo (+ → ×).
- Mobile responsive até 760px.

### Navegação

- Link "Guías" no navbar entre Productos e Nosotros.
- Link "Guías" no footer Mapa del Sitio.

## Validação (smoke test local)

- 10/10 guides retornam 200.
- 60 blocos JSON-LD válidos no total (6 por página × 10 páginas).
- Manzanilla guide: title 49 chars, meta description 158 chars,
  Article wordCount 1600, keywords com todos os 8 aliases curados,
  about apontando pro Product@id correto, 7 FAQs, 4 HowTo steps,
  body real 1304 palavras.
- Sitemap inclui as 10 guides corretamente.
- Internal link /producto/manzanilla-flor presente em Manzanilla guide
  (e equivalente em cada uma).

## Decisions made

1. **Single Python module para conteúdo** (guias_data.py) em vez de
   CMS/DB: versionável em git, revisável em PR, sem moving parts.
2. **Guide slug = product slug**: trivial topic cluster mapping.
3. **Templates não compartilhados com produtos**: produto e guia têm
   intents diferentes (commercial vs informational); JSON-LD distinto.
4. **CTA editorial obrigatório**: cada guia termina apontando pra
   produto + WhatsApp. Conversão é a métrica final.
5. **Imagens existentes do produto reaproveitadas com tratamento CSS**:
   sem dependência de IA generativa; visual surreal vem do gradient,
   mix-blend-mode e tipografia, não da foto em si. Substituível depois.
6. **Hreflang non-tocado**: guides usam o mesmo `es-PY` do site.

## What was rejected

- **Gerar imagens AI via fal-ai/MCP**: API não acessível diretamente
  nesta sessão. Decidido reaproveitar fotos de produto existentes com
  tratamento CSS dramático. Pode ser substituído quando user gerar AI.
- **Slug separado tipo /blog/<slug>**: rejeitado, /guias/ é mais
  específico ao posicionamento editorial e cluster por produto.
- **Article cross-canonical com /producto/**: rejeitado. Guide e produto
  têm intents distintos; canonicalizar um pro outro perde rankings.
- **CMS WordPress/headless**: rejeitado, complexidade desnecessária para
  10 entradas curadas.

## Next step

Push (com autorização do usuario) ou seguir para Fase B (search
server-side com normalização accent-strip + alias-aware) ou Fase C
(FAQPage + HowTo nas páginas de produto).
