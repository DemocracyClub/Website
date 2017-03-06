"""
DIW
MTW
UTW
"""

import requests

from django.core.management.base import BaseCommand

from authorities.models import Authority, MapitArea
from authorities import constants
from authorities.constants import AREA_TYPES


class Command(BaseCommand):

    def handle(self, *args, **options):
        for type in AREA_TYPES:
            self.get_type_from_mapit(type)

    def get_type_from_mapit(self, mapit_type):
        req = requests.get('%sareas/%s' % (
            constants.MAPIT_URL, mapit_type))
        for mapit_id, area in list(req.json().items()):
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
