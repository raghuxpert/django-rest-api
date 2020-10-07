from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'md1w9!&hu2*9p!7)e1)0&-7%n!kaabxcla97+38e@-t&f+(dik'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

# Application definition

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'raghav',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST' : '13.58.179.76',
        'PORT': '5432'
    }
}

