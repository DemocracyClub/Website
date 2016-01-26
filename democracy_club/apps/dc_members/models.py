import hashlib

import requests
from jsonfield import JSONField

from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    """
    Members are people who have done tasks in the past.  They are added when
    someone gives us their information with the intent of "joining" DC.
    """
    user = models.OneToOneField(User, null=True)
    name = models.CharField(blank=True, max_length=255)
    email = models.EmailField()
    constituency = models.CharField(blank=True, max_length=255)
    mapit_json = JSONField(null=True)
    postcode = models.CharField(blank=True, max_length=20)
    token = models.CharField(blank=True, max_length=255, db_index=True)
    source = models.CharField(blank=True, max_length=800)


    @models.permalink
    def get_absolute_url(self):
        return ('view_member', (), {})

    def generate_token(self):
        return hashlib.sha1("--".join([
            self.email,
            self.postcode
        ])).hexdigest()

    def _update_postcode(self):
        """
        When the postcode changes, grab the new json from mapit
        """
        clean_postcode = self.postcode.replace(' ', '')
        base_url = "http://mapit.mysociety.org/postcode/"
        res = requests.get(base_url + clean_postcode).json()
        self.mapit_json = res
        self.constituency = res['areas'][str(res['shortcuts']['WMC'])]['name']

    def save(self, *args, **kwargs):
        """
        Set the token if it doesn't exist
        """
        if not self.token:
            self.token = self.generate_token()

        if self.pk:
            orig = Member.objects.get(pk=self.pk)
            if orig.postcode != self.postcode:
                # The postcode has changed
                self._update_postcode()
        super(Member, self).save(*args, **kwargs)
