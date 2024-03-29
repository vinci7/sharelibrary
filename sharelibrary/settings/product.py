"""
Django settings for sharelibrary project.
Generated by 'django-admin startproject' using Django 3.0.3.
For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

from .base import *  # NOQA

import django_heroku

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Application definition

INSTALLED_APPS += [
]

MIDDLEWARE += [
]

#数据库设置
if os.getenv('DATABASE_URL') is not None:
    import dj_database_url
    DATABASES['default'] = dj_database_url.config()

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# Activate Django-Heroku.
django_heroku.settings(locals())