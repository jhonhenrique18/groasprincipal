# Checkpoint - Deploy 26 guias editoriais em produção

Date: 2026-05-03
Owner: Claude (Opus 4.7)
Phase: SEO Fase D extended — Deploy

## Why this exists

Usuário autorizou explicitamente push para produção via mensagem
"agora coloque em producao faca fit". Este checkpoint registra o
estado do código no momento do deploy e o que vai pra Railway.

## What was deployed

### 26 guias editoriais long-form (de 0 para 26 nesta sessão)

**Tier 1 — produto-guias canônicas (10):**
1. Manzanilla Flor (chamomile, hierbas digestivas)
2. Canela en Rama 6cm (panificação, bebidas, vietnamita)
3. Cúrcuma en Polvo (golden latte, suplementos)
4. Hibisco Flor (jamaica, coctelería, bebidas funcionais)
5. Spirulina en Polvo (proteína vegetal completa)
6. Quinoa en Grano (sin gluten, peruana)
7. Chía en Semillas (omega-3, panificação funcional)
8. Cacao Alcalino en Polvo (repostería industrial)
9. Anís Estrellado (panificação, licorería)
10. Clavo de Olor (chacinas, conservas, vino caliente)

**Tier 2 — produto-guias adicionadas com forte ângulo PY (11):**
11. Comino en Grano (asado paraguayo, chimichurri)
12. Comino en Polvo (industrial chacinas)
13. Pimienta del Reino en Polvo
14. Semilla de Anís ★ KILLER pra chipa paraguaya
15. Castaña de Cajú W1 Cruda
16. Almendra Americana
17. Nuez Mariposa (alfajores, panificação navideña)
18. Pistacho sin Cáscara (heladería autor)
19. Harina de Almendra Parmex (macarons, keto)
20. Curry
21. Paprika Dulce / Pimentón

**Tier 3 — guias estratégicas (5):**
22. Pillar: Insumos para Chipa Industrial
23. Pillar: 7 Especias Imprescindibles del Asado Paraguayo
24. Colorífico/Colorau (locro, sopa paraguaya, chacinas)
25. Sal Rosa del Himalaya Fino (gourmet premium)
26. Pillar institucional B2B: Cómo Elegir Importador

### Infraestrutura técnica

- `guias_data.py`: 2900+ linhas, 26 guias estruturadas, função get_guide
  e list_guides para route handlers. `from __future__ import annotations`
  para compatibilidade Python 3.9 local + 3.12 Railway.
- `app.py`: rotas `/guias` (listing) e `/guias/<slug>` (detail). Sitemap
  inclui 26 entries com priority 0.85, changefreq monthly.
- `templates/guias/index.html`: hero compact magazine-cover com 2 fotos
  overlapping, Fraunces serif headlines, grid de cards.
- `templates/guias/article.html`: layout editorial com TOC sticky desktop,
  drop cap, reading progress bar, hero dramatic, mid-article gallery,
  FAQ accordion, related guides, sticky CTA.
- `static/css/style.css`: 1400+ linhas. Editorial CSS magazine, hero
  treatments por categoria (warm/berry/green/earth), filter saturation
  para suavizar backdrops coloridos, button overrides.
- `static/js/app.js`: data-go-to-page check para separar modal vs navigation
  na página /productos.

### Marca dual mantida (estratégia confirmada)

- **Visível ao usuário**: "Especias del Paraguay" em hero, prosa, meta
  visível, título do tab. Trocados 33 mentions na prosa das guias.
- **Schema/SEO técnico**: "Grãos S.A." preservado em Organization,
  Article author/publisher, Brand, manufacturer (continuidade de
  Organization @id em graos.com.py para preservar autoridade SEO).
- **Domínio**: graos.com.py preservado (sem mudança).
- **Slugs/canonicals**: preservados (não houve rename).

### UX entregue

- Cards de produto com pill "Ver Producto" (data-go-to-page) que navega
  para /producto/{slug}, separado do click na imagem que abre Vista Rápida modal.
- Hint "Vista Rápida" surge na hover da imagem para sinalizar interação.
- Cards alinhados com flex column + margin-top:auto independente da
  quantidade de metadata.
- Botões CTA editoriais (Ver producto + Cotizar WhatsApp) com texto
  visível garantido por override de alta especificidade.

## Decisions made

1. Push direto pra main: usuário autorizou explicitamente.
2. Single commit comprehensivo cobrindo todo o trabalho post-Fase-D
   (em vez de múltiplos commits granulares) por ser interconectado.
3. NÃO incluir os arquivos órfãos do Codex (.planning/CLAUDE_CATCHUP_PROMPT.md,
   checkpoint security-reaudit, static/img/brand/profile-avatars) nesta
   commit; ficam pendentes para uma sessão Codex futura.

## What was rejected

- Tentar gerar imagens via fal-ai/IA: API não acessível na sessão; usadas
  fotos de produto existentes com tratamento CSS. Substituível depois.
- Múltiplos commits granulares: opted for single comprehensive commit
  pela interconectividade do trabalho.

## Next step

Após deploy, monitorar:
- Railway build status (auto-deploy on push to main).
- GSC: indexação das 26 novas URLs /guias/* (esperar 24-72h).
- GSC: aparição em queries genéricas que antes não ranqueavam
  (manzanilla, canela, comino, cúrcuma, anís, paprika, asado paraguayo).
- GA4: tráfego orgânico para /guias/.
- Conversão WhatsApp via guides.

Próximas fases possíveis (não programadas):
- Fase B: search server-side com normalização accent-strip + alias-aware.
- Fase C: FAQPage/HowTo schema também nas páginas /producto/* canônicas.
- Mais guides conforme demanda de busca real (medir após 30 dias).
