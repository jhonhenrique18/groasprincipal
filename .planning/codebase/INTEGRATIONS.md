# External Integrations

**Analysis Date:** 2026-04-04

## APIs & External Services

**Analytics:**
- Google Analytics 4 (GA4) - Tracking user behavior, product views, conversions
  - ID: `G-Y0QKNWRX66`
  - Implementation: JavaScript gtag() in `templates/base.html`
  - Events tracked: WhatsApp clicks, contact form submissions

**Search Console:**
- Google Search Console - SEO monitoring and indexing
  - Verification: `lcljspbV3Y0qxamB0NA-5pcytg0hB--iE1ktvrMUb38`
  - Implemented in `templates/base.html` meta tag

**Communication:**
- WhatsApp Business API - Product inquiry channel
  - Integration: Direct WhatsApp links (wa.me URLs) on product cards and modal
  - Admin-configurable phone number stored in `SiteSetting` model
  - Event tracking: GA4 events for WhatsApp clicks in `static/js/app.js`

## Data Storage

**Databases:**

*Production:*
- PostgreSQL via `DATABASE_URL` environment variable
  - Driver: `psycopg2-binary` 2.9.10
  - ORM: Flask-SQLAlchemy 3.1.1
  - Models defined in `models.py`: Category, Product, SiteSetting

*Development:*
- SQLite at `sqlite:///graos.db`
  - Automatic fallback in `config.py` when DATABASE_URL not set

**File Storage:**

*Images:*
- Railway persistent volume (production): Path via `RAILWAY_VOLUME_MOUNT_PATH` environment variable
- Local filesystem (development): `static/uploads/` directory
- Served via route `/uploads/<filename>` (production) or `/static/uploads/` (development)
- Processing: Pillow 11.1.0 for image validation and handling

*Static Assets:*
- Local filesystem only in `static/` directory (CSS, JS, icons, manifest)

**Caching:**
- HTTP cache headers via Flask response middleware in `app.py`
  - JS/CSS: 1-year immutable caching
  - Images: 30-day caching
  - HTML: 5-minute caching
- No Redis or external cache service currently used

## Authentication & Identity

**Admin Authentication:**
- Custom session-based authentication in `app.py`
- Credentials from environment variables: `ADMIN_USERNAME`, `ADMIN_PASSWORD`
- Fallback defaults: username='admin', password='graos2026' (change in production)
- Session storage: Flask session cookie
- Routes protected with `@login_required` decorator

**No user registration system** - Admin-only access pattern

## Monitoring & Observability

**Error Tracking:**
- No dedicated error tracking service (Sentry, etc.)
- Application logs to console/stdout (standard Flask/Gunicorn behavior)

**Logs:**
- Gunicorn stdout/stderr to Railway deployment logs
- No structured logging or log aggregation

**Analytics:**
- Google Analytics 4 for user behavior metrics
- Custom events: `whatsapp_click`, `form_submit` tracked via `gtag()` in `static/js/app.js`

## CI/CD & Deployment

**Hosting:**
- Railway.app platform
- Deployment from git branch (automatic on push)
- Environment variables configured in Railway dashboard

**Build Process:**
- No build step required
- Direct Python/Flask application run via Gunicorn
- Procfile: `web: gunicorn app:app`

**No CI Pipeline Service** - Deployment is direct to Railway

## Environment Configuration

**Required env vars (for production):**
- `DATABASE_URL` - PostgreSQL connection string
- `RAILWAY_VOLUME_MOUNT_PATH` - Persistent storage path for uploads
- `SECRET_KEY` - Flask session secret (cryptographic key)
- `ADMIN_USERNAME` - Admin login username
- `ADMIN_PASSWORD` - Admin login password
- `PORT` - HTTP server port (optional, defaults to 5000)

**Optional env vars:**
- All variables have fallback defaults in `config.py` for development

**Secrets location:**
- Railway environment variables dashboard (managed via Platform interface)
- Local development: Create `.env` file (listed in `.gitignore`)

## Webhooks & Callbacks

**Incoming:**
- Contact form at POST `/contacto` - Receives form submissions but does not send webhooks
- No external webhook receivers implemented

**Outgoing:**
- None currently implemented
- Contact form has placeholder for webhook integration: "can integrate with webhook later" (comment in `app.py` line 232)

## SEO & Content Services

**XML Sitemaps:**
- Dynamic sitemap generation at `/sitemap.xml` (static pages + categories + products)
- Product-specific sitemap with image data at `/sitemap-products.xml`
- Sitemaps output in XML format with proper schema.org formatting

**Robots.txt:**
- Dynamic robots.txt at `/robots.txt` with crawl directives and sitemap references

**Schema.org:**
- JSON-LD structured data for Organization and LocalBusiness types
- Embedded in `templates/base.html` with dynamic WhatsApp/email injection
- Supports geo-targeting for Paraguay (PY)

## Image Processing

**Service:**
- Pillow 11.1.0 (local Python library)
- No external CDN for image processing
- Image uploads handled by `save_image()` function in `app.py`
- Supported formats: PNG, JPG, JPEG, WEBP, GIF
- Max upload: 10MB

## Contact & Communication Integration

**Email:**
- No email service integrated (SMTP not configured)
- Email address stored as setting but not used for sending
- Admin-configurable in `/admin/configuracion` route

**WhatsApp:**
- Direct wa.me links (no API calls)
- Phone number stored as SiteSetting
- Integrated in modals, product cards, footer, floating button
- Message templates: "Hola, me interesa el producto: [product-name]"

---

*Integration audit: 2026-04-04*
