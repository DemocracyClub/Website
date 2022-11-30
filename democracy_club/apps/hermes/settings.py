from django.conf import settings
from django.utils.feedgenerator import Atom1Feed

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

try:
    from . import renderers

    MARKUP_RENDERER = getattr(settings, "MARKUP_RENDERER", renderers.markdown)
except:
    MARKUP_RENDERER = getattr(settings, "MARKUP_RENDERER", None)
