# Codebase Concerns

**Analysis Date:** 2026-04-04

## Security Issues

**Hardcoded Default Credentials:**
- Issue: Default admin password exposed in code and seed data
- Files: `config.py` (line 21), `seed.py` (line 59)
- Details: `ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'graos2026')` - hardcoded fallback password
- Impact: Anyone accessing source code or deployed app without environment variables set can log into admin panel
- Fix approach: Remove hardcoded defaults entirely; require environment variables and fail loudly during startup if missing. Add startup validation check in `app.py`

**Weak Secret Key Default:**
- Issue: Insecure default SECRET_KEY for session encryption
- Files: `config.py` (line 4)
- Details: `SECRET_KEY = os.environ.get('SECRET_KEY', 'graos-sa-secret-key-change-in-production')`
- Impact: If environment variable not set, Flask sessions use a predictable key, allowing session forgery attacks
- Fix approach: Generate random secret during initialization or fail startup; never ship with default production-like secrets

**Plain-Text Admin Authentication:**
- Issue: No password hashing on admin credentials
- Files: `app.py` (line 244)
- Details: Direct string comparison: `if username == app.config['ADMIN_USERNAME'] and password == app.config['ADMIN_PASSWORD']`
- Impact: Admin credentials stored in plaintext environment variables; if env vars exposed, login is compromised
- Fix approach: Implement proper password hashing with werkzeug.security (already available) or use bcrypt. Store hashed password in database, not env vars

**Unvalidated File Upload:**
- Issue: Image upload accepts any allowed extension without content validation
- Files: `app.py` (lines 61-72)
- Details: Function checks only file extension using `allowed_file()`, not actual file MIME type or content
- Impact: Potential for uploading malicious files disguised with image extension; no virus/malware scanning
- Fix approach: Validate actual file content using python-magic or PIL to verify image headers match extension

**Missing CSRF Protection:**
- Issue: No CSRF tokens on forms (admin and contact)
- Files: `templates/admin/product_form.html`, `templates/admin/category_form.html`, `templates/contacto.html`
- Details: Forms lack Flask-WTF CSRF tokens for state-changing operations (POST/PUT/DELETE)
- Impact: Cross-site request forgery attacks possible on admin forms and contact submission
- Fix approach: Integrate Flask-WTF, add `{{ csrf_token() }}` to all forms, protect routes with `@csrf.protect`

**XSS Vulnerability in Modal:**
- Issue: Unsanitized user input in product modal JavaScript
- Files: `static/js/app.js` (lines 116-150)
- Details: Product data from API injected directly into HTML without escaping:
  ```javascript
  imgHtml = '<img src="' + p.image + '" alt="' + p.name + '">'
  box.innerHTML = ... (contains p.name, p.origin, p.description, p.category_name)
  ```
- Impact: If product name/description contains JavaScript, it executes in user's browser; stored XSS if admin account compromised
- Fix approach: Use `textContent` for text, `createElement()` for DOM building, or sanitize with DOMPurify library before `innerHTML`

**Missing Input Sanitization:**
- Issue: Contact form data not sanitized before processing
- Files: `app.py` (lines 229-235)
- Details: Form submission accepted but not sanitized; no validation on form data before any storage
- Impact: If contact form data stored or forwarded via webhook, malicious input could cause issues
- Fix approach: Add input validation/sanitization with WTForms or marshmallow; escape before storing/displaying

**Exposed API Endpoint:**
- Issue: Unprotected API endpoint exposes product details to unauthenticated users
- Files: `app.py` (lines 134-137)
- Details: `/api/producto/<slug>` returns full product JSON without rate limiting or authentication
- Impact: Could enable scraping or reconnaissance; also used by modal popup to load data
- Fix approach: Consider rate limiting via Flask-Limiter; if internal use only, document as such

---

## Performance Bottlenecks

**N+1 Query in Related Products:**
- Issue: Related products query may trigger additional database lookups
- Files: `app.py` (lines 127-131)
- Details: Product view loads category for each related product:
  ```python
  related = Product.query.filter(...).limit(4).all()
  # Then template accesses product.category.name → lazy load per row
  ```
- Impact: If rendered in template, accesses category relationship 5+ times (1 main + 4 related), 5 database queries instead of 1-2
- Fix approach: Use `joinedload()` or explicit join: `Product.query.outerjoin(Category).options(contains_eager(Product.category))`

**Unoptimized Category/Product Queries:**
- Issue: Homepage featured products query lacks indexing hints
- Files: `app.py` (line 107)
- Details: `Product.query.filter_by(active=True, featured=True).order_by(Product.name).limit(8)`
- Impact: As products grow, full table scan on active+featured; no composite index strategy
- Fix approach: Add database indexes on `(featured, active, name)` in models via `db.Index()`

**Sitemap XML String Concatenation:**
- Issue: Large XML generated via string concatenation in Python
- Files: `app.py` (lines 156-189, 191-219)
- Details: Builds entire XML sitemap in memory via string concatenation for potentially hundreds of products
- Impact: Memory inefficient; slow response times; no streaming
- Fix approach: Use XML libraries (xml.etree.ElementTree) or template-based generation; implement pagination for large sitemaps

**Cart Modal Fetch per Product:**
- Issue: Each product modal click triggers API request
- Files: `static/js/app.js` (lines 107-156)
- Details: Modal opens → fetches `/api/producto/<slug>` for each click
- Impact: Network overhead; no caching; duplicated API calls if user opens same product multiple times
- Fix approach: Implement fetch caching in JavaScript; pre-load data or use server-side rendering for modal

---

## Tech Debt & Architecture Issues

**Monolithic Main Application File:**
- Issue: All routes and logic in single `app.py` file (424 lines)
- Files: `app.py`
- Details: Admin routes, public routes, context processors, helper functions all mixed; no separation of concerns
- Impact: Hard to test individual features; difficult to maintain as project grows; blueprint imports would help
- Fix approach: Split into blueprints: `routes/public.py`, `routes/admin.py`, `routes/api.py`, `helpers/`, `utils/`

**Hardcoded Domain in Sitemaps:**
- Issue: Domain hardcoded as string literal in sitemap routes
- Files: `app.py` (lines 160, 195)
- Details: `base = 'https://www.graos.com.py'` hardcoded in two sitemap functions
- Impact: Not configurable; would need code change to use different domain; production/staging requires different domains
- Fix approach: Move to config: `SITE_URL = os.environ.get('SITE_URL', 'https://www.graos.com.py')` in `config.py`, use in routes

**No Error Logging or Monitoring:**
- Issue: No structured logging or error tracking
- Files: All Python files
- Details: No logging module used; no error handlers beyond 404
- Impact: Production errors silent; no visibility into failures; hard to debug issues after deployment
- Fix approach: Add Python logging; integrate with error tracking (Sentry, LogRocket, etc.); log admin actions

**Database Transactions Not Explicitly Managed:**
- Issue: No explicit rollback or transaction management
- Files: `app.py` (multiple db.session.commit() calls), `models.py` (line 68)
- Details: Commits scattered throughout routes; no try/except for database errors
- Impact: Silent failures if database issues; partial data updates could leave inconsistent state
- Fix approach: Wrap critical operations in transactions with explicit rollback; use context managers

**No Rate Limiting on Admin Login:**
- Issue: Admin login endpoint accepts unlimited authentication attempts
- Files: `app.py` (lines 239-248)
- Details: `/admin/login` POST accepts unlimited password guesses with no throttling
- Impact: Brute force attacks possible on default credentials; slow but achievable
- Fix approach: Use Flask-Limiter to limit login attempts (e.g., 5 attempts per IP per 15 minutes)

**Session Storage Not Configured:**
- Issue: Session cookies stored in default (in-memory) Flask session
- Files: `config.py`
- Details: No `SESSION_PERMANENT`, `PERMANENT_SESSION_LIFETIME`, or backend (Redis/memcached) configured
- Impact: Sessions lost on restart; not suitable for production; no shared session store for multiple app instances
- Fix approach: Configure permanent sessions, set secure cookie flags (Secure, HttpOnly, SameSite), consider Redis backend

---

## Known Issues & Bugs

**Contact Form Not Actually Processing Submissions:**
- Issue: Contact form submission shows success but data not sent anywhere
- Files: `app.py` (lines 229-235)
- Details: Form accepted, flash message shown, redirects back to form, but no actual email/webhook/storage
- Impact: Users believe message sent; business never receives inquiries; leads lost
- Fix approach: Implement email sending (Flask-Mail + SMTP), webhook integration, or database storage of submissions

**No Migration System:**
- Issue: Database schema changes require manual SQL or re-seeding
- Files: All schema in `models.py`
- Details: No Alembic or Flask-Migrate setup
- Impact: Difficult to deploy schema changes in production; risky for data integrity
- Fix approach: Integrate Flask-Migrate: `flask db init`, `flask db migrate`, `flask db upgrade`

**Seed Data Contains Hardcoded Media Paths:**
- Issue: Seed file hardcodes image URLs that may not exist
- Files: `seed.py` (line 65)
- Details: `SiteSetting.set('hero_image', '/static/uploads/6a6805d27ce146bfa9af82e53d827753.png')` — assumes file exists
- Impact: If image not present on fresh deploy, hero breaks silently
- Fix approach: Validate seed data; store actual image files in repo or cloud storage; use environment variable for hero image

**Timezone Handling Not Explicit:**
- Issue: Timestamps use `datetime.utcnow()` but no timezone awareness
- Files: `models.py` (line 31), `app.py` (line 159)
- Details: `created_at = db.Column(db.DateTime, default=datetime.utcnow)` — naive datetime; mixed with strftime
- Impact: Ambiguous whether times are UTC or local; can cause bugs across regions
- Fix approach: Use `datetime.datetime.utcnow()` or switch to timezone-aware `datetime.datetime.now(datetime.UTC)` (Python 3.12+)

**Pillow Dependency Unused:**
- Issue: Pillow listed in requirements but not imported or used
- Files: `requirements.txt` (line 5)
- Details: Included but no image processing code exists
- Impact: Unnecessary dependency; bloated virtual environment
- Fix approach: Remove if not used, or add image resizing/optimization logic if intended

---

## Deployment & Configuration Issues

**Debug Mode Enabled in Production:**
- Issue: Flask debug mode hardcoded to True
- Files: `app.py` (line 424)
- Details: `app.run(..., debug=True)` always enabled
- Impact: Detailed error pages expose code/environment; code reloader slows startup; security risk
- Fix approach: Use `debug=os.environ.get('FLASK_DEBUG', False) != 'False'` or separate config

**No Werkzeug/SQLAlchemy Deprecation Handling:**
- Issue: Using deprecated PostgreSQL URI scheme (handled with workaround)
- Files: `config.py` (lines 7-8)
- Details: Code replaces `postgres://` with `postgresql://` but this is a band-aid
- Impact: Fragile; future SQLAlchemy versions may drop backward compat
- Fix approach: Ensure Railway/environment provides correct PostgreSQL URI format from start

**Multiple Database Initialization Patterns:**
- Issue: Both `init_db()` function and auto-seeding in `app.py`
- Files: `app.py` (lines 409-418)
- Details: `init_db()` called at module load time; also mentioned in seed.py docstring to "run once"
- Impact: Confusion about when/how to seed; automatic seeding on every app start could overwrite data
- Fix approach: Clarify: seeding should be one-time CLI command, not automatic; use Flask CLI: `flask seed`

**No Environment Validation:**
- Issue: App doesn't validate required environment variables on startup
- Files: `config.py`
- Details: Missing env vars silently use defaults (credentials, secret key)
- Impact: Misconfigured production deployment runs without warning
- Fix approach: Add startup validation in `app.py` to check required env vars exist before accepting requests

**Max Upload Size Not Enforced Properly:**
- Issue: MAX_CONTENT_LENGTH set but no per-field validation
- Files: `config.py` (line 19)
- Details: Global 10MB limit set, but no feedback on oversized image
- Impact: User uploads oversized file, gets generic error, unclear why submission failed
- Fix approach: Add client-side validation and server-side error message for file size

---

## Testing & Quality Gaps

**No Test Suite:**
- Issue: Zero test files in repository
- Files: None found
- Details: No unit tests, integration tests, or E2E tests
- Impact: Refactoring risky; bugs introduced unknowingly; regressions not caught
- Fix approach: Add `tests/` directory; use pytest; target 80%+ coverage on critical paths (auth, API, models)

**No Type Hints:**
- Issue: Python code has no type annotations
- Files: `app.py`, `models.py`, `config.py`, `seed.py`
- Details: All functions lack `: Type` hints on parameters/returns
- Impact: IDE autocomplete limited; refactoring harder; bugs caught only at runtime
- Fix approach: Add type hints to all functions; use `mypy` for static type checking in CI

**No Linting or Formatting:**
- Issue: No linter (pylint, flake8) or formatter (black, autopep8) configured
- Files: All Python files
- Details: Inconsistent style; trailing whitespace possible; import organization not enforced
- Fix approach: Add `black` for formatting, `flake8` or `ruff` for linting; configure pre-commit hooks

**No Frontend Build Pipeline:**
- Issue: HTML/CSS/JS served directly without optimization
- Files: `static/`, `templates/`
- Details: Large app.js (185 lines); CSS likely uncompressed; no minification
- Impact: Slower page loads; bandwidth waste
- Fix approach: Consider build tool (Webpack, Vite, or simple minifier script) for production

---

## Fragile Areas

**Category Deletion Constraint:**
- Issue: Deletion blocked if category has products, but error not graceful
- Files: `app.py` (lines 301-309)
- Details: Check blocks delete but doesn't redirect back with proper context
- Impact: User sees vague error; must navigate back manually
- Fix approach: Store category reference context in session; pre-load category before delete check; show affected product count

**Slug Generation Not Idempotent:**
- Issue: Slug created during product/category creation/edit, but not validated for collisions
- Files: `app.py` (lines 346, 289)
- Details: `slugify()` applied to name, but if two products have same name, slug collision occurs
- Impact: Second product with same name fails to save with database error
- Fix approach: Add slug uniqueness check before commit; generate sequential suffix (e.g., `-2`, `-3`) if collision

**Related Products Query Fragile:**
- Issue: Related products might be empty, causing template rendering issues
- Files: `app.py` (lines 127-131)
- Details: `.limit(4).all()` always returns list, but could be empty; template should handle
- Impact: If category has only 1 product, related section renders empty
- Fix approach: Verify template handles empty related list gracefully; consider fallback to other categories

---

## Scaling & Growth Concerns

**No Caching Strategy:**
- Issue: No caching on any routes (browser, CDN, or server-side)
- Files: All routes
- Details: Cache headers set (in `add_security_headers`) but no actual caching logic
- Impact: Repeated database queries for same data; slow site as product count grows
- Fix approach: Implement Flask-Caching with Redis backend; cache category list, featured products, product pages

**Single Database Connection String:**
- Issue: No connection pooling configuration
- Files: `config.py`
- Details: SQLAlchemy defaults to small pool; no size or overflow settings
- Impact: As concurrent users grow, connection pool exhaustion possible
- Fix approach: Add pool settings: `SQLALCHEMY_ENGINE_OPTIONS = {'pool_size': 10, 'pool_recycle': 3600}`

**No Read Replicas or Query Optimization:**
- Issue: All queries hit single database instance
- Files: All `app.py` queries
- Details: No separation of read/write databases
- Impact: Read-heavy operations (product listing, search) compete with writes; scales to point then fails
- Fix approach: Plan for read replicas; add query indexes; consider full-text search engine (Elasticsearch) later

**Image Storage Scalability:**
- Issue: Local filesystem or Railway volume for image storage; no CDN
- Files: `app.py` (lines 61-72), `config.py`
- Details: Images stored locally; served via Flask app
- Impact: Slow image delivery; app server tied up serving static files; won't scale geographically
- Fix approach: Migrate to S3/Cloudinary/similar; update `save_image()` to upload to cloud; serve via CDN

---

## Dependencies & Maintenance

**Pillow Unused Dependency:**
- Issue: Listed in requirements but not imported anywhere
- Files: `requirements.txt` (line 5)
- Impact: Unnecessary bloat; adds security surface area; unused features
- Fix approach: Remove or implement image resizing/optimization if intended

**No Dependency Pinning:**
- Issue: Requirements.txt pins to minor versions but not patch versions
- Files: `requirements.txt`
- Details: `flask==3.1.0` pins version, but no lock file (poetry.lock, pipenv.lock)
- Impact: Can't guarantee reproducible builds across environments
- Fix approach: Generate lock file: `pip freeze > requirements-lock.txt` or use Poetry/Pipenv

**Outdated Python Version (Minor):**
- Issue: Python 3.12.8 specified; 3.12 LTS will eventually EOL
- Files: `runtime.txt`
- Impact: Security updates will stop in ~2.5 years
- Fix approach: No action needed now, but plan upgrade path annually

---

## Missing Features That Indicate Incomplete Implementation

**Contact Form Not Integrated:**
- Issue: Form UI exists but backend doesn't process submissions
- Files: `templates/contacto.html`, `app.py` (lines 229-235)
- Details: Form shown, success message flashed, but no email/webhook/database storage
- Priority: High — leads being lost
- Fix approach: Implement email or webhook handler; consider Firebase Cloud Functions or Resend API

**No Admin Audit Trail:**
- Issue: No tracking of who deleted/edited what and when
- Files: `app.py` (admin routes)
- Details: Products edited silently without change history
- Priority: Medium — important for accountability
- Fix approach: Add audit log table; track `admin_id`, `action`, `changes`, `timestamp` for all admin operations

**No Search/Filter on Products:**
- Issue: Product page loads all products; no search or advanced filtering
- Files: `app.py` (line 120), `templates/productos.html`
- Details: Products listed but no way to search by name, origin, etc.
- Priority: Medium — improves UX as catalog grows
- Fix approach: Add search parameter handling; implement full-text search in database

**No Pagination on Product List:**
- Issue: All active products loaded into memory and template
- Files: `app.py` (line 120)
- Details: No `.paginate()` call; entire product list rendered
- Priority: Medium-Low — matters when product count exceeds 100+
- Fix approach: Use Flask-SQLAlchemy `.paginate()`; implement pagination UI in templates

---

*Concerns audit: 2026-04-04*
