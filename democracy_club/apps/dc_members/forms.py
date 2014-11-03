from django.forms import ModelForm

from .models import Member

class MemberUpdateForm(ModelForm):
    class Meta:
        model = Member
        exclude = ['token', 'user', 'constituency']