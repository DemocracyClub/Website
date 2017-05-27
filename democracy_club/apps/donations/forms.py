# -*- coding: utf-8 -*-
from django import forms

from .helpers import PAYMENT_TYPES, PAYMENT_UNITS


class DonationForm(forms.Form):
    payment_type = forms.ChoiceField(
        label="",
        choices=PAYMENT_TYPES,
        widget=forms.RadioSelect())

    amount = forms.ChoiceField(
        required=True,
        label="",
        choices=PAYMENT_UNITS,
        widget=forms.RadioSelect()
    )
