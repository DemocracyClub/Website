import os

from .base import setup_sentry
from .base import *  # noqa

if os.environ.get("APP_IS_BEHIND_CLOUDFRONT", False):
    FORCE_SCRIPT_NAME = "/"

ALLOWED_HOSTS = [os.environ.get("FQDN")]

# Override the database name and user if needed
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "HOST": os.environ.get("DATABASE_HOST"),
        "USER": "postgres",
        "PORT": "5432",
        "NAME": os.environ.get("POSTGRES_DATABASE_NAME"),
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
AWS_S3_HOST = "s3-eu-west-2.amazonaws.com"
AWS_S3_USE_SSL = False
AWS_S3_REGION_NAME = "eu-west-2"

AWS_STORAGE_BUCKET_NAME = os.environ.get("STORAGE_BUCKET_NAME")
AWS_S3_CUSTOM_DOMAIN = AWS_STORAGE_BUCKET_NAME

MEDIAFILES_LOCATION = "media"
MEDIA_URL = "https://{}/{}/".format(AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = "core.s3_lambda_storage.MediaStorage"

CSRF_TRUSTED_ORIGINS = [os.environ.get("FQDN")]

DEBUG = False

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")

setup_sentry()
