from hermes import models

from .. import settings
from . import HermesTestCase


class PostTestCase(HermesTestCase):
    def test_short(self):
        """A Post should return the truncated body if there is no summary"""
        expected = (
            "<p>I’ve got to find a way to escape the horrible ravages of youth. "
            "Suddenly, I’m going to the bathroom like clockwork, every three "
            "hours. And those jerks at Social Security…</p>"
        )
        self.assertEqual(expected, self.post1.short)

    def test_short_summary_rendered(self):
        """Post.short should return the rendered summary"""
        expected = "<h2>This is a summary</h2>"
        self.post1.summary = "#This is a summary"
        self.post1.save()

        self.assertEqual(expected, self.post1.short)

    def test_rendered(self):
        """A Post should be able to render its body into HTML"""
        self.post4.body = "##Markdown FTW!"
        self.post4.save()

        expected = "<h3>Markdown FTW!</h3>"

        self.assertEqual(expected, self.post4.rendered)

    def test_rendered_summary(self):
        """A Post should be able to render its summary into HTML"""
        self.post4.summary = "##Markdown FTW!"
        self.post4.save()

        expected = "<h3>Markdown FTW!</h3>"

        self.assertEqual(expected, self.post4.rendered_summary)

    def test_rendereded_no_renderer(self):
        """A Post should return its body if no renderer is defined"""
        renderer = settings.MARKUP_RENDERER
        settings.MARKUP_RENDERER = None
        expected = "<p>I&rsquo;ve got to find a way to escape the horrible ravages of youth. Suddenly, I&rsquo;m going to the bathroom like clockwork, every three hours. And those jerks at Social Security stopped sending me checks. Now &lsquo;I&rsquo;&lsquo; have to pay &lsquo;&rsquo;them&rsquo;! Well I&rsquo;da done better, but it&rsquo;s plum hard pleading a case while awaiting trial for that there incompetence. She also liked to shut up!</p>"
        self.assertEqual(expected, self.post1.rendered)

        settings.MARKUP_RENDERER = renderer

    def test_hero_upload_to(self):
        """The Post Hero Upload To method should know the path to save the Hero image"""
        expected = "hermes/heroes/leela-her-own_test_hero.jpg"
        self.assertEqual(
            expected, models.post_hero_upload_to(self.post1, "test.jpg")
        )

        expected = "hermes/heroes/raging-bender_test_hero.jpg"
        self.assertEqual(
            expected, models.post_hero_upload_to(self.post3, "test.jpg")
        )

    def test_unicode(self):
        """The Post should have a unicode representation"""
        expected = "A Tale of Two Santas"
        self.assertEqual(expected, self.post2.__unicode__())

        expected = "The Series Has Landed"
        self.assertEqual(expected, self.post4.__unicode__())

    def test_get_absolute_url(self):
        """The Post should know its absolute URL"""
        expected = "/blog/2010/06/10/leela-her-own/"
        self.assertEqual(expected, self.post1.get_absolute_url())

        expected = "/blog/2013/09/10/series-has-landed/"
        self.assertEqual(expected, self.post4.get_absolute_url())

    def test_reading_time(self):
        """A Post should know how long it would take a human to read it."""
        expected = 20
        self.post1.body = "test " * 6000
        self.post1.save()
        self.assertEqual(expected, self.post1.reading_time)

    def test_reading_time_very_short(self):
        """A Post should never think its reading time is less than a minute"""
        expected = 1
        self.post1.body = ""
        self.post1.save()
        self.assertEqual(expected, self.post1.reading_time)

    def test_multiple_authors(self):
        authors = self.post5.author.all()
        self.assertEqual(3, len(authors))

    def is_staff(self):
        """A Post authored by staff should link the name to the team page anchor"""
        response = self.client.get(self.post5.get_absolute_url())
        self.assertContains(
            response,
            '<a rel="author" href="/about/team/#Joyce">Joyce Byers</a>',
        )
        self.assertContains(
            response, '<a rel="author" href="/about/team/#Jim">Jim Hoppper</a>'
        )
        self.assertContains(response, "Mike Wheeler")
        self.assertNotContains(
            response,
            '<a rel="author" href="/about/team/#Mike">Mike Wheeler</a>',
        )

    def test_author_formatting(self):
        """A Post with 3+ authors should be formatted properly"""
        expected = """
            <address class="author">
            By <a rel="author" href="/about/team/#Jim">Jim Hopper</a>, 
            <a rel="author" href="/about/team/#Joyce">Joyce Byers</a> 
            and Mike Wheeler
            </address>"""
        response = self.client.get(self.post5.get_absolute_url())
        self.assertInHTML(expected, response.rendered_content)

    def test_generate_slug(self):
        """A Post should know how to generate its slug"""
        expected = "a-leela-of-her-own"
        self.assertEqual(expected, self.post1._generate_slug())


class PostQuerySetTestCase(HermesTestCase):
    def test_reverse_creation_order(self):
        """The Post QuerySet should return Posts in reverse creation order"""
        expected = [
            self.post5,
            self.post4,
            self.post3,
            self.post2,
            self.post1,
        ]
        self.assertEqual(expected, list(models.Post.objects.all()))

    def test_in_category(self):
        """The Post QuerySet should return Posts in a specific Category"""
        expected = [
            self.post5,
            self.post3,
            self.post2,
            self.post1,
        ]
        self.assertEqual(
            expected, list(models.Post.objects.in_category("programming"))
        )

    def test_recent(self):
        """The PostQuerySet recent method should return the most recent published Posts up to 'limit'"""
        expected = [
            self.post4,
            self.post2,
        ]
        self.assertEqual(expected, list(models.Post.objects.recent(limit=2)))

    def test_recent_no_limit(self):
        """The PostQuerySet recent method should return all the published Posts if no limit is set"""
        expected = [
            self.post4,
            self.post2,
            self.post1,
        ]
        self.assertEqual(expected, list(models.Post.objects.recent(limit=None)))

    def test_random(self):
        """The PostQuerySet random method should return a random set of Posts"""
        unexpected = models.Post.objects.random(limit=3)
        self.assertNotEqual(unexpected, models.Post.objects.random(limit=3))
        self.assertTrue(
            all(
                isinstance(post, models.Post)
                for post in models.Post.objects.random(limit=3)
            )
        )

    def test_created_on_year(self):
        """The PostQuerySet should know which Posts were created in which year"""
        expected = [
            self.post1,
        ]
        self.assertEqual(
            expected, list(models.Post.objects.created_on(year=2010))
        )

        expected = [
            self.post2,
        ]
        self.assertEqual(
            expected, list(models.Post.objects.created_on(year=2011))
        )

    def test_created_on_month_year(self):
        """The PostQuerySet should know which Posts were created in which month/year"""
        expected = [
            self.post3,
        ]
        self.assertEqual(
            expected, list(models.Post.objects.created_on(year=2012, month=8))
        )

        expected = [
            self.post4,
        ]
        self.assertEqual(
            expected, list(models.Post.objects.created_on(year=2013, month=9))
        )

    def test_created_on_month_year_day(self):
        """The PostQuerySet should know which Posts were created in which day/month/year"""
        expected = [
            self.post1,
        ]
        self.assertEqual(
            expected,
            list(models.Post.objects.created_on(year=2010, month=6, day=10)),
        )

        expected = [
            self.post3,
        ]
        self.assertEqual(
            expected,
            list(models.Post.objects.created_on(year=2012, month=8, day=10)),
        )

    def test_published(self):
        """The PostQuerySet should know what Posts are published"""
        expected = [
            self.post4,
            self.post2,
            self.post1,
        ]
        self.assertEqual(expected, list(models.Post.objects.published()))
