import unittest

from django.contrib.auth.models import User

from dc_members.models import Member


class ModelTests(unittest.TestCase):
    """
    Tests for the Member model
    """

    def setUp(self):
        self.user = User(username="symroe")
        self.user.save()

    def test_token_generation(self):
        """
        Make sure a new token is created when a model without one is saved.
        """
        member = Member(
            user=self.user,
            name="Sym Roe",
            email="a@b.com",
            constituency="South Norfolk",
            postcode="IP22 8DJ")
        member.save()

        self.assertEqual(member.token,
                         "a54b65b178bd253f69b6e0d0aaa29ee14757bb66")
