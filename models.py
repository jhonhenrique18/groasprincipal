from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(100), unique=True, nullable=False)
    order = db.Column(db.Integer, default=0)
    products = db.relationship('Product', backref='category', lazy=True)

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'slug': self.slug, 'order': self.order}


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    origin = db.Column(db.String(200), default='')
    description = db.Column(db.Text, default='')
    presentation = db.Column(db.String(300), default='')
    image = db.Column(db.String(500), default='')
    featured = db.Column(db.Boolean, default=False)
    active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # SEO breadth layer — additive over the existing graos.com.py / Grãos S.A.
    # baseline. None of these fields change the slug, canonical or sitemap
    # entry; they expand keyword coverage in title, meta and JSON-LD so generic
    # queries (e.g. "manzanilla") match a product whose canonical name is a
    # specific variant ("Manzanilla Flor"). Empty string == not curated yet.
    aliases = db.Column(db.Text, default='')
    scientific_name = db.Column(db.String(200), default='')
    seo_title_override = db.Column(db.String(200), default='')
    seo_description_override = db.Column(db.Text, default='')

    @property
    def alias_list(self):
        """Return aliases as a normalized list of trimmed, non-empty strings."""
        if not self.aliases:
            return []
        return [a.strip() for a in self.aliases.split(',') if a.strip()]

    @property
    def search_corpus(self):
        """Concatenated, lowercased text used for matching this product
        against a search query. Includes name, aliases, scientific name,
        category name and origin. The corpus is rebuilt on every access so it
        always reflects current values; no caching means no staleness when an
        admin edits a product."""
        parts = [
            self.name or '',
            self.scientific_name or '',
            self.category.name if self.category else '',
            self.origin or '',
        ] + self.alias_list
        return ' '.join(parts).lower()

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'slug': self.slug,
            'category_id': self.category_id,
            'category_name': self.category.name if self.category else '',
            'origin': self.origin,
            'description': self.description,
            'presentation': self.presentation,
            'image': self.image,
            'featured': self.featured,
            'active': self.active,
            'aliases': self.alias_list,
            'scientific_name': self.scientific_name,
        }


class SiteSetting(db.Model):
    __tablename__ = 'site_settings'
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(100), unique=True, nullable=False)
    value = db.Column(db.Text, default='')

    @staticmethod
    def get(key, default=''):
        s = SiteSetting.query.filter_by(key=key).first()
        return s.value if s else default

    @staticmethod
    def set(key, value):
        s = SiteSetting.query.filter_by(key=key).first()
        if s:
            s.value = value
        else:
            s = SiteSetting(key=key, value=value)
            db.session.add(s)
        db.session.commit()
