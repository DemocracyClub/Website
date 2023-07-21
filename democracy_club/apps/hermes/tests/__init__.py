from django import test
from django.contrib.auth.models import User
from django.urls import reverse
from hermes import models


class HermesTestCase(test.TestCase):
    fixtures = ("hermes",)

    def setUp(self):
        self.root_category = models.Category.objects.get(id=1)
        self.second_category = models.Category.objects.get(id=2)
        self.third_category = models.Category.objects.get(id=3)
        self.another_category = models.Category.objects.get(id=4)

        self.post1 = models.Post.objects.get(id=1)
        self.post2 = models.Post.objects.get(id=2)
        self.post3 = models.Post.objects.get(id=3)
        self.post4 = models.Post.objects.get(id=4)
        author_3 = User.objects.create(
            username="jimhopper",
            email="jim@mac.com",
            first_name="Jim",
            last_name="Hopper",
            is_staff=True,
        )
        author_4 = User.objects.create(
            username="joycebyers",
            email="joyce@mac.com",
            first_name="Joyce",
            last_name="Byers",
            is_staff=True,
        )
        author_5 = User.objects.create(
            username="mikewheeler",
            email="mike@mac.com",
            first_name="Mike",
            last_name="Wheeler",
            is_staff=False,
        )

        self.post5 = models.Post(
            id=5,
            subject="Stranger Things",
            body="Stranger Things is set in the summer of 1985 and shows the young friends maturing into teenagers and navigating new life challenges, all while a new threat looms over the tow.",
            category=self.second_category,
            slug="stranger-things",
        )
        self.post5.save()
        self.post5.author.add(author_3)
        self.post5.author.add(author_4)
        self.post5.author.add(author_5)
        self.post5.save()

        self.user = User.objects.get(id=1)

        self.client = test.Client()

    def url(self, url_name, *args, **kwargs):
        return reverse(url_name, args=args, kwargs=kwargs)

    def get(self, url):
        return self.client.get(url)
