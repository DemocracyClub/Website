import contextlib
import os
import sys
from os.path import abspath, dirname, join

import dc_design_system

# PATH vars


def here(*x):
    return join(abspath(dirname(__file__)), *x)


PROJECT_ROOT = here("..")


def root(*x):
    return join(abspath(PROJECT_ROOT), *x)


sys.path.insert(0, root("apps"))


DEBUG = True
THUMBNAIL_DEBUG = DEBUG

ADMINS = ()

MANAGERS = ADMINS

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "democracy_club",
        "USER": "postgres",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "",
    }
}


ALLOWED_HOSTS = []

TIME_ZONE = "Europe/London"

LANGUAGE_CODE = "en-gb"

SITE_ID = 1

USE_I18N = False

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = root("assets", "uploads")
MEDIA_URL = "/media/"

STATIC_ROOT = root("static_files")
STATIC_URL = "/static/"
STATICFILES_DIRS = (root("assets"),)

SECRET_KEY = "CHANGE THIS!!!"


MIDDLEWARE = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)


ROOT_URLCONF = "democracy_club.urls"

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = "democracy_club.wsgi.application"

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
    "dc_design_system",
    "pipeline",
    "sorl.thumbnail",
)

PROJECT_APPS = (
    "core.apps.CoreConfig",
    "hermes",
    "typogrify",
    "reports",
    "wheredoivote_user_feedback",
    "projects",
    "dc_utils",
)

INSTALLED_APPS += PROJECT_APPS

from dc_utils.settings.pipeline import *  # noqa
from dc_utils.settings.pipeline import get_pipeline_settings  # noqa
from dc_utils.settings.whitenoise import whitenoise_add_middleware  # noqa

MIDDLEWARE = whitenoise_add_middleware(MIDDLEWARE)

PIPELINE = get_pipeline_settings(
    extra_css=[
        "scss/styles.scss",
    ],
    extra_js=[
        "js/date.format.js",
    ],
    extra_include_paths=[
        dc_design_system.DC_SYSTEM_PATH + "/system",
    ],
)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        }
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [root("templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "django.contrib.auth.context_processors.auth",
                "dc_utils.context_processors.dc_django_utils",
            ],
            "debug": DEBUG,
        },
    },
]


TEST_RUNNER = "django.test.runner.DiscoverRunner"


# importing test settings file if necessary (TODO could be done better)
if len(sys.argv) > 1 and "test" in sys.argv[1]:
    from .testing import *  # noqa


REPORT_MARKDOWN_EXTENSIONS = ["toc", "meta", "md_in_html", "footnotes"]


def blog_markdown(value):
    import markdown

    config = {
        "extra": {
            "footnotes": {"UNIQUE_IDS": True},
        },
    }

    return markdown.markdown(
        value,
        extensions=["mdx_headdown", "extra", "footnotes", "smarty", "nl2br"],
        extension_configs=config,
    )


MARKUP_RENDERER = blog_markdown

SITE_TITLE = "Democracy Club"
CANONICAL_URL = f"https://{os.environ.get('FQDN')}"


def setup_sentry(environment=None):
    SENTRY_DSN = os.environ.get("SENTRY_DSN")
    if not SENTRY_DSN:
        return

    if not environment:
        environment = os.environ.get("DC_ENVIRONMENT", "staging")
    release = os.environ.get("GIT_HASH", "unknown")
    import sentry_sdk
    from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[AwsLambdaIntegration(), DjangoIntegration()],
        traces_sample_rate=0,
        environment=environment,
        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True,
        release=release,
    )


# .local.py overrides all the common settings.
with contextlib.suppress(ImportError):
    from .local import *  # noqa
