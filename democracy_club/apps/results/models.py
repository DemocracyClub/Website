from django.db import models

from django_extensions.db.models import TimeStampedModel

from everyelection.models import AuthorityElection

class ElectionResultSet(TimeStampedModel):
    election = models.ForeignKey(AuthorityElection)
    reported_turnout = models.IntegerField(blank=True, null=True)
    calculated_turnout = models.IntegerField(blank=True, null=True)

