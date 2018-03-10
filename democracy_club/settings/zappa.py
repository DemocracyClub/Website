import os

from .base import *  # noqa

if os.environ.get('SERVERTYPE', None) == 'AWS Lambda':
    GEOS_LIBRARY_PATH = '/var/task/libgeos_c.so'
FORCE_SCRIPT_NAME = '/'

ALLOWED_HOSTS = ['8yx8ogttjk.execute-api.eu-west-1.amazonaws.com']

# Override the database name and user if needed
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.environ.get('DATABASE_HOST'),
        'USER': os.environ.get('DATABASE_USER'),
        'PORT': '5432',
        'NAME': os.environ.get('DATABASE_NAME'),
        'PASSWORD': os.environ.get('DATABASE_PASS')
    }
}

TMP_ASSETS_ROOT = "/tmp/assets_root/"
STATIC_ROOT = '/tmp/static_root/'

# Make the tmp static dirs whenever django is started
os.makedirs(TMP_ASSETS_ROOT, exist_ok=True)
os.makedirs(STATIC_ROOT, exist_ok=True)

STATICFILES_FINDERS = (
    'core.s3_lambda_storage.ReadOnlySourceFileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.CachedFileFinder',
    'pipeline.finders.PipelineFinder',
)

# Used by ReadOnlySourceFileSystemFinder
READ_ONLY_PATHS = (
    (root('assets'), TMP_ASSETS_ROOT),  # noqa
)

PIPELINE['COMPILERS'] = ('core.s3_lambda_storage.LambdaSASSCompiler', )   # noqa

AWS_STORAGE_BUCKET_NAME = "static.dev.democracyclub.org.uk"
AWS_S3_SECURE_URLS = True
AWS_S3_HOST = 's3-eu-west-1.amazonaws.com'
AWS_S3_CUSTOM_DOMAIN = "static-dev.democracyclub.org.uk"
AWS_S3_USE_SSL = False

STATICFILES_LOCATION = 'static'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
STATICFILES_STORAGE = 'core.s3_lambda_storage.StaticStorage'

MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://{}/{}/".format(AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'core.s3_lambda_storage.MediaStorage'

CSRF_TRUSTED_ORIGINS = ['stage.democracyclub.org.uk']

DEBUG = False
GOCARDLESS_ACCESS_TOKEN = os.environ.get('GOCARDLESS_ACCESS_TOKEN')

BACKLOG_TRELLO_KEY = os.environ.get('BACKLOG_TRELLO_KEY')
BACKLOG_TRELLO_TOKEN = os.environ.get('BACKLOG_TRELLO_TOKEN')
