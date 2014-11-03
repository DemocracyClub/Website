import os

import hashlib

from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    """
    Members are people who have done tasks in the past.  They are added when
    someone gives us their information with the intent of "joining" DC.
    """
    user = models.ForeignKey(User, unique=True)
    name = models.CharField(blank=True, max_length=255)
    email = models.EmailField()
    # TODO FK to...PoPit? MaPit?
    constituency = models.CharField(blank=True, max_length=255)
    # TODO Convert to proper postcode field
    postcode = models.CharField(blank=True, max_length=20)
    token = models.CharField(blank=True, max_length=255, db_index=True)


    @models.permalink
    def get_absolute_url(self):
        return ('view_member', (), {})

    def generate_token(self):
        return hashlib.sha1("--".join([
            self.email,
            self.postcode
        ])).hexdigest()

    def save(self, *args, **kwargs):
        """
        Set the token if it doesn't exist
        """
        if not self.token:
            self.token = self.generate_token()
        super(Member, self).save(*args, **kwargs)