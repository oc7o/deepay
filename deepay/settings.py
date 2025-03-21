"""
Django settings for deepay project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from datetime import timedelta
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
##SECRET_KEY = "django-insecure-y*-ai=-q43dt1=t-w5)1qx@)+@l)3kk!$_sq*n&vf8&bz6cqt)"
SECRET_KEY = os.environ.get("SECRET_KEY", "DEFAULT_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("ENV", "dev") == "dev"

ALLOWED_HOSTS = []
ALLOWED_HOSTS_ENV = os.environ.get("ALLOWED_HOSTS", "localhost")
ALLOWED_HOSTS.extend(ALLOWED_HOSTS_ENV.split(","))

INTERNAL_IPS = []

if DEBUG:
    INTERNAL_IPS.append("127.0.0.1")

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

CSRF_TRUSTED_ORIGINS = []
CSRF_TRUSTED_ORIGINS_ENV = os.environ.get(
    "CSRF_TRUSTED_ORIGINS", "https://localhost:8000"
)
CSRF_TRUSTED_ORIGINS.extend(CSRF_TRUSTED_ORIGINS_ENV.split(","))


# Application definition

INSTALLED_APPS = [
    # core apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # third party apps
    "strawberry_django",
    "corsheaders",
    "strawberry_django_jwt.refresh_token",
    "django_filters",
    "mptt",
    "storages",
    # local apps
    "deepay.apps.users",
    "deepay.apps.forum",
    "deepay.apps.inventory",
    "deepay.apps.payments",
    "deepay.apps.basket",
    "deepay.apps.vendor",
    "deepay.apps.escrow",
    "deepay.apps.demo",
    "deepay.apps.captcha",
    "deepay.apps.landing",
]

if DEBUG:
    # dev apps
    INSTALLED_APPS += ("django_browser_reload",)
    INSTALLED_APPS += ("debug_toolbar",)


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # CORS Headers
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

if DEBUG:
    MIDDLEWARE += ("django_browser_reload.middleware.BrowserReloadMiddleware",)
    MIDDLEWARE += ("debug_toolbar.middleware.DebugToolbarMiddleware",)


ROOT_URLCONF = "deepay.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "deepay.apps.basket.context_processors.basket_context",
            ],
        },
    },
]

WSGI_APPLICATION = "deepay.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASE_TYPE = os.environ.get("DATABASE_TYPE", "sqlite3")

if DATABASE_TYPE == "sqlite3":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

elif DATABASE_TYPE == "postgres":
    if os.environ.get("DATABASE_URL", None) is None:
        DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.postgresql_psycopg2",
                "NAME": os.environ.get("POSTGRES_DB"),
                "USER": os.environ.get("POSTGRES_USER", "postgres"),
                "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
                "HOST": os.environ.get("POSTGRES_HOST"),
                "PORT": os.environ.get("POSTGRES_PORT", "5432"),
            }
        }

    else:
        import dj_database_url

        DATABASES = {"default": dj_database_url.config()}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STORAGE = os.environ.get("STORAGE", "local")

if STORAGE == "local":
    #####################
    ### LOCAL STORAGE ###
    #####################

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/4.0/howto/static-files/

    STATIC_ROOT = BASE_DIR / "tmp" / "static"
    STATIC_URL = "/media/static/"
    STATICFILES_DIRS = [BASE_DIR / "static"]
    STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

    # Media files (images, videos, etc.)

    MEDIA_ROOT = BASE_DIR / "tmp" / "media"
    MEDIA_URL = "/media/"

if STORAGE == "s3":
    ##############
    ### AWS S3 ###
    ##############

    AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
    AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
    AWS_STORAGE_BUCKET_NAME = os.environ["AWS_STORAGE_BUCKET_NAME"]
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
    AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}

    AWS_DEFAULT_ACL = "public-read"
    AWS_LOCATION = "static"

    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/"

    DEFAULT_FILE_STORAGE = "deepay.s3utils.MediaRootS3BotoStorage"
    STATICFILES_STORAGE = "deepay.s3utils.StaticRootS3BotoStorage"


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


### CORS

CORS_ALLOW_ALL_ORIGINS = True

### GRAPHQL CONFIGURATION ###

AUTH_USER_MODEL = "users.ExtendUser"


GRAPHQL_JWT = {
    # ...
    "JWT_VERIFY_EXPIRATION": True,
    "JWT_LONG_RUNNING_REFRESH_TOKEN": True,
    "JWT_EXPIRATION_DELTA": timedelta(minutes=5),
    "JWT_REFRESH_EXPIRATION_DELTA": timedelta(days=7),
}

AUTHENTICATION_BACKENDS = [
    "strawberry_django_jwt.backends.JSONWebTokenBackend",
    "django.contrib.auth.backends.ModelBackend",
]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


#####################

LOGIN_REDIRECT_URL = "users:settings"
LOGOUT_REDIRECT_URL = "landing:landing"

DEFAULT_PLACEHOLDER_IMAGE = {"url": STATIC_URL + "defaults/placeholder.png"}

#####################
### BTCPAY SERVER ###
#####################

BTCPAY_TOKEN = os.environ.get("BTCPAY_TOKEN", "")
BTCPAY_SERVER_URL = os.environ.get("BTCPAY_SERVER_URL", "")
BTCPAY_STORE_ID = os.environ.get("BTCPAY_STORE_ID", "")
BTCPAY_CURRENCY = "EUR"
