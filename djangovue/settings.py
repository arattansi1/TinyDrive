"""
Django settings for djangovue project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import django_heroku


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3r!dxw%38#g9tyu73p2sd7@!#pv)w+%7(tz9k@%c_hx26k=rwc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['tinydrive.herokuapp.com', 'localhost']


# Application definition

INSTALLED_APPS = [
    #'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'social_django',
    'backend.apps.BackendConfig',
    'widget_tweaks',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

ROOT_URLCONF = 'djangovue.urls'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'duhlkeofl',
    'API_KEY': '647672672161276',
    'API_SECRET': 'Zy3BToEJdDrBvA-CxqNoTHiWK88'
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.RawMediaCloudinaryStorage'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangovue.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tinydrive',
        'USER': 'project',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'
MEDIA_URL = '/file/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)


# Auth0

SOCIAL_AUTH_TRAILING_SLASH = False  # Remove trailing slash from routes
SOCIAL_AUTH_AUTH0_DOMAIN = 'project-tinydrive.auth0.com'
SOCIAL_AUTH_AUTH0_KEY = 'LQAUg4yj15s69aZ5yIwIxNi21CFNIB9k'
SOCIAL_AUTH_AUTH0_SECRET = 'AMHAhu6eXqDimXsCyH3HC2H9lpi-8j_SfDy-26S8x2tu_BXQGh_joCDqEBgyuW1M'
SOCIAL_AUTH_AUTH0_SCOPE = [
    'openid',
    'profile',
]

AUTHENTICATION_BACKENDS = {
    'backend.login.Auth0',
    'django.contrib.auth.backends.ModelBackend',
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

LOGIN_URL = '/login/auth0'
LOGIN_REDIRECT_URL = '/upload'
LOGOUT_REDIRECT_URL = '/'

django_heroku.settings(locals())
