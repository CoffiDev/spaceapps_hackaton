# -*- encoding: utf-8 -*-

from __future__ import unicode_literals, absolute_import

import os, locale

locale.setlocale(locale.LC_ALL, '')

PROJECT_NAME = 'space'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fie@x-&$&r78adt9b+q0i5mumhl11)s&4*z&!+bzr#z@$2qynl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    # Django apps
    'django.contrib.contenttypes',
    'django.contrib.humanize',

    # Project apps

    # Third party apps
    'django_extensions',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware'
)

ROOT_URLCONF = '%s.urls' % PROJECT_NAME

WSGI_APPLICATION = '%s.wsgi.application' % PROJECT_NAME


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'es-MX'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Translations
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# Fixtures
FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'fixtures'),
)

DATE_FORMAT = '%d-%b-%Y'

DATETIME_FORMAT = '%d-%b-%Y %H:%M'

DATE_INPUT_FORMATS = ['%d-%b-%Y']

DATETIME_INPUT_FORMATS = [
    '%d-%b-%Y', '%d-%b-%Y %H:%M:%S', '%d-%b-%Y  %H:%M'
]

