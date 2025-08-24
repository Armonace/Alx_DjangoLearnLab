from .settings import *               # start from your base dev settings
import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# ---- Core hardening ----
DEBUG = False
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]   # set in env on server
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "").split(",")  # e.g. "api.example.com,localhost"

CSRF_TRUSTED_ORIGINS = [u for u in os.environ.get("DJANGO_CSRF_TRUSTED", "").split(",") if u]

# ---- Database (Postgres recommended) ----
# Example DATABASE_URL: postgres://USER:PASSWORD@HOST:5432/DBNAME
DATABASES = {
    "default": dj_database_url.config(
        env="DATABASE_URL",
        conn_max_age=600,
        ssl_require=bool(int(os.environ.get("DB_SSL_REQUIRE", "1")))
    )
}

# ---- Static & Media ----
# Option A: Whitenoise (simple single-server static)
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# Whitenoise
INSTALLED_APPS = ["whitenoise.runserver_nostatic"] + INSTALLED_APPS
MIDDLEWARE = ["whitenoise.middleware.WhiteNoiseMiddleware"] + MIDDLEWARE
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Media
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Option B (S3) – comment Whitenoise bits and use:
# INSTALLED_APPS += ["storages"]
# DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
# AWS_STORAGE_BUCKET_NAME = os.environ["AWS_STORAGE_BUCKET_NAME"]
# AWS_S3_REGION_NAME = os.environ.get("AWS_S3_REGION_NAME", "eu-west-1")
# AWS_S3_SIGNATURE_VERSION = "s3v4"
# AWS_S3_FILE_OVERWRITE = False
# AWS_DEFAULT_ACL = None

# ---- Security headers ----
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = bool(int(os.environ.get("SECURE_SSL_REDIRECT", "1")))
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = int(os.environ.get("SECURE_HSTS_SECONDS", "31536000"))  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# ---- REST Framework production defaults ----
REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = ["rest_framework.renderers.JSONRenderer"]

# ---- Logging ----
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json": {
            "format": '{"time":"%(asctime)s","level":"%(levelname)s","name":"%(name)s","message":"%(message)s"}'
        }
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "json"},
    },
    "root": {"handlers": ["console"], "level": "INFO"},
}
