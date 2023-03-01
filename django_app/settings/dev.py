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

# Note:
#   This is an example of how multiple applications could go to multiple databases. Since this is a simple example
#   when the default django user's entity / model / table is used also as a foreign key for part of the exercise all
#   the routers go to the same database (users_pets_api) and we don't get any benefit from separating data in multiple
#   routers since we would lose the availability of foreign keys reference to the user model risking the integrity of
#   data of the pet owners entity information. I just leave it here as an example of how we can use routers to separate
#   data from multiple applications

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db', 'default.db.sqlite3'),
    },
    'project_admin_auth_users_db': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db', 'project.admin.db.sqlite3'),
    },
    'users_pets_api': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db', 'users.pets.api.db.sqlite3'),
    }
}
