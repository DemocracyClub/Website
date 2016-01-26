import csv
import datetime

import requests

from django.core.management.base import BaseCommand

from authorities.models import (Authority, AuthorityServiceCategory,
                                AuthorityServiceDetails)
from authorities import constants


class Command(BaseCommand):
    def handle(self, **options):
        # self.import_categories()
        self.import_local_service_details()

    def import_local_service_details(self):

        req = requests.get(constants.LOCAL_SERVICES_DETAILS_URL)
        details = csv.reader(req.content.decode('latin-1').splitlines())
        next(details)
        for detail in details:
            try:
                authority = Authority.objects.get(ons_id=detail[1])
                self.make_category(authority, detail)
            except Authority.DoesNotExist:
                continue

    def make_category(self, authority, detail):
        date = datetime.datetime.strptime(detail[7], "%d-%m-%Y %H:%M:%S")
        category, created = AuthorityServiceCategory.objects.get_or_create(
            pk=detail[4],
            defaults={
                'description': detail[3]
            }
        )
        AuthorityServiceDetails.objects.get_or_create(
            SNAC=authority,
            LAid=detail[2],
            LGSL=category,
            LGIL=detail[5],
            URL=detail[6],
            last_updated=date,
        )

    def import_categories(self):
        req = requests.get(constants.ALPHAGOV_LOCAL_SERVICES_CSV_URL)
        categories = csv.reader(req.content.decode('utf8').splitlines())
        next(categories)
        for category in categories:
            AuthorityServiceCategory.objects.get_or_create(
                LGSL=int(category[0]),
                description=category[1],
                providing_tier=category[2]
            )
