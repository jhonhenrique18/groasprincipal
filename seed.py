"""
Seed script — populates the database with initial products, categories and settings.
Run once after first deploy: python seed.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from app import app, db
from models import Category, Product, SiteSetting


def seed():
    with app.app_context():
        # ── Categories (skip if already exist) ──
        if Category.query.count() > 0:
            print("Categories already exist, skipping category seed.")
        else:
            categories = [
                Category(name='Especias y Condimentos', slug='especias-y-condimentos', order=1),
                Category(name='Hierbas Medicinales', slug='hierbas-medicinales', order=2),
                Category(name='Tés e Infusiones', slug='tes-e-infusiones', order=3),
                Category(name='Suplementos Naturales', slug='suplementos-naturales', order=4),
                Category(name='Frutos Secos y Semillas', slug='frutos-secos-y-semillas', order=5),
            ]
            for c in categories:
                db.session.add(c)
            db.session.commit()
            print(f"Seeded {len(categories)} categories.")

        # Helper: get category by slug
        def cat(slug):
            return Category.query.filter_by(slug=slug).first()

        # ── Products (skip if already exist) ──
        if Product.query.count() > 0:
            print("Products already exist, skipping product seed.")
        else:
            products = [
                Product(
                    name='Curcuma en Polvo',
                    slug='curcuma-en-polvo',
                    category_id=cat('especias-y-condimentos').id,
                    origin='India',
                    presentation='10Kg y 25Kg',
                    image='/static/uploads/d99600d690ae4ee194965f28587e0a5b.png',
                    featured=True,
                    active=True,
                ),
                Product(
                    name='Canela en Rama 6cm',
                    slug='canela-en-rama-6cm',
                    category_id=cat('hierbas-medicinales').id,
                    origin='Vietnã',
                    presentation='10Kg',
                    image='/static/uploads/be939fecee924cdd962b8a6e963c69d0.png',
                    featured=True,
                    active=True,
                ),
                Product(
                    name='Anis Estrellado',
                    slug='anis-estrellado',
                    category_id=cat('especias-y-condimentos').id,
                    origin='Vietnã',
                    presentation='10Kg',
                    image='/static/uploads/c6c4adf3bef14b34b67cf361fe3f8f28.png',
                    featured=True,
                    active=True,
                ),
                Product(
                    name='Clavo de Olor',
                    slug='clavo-de-olor',
                    category_id=cat('especias-y-condimentos').id,
                    origin='Brasil',
                    presentation='25Kg',
                    image='/static/uploads/f1d1e2d3e56b42eda65f8fd91f410252.png',
                    featured=True,
                    active=True,
                ),
                Product(
                    name='Comino en Grano',
                    slug='comino-en-grano',
                    category_id=cat('especias-y-condimentos').id,
                    origin='Egipto',
                    presentation='25Kg',
                    image='/static/uploads/8e4b12ad03ff4c9ab0eb95b166d12898.png',
                    featured=True,
                    active=True,
                ),
                Product(
                    name='Manzanilla Flor',
                    slug='manzanilla-flor',
                    category_id=cat('tes-e-infusiones').id,
                    origin='Brasil',
                    presentation='Cajas de 12,5Kg',
                    image='/static/uploads/0bea983b885049539ad6e2951e018c22.png',
                    featured=True,
                    active=True,
                ),
            ]
            for p in products:
                db.session.add(p)
            db.session.commit()
            print(f"Seeded {len(products)} products.")

        # ── Site Settings (only set if not already configured) ──
        if not SiteSetting.get('whatsapp'):
            SiteSetting.set('whatsapp', '+595 983002684')
            print("Set default WhatsApp.")
        if not SiteSetting.get('email'):
            SiteSetting.set('email', 'jhonatan@grupo-dip.com')
            print("Set default email.")
        if not SiteSetting.get('hero_image'):
            SiteSetting.set('hero_image', '/static/uploads/6a6805d27ce146bfa9af82e53d827753.png')
            print("Set default hero image.")

        print("\nSeed completed!")


if __name__ == '__main__':
    seed()
