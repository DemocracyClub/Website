import time

import requests
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.geos import Point

from authorities.models import Authority, AuthorityGeo
from authorities import constants
from authorities.helpers import geocode


class Command(BaseCommand):
    def handle(self, **options):
        for council_type in constants.AUTHORITY_TYPES:
            self.get_type_from_mapit(council_type)

    def get_wkt_from_mapit(self, area_id):
        req = requests.get('%sarea/%s.wkt' % (constants.MAPIT_URL, area_id))
        area = req.text
        if area.startswith('POLYGON'):
            area = area[7:]
            area = "MULTIPOLYGON(%s)" % area
        return GEOSGeometry(area, srid=27700)
        return area

    def get_contact_info_from_gov_uk(self, council_id):
        req = requests.get("%s%s" % (constants.GOV_UK_LA_URL, council_id))
        soup = BeautifulSoup(req.text, "html.parser")
        info = {}
        article = soup.findAll('article')[0]
        info['website'] = article.find(id='url')['href'].strip()
        info['email'] = article.find(
            id='authority_email').a['href'].strip()[7:]
        info['phone'] = article.find(id='authority_phone').text.strip()[7:]
        info['address'] = "\n".join(
            article.find(id='authority_address').stripped_strings)
        info['postcode'] = article.find(id='authority_postcode').text
        return info

    def get_type_from_mapit(self, authority_type):
        req = requests.get('%sareas/%s' % (
            constants.MAPIT_URL, authority_type))
        for mapit_id, council in list(req.json().items()):
            authority_id = council['codes'].get('gss')
            ons_id = council['codes'].get('ons')
            if not authority_id:
                authority_id = council['codes'].get('ons')
            print(authority_id)
            contact_info = {
                'name': council['name'],
                'ons_id': ons_id,
            }
            if authority_type != "LGD":
                contact_info.update(
                    self.get_contact_info_from_gov_uk(authority_id))
            authority, created = Authority.objects.update_or_create(
                pk=authority_id,
                mapit_id=mapit_id,
                authority_type=authority_type,
                defaults=contact_info,
            )

            if not hasattr(authority, 'authoritygeo'):
                authority_geo = AuthorityGeo(authority=authority)
            else:
                authority_geo = authority.authoritygeo


            if not authority_geo.area:
                authority_geo.area = self.get_wkt_from_mapit(mapit_id)
                authority_geo.save()
                time.sleep(1)
            if not authority_geo.location:
                print(authority.postcode)
                try:
                    l = geocode(authority.postcode)
                except:
                    continue
                time.sleep(1)
                authority_geo.location = Point(l['wgs84_lon'], l['wgs84_lat'])
                authority_geo.save()
                authority.authority_geo = authority_geo
                authority.save()
