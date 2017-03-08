from .base import *  # noqa

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'dc_website_test',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}



BACKLOG_TRELLO_BOARD_ID = "empty"
BACKLOG_TRELLO_DEFAULT_LIST_ID = "empty"
BACKLOG_TRELLO_KEY = "empty"
BACKLOG_TRELLO_TOKEN = "empty"
