from django.db import models
from django.contrib.auth.models import User

from django_extensions.db.models import TimeStampedModel

from authorities.models import Authority, MapitArea


class AuthorityElection(models.Model):
    election_id = models.CharField(primary_key=True, max_length=255)
    authority = models.ForeignKey(Authority)
    election_date = models.DateField(default="2016-05-05")
    percent_posts = models.IntegerField(blank=False, null=False)

    @property
    def formatted_election_date(self):
        return self.election_date.strftime("%d %b, %Y")

    @property
    def chart_url(self):
        remainder = 100 - self.percent_posts
        base_url = "https://chart.googleapis.com/chart?"
        args = "cht=p&chd=t:{0},{1}&chco=27826E|FFFFFF&chs=50x50".format(
            self.percent_posts,
            remainder
        )
        return base_url+args

    @property
    def percent_to_words(self):
        if self.percent_posts < 25:
            return "about one quarter"
        if self.percent_posts < 35:
            return "about one third"
        if self.percent_posts <= 50:
            return "about half"
        if self.percent_posts < 70:
            return "about two thirds"
        if self.percent_posts > 70 and self.percent_posts < 100:
            return "over two thirds"
        if self.percent_posts >= 100:
            return "all"

    def __str__(self):
        return "{0} – {1} ({2})".format(
            self.authority.name,
            self.formatted_election_date,
            self.percent_to_words,
        )


class AuthorityElectionPosition(TimeStampedModel):
    authority_election = models.ForeignKey(AuthorityElection)
    user = models.ForeignKey(User)
    area = models.ForeignKey(MapitArea)
    seats = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return "{0} ({1})".format(
            self.authority_election,
            self.area
        )


class AuthorityElectionSkipped(TimeStampedModel):
    authority_election = models.ForeignKey(AuthorityElection)
    user = models.ForeignKey(User)
    notes = models.TextField(blank=True)
