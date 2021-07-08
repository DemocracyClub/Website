import os

from .base import *  # noqa

ZAPPA_STAGE = os.environ["STAGE"]
assert ZAPPA_STAGE in ("dev", "prod")

FORCE_SCRIPT_NAME = "/"

ALLOWED_HOSTS = [
    "8yx8ogttjk.execute-api.eu-west-1.amazonaws.com",  # Dev
    "qwhhmkhcfk.execute-api.eu-west-1.amazonaws.com",  # Prod
]

# Override the database name and user if needed
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "HOST": os.environ.get("DATABASE_HOST"),
        "USER": os.environ.get("DATABASE_USER"),
        "PORT": "5432",
        "NAME": os.environ.get("DATABASE_NAME"),
        "PASSWORD": os.environ.get("DATABASE_PASS"),
    }
}

WHITENOISE_AUTOREFRESH = False
PIPELINE["PIPELINE_ENABLED"] = True  # noqa
PIPELINE["PIPELINE_COLLECTOR_ENABLED"] = False  # noqa

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

AWS_S3_SECURE_URLS = True
AWS_S3_HOST = "s3-eu-west-1.amazonaws.com"
AWS_S3_USE_SSL = False
AWS_S3_REGION_NAME = "eu-west-2"

if ZAPPA_STAGE == "dev":
    AWS_STORAGE_BUCKET_NAME = "static.dev.democracyclub.org.uk"
    AWS_S3_CUSTOM_DOMAIN = "static-dev.democracyclub.org.uk"
else:
    AWS_STORAGE_BUCKET_NAME = "static.democracyclub.org.uk"
    AWS_S3_CUSTOM_DOMAIN = "static.democracyclub.org.uk"

MEDIAFILES_LOCATION = "media"
MEDIA_URL = "https://{}/{}/".format(AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = "core.s3_lambda_storage.MediaStorage"

CSRF_TRUSTED_ORIGINS = [
    "stage.democracyclub.org.uk",
    "democracyclub.org.uk",
]

DEBUG = False
GOCARDLESS_ACCESS_TOKEN = os.environ.get("GOCARDLESS_ACCESS_TOKEN")

BACKLOG_TRELLO_KEY = os.environ.get("BACKLOG_TRELLO_KEY")
BACKLOG_TRELLO_TOKEN = os.environ.get("BACKLOG_TRELLO_TOKEN")


GOCARDLESS_APP_ID = os.environ.get("GOCARDLESS_APP_ID")
GOCARDLESS_APP_SECRET = os.environ.get("GOCARDLESS_APP_SECRET")
GOCARDLESS_ACCESS_TOKEN = os.environ.get("GOCARDLESS_ACCESS_TOKEN")
GOCARDLESS_MERCHANT_ID = os.environ.get("GOCARDLESS_MERCHANT_ID")

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")


import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn=os.environ.get("SENTRY_DSN"),
    integrations=[DjangoIntegration()],
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,
)


if ZAPPA_STAGE == "prod":
    AWS_CLOUD_FRONT_ID = "E3E7Y3O7VH1EMS"
else:
    AWS_CLOUD_FRONT_ID = "E19EM1B0PXPYCH"
