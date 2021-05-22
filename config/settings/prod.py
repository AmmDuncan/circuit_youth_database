from _base import *

DEBUG = False

ALLOWED_HOSTS = ["circuityouth.herokuapp.com"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get("DB_HOST", 'localhost'),
        'PORT': os.environ.get("DB_PORT", '5432'),
        'NAME': os.environ.get("DB_NAME", 'circuit_youth'),
        'USER': os.environ.get("DB_USER", 'postgres'),
        'PASSWORD': os.environ.get("DB_PASSWORD"),
    }
}