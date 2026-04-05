# Architecture

**Analysis Date:** 2026-04-04

## Pattern Overview

**Overall:** Monolithic Flask MVC (Model-View-Controller)

**Key Characteristics:**
- Single Flask application instance serving both public site and admin panel
- SQLAlchemy ORM for database abstraction
- Server-side template rendering with Jinja2
- Session-based authentication for admin access
- RESTful API endpoints for dynamic product data
- Static asset management with cache headers

## Layers

**Presentation Layer:**
- Purpose: Render HTML templates and serve static assets to clients
- Location: `templates/`, `static/`
- Contains: HTML templates (Jinja2), CSS stylesheets, JavaScript modules
- Depends on: Flask context processors for site settings injection
- Used by: Browser clients (public and admin)

**Application/Route Layer:**
- Purpose: Define HTTP endpoints, handle requests/responses, coordinate business logic
- Location: `app.py` (all route handlers)
- Contains: Route decorators, request handlers, view functions
- Depends on: Models for data access, Config for settings
- Used by: HTTP clients, form submissions

**Business Logic Layer:**
- Purpose: Handle core operations like image upload, slug generation, authentication
- Location: Helper functions in `app.py` (lines 17-72)
- Contains: `allowed_file()`, `slugify()`, `login_required()`, `save_image()`, context processors
- Depends on: Config, file system, werkzeug utilities
- Used by: Route handlers

**Data Layer:**
- Purpose: Define database schema and provide data access patterns
- Location: `models.py`
- Contains: SQLAlchemy models (Category, Product, SiteSetting)
- Depends on: SQLAlchemy ORM, datetime library
- Used by: Route handlers, seed script

**Configuration Layer:**
- Purpose: Centralize environment-aware settings
- Location: `config.py`
- Contains: Database URI, upload folder, secret key, admin credentials
- Depends on: Environment variables
- Used by: Flask app initialization

## Data Flow

**Public Page View Request:**

1. Browser requests `/` or `/productos` or `/producto/<slug>`
2. Flask route handler (`index()`, `productos()`, `producto()`) receives request
3. Handler queries database via SQLAlchemy models (Category, Product)
4. Context processor injects site settings (WhatsApp, email, hero image) into template context
5. Jinja2 renders template with data
6. Response headers add cache/security directives
7. HTML sent to browser

**Product Modal Load (JavaScript):**

1. User clicks product card on public site
2. JavaScript event listener opens modal dialog
3. AJAX fetch to `/api/producto/<slug>` endpoint
4. Route handler queries Product by slug, returns `to_dict()` JSON
5. JavaScript populates modal with product details
6. Modal displays with WhatsApp contact link

**Admin Product Create/Edit:**

1. Admin navigates to `/admin/producto/nuevo` (new) or `/admin/producto/<id>/editar` (edit)
2. `login_required` decorator validates session (line 33-39)
3. GET request renders form template with category list
4. POST request processes form data with validation
5. If file uploaded, `save_image()` generates UUID filename, saves to `UPLOAD_FOLDER`
6. `slugify()` generates URL-safe slug from product name
7. Product created or updated via SQLAlchemy
8. Redirect to products list with flash message
9. Data persists to database (SQLite local or PostgreSQL production)

**Site Settings Update:**

1. Admin submits `/admin/configuracion` form
2. `SiteSetting.set(key, value)` called for each setting
3. Settings stored in `site_settings` table using key-value pattern
4. On next public page load, `inject_site_settings()` context processor retrieves settings
5. Settings available in all template renders via context

**State Management:**

- Session state: Admin login stored in Flask session (line 245: `session['admin_logged_in'] = True`)
- Database state: All persistent data in SQLAlchemy models
- Request state: Form submissions handled via POST, redirect pattern to prevent duplication
- Context state: Template context injected via context processor (line 77-89)

## Key Abstractions

**SiteSetting (Key-Value Store):**
- Purpose: Flexible configuration management without code changes
- Examples: WhatsApp number, email, hero image URL stored in database
- Pattern: Static get/set methods (lines 55-68 in models.py) use singleton pattern per key
- Usage: Admin configures via form, retrieved in context processor for all templates

**Product.to_dict():**
- Purpose: Serialize Product model to JSON for AJAX responses
- Examples: Used in `/api/producto/<slug>` endpoint (line 137 in app.py)
- Pattern: Instance method returning dictionary with all product fields
- Usage: Allows JavaScript modal to populate without page reload

**Category Relationships:**
- Purpose: Organize products hierarchically, enable filtering
- Examples: `Product.category_id` foreign key, `Category.products` backref
- Pattern: SQLAlchemy relationship allows `category.products` iteration and cascading queries
- Usage: Public site displays products by category with slug-based routing

## Entry Points

**Application Startup:**
- Location: `app.py` (lines 11-13)
- Triggers: `python app.py` or gunicorn server startup
- Responsibilities: Initialize Flask app, configure with Config, initialize database

**Database Initialization:**
- Location: `app.py` (lines 407-418)
- Triggers: App context initialization at startup
- Responsibilities: Create tables via `db.create_all()`, seed data if empty

**Public Homepage:**
- Location: `app.py` route `/` (line 105-109)
- Triggers: GET request to domain root
- Responsibilities: Fetch featured products and categories, render index template

**Admin Dashboard:**
- Location: `app.py` route `/admin` (line 255-266)
- Triggers: Authenticated GET request to `/admin`
- Responsibilities: Count products/categories, display dashboard stats

**SEO Routes:**
- Location: `app.py` routes `/robots.txt`, `/sitemap.xml`, `/sitemap-products.xml` (lines 141-219)
- Triggers: GET requests from search engine crawlers
- Responsibilities: Generate XML sitemaps dynamically from database, control crawler access

## Error Handling

**Strategy:** Flask's default error handling with custom templates

**Patterns:**

- 404 Not Found: Custom handler (line 221-223) renders `404.html`
- Database query failures: Flask automatic 404 via `first_or_404()` (line 116, 126)
- Form validation: Flash messages with error category (lines 285, 336)
- File upload: Extension validation before save (lines 19-20, 62-67)
- Authentication: Redirect to login page if session not found (lines 34-38)
- Database operations: Direct commit without try/catch (assumes Railway/hosting stability)

## Cross-Cutting Concerns

**Security Headers (lines 43-59):**
- Pattern: `@app.after_request` decorator adds headers to all responses
- Implements: X-Content-Type-Options, X-Frame-Options, X-XSS-Protection, Strict-Transport-Security
- Effect: Applied to every HTTP response automatically

**Caching Strategy (lines 52-58):**
- Static assets (CSS, JS): 1 year immutable cache
- Images (product uploads): 30 days
- HTML pages: 5 minutes (allows static caching while staying fresh)
- Pattern: Content-Type inspection in after_request hook

**SEO Metadata (templates/base.html):**
- Open Graph tags for social sharing
- Schema.org JSON-LD for rich snippets
- Hreflang tags for regional targeting
- Google Search Console verification meta tag
- Pattern: Base template includes all meta, child templates override specific blocks

**Logging:** 
- Strategy: Flask development server console logs (no external service)
- Pattern: Print statements in seed script, flash messages for user feedback

**Validation:**
- Product creation: Name and category required (line 335)
- Category deletion: Prevents deletion if products exist (line 303-304)
- Image upload: File extension whitelist only (line 19-20)
- Pattern: Validation before database operation, flash error feedback

**Authentication:**
- Method: Session-based with hardcoded credentials from config
- Pattern: `login_required` decorator (lines 33-39) wraps admin routes
- Storage: Flask session object (line 245)
- Logout: Session.pop removes admin_logged_in flag (line 252)

---

*Architecture analysis: 2026-04-04*
