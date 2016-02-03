"""
DIW
MTW
UTW
"""

import time

import requests
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.geos import Point

from authorities.models import Authority, MapitArea
from authorities import constants
from authorities.helpers import geocode


class Command(BaseCommand):

    def add_arguments(self, parser):
            parser.add_argument('mapit_type', type=str)

    def handle(self, *args, **options):
        print(options)
        self.get_type_from_mapit(options['mapit_type'])

    def get_type_from_mapit(self, mapit_type):
        req = requests.get('%sareas/%s' % (
            constants.MAPIT_URL, mapit_type))
        for mapit_id, area in list(req.json().items()):
            print(area)
            authority = Authority.objects.get(mapit_id=area['parent_area'])
            MapitArea.objects.get_or_create(
                gss=area['codes']['gss'],
                parent_authority=authority,
                name=area['name'],
                area_type=area['type'],
                unit_id=area['codes']['unit_id'],
                type_name=area['type_name'],
                country_name=area['country_name'],
            )
