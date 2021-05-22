from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'csub==khl6pq27zbh6fuoein3l$u#pnb=&@(-@y@xar43hq$ox'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'localhost',
        'PORT': '5432',
        'NAME': 'circuit_youth_dev',
        'USER': 'postgres',
        'PASSWORD': "Kofori123",
    }
}