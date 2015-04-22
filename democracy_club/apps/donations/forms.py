from django import forms

from .helpers import PAYMENT_TYPES, INTERVAL_UNITS

class DonationForm(forms.Form):
    amount = forms.DecimalField(
        decimal_places=2,
        required=True,
        label="I would like to give",
        min_value=1,
        widget=forms.NumberInput(
            attrs={'min': '0', 'max': '10', 'step': '0.25'}
            )
        )
    payment_type = forms.ChoiceField(
        choices=PAYMENT_TYPES,
        widget=forms.RadioSelect())
    interval_length = forms.IntegerField(label="Every")
    interval_unit = forms.ChoiceField(
        choices=INTERVAL_UNITS,
        widget=forms.RadioSelect())
