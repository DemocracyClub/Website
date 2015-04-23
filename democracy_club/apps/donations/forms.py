# -*- coding: utf-8 -*-
from django import forms

from .helpers import PAYMENT_TYPES, INTERVAL_UNITS, FRIENDLY_INTERVALS

class DonationForm(forms.Form):
    amount = forms.DecimalField(
        decimal_places=2,
        required=True,
        label="I’m happy to help, and can give",
        min_value=1,
        widget=forms.NumberInput(
            attrs={'min': '1', 'step': '0.25'}
            )
        )
    payment_interval = forms.ChoiceField(
        choices=FRIENDLY_INTERVALS,
        widget=forms.RadioSelect())



    payment_type = forms.ChoiceField(
        choices=PAYMENT_TYPES,
        widget=forms.HiddenInput())
    interval_length = forms.IntegerField(
        widget=forms.HiddenInput(),
        required=False)
    interval_unit = forms.ChoiceField(
        choices=INTERVAL_UNITS,
        widget=forms.HiddenInput(),
        required=False)


    def clean(self):
        data = super(DonationForm, self).clean()
        if data['payment_interval'] == "once":
            data['payment_type'] = "bill"
        else:
            data['payment_type'] = "subscription"

        if data['payment_interval'] == "weekly":
            data['interval_unit'] = "week"

        if data['payment_interval'] == "monthly":
            data['interval_unit'] = "month"

        data['interval_length'] = 1

        del data['payment_interval']

        return data