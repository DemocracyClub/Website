import csv

import requests

from django.core.management.base import BaseCommand

from authorities.models import Authority
from everyelection.models import AuthorityElection

class Command(BaseCommand):
    def handle(self, **options):
        sheet_url = "https://docs.google.com/spreadsheets/d/1YM-inMb-WLzyNN8e7eOFoIm_woJFaWPAlYfOUVuHuy0/pub?gid=842349154&single=true&output=csv"
        req = requests.get(sheet_url)
        data = csv.reader(req.content.decode('utf8').splitlines())
        next(data)
        for row in data:
            authority = self.authority_from_name(row[0])
            election_id = row[8]
            percent_posts = self.words_to_percent_posts(row[2])
            election_date = "2016-05-05"
            AuthorityElection.objects.get_or_create(
                election_id=election_id,
                defaults={
                    "authority": authority,
                    "percent_posts": percent_posts,
                    "election_date": election_date,
                }
            )


    def authority_from_name(self, name):
        name = "{0} ".format(name)
        return Authority.objects.get(name__startswith=name)

    def words_to_percent_posts(self, word):
        if word == "Half":
            return 50
        if word == "Third":
            return 33
        if word == "Whole":
            return 100
