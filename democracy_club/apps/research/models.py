from django.db import models

from django_extensions.db.models import TimeStampedModel


class Answer(TimeStampedModel):
    answer_set = models.CharField(blank=True, max_length=255, db_index=True)
    question = models.TextField(blank=True, db_index=True)
    answer = models.CharField(blank=True, max_length=100)
    source = models.CharField(blank=True, max_length=255, db_index=True)
