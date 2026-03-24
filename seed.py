"""
Seed script — populates the database with categories, products and settings.
Loads data from seed_data.json. Run once after first deploy: python seed.py
"""
import os
import sys
import json

sys.path.insert(0, os.path.dirname(__file__))

from app import app, db
from models import Category, Product, SiteSetting


def seed():
    with app.app_context():
        data_path = os.path.join(os.path.dirname(__file__), 'seed_data.json')
        with open(data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # ── Categories ──
        if Category.query.count() > 0:
            print("Categories already exist, skipping category seed.")
        else:
            for c in data['categories']:
                db.session.add(Category(name=c['name'], slug=c['slug'], order=c['order']))
            db.session.commit()
            print(f"Seeded {len(data['categories'])} categories.")

        # Helper
        def cat(slug):
            return Category.query.filter_by(slug=slug).first()

        # ── Products ──
        if Product.query.count() > 0:
            print("Products already exist, skipping product seed.")
        else:
            for p in data['products']:
                category = cat(p['category_slug'])
                if not category:
                    print(f"  Warning: category '{p['category_slug']}' not found for {p['name']}")
                    continue
                db.session.add(Product(
                    name=p['name'],
                    slug=p['slug'],
                    category_id=category.id,
                    origin=p.get('origin', ''),
                    description=p.get('description', ''),
                    presentation=p.get('presentation', ''),
                    image=p.get('image', ''),
                    featured=p.get('featured', False),
                    active=p.get('active', True),
                ))
            db.session.commit()
            print(f"Seeded {len(data['products'])} products.")

        # ── Site Settings ──
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
