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
            category=self.category_1,
            summary="Foo summary",
            body="Foo body",
        )
        self.foo_tag = models.Tag.objects.create(name="Foo Tag", slug="foo")
        self.bar_tag = models.Tag.objects.create(name="Bar", slug="bar")
        self.blog_with_multiple_tags.tags.set([self.foo_tag, self.bar_tag])
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
        self.assertContains(response, "Foo Tag")
        self.assertContains(response, 'href="/blog/tag/foo/"')

    def test_post_list_tag_filter(self):
        """The blog list shows a filter link for each tag in use"""
        response = self.client.get("/blog/")
        self.assertEqual(
            list(response.context["all_tags"]), [self.bar_tag, self.foo_tag]
        )
        self.assertContains(response, "Foo Tag")

    def test_tag_name_and_slug_editable(self):
        """Renaming a tag changes what's shown and where it links"""
        self.foo_tag.name = "Who Can I Vote For"
        self.foo_tag.slug = "wcivf"
        self.foo_tag.save()
        response = self.client.get(
            self.blog_with_multiple_tags.get_absolute_url()
        )
        self.assertContains(response, "Who Can I Vote For")
        self.assertContains(response, 'href="/blog/tag/wcivf/"')

    def test_for_tag(self):
        self.assertEqual(
            list(models.Post.objects.for_tag("FOO")),
            [self.blog_with_multiple_tags],
        )
        self.assertEqual(
            list(models.Post.objects.for_tag(self.bar_tag)),
            [self.blog_with_multiple_tags],
        )

    def test_posts_for_tag_template_tag(self):
        from hermes.templatetags.post_tags import posts_for_tag

        context = posts_for_tag("foo")
        self.assertEqual(context["tag"], self.foo_tag)
        self.assertEqual(list(context["posts"]), [self.blog_with_multiple_tags])

        context = posts_for_tag("missing")
        self.assertIsNone(context["tag"])
        self.assertEqual(list(context["posts"]), [])
