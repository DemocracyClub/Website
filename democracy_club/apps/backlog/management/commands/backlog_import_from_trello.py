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
        url_fmt = "{}/lists/{}/cards?key={}&token={}"
        url = url_fmt.format(self.base_url, self.list_id, self.key, self.token)
        list_data = requests.get(url).json()

        self.initial_ids = set(Card.objects.values_list('pk', flat=True))
        self.seen_ids = set()

        for card_dict in list_data:
            self.import_card(card_dict)

        self.clean_up()

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
        x = requests.get(card_detail_url)
        import ipdb; ipdb.set_trace()

        # TODO get pluginData too

    def clean_up(self):
        print(self.seen_ids.difference(self.initial_ids))
        unpublish_ids = self.initial_ids.difference(self.seen_ids)
        Card.objects.filter(pk__in=unpublish_ids).update(published=False)
