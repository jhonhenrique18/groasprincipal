# Technology Stack

**Analysis Date:** 2026-04-04

## Languages

**Primary:**
- Python 3.12.8 - Backend application, all server logic

**Secondary:**
- HTML/Jinja2 - Server-side templating
- CSS - Styling and animations
- JavaScript (vanilla) - Client-side interactivity, no build tools

## Runtime

**Environment:**
- Python 3.12.8
- Deployment on Railway platform

**Package Manager:**
- pip (Python package manager)
- Lockfile: `requirements.txt` (present)

## Frameworks

**Core:**
- Flask 3.1.0 - Web application framework, routing, request handling
- Flask-SQLAlchemy 3.1.1 - ORM and database abstraction layer

**Build/Dev:**
- Gunicorn 23.0.0 - WSGI HTTP server for production deployment
- Werkzeug (via Flask) - WSGI utilities, file upload handling

**Utilities:**
- Pillow 11.1.0 - Image processing (uploaded product images)

## Key Dependencies

**Critical:**
- `psycopg2-binary` 2.9.10 - PostgreSQL database driver for production connectivity

**Functional:**
- `flask` 3.1.0 - Core web framework
- `flask-sqlalchemy` 3.1.1 - ORM for database operations
- `gunicorn` 23.0.0 - Production HTTP server
- `Pillow` 11.1.0 - Image manipulation (upload support)

## Configuration

**Environment:**
- Configuration via environment variables defined in `config.py`
- Key env vars: `SECRET_KEY`, `DATABASE_URL`, `RAILWAY_VOLUME_MOUNT_PATH`, `ADMIN_USERNAME`, `ADMIN_PASSWORD`, `PORT`
- Default values provided in `config.py` for local development

**Build:**
- No build configuration required (vanilla JavaScript, no transpilation)
- `Procfile` specifies production startup command

## Platform Requirements

**Development:**
- Python 3.12.8
- pip for package management
- Virtual environment support (venv/virtualenv)
- Git for version control

**Production:**
- Railway platform (https://railway.app)
- PostgreSQL database with URL format: `postgresql://user:password@host:port/dbname`
- Persistent volume storage at `RAILWAY_VOLUME_MOUNT_PATH` for image uploads
- HTTP server accessible on configured PORT

## Database

**Production:**
- PostgreSQL via environment variable `DATABASE_URL`

**Development:**
- SQLite at `sqlite:///graos.db` (local file-based)
- Automatically created on app startup

## Frontend Stack

**No build tooling:** The frontend is completely unbundled:
- Vanilla JavaScript with no npm/Node.js dependencies
- CSS is plain, written in `static/css/` with CSS variables for theming
- HTML is server-rendered via Jinja2 templates
- No transpilation, minification, or module bundling

## Storage

**Image uploads:**
- Production: Railway persistent volume at path specified by `RAILWAY_VOLUME_MOUNT_PATH`
- Development: Local `static/uploads/` directory
- Max file size: 10MB (configured in `config.py`)
- Allowed formats: PNG, JPG, JPEG, WEBP, GIF

---

*Stack analysis: 2026-04-04*
