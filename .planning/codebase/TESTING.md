# Testing Patterns

**Analysis Date:** 2026-04-04

## Test Framework

**Status:** No testing framework detected

This codebase currently has **no automated tests**. There are:
- No test files (no `*_test.py`, `test_*.py`, `*_spec.py` files)
- No test runner configuration (`pytest.ini`, `setup.cfg`, `tox.ini`)
- No testing dependencies in `requirements.txt` (Flask, SQLAlchemy, Gunicorn, Pillow, psycopg2 only)

**Recommended Setup (for future implementation):**
```
# Add to requirements.txt:
pytest==7.4.0
pytest-flask==1.2.0
pytest-cov==4.1.0
```

## Run Commands (If Implemented)

Once testing framework is added, conventions would be:

```bash
pytest                          # Run all tests
pytest -v                       # Verbose output
pytest --cov=.                  # Coverage report
pytest -k "test_login"          # Run specific test
pytest -x                       # Stop on first failure
```

## Testing Strategy (Current Approach)

**Manual Testing Only:**
- Routes tested via browser/Postman
- Admin panel functionality verified in UI
- No regression protection
- High risk of breaking changes

**What Should Be Tested:**
- Route handlers (all public and admin routes)
- Database models and relationships
- Helper functions (slugify, allowed_file)
- Authentication decorator
- Form validation and error handling
- SEO routes (robots.txt, sitemap.xml)

## Database Testing Approach

**Current:** SQLite for development (defined in `config.py`)

```python
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///graos.db')
```

**For Testing (recommended pattern):**
- Use in-memory SQLite for unit tests
- Provide test fixture that creates/tears down database

**Example pattern to implement:**

```python
# tests/conftest.py
import pytest
from app import app, db

@pytest.fixture
def test_client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()
```

## Test File Organization

**Recommended Structure (not currently implemented):**

```
tests/
├── conftest.py                 # Pytest fixtures and configuration
├── test_routes.py              # Route handler tests
├── test_models.py              # Model and database tests
├── test_helpers.py             # Helper function tests
├── test_auth.py                # Authentication and login tests
├── test_forms.py               # Form validation tests
└── fixtures/
    ├── categories.json         # Test data
    └── products.json           # Test data
```

**Naming Convention (if implemented):**
- Test files: `test_*.py`
- Test functions: `test_<feature>_<scenario>()` (e.g., `test_login_success()`, `test_login_invalid_password()`)
- Test classes: `Test<Component>` (e.g., `TestProductRoutes`)

## Test Structure Pattern (To Implement)

**Recommended Arrange-Act-Assert pattern:**

```python
def test_admin_login_success(test_client):
    # Arrange
    app.config['ADMIN_USERNAME'] = 'testadmin'
    app.config['ADMIN_PASSWORD'] = 'testpass123'
    
    # Act
    response = test_client.post('/admin/login', data={
        'username': 'testadmin',
        'password': 'testpass123'
    })
    
    # Assert
    assert response.status_code == 302
    assert response.location.endswith('/admin')
```

**For Route Tests:**

```python
def test_index_returns_featured_products(test_client):
    """GET / should render index with featured products."""
    response = test_client.get('/')
    assert response.status_code == 200
    assert b'Grãos S.A.' in response.data
```

**For Model Tests:**

```python
def test_product_to_dict(test_client):
    """Product.to_dict() should return proper dictionary structure."""
    # Create test product
    category = Category(name='Test', slug='test', order=1)
    product = Product(
        name='Test Product',
        slug='test-product',
        category_id=1,
        image='/test.png'
    )
    
    result = product.to_dict()
    assert result['name'] == 'Test Product'
    assert result['slug'] == 'test-product'
    assert 'image' in result
```

## Fixtures and Test Data

**Current Status:** No fixtures or test data generators

**Pattern to Implement:**

Create `tests/fixtures/` directory with:

```json
// tests/fixtures/categories.json
[
  {
    "id": 1,
    "name": "Especias",
    "slug": "especias",
    "order": 1
  },
  {
    "id": 2,
    "name": "Condimentos",
    "slug": "condimentos",
    "order": 2
  }
]
```

**Factory pattern in conftest.py:**

```python
@pytest.fixture
def sample_category(test_client):
    """Fixture that creates a test category."""
    with app.app_context():
        cat = Category(name='Test Category', slug='test-category', order=1)
        db.session.add(cat)
        db.session.commit()
        yield cat

@pytest.fixture
def sample_product(sample_category):
    """Fixture that creates a test product."""
    with app.app_context():
        prod = Product(
            name='Test Product',
            slug='test-product',
            category_id=sample_category.id,
            description='Test description'
        )
        db.session.add(prod)
        db.session.commit()
        yield prod
```

## Mocking Patterns

**Current Status:** No mocking framework detected

**Recommended Approach (to implement):**

Use `unittest.mock` from Python standard library (no external dependency):

```python
from unittest.mock import patch, MagicMock

def test_save_image_skips_invalid_files(test_client):
    """save_image() should return empty string for invalid files."""
    mock_file = MagicMock()
    mock_file.filename = 'test.exe'
    
    result = save_image(mock_file)
    assert result == ''
    mock_file.save.assert_not_called()

def test_slugify_handles_accents():
    """slugify() should remove Portuguese/Spanish accents."""
    assert slugify('Café com Açúcar') == 'cafe-com-acucar'
    assert slugify('Pimienta Negra') == 'pimienta-negra'
```

**What to Mock:**
- File uploads (mock Werkzeug FileStorage objects)
- Environment variables (for testing Railway-specific paths)
- External API calls (if WhatsApp integration added later)

**What NOT to Mock:**
- Database models (use test database instead)
- Helper functions (they're simple and should be tested directly)
- Flask test client (it's designed for testing)

## Coverage Targets (To Implement)

**Recommended Minimums:**
- Overall: 80%+ coverage
- Route handlers: 90%+ (these handle user input)
- Models: 95%+ (critical for data integrity)
- Helpers: 100% (small, pure functions)

**Run Coverage:**

```bash
pytest --cov=app --cov=models --cov=helpers --cov-report=html
# Opens htmlcov/index.html for detailed report
```

## Test Types (To Implement)

**Unit Tests:**
- Individual functions: `slugify()`, `allowed_file()`, `to_dict()` methods
- SQLAlchemy model behavior
- File size validation
- Each test should be independent and fast (<100ms)
- Location: `tests/test_helpers.py`, `tests/test_models.py`

**Integration Tests:**
- Route + database interactions: POST create product → verify in DB
- Form validation → database state changes
- Admin authentication → protected route access
- Location: `tests/test_routes.py`, `tests/test_auth.py`

**E2E Tests:**
- Currently: Not automated, manual browser testing only
- Would require Selenium or Playwright if added
- Should test: user workflows (browse products, admin login, form submission)
- Current recommendation: Focus on unit + integration first

## Async Testing (If Implemented)

**JavaScript/Frontend Testing:**
Current `app.js` (184 lines) would need framework like Jest:

```javascript
// tests/app.test.js
describe('Product Modal', () => {
  beforeEach(() => {
    document.body.innerHTML = `
      <div id="productModal"></div>
      <div class="product-card" data-slug="test-product"></div>
    `;
  });

  test('openProductModal should fetch product data', async () => {
    global.fetch = jest.fn(() =>
      Promise.resolve({
        json: () => Promise.resolve({ name: 'Test', slug: 'test-product' })
      })
    );

    // Call openProductModal
    // Assert fetch was called with correct slug
  });
});
```

## Error Testing Patterns

**Current error handling approaches (to test):**

1. **404 Handling** (app.py:221-223):
```python
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Test pattern:
def test_invalid_product_slug_returns_404(test_client):
    response = test_client.get('/producto/nonexistent-slug')
    assert response.status_code == 404
```

2. **Form Validation Errors** (app.py:335-337):
```python
if not name or not category_id:
    flash('Nombre y categoría son obligatorios', 'error')

# Test pattern:
def test_product_form_requires_name_and_category(test_client):
    response = test_client.post('/admin/producto/nuevo', data={
        'name': '',
        'category_id': ''
    }, follow_redirects=False)
    # Assert flash message appears
```

3. **Flash Messages** (test for success/error feedback):
```python
def test_category_delete_shows_success_message(test_client):
    category = create_test_category()
    response = test_client.post(
        f'/admin/categoria/{category.id}/eliminar',
        follow_redirects=True
    )
    assert b'Categoría eliminada' in response.data
```

## Testing Checklist (Features to Add Tests For)

**High Priority (Core Functionality):**
- [ ] GET / returns 200 with featured products
- [ ] GET /productos returns all active products
- [ ] GET /producto/<slug> returns 404 if inactive/missing
- [ ] POST /admin/login with correct credentials sets session
- [ ] POST /admin/login with wrong password shows error
- [ ] POST /admin/producto/nuevo creates product in database
- [ ] POST /admin/categoria/<id>/eliminar fails if products exist

**Medium Priority (Data Integrity):**
- [ ] Product.to_dict() includes all required fields
- [ ] Category.to_dict() returns correct structure
- [ ] SiteSetting.get() returns default if key missing
- [ ] slugify() removes accents and special characters
- [ ] allowed_file() rejects non-image extensions

**Lower Priority (Edge Cases):**
- [ ] POST /producto with missing file doesn't crash
- [ ] XSS protection headers are set
- [ ] HSTS header only in production
- [ ] Robots.txt correctly disallows admin paths
- [ ] Sitemap.xml includes all active products

## Current Testing Limitations

**Gaps:**
1. No automated regression testing
2. No CI/CD pipeline (GitHub Actions, etc.)
3. No pre-commit hooks to run tests
4. Database migrations not tested
5. Admin form file upload logic not verified
6. SEO sitemap generation not validated
7. Session/authentication edge cases not covered

**Risk Areas (High Impact if Broken):**
- Admin authentication decorator (`login_required`)
- Database model relationships and cascades
- File upload and validation logic
- SEO route generation (robots.txt, sitemap.xml)
- Product/category slug uniqueness

---

*Testing analysis: 2026-04-04*
