import os
import re
import uuid
from functools import wraps
from flask import (Flask, render_template, request, redirect, url_for,
                   flash, session, jsonify, send_from_directory, Response, make_response)
from werkzeug.utils import secure_filename
from config import Config
from models import db, Category, Product, SiteSetting

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

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

def save_image(file):
    if file and allowed_file(file.filename):
        ext = file.filename.rsplit('.', 1)[1].lower()
        filename = f"{uuid.uuid4().hex}.{ext}"
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        # If using Railway volume, serve via /uploads/ route; otherwise static path
        if os.environ.get('RAILWAY_VOLUME_MOUNT_PATH'):
            return f"/uploads/{filename}"
        return f"/static/uploads/{filename}"
    return ''

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

# ──────────────────── UPLOADED FILES (Railway volume) ────────────────────

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """Serve uploaded files from Railway persistent volume or local uploads folder."""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

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
    if slug:
        cat = Category.query.filter_by(slug=slug).first_or_404()
        products = Product.query.filter_by(active=True, category_id=cat.id).order_by(Product.name).all()
        current_cat = cat
    else:
        products = Product.query.filter_by(active=True).order_by(Product.name).all()
        current_cat = None
    return render_template('productos.html', products=products, categories=categories, current_cat=current_cat)

@app.route('/producto/<slug>')
def producto(slug):
    product = Product.query.filter_by(slug=slug, active=True).first_or_404()
    related = Product.query.filter(
        Product.category_id == product.category_id,
        Product.id != product.id,
        Product.active == True
    ).limit(4).all()
    return render_template('producto.html', product=product, related=related)

@app.route('/api/producto/<slug>')
def api_producto(slug):
    product = Product.query.filter_by(slug=slug, active=True).first_or_404()
    return jsonify(product.to_dict())

# ──────────────────── SEO ROUTES ────────────────────

@app.route('/robots.txt')
def robots():
    content = """User-agent: *
Allow: /
Disallow: /admin/
Disallow: /api/

Sitemap: https://www.graos.com.py/sitemap.xml
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

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        # Process contact form (can integrate with webhook later)
        flash('Mensaje enviado con éxito. Nos pondremos en contacto pronto.', 'success')
        return redirect(url_for('contacto'))
    return render_template('contacto.html')

# ──────────────────── ADMIN ROUTES ────────────────────

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        if username == app.config['ADMIN_USERNAME'] and password == app.config['ADMIN_PASSWORD']:
            session['admin_logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        flash('Credenciales incorrectas', 'error')
    return render_template('admin/login.html')

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('admin_login'))

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

def init_db():
    """Create tables and run seed if database is empty."""
    db.create_all()
    if Category.query.count() == 0:
        # First run — seed all data
        from seed import seed
        seed()

with app.app_context():
    init_db()

# ──────────────────── RUN ────────────────────

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
