import datetime

from django.test import TestCase

from django.contrib.auth.models import User

from authorities.models import Authority

from .forms import AuthorityElectionSkippedForm
from .models import AuthorityElection

class TestAuthorityElectionSkippedForm(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test')
        a = Authority.objects.create(name="test")
        self.election = AuthorityElection.objects.create(
            election_id="test.123",
            authority=a,
            election_date=datetime.datetime.now(),
            percent_posts=33,
        )

    def test_create(self):
        form = AuthorityElectionSkippedForm({
            'user': self.user.pk,
            'authority_election': self.election.pk,
            'notes': "this is a test",
        })
        form.is_valid()
        form.save()

