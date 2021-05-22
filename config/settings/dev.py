import os

from _base import *

ALLOWED_HOSTS = []

SECRET_KEY = os.environ.get('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'localhost',
        'PORT': '5432',
        'NAME': 'circuit_youth',
        'USER': 'postgres',
        'PASSWORD': os.environ.get("DB_PASSWORD"),
    }
}