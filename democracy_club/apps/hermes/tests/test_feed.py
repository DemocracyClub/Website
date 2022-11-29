import feedparser

from . import HermesTestCase
from hermes import models


class LatestPostFeedTestCase(HermesTestCase):
    def url(self):
        return super(LatestPostFeedTestCase, self).url("hermes_post_feed")

    def test_feed_contains_posts(self):
        response = self.get(self.url())
        data = feedparser.parse(response.content)

        post_urls = [post["id"] for post in data["entries"]]
        expected = [
            "http://example.com{url}".format(url=post.get_absolute_url())
            for post in models.Post.objects.published()
        ]

        self.assertEqual(expected, post_urls)

    def test_blog_title(self):
        response = self.get(self.url())
        data = feedparser.parse(response.content)

        self.assertEqual(data["feed"]["title"], "Democracy Club Blog")
