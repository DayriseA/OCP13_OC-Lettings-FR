"""Django settings for oc_lettings_site project."""

import os
import logging
import sentry_sdk

from pathlib import Path
from dotenv import load_dotenv
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import LoggingIntegration

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env file
dotenv_path = BASE_DIR.joinpath(".env")
load_dotenv(dotenv_path)
sentry_dsn = os.getenv("OCL_SENTRY_DSN")

if sentry_dsn:
    sentry_sdk.init(
        dsn=sentry_dsn,
        integrations=[
            DjangoIntegration(),
            LoggingIntegration(
                level=logging.INFO,  # Capture info and above as breadcrumbs
                event_level=logging.ERROR,  # Send errors and above as events
            ),
        ],
        enable_tracing=True,
        send_default_pii=True,
    )


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "fp$9^593hsriajg$_%=5trot9g!1qa@ew(o-1#@=&4%=hp46(s"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "False") == "True"

if DEBUG:
    ALLOWED_HOSTS = []
else:
    # SECURITY WARNING: define your production hosts here
    # Since currently developping locally, we will use localhost for now
    ALLOWED_HOSTS = ["localhost", "127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    "oc_lettings_site.apps.OCLettingsSiteConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "lettings",
    "profiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "oc_lettings_site.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR.joinpath("templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "oc_lettings_site.wsgi.application"

# Database. (We use PostgreSQL and the environment variables are set in the .env file)
# https://docs.djangoproject.com/en/5.0/ref/databases/

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}

# Since Django 3.2 the default value for the AutoField is changed to BigAutoField
# Easy to migrate as there is currently no use of ManyToManyField
# https://docs.djangoproject.com/en/3.2/releases/3.2/#customizing-type-of-auto-created-primary-keys

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa
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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Ensure the 'logs' directory exists
LOGS_DIR = os.path.join(BASE_DIR, "logs")
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

# Logging configuration
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "{levelname}:{asctime}:{module}:{message}",
            "style": "{",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "verbose": {
            "format": "{levelname}:{asctime}:{pathname}:{funcName}({lineno}){message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG" if DEBUG else "WARNING",
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
        "django_console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
        "file_debug": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": os.path.join(LOGS_DIR, "debug.log"),
            "formatter": "verbose",
        },
        "file_info": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": os.path.join(LOGS_DIR, "logs.log"),
            "formatter": "verbose",
        },
        "file_django": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": os.path.join(LOGS_DIR, "django.log"),
            "formatter": "verbose",
        },
    },
    "root": {
        "handlers": ["console", "file_debug" if DEBUG else "file_info"],
        "level": "DEBUG" if DEBUG else "INFO",
    },
    "loggers": {
        "django": {
            "handlers": ["file_django", "django_console"],
            # Change this if you really want to see all the django default DEBUG:
            "level": "INFO" if DEBUG else "WARNING",
            "propagate": False,
        },
    },
}
