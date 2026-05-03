from __future__ import annotations

import os
import re
import uuid
from functools import wraps
from flask import (Flask, render_template, request, redirect, url_for,
                   flash, session, jsonify, send_from_directory, Response, make_response)
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_wtf.csrf import CSRFProtect
from config import Config
from models import db, Category, Product, SiteSetting
from meta_capi import send_capi_event, user_data_from_request
from seo_aliases import PRODUCT_ALIASES, lookup as seo_lookup
from guias_data import GUIDES, get_guide, list_guides
from categories_data import CATEGORY_CONTENT, get_category_content


def default_product_faq(product) -> list[dict]:
    """Generic high-quality B2B FAQ template for products without dedicated
    guides. Parameterized by product attributes so each product gets a
    coherent FAQ that actually relates to itself, not boilerplate.

    Used by the producto() route to populate FAQPage schema on every
    canonical /producto/<slug> page. Products that DO have a dedicated
    guide pull the richer FAQ from that guide instead.
    """
    aliases = product.alias_list[:4] if product.alias_list else []
    aliases_str = ', '.join(aliases) if aliases else ''
    cat_lower = product.category.name.lower() if product.category else ''
    return [
        {
            'q': f'¿Qué es {product.name}?',
            'a': (
                f'{product.name}'
                + (f' (también conocido como {aliases_str})' if aliases_str else '')
                + f' es un producto de la categoría {product.category.name} importado al por mayor por Especias del Paraguay '
                + (f'desde {product.origin}. ' if product.origin else 'con calidad estable lote a lote. ')
                + (product.description if product.description else f'Ideal para industria, gastronomía profesional y reventa.')
            ),
        },
        {
            'q': f'¿De dónde es el origen de {product.name}?',
            'a': (
                f'Origen: {product.origin}. Importación directa con certificado de origen y análisis bromatológico básico.'
                if product.origin else
                'Importación directa con certificado de origen disponible bajo pedido. Cada lote viene con análisis bromatológico básico.'
            ),
        },
        {
            'q': '¿Cuál es la presentación al por mayor disponible?',
            'a': (
                f'Presentación estándar: {product.presentation}. Para volúmenes mayores se cotiza por proyecto.'
                if product.presentation else
                'Presentación según volumen requerido. Consulte por WhatsApp para cotización al volumen específico.'
            ),
        },
        {
            'q': '¿Hacen entregas a todo el Paraguay?',
            'a': 'Sí. Despachamos a todo el territorio nacional con factura legal. Para volúmenes mayoristas trabajamos transferencia bancaria y coordinamos logística según destino.',
        },
        {
            'q': '¿Trabajan con factura legal y crédito fiscal IVA?',
            'a': 'Sí. Toda venta lleva factura legal con IVA discriminado, apta para crédito fiscal y registro contable. Sin factura no operamos.',
        },
        {
            'q': f'¿Cuál es el pedido mínimo para mayoristas de {product.name}?',
            'a': (
                f'El formato mayorista de {product.name} es {product.presentation}. Para volúmenes menores y reventa al por menor también atendemos por consulta directa por WhatsApp.'
                if product.presentation else
                f'Atendemos cualquier volumen serio. Para consultar disponibilidad y cotización para {product.name}, contactar por WhatsApp.'
            ),
        },
    ]


def product_faq_and_howto(product, slug: str) -> tuple[list[dict], dict | None]:
    """Resolve the FAQ and HowTo data for a product page. If a dedicated
    editorial guide exists for this product slug, use the curated FAQ +
    first HowTo from the guide. Otherwise fall back to the generic
    template. Returns (faq_list, howto_dict_or_None).
    """
    guide = get_guide(slug)
    if guide:
        faq = guide.get('faq', []) or default_product_faq(product)
        howto = None
        for section in guide.get('sections', []):
            if section.get('howto'):
                howto = section['howto']
                break
        return faq, howto
    return default_product_faq(product), None

app = Flask(__name__)
app.config.from_object(Config)
# Fail loud if SECRET_KEY is missing in production. Config.py auto-generates
# in local dev only; in production (DATABASE_URL set) the env var is required.
if not app.config.get('SECRET_KEY'):
    raise RuntimeError(
        'SECRET_KEY environment variable is required in production. '
        'Set it in Railway Variables.'
    )
db.init_app(app)

# Rate limiter. In-memory is OK for single-instance deploys; move to Redis
# later if scaling out. `get_remote_address` reads X-Forwarded-For-aware IP.
limiter = Limiter(
    key_func=get_remote_address,
    app=app,
    default_limits=[],  # no blanket limit; apply per-route explicitly
    storage_uri='memory://',
)

# CSRF protection. Active for every POST by default. sendBeacon-style
# endpoints that cannot carry a token are exempted explicitly below.
csrf = CSRFProtect(app)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp', 'gif'}

# ──────────────────── HELPERS ────────────────────

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[áàãâä]', 'a', text)
    text = re.sub(r'[éèêë]', 'e', text)
    text = re.sub(r'[íìîï]', 'i', text)
    text = re.sub(r'[óòõôö]', 'o', text)
    text = re.sub(r'[úùûü]', 'u', text)
    text = re.sub(r'[ñ]', 'n', text)
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('admin_logged_in'):
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return decorated

# ──────────────────── SEO: SECURITY & CACHE HEADERS ────────────────────

@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    response.headers['Permissions-Policy'] = 'geolocation=(), microphone=(), camera=()'
    if not app.debug:
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    # Cache headers for static assets
    if response.content_type and ('css' in response.content_type or 'javascript' in response.content_type):
        response.headers['Cache-Control'] = 'public, max-age=31536000, immutable'
    elif response.content_type and 'image' in response.content_type:
        response.headers['Cache-Control'] = 'public, max-age=31536000, immutable'
    elif response.content_type and 'text/html' in response.content_type:
        response.headers['Cache-Control'] = 'public, max-age=300'
    return response

def save_image(file):
    """Save an uploaded image as optimized WebP (with a -sm thumbnail).

    Security: we force a real decode via Image.load() before accepting the
    file. If decode fails, the upload is refused and nothing is written.
    There is NO fallback to write raw bytes — an attacker with admin access
    cannot use this function to drop a non-image file into the uploads dir.
    """
    if not file or not allowed_file(file.filename):
        return ''

    from PIL import Image as PILImage

    unique = uuid.uuid4().hex
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    try:
        img = PILImage.open(file)
        img.load()  # force decode — raises on fake/corrupt images

        if img.mode == 'RGBA':
            bg = PILImage.new('RGB', img.size, (255, 255, 255))
            bg.paste(img, mask=img.split()[3])
            img = bg
        elif img.mode != 'RGB':
            img = img.convert('RGB')

        sizes = {'': 600, '-sm': 400}
        for suffix, size in sizes.items():
            resized = img.copy()
            w, h = resized.size
            if w != h:
                side = min(w, h)
                left = (w - side) // 2
                top = (h - side) // 2
                resized = resized.crop((left, top, left + side, top + side))
            if max(w, h) > size:
                resized = resized.resize((size, size), PILImage.LANCZOS)
            out_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{unique}{suffix}.webp")
            resized.save(out_path, format='WEBP', quality=85, method=4)

        filename = f"{unique}.webp"
    except Exception:
        app.logger.warning('save_image: rejected upload %r', file.filename)
        return ''

    if os.environ.get('RAILWAY_VOLUME_MOUNT_PATH'):
        return f"/uploads/{filename}"
    return f"/static/uploads/{filename}"

# ──────────────────── TEMPLATE FILTERS ────────────────────

@app.template_filter('img_sm')
def img_sm_filter(image_path):
    """Return the -sm (400px thumbnail) variant of an image path,
    but ONLY if the -sm file actually exists on disk. Otherwise return
    the original path so the browser always has a working image."""
    if not image_path:
        return image_path
    if '.' not in image_path:
        return image_path
    base, ext = image_path.rsplit('.', 1)
    sm_path = f"{base}-sm.{ext}"

    # Resolve the filesystem path to check existence
    sm_filename = sm_path.split('/')[-1]
    full_path = os.path.join(app.config['UPLOAD_FOLDER'], sm_filename)
    if os.path.isfile(full_path):
        # Return the -sm URL using the same prefix as the original
        prefix = image_path.rsplit('/', 1)[0]  # e.g. /static/uploads or /uploads
        return f"{prefix}/{sm_filename}"
    return image_path

# ──────────────────── CONTEXT PROCESSOR ────────────────────

@app.context_processor
def inject_site_settings():
    """Make site settings available in ALL templates."""
    whatsapp_raw = SiteSetting.get('whatsapp', '')
    # Strip everything except digits for the wa.me link
    whatsapp_digits = re.sub(r'[^0-9]', '', whatsapp_raw)
    return {
        'site_whatsapp_raw': whatsapp_raw,
        'site_whatsapp_digits': whatsapp_digits,
        'site_whatsapp_link': f"https://wa.me/{whatsapp_digits}" if whatsapp_digits else '#',
        'site_whatsapp_display': whatsapp_raw if whatsapp_raw else '+595 XXX XXX XXX',
        'site_email': SiteSetting.get('email', ''),
        'site_hero_image': SiteSetting.get('hero_image', ''),
    }

@app.context_processor
def inject_meta_tracking():
    """Expose Meta Pixel config + per-request event_id so the server-side
    PageView CAPI and the client-side Pixel PageView can share event_id."""
    return {
        'meta_pixel_id': app.config.get('META_PIXEL_ID') or '',
        'meta_domain_verification': app.config.get('META_DOMAIN_VERIFICATION') or '',
        'meta_page_event_id': uuid.uuid4().hex,
    }

EP_EXTERNAL_ID_COOKIE = '_ep_eid'

@app.after_request
def ensure_external_id_cookie(response):
    """Set a long-lived first-party external_id cookie for cross-session
    matching quality. Only set on HTML responses where the cookie is absent."""
    if request.cookies.get(EP_EXTERNAL_ID_COOKIE):
        return response
    ctype = response.content_type or ''
    if 'text/html' not in ctype:
        return response
    response.set_cookie(
        EP_EXTERNAL_ID_COOKIE,
        uuid.uuid4().hex,
        max_age=60 * 60 * 24 * 365,  # 1 year
        httponly=False,
        samesite='Lax',
        secure=not app.debug,
    )
    return response

# ──────────────────── UPLOADED FILES (Railway volume) ────────────────────

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """Serve uploaded files from Railway persistent volume or local uploads folder."""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/static/uploads/<filename>')
def static_uploads_fallback(filename):
    """Fallback: if DB stores /static/uploads/xxx but we're on Railway,
    serve from the persistent volume instead of the (empty) static dir.
    In development this route is shadowed by Flask's built-in static handler,
    so it only activates on Railway where static/uploads/ doesn't exist."""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

# ──────────────────── PUBLIC ROUTES ────────────────────

@app.route('/')
def index():
    featured = Product.query.filter_by(active=True, featured=True).order_by(Product.name).limit(8).all()
    categories = Category.query.order_by(Category.order).all()
    return render_template('index.html', featured=featured, categories=categories)

@app.route('/productos')
@app.route('/productos/<slug>')
def productos(slug=None):
    categories = Category.query.order_by(Category.order).all()
    cat_counts = {c.id: Product.query.filter_by(active=True, category_id=c.id).count() for c in categories}
    total_count = Product.query.filter_by(active=True).count()
    if slug:
        cat = Category.query.filter_by(slug=slug).first_or_404()
        products = Product.query.filter_by(active=True, category_id=cat.id).order_by(Product.name).all()
        current_cat = cat
    else:
        products = Product.query.filter_by(active=True).order_by(Product.name).all()
        current_cat = None
    # Aggregated, deduped alias pool for the listing page's SEO blocks.
    # Featured products contribute their aliases first so the head-of-list
    # in meta tags and the "Incluye:" header surfaces the highest-volume
    # search terms (manzanilla, canela, etc.) ahead of alphabetical noise.
    # Cap at 30 keeps meta tags within reasonable size limits.
    products_for_aliases = sorted(products, key=lambda p: (not p.featured, p.name))
    alias_pool: list[str] = []
    seen: set[str] = set()
    for p in products_for_aliases:
        for a in p.alias_list:
            key = a.lower()
            if key in seen:
                continue
            seen.add(key)
            alias_pool.append(a)
            if len(alias_pool) >= 30:
                break
        if len(alias_pool) >= 30:
            break
    # Editorial intro + FAQ for category hub pages. None when on the
    # all-products page (no current_cat) or when the category was not
    # curated yet — the template gates the render with `if`.
    category_content = get_category_content(current_cat.slug) if current_cat else None
    return render_template(
        'productos.html',
        products=products, categories=categories, current_cat=current_cat,
        cat_counts=cat_counts, total_count=total_count, alias_pool=alias_pool,
        category_content=category_content,
    )

@app.route('/producto/<slug>')
def producto(slug):
    product = Product.query.filter_by(slug=slug, active=True).first_or_404()
    related = Product.query.filter(
        Product.category_id == product.category_id,
        Product.id != product.id,
        Product.active == True
    ).limit(4).all()
    # FAQPage and HowTo schema population. If the product has a dedicated
    # guide we reuse the curated FAQ and HowTo; otherwise the helper
    # synthesizes a high-quality B2B FAQ from the product's own attributes.
    faq, howto = product_faq_and_howto(product, slug)
    # If a dedicated guide exists, expose the URL so the product page can
    # promote it as an authoritative deep dive related to this product.
    has_guide = bool(get_guide(slug))
    return render_template(
        'producto.html', product=product, related=related,
        faq=faq, howto=howto, has_guide=has_guide,
    )

@app.route('/api/producto/<slug>')
def api_producto(slug):
    product = Product.query.filter_by(slug=slug, active=True).first_or_404()
    return jsonify(product.to_dict())

# ──────────────────── GUÍAS / EDITORIAL CONTENT ────────────────────

@app.route('/guias')
@app.route('/guias/')
def guias_index():
    """Editorial index page: listing of all curated long-form guides.

    Each card links to /guias/<slug>. The slug always mirrors a product
    slug so the related product can be resolved cheaply on the detail
    page. We hydrate the related Product (when it exists) for image and
    aliases so cards can show the same product photo treated editorially.
    """
    guides = list_guides()
    # Hydrate each guide summary with its related product (image, aliases)
    # so the index can render with editorial treatment.
    enriched = []
    for g in guides:
        product = Product.query.filter_by(slug=g['product_slug'], active=True).first()
        enriched.append({
            **g,
            'product': product,
        })
    return render_template('guias/index.html', guides=enriched)


@app.route('/guias/<slug>')
def guia_detail(slug):
    """Single editorial guide. Falls back to 404 if the slug isn't curated.

    The template expects:
    - guide: the full dict from GUIDES[slug]
    - product: the related Product object (for image, aliases, CTA link)
    - related_guides: short summaries of guides linked from `related_slugs`
    - category_products: up to 6 OTHER active products in the same category,
      used by the mid-article gallery to add visual richness without
      requiring per-guide image generation.
    """
    guide = get_guide(slug)
    if not guide:
        return render_template('404.html'), 404
    product = Product.query.filter_by(slug=guide['product_slug'], active=True).first()
    related_guides = []
    for rs in guide.get('related_slugs', []):
        rg = get_guide(rs)
        if rg:
            related_guides.append({
                'slug': rs,
                'title': rg['title'],
                'dek': rg['dek'],
                'category': rg['category'],
                'product_slug': rg['product_slug'],
                'reading_time': rg['reading_time'],
                'product': Product.query.filter_by(slug=rg['product_slug'], active=True).first(),
            })
    # Extra image variety: pull up to 6 OTHER products from the same category
    # (excluding the guide's main product) so the mid-article gallery has real
    # photos to show. Falls back to empty list if the product is detached.
    category_products = []
    if product:
        category_products = (
            Product.query
            .filter(
                Product.category_id == product.category_id,
                Product.id != product.id,
                Product.active == True,
                Product.image != '',
            )
            .order_by(Product.featured.desc(), Product.name)
            .limit(6)
            .all()
        )
    return render_template(
        'guias/article.html',
        guide=guide, product=product, related_guides=related_guides,
        category_products=category_products, slug=slug,
    )

# ──────────────────── SEO ROUTES ────────────────────

@app.route('/robots.txt')
def robots():
    content = """User-agent: *
Allow: /
Disallow: /admin/
Disallow: /api/
Disallow: /uploads/

Crawl-delay: 1

Sitemap: https://www.graos.com.py/sitemap.xml
Sitemap: https://www.graos.com.py/sitemap-products.xml
"""
    return Response(content, mimetype='text/plain')

@app.route('/sitemap.xml')
def sitemap():
    from datetime import datetime as dt
    today = dt.utcnow().strftime('%Y-%m-%d')
    base = 'https://www.graos.com.py'
    pages = []
    # Static pages
    pages.append({'loc': base + '/', 'priority': '1.0', 'changefreq': 'weekly', 'lastmod': today})
    pages.append({'loc': base + '/productos', 'priority': '0.9', 'changefreq': 'weekly', 'lastmod': today})
    pages.append({'loc': base + '/guias', 'priority': '0.85', 'changefreq': 'weekly', 'lastmod': today})
    pages.append({'loc': base + '/nosotros', 'priority': '0.7', 'changefreq': 'monthly', 'lastmod': today})
    pages.append({'loc': base + '/contacto', 'priority': '0.7', 'changefreq': 'monthly', 'lastmod': today})
    # Category pages
    categories = Category.query.order_by(Category.order).all()
    for c in categories:
        pages.append({'loc': base + '/productos/' + c.slug, 'priority': '0.8', 'changefreq': 'weekly', 'lastmod': today})
    # Product pages
    products = Product.query.filter_by(active=True).all()
    for p in products:
        lastmod = p.created_at.strftime('%Y-%m-%d') if p.created_at else today
        pages.append({'loc': base + '/producto/' + p.slug, 'priority': '0.8', 'changefreq': 'weekly', 'lastmod': lastmod})
    # Editorial guides (long-form content, high SEO priority for topic clusters)
    for guide_slug, guide in GUIDES.items():
        pages.append({
            'loc': f"{base}/guias/{guide_slug}",
            'priority': '0.85',
            'changefreq': 'monthly',
            'lastmod': guide.get('updated', guide.get('published', today)),
        })

    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for page in pages:
        xml += '  <url>\n'
        xml += f'    <loc>{page["loc"]}</loc>\n'
        xml += f'    <lastmod>{page["lastmod"]}</lastmod>\n'
        xml += f'    <changefreq>{page["changefreq"]}</changefreq>\n'
        xml += f'    <priority>{page["priority"]}</priority>\n'
        xml += '  </url>\n'
    xml += '</urlset>'
    response = make_response(xml)
    response.headers['Content-Type'] = 'application/xml'
    return response

@app.route('/sitemap-products.xml')
def sitemap_products():
    from datetime import datetime as dt
    today = dt.utcnow().strftime('%Y-%m-%d')
    base = 'https://www.graos.com.py'
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
    xml += '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n'
    products = Product.query.filter_by(active=True).all()
    for p in products:
        lastmod = p.created_at.strftime('%Y-%m-%d') if p.created_at else today
        xml += '  <url>\n'
        xml += f'    <loc>{base}/producto/{p.slug}</loc>\n'
        xml += f'    <lastmod>{lastmod}</lastmod>\n'
        xml += '    <changefreq>weekly</changefreq>\n'
        xml += '    <priority>0.9</priority>\n'
        if p.image:
            image_url = p.image if p.image.startswith('http') else f'{base}{p.image}'
            xml += '    <image:image>\n'
            xml += f'      <image:loc>{image_url}</image:loc>\n'
            xml += f'      <image:title>{p.name}</image:title>\n'
            if p.origin:
                xml += f'      <image:caption>{p.name} — Origen: {p.origin}</image:caption>\n'
            xml += '    </image:image>\n'
        xml += '  </url>\n'
    xml += '</urlset>'
    response = make_response(xml)
    response.headers['Content-Type'] = 'application/xml'
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/contacto', methods=['GET', 'POST'])
@limiter.limit('3 per 10 minutes', methods=['POST'])
def contacto():
    if request.method == 'POST':
        # Honeypot: field is hidden from humans; only bots fill it. Silently
        # pretend the submit worked so bots don't learn they were detected.
        if request.form.get('website'):
            app.logger.info('contacto: honeypot tripped from %s', request.remote_addr)
            flash('Mensaje enviado con éxito. Nos pondremos en contacto pronto.', 'success')
            return redirect(url_for('contacto'))

        event_id = request.form.get('meta_event_id') or uuid.uuid4().hex
        user_data = user_data_from_request(request, form=request.form)
        send_capi_event(
            'Lead',
            event_id,
            request.url,
            user_data=user_data,
            custom_data={'content_name': 'contact_form', 'content_category': 'lead'},
        )
        flash('Mensaje enviado con éxito. Nos pondremos en contacto pronto.', 'success')
        return redirect(url_for('contacto'))
    return render_template('contacto.html')

@app.route('/api/meta-capi-event', methods=['POST'])
@csrf.exempt
@limiter.limit('60 per minute')
def api_meta_capi_event():
    """Companion endpoint for client-side Meta events. Receives event_name,
    event_id, event_source_url and custom_data and forwards to CAPI so the
    server-side copy of the event can be deduplicated against the Pixel."""
    payload = request.get_json(silent=True) or {}
    event_name = payload.get('event_name')
    event_id = payload.get('event_id')
    if not event_name or not event_id:
        return ('', 204)
    allowed = {'Contact', 'Lead', 'ViewContent', 'Search', 'PageView'}
    if event_name not in allowed:
        return ('', 204)
    send_capi_event(
        event_name,
        event_id,
        payload.get('event_source_url') or request.referrer or request.url,
        user_data=user_data_from_request(request),
        custom_data=payload.get('custom_data') or {},
    )
    return ('', 204)

# ──────────────────── ADMIN ROUTES ────────────────────

@app.route('/admin/login', methods=['GET', 'POST'])
@limiter.limit('5 per 15 minutes', methods=['POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        stored_hash = SiteSetting.get('admin_password_hash')
        if (username == app.config['ADMIN_USERNAME']
                and stored_hash
                and check_password_hash(stored_hash, password)):
            session['admin_logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        flash('Credenciales incorrectas', 'error')
    return render_template('admin/login.html')

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('admin_login'))

@app.route('/admin/migrate-images')
@login_required
def admin_migrate_images():
    """Full image migration: sync paths, copy WebP to volume, fix all DB paths."""
    import json, shutil
    volume = os.environ.get('RAILWAY_VOLUME_MOUNT_PATH')
    results = []

    # Step 1: Copy ALL WebP files from static/uploads/ to Railway volume
    copied = 0
    if volume:
        src_dir = os.path.join(app.root_path, 'static', 'uploads')
        dst_dir = os.path.join(volume, 'uploads')
        os.makedirs(dst_dir, exist_ok=True)
        if os.path.isdir(src_dir):
            for f in os.listdir(src_dir):
                src = os.path.join(src_dir, f)
                dst = os.path.join(dst_dir, f)
                if os.path.isfile(src) and not os.path.exists(dst):
                    shutil.copy2(src, dst)
                    copied += 1
        results.append(f'Copied {copied} files to volume')

    # Step 2: For every product, ensure image path points to existing WebP
    fixed = 0
    for p in Product.query.all():
        if not p.image:
            continue
        old_path = p.image
        new_path = old_path
        # Fix /static/uploads/ → /uploads/ on Railway
        if volume and new_path.startswith('/static/uploads/'):
            new_path = new_path.replace('/static/uploads/', '/uploads/')
        # Fix .png → .webp if WebP exists
        if new_path.endswith('.png'):
            webp_path = new_path.rsplit('.', 1)[0] + '.webp'
            # Check if WebP file actually exists
            if volume:
                check_dir = os.path.join(volume, 'uploads')
            else:
                check_dir = os.path.join(app.root_path, 'static', 'uploads')
            webp_filename = webp_path.split('/')[-1]
            if os.path.exists(os.path.join(check_dir, webp_filename)):
                new_path = webp_path
        if new_path != old_path:
            p.image = new_path
            fixed += 1
    db.session.commit()
    results.append(f'Fixed {fixed} DB image paths')

    # Step 3: Fill empty images from seed_data.json
    data_path = os.path.join(os.path.dirname(__file__), 'seed_data.json')
    synced = 0
    if os.path.exists(data_path):
        with open(data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        seed_map = {p['slug']: p.get('image', '') for p in data['products']}
        for p in Product.query.filter((Product.image == '') | (Product.image == None)).all():
            seed_img = seed_map.get(p.slug, '')
            if seed_img:
                if volume:
                    seed_img = seed_img.replace('/static/uploads/', '/uploads/')
                if seed_img.endswith('.png'):
                    seed_img = seed_img.rsplit('.', 1)[0] + '.webp'
                p.image = seed_img
                synced += 1
        db.session.commit()
    results.append(f'Synced {synced} empty products from seed')

    flash(' | '.join(results), 'success')
    return redirect(url_for('admin_dashboard'))

@app.route('/admin')
@login_required
def admin_dashboard():
    total_products = Product.query.count()
    total_categories = Category.query.count()
    active_products = Product.query.filter_by(active=True).count()
    featured_products = Product.query.filter_by(featured=True).count()
    return render_template('admin/dashboard.html',
        total_products=total_products,
        total_categories=total_categories,
        active_products=active_products,
        featured_products=featured_products)

# ── Admin Categories ──

@app.route('/admin/categorias')
@login_required
def admin_categories():
    categories = Category.query.order_by(Category.order).all()
    return render_template('admin/categories.html', categories=categories)

@app.route('/admin/categoria/nueva', methods=['GET', 'POST'])
@app.route('/admin/categoria/<int:id>/editar', methods=['GET', 'POST'])
@login_required
def admin_category_form(id=None):
    cat = Category.query.get(id) if id else None
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        order = int(request.form.get('order', 0))
        if not name:
            flash('El nombre es obligatorio', 'error')
            return render_template('admin/category_form.html', cat=cat)
        if cat:
            cat.name = name
            cat.slug = slugify(name)
            cat.order = order
        else:
            cat = Category(name=name, slug=slugify(name), order=order)
            db.session.add(cat)
        db.session.commit()
        flash('Categoría guardada', 'success')
        return redirect(url_for('admin_categories'))
    return render_template('admin/category_form.html', cat=cat)

@app.route('/admin/categoria/<int:id>/eliminar', methods=['POST'])
@login_required
def admin_category_delete(id):
    cat = Category.query.get_or_404(id)
    if cat.products:
        flash('No se puede eliminar: tiene productos asociados', 'error')
    else:
        db.session.delete(cat)
        db.session.commit()
        flash('Categoría eliminada', 'success')
    return redirect(url_for('admin_categories'))

# ── Admin Products ──

@app.route('/admin/productos')
@login_required
def admin_products():
    products = Product.query.order_by(Product.created_at.desc()).all()
    return render_template('admin/products.html', products=products)

@app.route('/admin/producto/nuevo', methods=['GET', 'POST'])
@app.route('/admin/producto/<int:id>/editar', methods=['GET', 'POST'])
@login_required
def admin_product_form(id=None):
    product = Product.query.get(id) if id else None
    categories = Category.query.order_by(Category.order).all()

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        category_id = request.form.get('category_id', type=int)
        origin = request.form.get('origin', '').strip()
        description = request.form.get('description', '').strip()
        presentation = request.form.get('presentation', '').strip()
        featured = request.form.get('featured') == 'on'
        active = request.form.get('active') == 'on'

        if not name or not category_id:
            flash('Nombre y categoría son obligatorios', 'error')
            return render_template('admin/product_form.html', product=product, categories=categories)

        image_url = product.image if product else ''
        file = request.files.get('image')
        if file and file.filename:
            image_url = save_image(file)

        if product:
            product.name = name
            product.slug = slugify(name)
            product.category_id = category_id
            product.origin = origin
            product.description = description
            product.presentation = presentation
            product.featured = featured
            product.active = active
            if image_url:
                product.image = image_url
        else:
            product = Product(
                name=name, slug=slugify(name), category_id=category_id,
                origin=origin, description=description, presentation=presentation,
                image=image_url, featured=featured, active=active
            )
            db.session.add(product)

        db.session.commit()
        flash('Producto guardado', 'success')
        return redirect(url_for('admin_products'))

    return render_template('admin/product_form.html', product=product, categories=categories)

@app.route('/admin/producto/<int:id>/eliminar', methods=['POST'])
@login_required
def admin_product_delete(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    flash('Producto eliminado', 'success')
    return redirect(url_for('admin_products'))

# ── Admin Settings ──

@app.route('/admin/configuracion', methods=['GET', 'POST'])
@login_required
def admin_settings():
    if request.method == 'POST':
        # WhatsApp
        whatsapp = request.form.get('whatsapp', '').strip()
        SiteSetting.set('whatsapp', whatsapp)

        # Email
        email = request.form.get('email', '').strip()
        SiteSetting.set('email', email)

        # Hero image upload
        hero_file = request.files.get('hero_image')
        if hero_file and hero_file.filename:
            hero_url = save_image(hero_file)
            if hero_url:
                SiteSetting.set('hero_image', hero_url)

        flash('Configuración guardada con éxito', 'success')
        return redirect(url_for('admin_settings'))

    return render_template('admin/settings.html',
        whatsapp=SiteSetting.get('whatsapp', ''),
        email=SiteSetting.get('email', ''),
        hero_image=SiteSetting.get('hero_image', ''))

# ──────────────────── INIT DB ────────────────────

def ensure_admin_password_hash():
    """Bootstrap admin auth: on first boot, hash the ADMIN_PASSWORD env var
    and persist it in SiteSetting. After this runs once, the env var can
    (and should) be removed from Railway — all logins use the stored hash.

    Idempotent: only seeds when no hash is present in DB.
    """
    if SiteSetting.get('admin_password_hash'):
        return
    bootstrap_password = os.environ.get('ADMIN_PASSWORD', '')
    if not bootstrap_password:
        app.logger.warning(
            'admin_password_hash missing in DB and ADMIN_PASSWORD env var empty; '
            'admin login is disabled until ADMIN_PASSWORD is set on this service'
        )
        return
    SiteSetting.set(
        'admin_password_hash',
        generate_password_hash(bootstrap_password, method='pbkdf2:sha256:600000'),
    )
    app.logger.info(
        'Admin password hashed and persisted; ADMIN_PASSWORD env var may now be removed'
    )


def _ensure_seo_columns():
    """Idempotent ALTER TABLE — adds the SEO breadth columns to `products`
    if they are missing. Works on both SQLite (dev) and PostgreSQL (prod)
    because the column adds use a syntax both engines accept and we gate
    each ADD with an inspector check, so re-running is a no-op.

    Why not Alembic: the project never adopted a migration framework and
    using one for four columns would be over-engineering. Keeping the
    bootstrap path single-file lets a fresh Railway deploy come up with
    only `db.create_all()` + this helper running once on boot.
    """
    from sqlalchemy import inspect, text
    inspector = inspect(db.engine)
    existing_cols = {c['name'] for c in inspector.get_columns('products')}

    new_cols = {
        'aliases': "TEXT DEFAULT ''",
        'scientific_name': "VARCHAR(200) DEFAULT ''",
        'seo_title_override': "VARCHAR(200) DEFAULT ''",
        'seo_description_override': "TEXT DEFAULT ''",
    }

    added = []
    with db.engine.begin() as conn:
        for col, ddl in new_cols.items():
            if col in existing_cols:
                continue
            conn.execute(text(f"ALTER TABLE products ADD COLUMN {col} {ddl}"))
            added.append(col)
    if added:
        app.logger.info('SEO migration: added columns %s to products', added)


def _backfill_seo_aliases():
    """For every product whose aliases column is empty, look up the curated
    aliases in seo_aliases.PRODUCT_ALIASES and write them in. Runs on every
    boot so newly-curated entries flow into prod automatically; existing
    aliases are left untouched (admin overrides win).
    """
    backfilled = 0
    for p in Product.query.filter((Product.aliases == '') | (Product.aliases.is_(None))).all():
        entry = seo_lookup(p.slug)
        if not entry['aliases'] and not entry['scientific_name']:
            continue
        if entry['aliases']:
            p.aliases = entry['aliases']
        if entry['scientific_name'] and not p.scientific_name:
            p.scientific_name = entry['scientific_name']
        backfilled += 1
    if backfilled:
        db.session.commit()
        app.logger.info('SEO migration: backfilled aliases on %d products', backfilled)


def init_db():
    """Create tables and run seed if database is empty."""
    db.create_all()
    _ensure_seo_columns()
    if Category.query.count() == 0:
        # First run — seed all data
        import json
        data_path = os.path.join(os.path.dirname(__file__), 'seed_data.json')
        with open(data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for c in data['categories']:
            db.session.add(Category(name=c['name'], slug=c['slug'], order=c['order']))
        db.session.commit()
        for p in data['products']:
            cat = Category.query.filter_by(slug=p['category_slug']).first()
            if not cat:
                continue
            seo = seo_lookup(p['slug'])
            db.session.add(Product(
                name=p['name'], slug=p['slug'], category_id=cat.id,
                origin=p.get('origin', ''), description=p.get('description', ''),
                presentation=p.get('presentation', ''), image=p.get('image', ''),
                featured=p.get('featured', False), active=p.get('active', True),
                aliases=seo['aliases'], scientific_name=seo['scientific_name'],
            ))
        db.session.commit()
        if not SiteSetting.get('whatsapp'):
            SiteSetting.set('whatsapp', '+595 983002684')
        if not SiteSetting.get('email'):
            SiteSetting.set('email', 'jhonatan@grupo-dip.com')
        if not SiteSetting.get('hero_image'):
            SiteSetting.set('hero_image', '/static/uploads/6a6805d27ce146bfa9af82e53d827753.png')
    else:
        # Existing DB — backfill aliases for products that don't have them yet
        _backfill_seo_aliases()
    ensure_admin_password_hash()

with app.app_context():
    init_db()

# ──────────────────── RUN ────────────────────

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
