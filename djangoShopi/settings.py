"""
Django settings for djangoShopi project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from decouple import config
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default="django-insecure-@&_a6mdrkjm8h!dt8rcrp6z(gvqupl$v&d$xmi)0aqjek8@mo_")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =  config("DEBUG", default=False, cast=bool)    # use True in development

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.accounts',
    'apps.general',
    # allauth authentications
    'allauth',
    'allauth.account',
    # Optional -- requires install using `django-allauth[socialaccount]`.
    'allauth.socialaccount',
    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.github',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Add the account middleware:
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'djangoShopi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'djangoShopi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

ALTERNATIVE_DBS = {
    "postgres": {
        "ENGINE": config("ENGINE",default="django.db.backends.postgresql"),
        "NAME": config("DB_NAME", default="postgres"),
        "USER": config("DB_USER", default="postgres"),
        "PASSWORD": config("DB_PASSWORD", default="postgres"),
        "HOST": config("DB_HOST", default="127.0.0.1"),
        "PORT": config("DB_PORT", default=5432),
    },
    
    'sqlite3': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DATABASES = {
    "default": ALTERNATIVE_DBS[config("USE_DB", default="sqlite3")],
}
    


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = config("LANGUAGE_CODE",default="en-us")

TIME_ZONE = config("TIME_ZONE",default="UTC")

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configure AUTHENTICATION_BACKENDS
AUTHENTICATION_BACKENDS = [
    
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
    
]


# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': config("GOOGLE_CLIENT_ID",default="123"),
            'secret': config("GOOGLE_SECRET",default="456"),
            'key': ''
        }
    },
    'github': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': config("GITHUB_CLIENT_ID",default="123"),
            'secret': config("GITHUB_SECRET",default="456"),
            'key': ''
        }
    }
}


# Configure email backend 
EMAIL_BACKEND = config("EMAIL_BACKEND",default="django.core.mail.backends.console.EmailBackend")
EMAIL_HOST = config("EMAIL_HOST",default="")
EMAIL_USE_TLS = config("EMAIL_USE_TLS", default=True, cast=bool)
EMAIL_PORT = config("EMAIL_USER",default=587)
EMAIL_HOST_USER =  config("EMAIL_USER",default="")
EMAIL_HOST_PASSWORD =  config("EMAIL_PASSWORD",default="")


# Redirect user by login
LOGIN_REDIRECT_URL='/'
# Redirect user by logout
ACCOUNT_LOGOUT_REDIRECT_URL='/'

ACCOUNT_AUTHENTICATION_METHOD= "email"
ACCOUNT_EMAIL_REQUIRED=True


ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS=1
ACCOUNT_EMAIL_REQUIRED=True
ACCOUNT_EMAIL_VERIFICATION="mandatory"
ACCOUNT_MAX_EMAIL_ADDRESSES=1
ACCOUNT_LOGOUT_ON_GET = True

# Static media file config
STATIC_URL = 'static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATICFILES_DIRS = [
    BASE_DIR / "static",
]