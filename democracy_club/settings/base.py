import sys
from os.path import join, abspath, dirname

# PATH vars

here = lambda *x: join(abspath(dirname(__file__)), *x)
PROJECT_ROOT = here("..")
root = lambda *x: join(abspath(PROJECT_ROOT), *x)

sys.path.insert(0, root('apps'))


DEBUG = True
THUMBNAIL_DEBUG = DEBUG

ADMINS = ()

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'democracy_club',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}


ALLOWED_HOSTS = []

TIME_ZONE = 'Europe/London'

LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

USE_I18N = False

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = root('assets', 'uploads')
MEDIA_URL = '/media/'

STATIC_ROOT = root('static_files')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    root('assets'),
)

SECRET_KEY = 'CHANGE THIS!!!'

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'donations.middleware.DonationFormMiddleware',
)

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    "dc_members.authentication.MemberTokenBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
]

ROOT_URLCONF = 'democracy_club.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'democracy_club.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'localflavor',
    'markdown_deux',
    'django_extensions',
    'rest_framework',
    'corsheaders',
    'dc_theme',
    'pipeline',
    'sorl.thumbnail',
    'dc_signup_form',
    'dc_signup_form.signup_server',
)

PROJECT_APPS = (
    'core.apps.CoreConfig',
    'dc_members',
    'hermes',
    'typogrify',
    'django_markdown',
    'research',
    'report_2016',
    'report_2017',
    'report_2018',
    'report_2019',
    'report_whos_missing',
    'wheredoivote_user_feedback',
    'backlog',
    'mailing_list',
    'projects',
)

ALLAUTH_APPS = (
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.tumblr',
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.facebook',
)

INSTALLED_APPS += PROJECT_APPS
INSTALLED_APPS += ALLAUTH_APPS

from dc_theme.settings import get_pipeline_settings
from dc_theme.settings import (STATICFILES_FINDERS, SASS_INCLUDE_PATHS)  # noqa


PIPELINE = get_pipeline_settings(
    extra_css=['css/styles.scss', ],
    extra_js=['js/date.format.js', ],
)
PIPELINE['STYLESHEETS']['styles']['extra_context']['media'] = "screen,projection,print"

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            root('templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                'django.template.context_processors.request',
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "django.contrib.auth.context_processors.auth",
                'dc_theme.context_processors.dc_theme_context',
                'dc_signup_form.context_processors.signup_form',
            ],
            'debug': DEBUG
        },
    },
]


AUTH_PROFILE_MODULE = 'dc_members.Member'
LOGIN_REDIRECT_URL = "/members/"
SOCIALACCOUNT_AUTO_SIGNUP = True
SOCIALACCOUNT_QUERY_EMAIL=True
ACCOUNT_USERNAME_REQUIRED = False
SOCIALACCOUNT_PROVIDERS = {
     'google': {'SCOPE': ['https://www.googleapis.com/auth/userinfo.profile'],
                'AUTH_PARAMS': {'access_type': 'online'}},
     'facebook': {
        'SCOPE': ['email',],
        # 'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'METHOD': 'oauth2',
     },
}
ACCOUNT_EMAIL_VERIFICATION = "optional"
ACCOUNT_EMAIL_REQUIRED = True
LOGIN_REDIRECT_URL = "/everyelection/"


# EMAILS

TEST_RUNNER = 'django.test.runner.DiscoverRunner'


# importing test settings file if necessary (TODO could be done better)
if len(sys.argv) > 1 and 'test' in sys.argv[1]:
    from .testing import *  # noqa


MARKDOWN_DEUX_STYLES = {
    "default": {
        "extras": {
            "code-friendly": True,
            "markdown-in-html": True,
            "footnotes": True,
            "header-ids": True,
            "smarty-pants": True,
            "toc": {},
        },
        "safe_mode": False,
    },
}

GO_CARDLESS_PAYMENT_NAME = "Democracy Club Donation"
GO_CARDLESS_PAYMENT_DESCRIPTION = "Helping Democracy Club "\
"increase the quality of information on elections & the democratic processes"
GOCARDLESS_REDIRECT_URL = "https://democracyclub.org.uk/donate/process/"

CORS_URLS_REGEX = r'^/research/answers/*|/members/api/members/*$'
CORS_ORIGIN_WHITELIST = (
        'localhost:8000',
        'localhost:4000',
        'yournextmp.com',
        'meetyournextmp.com',
        'electionmentions.com',
        'cv.democracyclub.org.uk',
        'pollingstations.democracyclub.org.uk',
        'democracyclub.org.uk',
    )


SITE_TITLE = "Democracy Club"

BACKLOG_TRELLO_BOARD_ID = "O00ATMzS"
BACKLOG_TRELLO_DEFAULT_LIST_ID = "58bd618abc9a825bd64b5d8f"



# .local.py overrides all the common settings.
import os
try:
    if os.environ.get('FRAMEWORK', None) == 'Zappa':
        from .zappa import *  # noqa
    else:
        from .local import *  # noqa
except ImportError:
    pass
