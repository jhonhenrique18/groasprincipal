import os
import secrets

class Config:
    # SECRET_KEY must be set via env in every environment. Empty or missing
    # value in production is refused at app import time (see app.py below).
    # In local dev (SQLite fallback, no DATABASE_URL) we auto-generate a
    # random key per-process so the developer doesn't need to set it manually.
    _secret = os.environ.get('SECRET_KEY', '')
    if not _secret and not os.environ.get('DATABASE_URL'):
        _secret = secrets.token_hex(32)
    SECRET_KEY = _secret
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///graos.db')
    # Railway uses postgres:// but SQLAlchemy needs postgresql://
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith('postgres://'):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace('postgres://', 'postgresql://', 1)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Upload folder: use RAILWAY_VOLUME_MOUNT_PATH if available (persistent storage),
    # otherwise fall back to local static/uploads
    _volume = os.environ.get('RAILWAY_VOLUME_MOUNT_PATH', '')
    if _volume:
        UPLOAD_FOLDER = os.path.join(_volume, 'uploads')
    else:
        UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads')

    MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10MB max upload
    ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME', 'admin')
    # ADMIN_PASSWORD is read directly from os.environ by the bootstrap in
    # app.py::ensure_admin_password_hash. The app NEVER compares plaintext —
    # the env var is hashed to the DB on first boot and can be removed after.

    # Meta (Facebook) tracking — Pixel + Conversions API
    META_PIXEL_ID = os.environ.get('META_PIXEL_ID', '')
    META_CAPI_ACCESS_TOKEN = os.environ.get('META_CAPI_ACCESS_TOKEN', '')
    META_TEST_EVENT_CODE = os.environ.get('META_TEST_EVENT_CODE', '')
    META_DOMAIN_VERIFICATION = os.environ.get(
        'META_DOMAIN_VERIFICATION',
        'vxgeoxsdul1vqi8dkaws3db2fcplfp',
    )
