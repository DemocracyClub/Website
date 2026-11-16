from django.urls import reverse
from hermes import models

from . import HermesTestCase


class PostListViewTestCase(HermesTestCase):
    def url(self):
        return super(PostListViewTestCase, self).url("hermes_post_list")

    def test_context_contains_posts(self):
        """The PostListView Context should contain a QuerySet of all Posts"""
        response = self.get(self.url())
        expected = list(models.Post.objects.published())
        self.assertEqual(expected, list(response.context["posts"]))

    def test_tag_filter_lists_tags_in_use(self):
        """The PostListView offers a filter link for each tag in use"""
        foo = models.Tag.objects.create(name="Foo", slug="foo")
        models.Tag.objects.create(name="Unused", slug="unused")
        self.post1.tags.add(foo)

        response = self.get(self.url())
        self.assertIn(foo, response.context["all_tags"])
        self.assertNotIn(
            "Unused", [t.name for t in response.context["all_tags"]]
        )
        self.assertContains(response, 'href="/blog/tag/foo/"')


class TagPostListViewTestCase(HermesTestCase):
    def url(self, tag):
        return super(TagPostListViewTestCase, self).url(
            "hermes_post_list_by_tag", tag=tag
        )

    def setUp(self):
        super().setUp()
        self.tag = models.Tag.objects.create(
            name="Test Studies", slug="test-studies"
        )
        self.post1.tags.add(self.tag)

    def test_get_queryset(self):
        """The TagPostListView Context should contain a QuerySet of all Posts
        with the given tag
        """
        response = self.get(self.url("test-studies"))
        expected = list(models.Post.objects.for_tag("test-studies"))
        self.assertEqual(expected, [self.post1])
        self.assertEqual(expected, list(response.context["posts"]))
        self.assertEqual(response.context["tag"], self.tag)

    def test_filter_shows_all_tags_on_tag_page(self):
        """The tag filter isn't limited to tags on the listed posts"""
        other = models.Tag.objects.create(name="Other", slug="other")
        self.post2.tags.add(other)
        response = self.get(self.url("test-studies"))
        self.assertIn(other, response.context["all_tags"])
        self.assertContains(response, 'href="/blog/tag/other/"')
        self.assertContains(
            response, 'href="/blog/tag/test-studies/" aria-current="true"'
        )

    def test_filter_hides_tags_only_on_unpublished_posts(self):
        draft_only = models.Tag.objects.create(name="Draft", slug="draft")
        draft = models.Post.objects.filter(is_published=False).first()
        draft.tags.add(draft_only)
        response = self.get(self.url("test-studies"))
        self.assertNotIn(draft_only, response.context["all_tags"])

    def test_unknown_tag_404s(self):
        response = self.get(self.url("nope"))
        self.assertEqual(response.status_code, 404)

    def test_non_canonical_slug_redirects(self):
        """Old-style mixed-case tag URLs redirect to the canonical slug"""
        response = self.get(self.url("Test-Studies"))
        self.assertRedirects(
            response, self.url("test-studies"), status_code=301
        )

    def test_renamed_slug_redirects(self):
        self.tag.slug = "studies"
        self.tag.save()
        self.assertRedirects(
            self.get(self.url("test-studies")),
            self.url("studies"),
            status_code=301,
        )
        # Old slugs are matched case-insensitively too
        self.assertRedirects(
            self.get(self.url("Test-Studies")),
            self.url("studies"),
            status_code=301,
        )
        self.assertEqual(
            list(models.Post.objects.for_tag("test-studies")), [self.post1]
        )

    def test_chained_renames_all_redirect_to_current_slug(self):
        self.tag.slug = "second"
        self.tag.save()
        self.tag.slug = "third"
        self.tag.save()
        for old in ("test-studies", "second"):
            self.assertRedirects(
                self.get(self.url(old)), self.url("third"), status_code=301
            )
        self.assertEqual(
            sorted(self.tag.slug_redirects.values_list("old_slug", flat=True)),
            ["second", "test-studies"],
        )

    def test_renaming_back_removes_redirect(self):
        self.tag.slug = "studies"
        self.tag.save()
        self.tag.slug = "test-studies"
        self.tag.save()
        self.assertEqual(
            list(self.tag.slug_redirects.values_list("old_slug", flat=True)),
            ["studies"],
        )
        response = self.get(self.url("test-studies"))
        self.assertEqual(response.status_code, 200)

    def test_new_tag_can_claim_an_old_slug(self):
        self.tag.slug = "studies"
        self.tag.save()
        new_tag = models.Tag.objects.create(name="New", slug="test-studies")
        response = self.get(self.url("test-studies"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["tag"], new_tag)
        self.assertFalse(self.tag.slug_redirects.exists())

    def test_slugs_are_lowercased(self):
        tag = models.Tag.objects.create(name="Upper", slug="UpperCase")
        self.assertEqual(tag.slug, "uppercase")

    def test_query_string_tag_redirects_to_tag_page(self):
        """Old-style /blog/?tag=... links go to the tag page"""
        self.assertRedirects(
            self.get(reverse("hermes_post_list") + "?tag=Test-Studies"),
            self.url("test-studies"),
            status_code=301,
        )

    def test_unknown_query_string_tag_shows_all_posts(self):
        response = self.get(reverse("hermes_post_list") + "?tag=nope")
        self.assertEqual(response.status_code, 200)


class ArchivePostListViewTestCase(HermesTestCase):
    def url(self, year=None, month=None, day=None):
        if year and month and day:
            url_name = "hermes_archive_year_month_day"
            kwargs = {
                "year": year,
                "month": month,
                "day": day,
            }
        elif year and month:
            url_name = "hermes_archive_year_month"
            kwargs = {
                "year": year,
                "month": month,
            }
        else:
            url_name = "hermes_archive_year"
            kwargs = {
                "year": year,
            }

        return super(ArchivePostListViewTestCase, self).url(url_name, **kwargs)

    def test_context_contains_posts_by_month_year_day(self):
        """The ArchivePostListView Context should contain a QuerySet of all
        Posts on the given month/day/year
        """
        response = self.get(self.url(year=2010, month=6, day=10))
        expected = list(
            models.Post.objects.created_on(year=2010, month=6, day=10)
        )
        self.assertEqual(expected, list(response.context["posts"]))

    def test_context_contains_posts_by_month_year(self):
        """The ArchivePostListView Context should contain a QuerySet of all
        Posts on the given month/day
        """
        response = self.get(self.url(year=2011, month=7))
        expected = list(models.Post.objects.created_on(year=2011, month=7))
        self.assertEqual(expected, list(response.context["posts"]))

    def test_context_contains_posts_by_year(self):
        """The ArchivePostListView Context should contain a QuerySet of all
        Posts in the given year
        """
        response = self.get(self.url(year=2012))
        expected = list(models.Post.objects.created_on(year=2012))
        self.assertEqual(expected, list(response.context["posts"]))


class PostDetailViewTestCase(HermesTestCase):
    def url(self, post):
        return post.get_absolute_url()

    def test_context_contains_post(self):
        response = self.get(self.url(self.post1))
        expected = self.post1
        self.assertEqual(expected, response.context["post"])
