from django.test import TestCase

import vcr

from django.core.management import call_command

from backlog.models import Card


class TestBacklogImporter(TestCase):
    @vcr.use_cassette(
        "fixtures/vcr_cassettes/test_backlog_import_cards.yaml",
        filter_query_parameters=["key", "token"],
    )
    def test_backlog_import_cards(self):
        assert Card.objects.count() == 0
        call_command("backlog_import_from_trello")
        assert Card.objects.count() == 4
