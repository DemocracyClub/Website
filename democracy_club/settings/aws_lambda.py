import os

from .base import setup_sentry
from .base import *  # noqa

FORCE_SCRIPT_NAME = "/"

ALLOWED_HOSTS = ["*"]

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
AWS_S3_HOST = "s3-eu-west-1.amazonaws.com"
AWS_S3_USE_SSL = False
AWS_S3_REGION_NAME = "eu-west-2"

# Stage
AWS_STORAGE_BUCKET_NAME = "static.dev.democracyclub.org.uk"
AWS_S3_CUSTOM_DOMAIN = "static-dev.democracyclub.org.uk"

# # Prod
# AWS_STORAGE_BUCKET_NAME = "static.democracyclub.org.uk"
# AWS_S3_CUSTOM_DOMAIN = "static.democracyclub.org.uk"

MEDIAFILES_LOCATION = "media"
MEDIA_URL = "https://{}/{}/".format(AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = "core.s3_lambda_storage.MediaStorage"

CSRF_TRUSTED_ORIGINS = [
    "stage.democracyclub.org.uk",
    "democracyclub.org.uk",
]

DEBUG = False

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")

setup_sentry()


# if ZAPPA_STAGE == "prod":
#     AWS_CLOUD_FRONT_ID = "E3E7Y3O7VH1EMS"
# else:
#     AWS_CLOUD_FRONT_ID = "E19EM1B0PXPYCH"
