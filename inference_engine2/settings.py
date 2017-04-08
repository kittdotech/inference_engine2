"""
Django settings for inference_engine2 project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q1%u(oc%%d^4k3sh&tzn8(jp7m1!=+c(54u58_#y!#xax3z%q5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

"""CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}"""


# Application definition
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
#SESSION_FILE_PATH = BASE_DIR

BOOTSTRAP3_FOLDER = os.path.abspath(os.path.join(BASE_DIR, '..', 'bootstrap3'))

if BOOTSTRAP3_FOLDER not in sys.path:
    sys.path.insert(0, BOOTSTRAP3_FOLDER)
# DAB_FIELD_RENDERER = 'django_admin_bootstrapped.renderers.BootstrapFieldRenderer'


INSTALLED_APPS = (
    # 'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'inference2',
    'bootstrap3',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django_tools.middlewares.ThreadLocal.ThreadLocalMiddleware',
)

ROOT_URLCONF = 'inference_engine2.urls'

TEMPLATES = (
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG,
        },
    },
)

WSGI_APPLICATION = 'inference_engine2.wsgi.application'
SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_AGE = 5 * 60
# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
CONFIG_TYPE = 0  # os.getenv('CLEARDB_DATABASE_URL','')
if CONFIG_TYPE:
    DICT = {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heroku_e080b104b4741bc',
        'HOST': 'us-cdbr-iron-east-03.cleardb.net',
        'USER': 'bddaf22a8f080b',
        'PASSWORD': 'c4c504bd',

    }

if not CONFIG_TYPE:
    DEVELOP = os.getenv('DEVELOP', '')
    DB_PASSWORD = 'deductive'
    if DEVELOP:
        DB_PASSWORD = 'root'
    DICT = {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'inference_engine',
        'HOST': '34.208.135.45',
        'USER': 'root',
        'PASSWORD': 'password',

    }

DATABASES = {
    'default': DICT
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
# change file name here
MANUAL_FILE = "IE_Manual.docx"
MANUAL_PATH = os.path.join(BASE_DIR, MANUAL_FILE)

DICT_DIRS = os.path.join(BASE_DIR, "dicts")

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = ( os.path.join(BASE_DIR,'static/'),  )


# Settings for django-bootstrap3
BOOTSTRAP3 = {
    'set_required': False,  # For Django <= 1.8 only
    'error_css_class': 'bootstrap3-error',
    'required_css_class': 'bootstrap3-required',
    'javascript_in_head': True,
}

from django.contrib import messages

MESSAGE_TAGS = {
            messages.SUCCESS: 'alert-success success',
            messages.WARNING: 'alert-warning warning',
            messages.ERROR: 'alert-danger error'
}