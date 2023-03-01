# Common Settings to all environments

from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3z&-v^f1+30_ms1oup&5m!!em81vc$kjd%m7z=^j%2xuxu=mv0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "localhost"
]

# Cache Configuration
CACHES = {
     'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache'
     }
}

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'default.db.sqlite3'),
    },
    'project_admin_db': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'project.admin.db.sqlite3'),
    },
    'auth_users_db': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'auth.users.db.sqlite3'),
    },
    'users_pets_api': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'users.pets.api.db.sqlite3'),
    }
}
