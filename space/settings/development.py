# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

import os

from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'space',
        'USER': 'alex',
    },
}

STATIC_URL = '/assets/'

STATIC_ROOT = 'assets'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


MEDIA_URL = '/media/'
MEDIA_ROOT = 'media/'


TEMPLATE_DIRS = (BASE_DIR + 'templates',)

INSTALLED_APPS += (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.staticfiles',
    'django.contrib.sessions'
)
