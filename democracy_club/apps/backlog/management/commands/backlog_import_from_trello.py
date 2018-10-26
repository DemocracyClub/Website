import json

import requests

from django.core.management.base import BaseCommand
from django.conf import settings

from backlog.models import Card, CardLabel


class Command(BaseCommand):
    help = "Imports cards from Trello in to the backlog"

    def handle(self, *args, **options):
        self.list_id = settings.BACKLOG_TRELLO_DEFAULT_LIST_ID
        self.key = settings.BACKLOG_TRELLO_KEY
        self.token = settings.BACKLOG_TRELLO_TOKEN
        self.base_url = "https://api.trello.com/1"
        self.custom_field_plugin_id = "56d5e249a98895a9797bebb9"
        url_fmt = "{}/lists/{}/cards?key={}&token={}"
        url = url_fmt.format(self.base_url, self.list_id, self.key, self.token)
        list_data = requests.get(url).json()

        self.initial_ids = set(Card.objects.values_list('pk', flat=True))
        self.seen_ids = set()

        self.setup_board_info()

        for card_dict in list_data:
            self.import_card(card_dict)

        self.clean_up()

    def setup_board_info(self):
        req = requests.get("{}/boards/{}/pluginData?key={}&token={}".format(
            self.base_url, settings.BACKLOG_TRELLO_BOARD_ID, self.key, self.token
        ))
        self.plugin_field_map = {}
        for plugin in req.json():
            if plugin['idPlugin'] == self.custom_field_plugin_id:
                pluginData_values = json.loads(plugin['value'])
                for field in pluginData_values['fields']:
                    for o in field.get('o', []):
                        self.plugin_field_map[o['id']] = o['value']

    def import_card(self, card_dict):
        labels = []
        for label in card_dict['labels']:
            labels.append(CardLabel.objects.update_or_create(
                trello_id=label['id'],
                defaults={
                    'name': label['name'],
                    'colour': label['color'],
                }
            )[0])

        card = Card.objects.update_or_create(
            trello_id=card_dict['id'],
            defaults={
                'title': card_dict['name'],
                'text': card_dict['desc'],
                'weight': card_dict['pos'],
                'url': card_dict['url'],
                'comment_count': card_dict['badges']['comments']

            }
        )[0]
        self.seen_ids.add(card.pk)
        card.labels.add(*labels)

        card_detail_url = "{}/cards/{}/pluginData?key={}&token={}".format(
            self.base_url, card.pk, self.key, self.token
        )
        card_detail_dict = requests.get(card_detail_url).json()
        for plugin in card_detail_dict:
            if plugin['idPlugin'] == self.custom_field_plugin_id:
                # Custom fields plugin
                pluginData_values = json.loads(plugin['value'])
                for key, value in pluginData_values['fields'].items():
                    if key == "O00ATMzS-tWOnUg":
                        card.cta_url = value
                    if key == "O00ATMzS-jUK8AT":
                        card.time_required = self.plugin_field_map.get(value)
        card.save()

    def clean_up(self):
        unpublish_ids = self.initial_ids.difference(self.seen_ids)
        Card.objects.filter(pk__in=unpublish_ids).update(published=False)
