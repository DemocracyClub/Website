from django.test import TestCase

import helpers

class TestGoCardless(TestCase):
    def test_helpers(self):
        gc = helpers.GoCardlessHelper()
        self.assertTrue(gc.get_payment_url(3))
        self.assertTrue(gc.get_payment_url(3.5))
        self.assertTrue(gc.get_payment_url(
            3,
            payment_type="subscription",
            interval_length=1,
            interval_unit="month",
            ))
