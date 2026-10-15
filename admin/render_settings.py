"""Configuration for a public portfolio demo with a disposable database."""
import os
from .settings import *

DEBUG = False
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
_hostname = os.environ.get("RENDER_EXTERNAL_HOSTNAME", "localhost")
ALLOWED_HOSTS = [_hostname, "localhost", "127.0.0.1", "testserver"]
CSRF_TRUSTED_ORIGINS = [f"https://{_hostname}"]
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "demo.sqlite3"}}
STORAGES = {
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {"BACKEND": "whitenoise.storage.CompressedStaticFilesStorage"},
}
