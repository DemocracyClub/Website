import unittest

from members.models import Member


class ModelTests(unittest.TestCase):
    """
    Tests for the Member model
    """

    def test_token_generation(self):
        """
        Make sure a new token is created when a model without one is saved.
        """
        member = Member(
            name="Sym Roe",
            email="a@b.com",
            constituency="South Norfolk",
            postcode="IP22 8DJ")
        member.save()

        self.assertTrue(member.token != None)
        self.assertTrue(len(member.token) == 40)
