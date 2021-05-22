from ._base import *

DEBUG = False

ALLOWED_HOSTS = ["circuityouth.herokuapp.com"]

SECRET_KEY = os.environ.get('SECRET_KEY')

DATABASES = {
    'default': {
        'HOST': os.environ.get("DB_HOST", 'localhost'),
        'PORT': os.environ.get("DB_PORT", '5432'),
        'NAME': os.environ.get("DB_NAME", 'circuit_youth'),
        'USER': os.environ.get("DB_USER", 'postgres'),
        'PASSWORD': os.environ.get("DB_PASSWORD"),
    }
}