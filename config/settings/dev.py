from _base import *

ALLOWED_HOSTS = []

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