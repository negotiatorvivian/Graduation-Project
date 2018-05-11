#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Django settings for blackFriday project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

try:
    import configparser
except:
    from six.moves import configparser
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm(8u7fau#g8z&hkey85s_*2n@x!37ju5vm!=!vg@7sewy7k_f&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# TEMPLATE_DEBUG = True

ALLOWED_HOSTS = '*'


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shopping',
    'recommendation'
)

MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'blackFriday.urls'

WSGI_APPLICATION = 'blackFriday.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shopping_route',
        'USER': 'root',
        'PASSWORD': 'zhangziwei',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
           'charset': 'utf8mb4'
        }
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
MEDIA_ROOT = '/data/'

import os
LOG_PATH = '/data/logs/shopping'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        }
    },
    'handlers': {
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'simple',
            'filename': os.path.join(LOG_PATH, "error.log"),
            'when': 'midnight',
            'interval': 1,
            'backupCount': 0
        },
        'info': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'simple',
            'filename': os.path.join(LOG_PATH, "info.log"),
            'when': 'midnight',
            'interval': 1,
            'backupCount': 0
        }
    },
    'loggers': {
        'error': {
            'handlers': ['error'],
            'level': 'ERROR',
            'propagate': False
        },
        'info': {
            'handlers': ['info'],
            'level': 'INFO',
            'propagate': False
        }
    }
}



