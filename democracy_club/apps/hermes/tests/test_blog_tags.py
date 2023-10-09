from hermes import models

from . import HermesTestCase


class BlogTestCase(HermesTestCase):
    def setUp(self):
        # author = User.objects.create(
        #     username="jimhopper",
        #     email="jim@mac.com",
        #     first_name="Jim",
        #     last_name="Hopper",
        #     is_staff=True,
        # )
        self.category_1 = models.Category.objects.create(
            title="Foo",
            slug="foo",
        )
        self.category_2 = models.Category.objects.create(
            title="Bar",
            slug="bar",
        )
        self.blog_with_multiple_tags = models.Post.objects.create(
            is_published=True,
            subject="Foo",
            slug="foo",
            tags=["foo", "bar"],
            category=self.category_1,
            summary="Foo summary",
            body="Foo body",
        )
        self.blog_without_tags = models.Post.objects.create(
            is_published=True,
            subject="Bar",
            slug="bar",
            category=self.category_2,
            summary="Bar summary",
            body="Bar body",
        )
        self.posts = [self.blog_with_multiple_tags, self.blog_without_tags]

    def test_blog_without_tags(self):
        """Don't show the tag icon if a post doesn't have any tags"""
        response = self.client.get(self.blog_without_tags.get_absolute_url())
        self.assertNotContains(response, "🏷️")

    def test_blog_with_tags(self):
        """Show the tag icon if a post has tags"""
        response = self.client.get(
            self.blog_with_multiple_tags.get_absolute_url()
        )
        self.assertContains(response, "🏷️")
        self.assertContains(response, "foo")
