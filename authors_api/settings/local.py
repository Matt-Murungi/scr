from .base import *  # noqa
from .base import env


SECRET_KEY = env("DJANGO_SECRET_KEY", default='h1RQCLo8nHNGDimrkjUqDqi4-ArTOHjeGAsLTBrlOx6-s-erUFw')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
CSRF_TRUSTED_ORIGINS = ['http://localhost:8080']
