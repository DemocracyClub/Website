from django.test import TestCase

from everyelection.models import AuthorityElection


class ResultsRecordingTestCase(TestCase):
    def setUp(self):
        self.election = AuthorityElection.objects.create(
            election_id="local.test.2016.05.05",
            authority_id=1,
            election_date="2016-05-05",
            percent_posts="30"
        )

    # def test_
