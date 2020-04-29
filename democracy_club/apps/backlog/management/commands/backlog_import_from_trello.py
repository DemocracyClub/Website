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
        url_fmt = "{}/lists/{}/cards?customFieldItems=true&key={}&token={}"
        url = url_fmt.format(self.base_url, self.list_id, self.key, self.token)
        list_data = requests.get(url).json()

        self.initial_ids = set(Card.objects.values_list("pk", flat=True))
        self.seen_ids = set()

        self.setup_board_info()
        for card_dict in list_data:
            self.import_card(card_dict)

        self.clean_up()

    def setup_board_info(self):
        req = requests.get(
            "{}/boards/{}/customFields?key={}&token={}".format(
                self.base_url,
                settings.BACKLOG_TRELLO_BOARD_ID,
                self.key,
                self.token,
            )
        )
        self.customfield_map = {}
        for field in req.json():
            self.customfield_map[field["id"]] = field

    def import_card(self, card_dict):
        labels = []
        for label in card_dict["labels"]:
            labels.append(
                CardLabel.objects.update_or_create(
                    trello_id=label["id"],
                    defaults={"name": label["name"], "colour": label["color"],},
                )[0]
            )

        card = Card.objects.update_or_create(
            trello_id=card_dict["id"],
            defaults={
                "title": card_dict["name"],
                "text": card_dict["desc"],
                "weight": card_dict["pos"],
                "url": card_dict["url"],
                "comment_count": card_dict["badges"]["comments"],
            },
        )[0]
        self.seen_ids.add(card.pk)
        card.labels.add(*labels)

        for custom_field_value in card_dict["customFieldItems"]:
            for field_id, field in self.customfield_map.items():
                if field["id"] == custom_field_value["idCustomField"]:
                    if field["id"] == "5a986717d6afbd6de1d24563":
                        # CTA_URL
                        card.cta_url = custom_field_value["value"]["text"]
                    if field["id"] == "5a986717d6afbd6de1d2455c":
                        # Time Required
                        for option in field["options"]:
                            if option["id"] == custom_field_value["idValue"]:
                                card.time_required = option["value"]["text"]

        card.save()

    def clean_up(self):
        unpublish_ids = self.initial_ids.difference(self.seen_ids)
        Card.objects.filter(pk__in=unpublish_ids).update(published=False)
