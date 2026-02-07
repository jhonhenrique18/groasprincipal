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
