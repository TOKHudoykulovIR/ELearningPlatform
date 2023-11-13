import os
from .base import *

DEBUG = False

"""
When DEBUG is False and a view raises an exception, 
all information will be sent by email to the people listed in the ADMINS setting
"""
ADMINS = [
    ('Khudoykulov T', 'tokhirjonbek@gmail.com'),
]

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}

REDIS_URL = 'redis://cache:6379'
CACHES['default']['LOCATION'] = REDIS_URL
CHANNEL_LAYERS['default']['CONFIG']['hosts'] = [REDIS_URL]

# Security. Django will redirect HTTP requests to HTTPS; session and CSRF cookies will be sent only over HTTPS.
CSRF_COOKIE_SECURE = True  # use a secure cookie for cross-site request forgery (CSRF) protection.
SESSION_COOKIE_SECURE = True  # use a secure session cookie
SECURE_SSL_REDIRECT = True  # whether HTTP requests have to be redirected to HTTPS.
