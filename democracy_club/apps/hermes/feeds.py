from django.contrib.syndication.views import Feed
from hermes.models import Post

from .settings import (
    SYNDICATION_FEED_DESCRIPTION,
    SYNDICATION_FEED_LINK,
    SYNDICATION_FEED_TITLE,
    SYNDICATION_FEED_TYPE,
)


class LatestPostFeed(Feed):
    title = SYNDICATION_FEED_TITLE
    link = SYNDICATION_FEED_LINK
    description = SYNDICATION_FEED_DESCRIPTION
    feed_type = SYNDICATION_FEED_TYPE
    description_template = "hermes/feed_post_description.html"

    def items(self):
        return Post.objects.recent(limit=5)

    def item_title(self, item):
        return item.subject

    def item_description(self, item):
        return item.body

    def item_pubdate(self, item):
        return item.created_on

    def item_updateddate(self, item):
        return item.modified_on

    def item_categories(self, item):
        return [category.title for category in item.category.hierarchy()]

    def item_author_name(self, item):
        authors = [
            author.first_name + " " + author.last_name
            for author in item.author.all()
        ]
        if len(authors) == 1:
            return authors[0]
        return ", ".join(authors)

    def item_author_email(self, item):
        emails = [author.email for author in item.author.all()]
        if len(emails) == 1:
            return emails[0]
        return "; ".join(emails)
