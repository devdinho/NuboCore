import os

from dotenv import load_dotenv

from armoreddjango.settings.base import *

SITE_ID = 1

load_dotenv(override=True)

DEBUG = os.getenv("DEBUG")

POSTGRES_DB = "armoreddjango_db"
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_HOST = "armoreddjango_db"
DB_PORT = os.getenv("DB_PORT", 5432)

SECRET_KEY = os.getenv("SECRET_KEY")

ALLOWED_HOSTS = [
    "0.0.0.0",
    "localhost",
    # "insert your domai, armoreddjango.dinho.dev"
]

CSRF_TRUSTED_ORIGINS = ["http://localhost:8003", "http://0.0.0.0:8003", "https://armoreddjango.dinho.dev"]

CORS_ALLOWED_ORIGINS = CSRF_TRUSTED_ORIGINS

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": POSTGRES_DB,
        "USER": POSTGRES_USER,
        "PASSWORD": POSTGRES_PASSWORD,
        "HOST": DB_HOST,
        "PORT": DB_PORT,
    }
}
