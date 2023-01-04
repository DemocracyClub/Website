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

    def test_qs_contains_tags(self):
        """The PostListView can filter tags if requested"""

        self.post1.tags.append("foo")
        self.post1.save()

        self.post2.tags.append("foo")
        self.post2.save()

        self.post3.tags.append("bar")
        self.post3.save()

        response = self.get(self.url() + "?tag=foo")
        expected = list(models.Post.objects.published().filter(tags=["foo"]))
        self.assertEqual(expected, list(response.context["posts"]))
        self.assertContains(response, self.post1.subject)
        self.assertNotContains(response, self.post3.subject)


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
