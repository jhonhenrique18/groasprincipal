import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'graos-sa-secret-key-change-in-production')
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
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'graos2026')
