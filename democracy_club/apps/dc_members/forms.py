from django.forms import ModelForm

from localflavor.gb.forms import GBPostcodeField

from .models import Member

class MemberUpdateForm(ModelForm):
    class Meta:
        model = Member
        exclude = [
            'token',
            'user',
            'constituency',
            'mapit_json',
            'source',
        ]

    postcode = GBPostcodeField(required=True)
