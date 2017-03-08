from django.test import TestCase

from backlog.models import Card


class TestBacklogView(TestCase):

    def setUp(self):
        self.card = Card(
            time_required="10 minutes",
            weight=1,
            title="A test task"
        )
        self.card.save()

    def test_info_on_backlog_cards(self):
        resp = self.client.get('/backlog/')
        self.assertContains(resp, "Time required: <strong>10 minutes")
        self.assertContains(resp, self.card.title)
