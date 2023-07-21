from django.conf import settings
from django.utils.feedgenerator import Atom1Feed

from . import renderers

SYNDICATION_FEED_TITLE = getattr(
    settings, "SYNDICATION_FEED_TITLE", "Democracy Club Blog"
)
SYNDICATION_FEED_LINK = getattr(settings, "SYNDICATION_FEED_LINK", "/")
SYNDICATION_FEED_DESCRIPTION = getattr(
    settings, "SYNDICATION_FEED_DESCRIPTION", ""
)
SYNDICATION_FEED_TYPE = getattr(settings, "SYNDICATION_FEED_TYPE", Atom1Feed)

HERMES_SHORT_TRUNCATE_WORDS = getattr(
    settings, "HERMES_SHORT_TRUNCATE_WORDS", 30
)

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"


MARKUP_RENDERER = getattr(settings, "MARKUP_RENDERER", renderers.markdown)
