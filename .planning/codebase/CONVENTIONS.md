# Coding Conventions

**Analysis Date:** 2026-04-04

## Naming Patterns

**Files:**
- Python modules: lowercase with underscores (`app.py`, `config.py`, `models.py`, `seed.py`)
- Template files: lowercase with hyphens or underscores (`base.html`, `product_form.html`, `admin/dashboard.html`)
- Static assets: lowercase with hyphens (`style.css`, `admin.css`, `app.js`)
- Image files: UUID-based unique names for uploads (`09e9628098da474cb500c0d384eb35e5.png`)

**Functions:**
- Python functions: snake_case (`allowed_file()`, `slugify()`, `login_required()`, `save_image()`)
- JavaScript functions: camelCase (`openProductModal()`, `closeModal()`, `step()`)
- Route handlers: snake_case, descriptive (`admin_login()`, `admin_product_form()`, `api_producto()`)
- Helper functions: prefixed descriptors (`inject_site_settings()`, `init_db()`)

**Variables:**
- Python: snake_case (`admin_logged_in`, `featured_products`, `upload_folder`, `whatsapp_raw`)
- JavaScript: camelCase in modern code, var prefix for scope tracking (`imgHtml`, `detailsHtml`, `waLink`, `modalClose`)
- Database fields: snake_case (`created_at`, `category_id`, `featured`, `active`)
- CSS custom properties: kebab-case (`--green`, `--gray-800`, `--max-w`, `--nav-h`)

**Types (Python):**
- Model classes: PascalCase (`Category`, `Product`, `SiteSetting`)
- Database columns: lowercase with underscores in SQLAlchemy (`db.String`, `db.Integer`, `db.DateTime`)

## Code Style

**Formatting:**
- No automatic formatter configured (black, isort not detected)
- Manual PEP 8 style observed in Python code
- CSS uses minified format (single line per section with comments)
- JavaScript uses unminified format for readability

**Line Length:**
- Python: Generally follows 80-100 character limit (flexible)
- JavaScript: No strict limit observed, pragmatic line breaks

**Imports Organization (Python):**
1. Standard library (`os`, `re`, `uuid`, `functools`, `json`, `sys`)
2. Third-party Flask and extensions (`flask`, `werkzeug`, `flask_sqlalchemy`)
3. Local application imports (`config`, `models`, `seed`)

Example from `app.py`:
```python
import os
import re
import uuid
from functools import wraps
from flask import (Flask, render_template, request, redirect, url_for,
                   flash, session, jsonify, send_from_directory, Response, make_response)
from werkzeug.utils import secure_filename
from config import Config
from models import db, Category, Product, SiteSetting
```

**Imports Organization (JavaScript):**
- No formal imports used; all functionality in single `app.js`
- Code organized by functional sections with comments (`/* ═══ SECTION ═══ */`)

## Linting & Code Quality

**Linting:** Not detected - no `.eslintrc*`, `flake8`, or `pylint` config files
**Formatting:** No detected linters or formatters (no black, prettier, isort config)

**Manual style indicators:**
- Comments use decorative separators: `# ──────────────────── LABEL ────────────────────`
- Section markers in JavaScript: `/* ═══ LABEL ═══ */`
- Organized by feature/route in Python files

## Error Handling

**Patterns:**
- Flash messages for user feedback: `flash('Message text', 'error')` or `flash('Message text', 'success')`
- 404 handling: `first_or_404()` and `get_or_404()` from Flask-SQLAlchemy
- Custom error handler registered: `@app.errorhandler(404)` returns 404.html template
- Exception handling via Flask's built-in mechanisms (no try/except blocks observed in main code)

**Validation:**
- Client-side validation in forms (HTML required attributes)
- Server-side validation: explicit checks before database operations
  - Example: `if not name or not category_id: flash('error message')`
- File validation: `allowed_file()` checks file extension against whitelist

**Form Processing:**
- Direct request.form.get() with optional type conversion
- Strip whitespace from user input: `.strip()`
- Boolean fields: check for 'on' value from checkbox inputs

Example from `app.py` lines 326-338:
```python
if request.method == 'POST':
    name = request.form.get('name', '').strip()
    category_id = request.form.get('category_id', type=int)
    origin = request.form.get('origin', '').strip()
    featured = request.form.get('featured') == 'on'
    active = request.form.get('active') == 'on'
    
    if not name or not category_id:
        flash('Nombre y categoría son obligatorios', 'error')
        return render_template('admin/product_form.html', product=product, categories=categories)
```

## Logging

**Framework:** Python `print()` for seed script logging only

**Patterns:**
- No centralized logging framework detected
- Seed script uses `print()` for progress: `print(f"Seeded {len(data['categories'])} categories.")`
- Flask flash messages used for user-visible feedback instead of logging

**JavaScript:**
- No logging framework; no console.log statements observed
- Errors caught silently with fallback messaging: `box.innerHTML = '<div class="modal-loading">Error al cargar el producto.</div>'`

## Comments

**When to Comment:**
- Section headers: decorative separators for major code blocks
- Non-obvious regex patterns: `re.sub(r'[áàãâä]', 'a', text)` used without comment but self-explanatory
- Complex algorithms: Counter animation in `app.js` includes step function
- Database schema relationships documented in models

**JSDoc/TSDoc:**
- Not used in this codebase
- Python docstrings minimal: only seed() function has docstring
- Seed function docstring example from `seed.py` line 1-4:
```python
"""
Seed script — populates the database with categories, products and settings.
Loads data from seed_data.json. Run once after first deploy: python seed.py
"""
```

**Inline Comments:**
- Decorative markers for sections: `# ──────────────────── HELPERS ────────────────────`
- Purpose markers: `# If using Railway volume, serve via /uploads/ route; otherwise static path`
- Helper function comments: `# Strip everything except digits for the wa.me link`
- Category lookup helper: `# Helper` comment at line 30 in `seed.py`

## Function Design

**Size:**
- Small, focused functions preferred
- Route handlers typically 5-20 lines
- Helper functions: 5-10 lines
- Longest function: `admin_product_form()` at ~50 lines (acceptable due to form complexity)

**Parameters:**
- Explicit parameters for route handlers (Flask style)
- Default parameters used for optional form fields: `request.form.get('origin', '').strip()`
- **kwargs pattern: `f(*args, **kwargs)` in decorator pattern

**Return Values:**
- Flask routes return: `render_template()`, `redirect()`, `jsonify()`, `Response`
- Helper functions return: primitives (strings, booleans), database objects
- API routes return JSON via `jsonify()`

## Module Design

**Exports:**
- `app.py`: Flask app object and routes
- `models.py`: Database models (Category, Product, SiteSetting)
- `config.py`: Config class with environment-based settings
- `seed.py`: seed() function for database initialization

**Barrel Files:**
- Not used; imports are explicit

**Database Transaction Pattern:**
- All database operations use `db.session.add()`, `db.session.delete()`, `db.session.commit()`
- Model methods: `@staticmethod` for utility methods (e.g., `SiteSetting.get()`, `SiteSetting.set()`)

**Context Processors:**
- `@app.context_processor` for injecting template globals (line 76-89)
- Makes site settings available to all templates

**Decorators:**
- `@login_required` custom decorator wraps protected routes
- `@app.after_request` for security headers
- `@app.context_processor` for template context
- `@app.route()` for URL routing (supports multiple URLs: `/admin/categoria/<int:id>/editar` and `/admin/categoria/nueva`)

## Security Patterns

**Authentication:**
- Custom `login_required()` decorator checks `session.get('admin_logged_in')`
- Session-based with username/password comparison (lines 244)
- No password hashing; credentials stored in environment variables

**Security Headers:**
- Added via `@app.after_request` decorator (lines 43-59)
- Includes: X-Content-Type-Options, X-Frame-Options, X-XSS-Protection, Referrer-Policy, Permissions-Policy, HSTS
- Cache control headers vary by content type

**File Uploads:**
- Whitelist validation: `ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp', 'gif'}`
- UUID-based filename generation for security
- Size limit: 10MB max (`MAX_CONTENT_LENGTH = 10 * 1024 * 1024`)

**URL Slugs:**
- Auto-generated from product/category names via `slugify()` function
- Removes accents and special characters, uses kebab-case

## Template Patterns

**Template Inheritance:**
- Two-level hierarchy: `base.html` and `admin/base.html` as parents
- Blocks used: `{% block title %}`, `{% block content %}`, `{% block meta_* %}`
- Context processor provides globals: site settings, WhatsApp info

**Conditionals:**
- `{% if condition %}...{% endif %}`
- `{% for item in list %}...{% endfor %}`
- Active route detection: `{% if request.endpoint == 'admin_dashboard' %}active{% endif %}`

**Filters:**
- Standard Jinja2: `{{ value|lower }}`, `{{ list|length }}`
- No custom filters observed

---

*Convention analysis: 2026-04-04*
