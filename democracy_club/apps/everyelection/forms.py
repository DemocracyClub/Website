from django.forms import (ModelForm, IntegerField)

from .models import (AuthorityElection, AuthorityElectionPosition,
                     AuthorityElectionSkipped)


class AuthorityAreaForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        self.user = user

        for area in self.instance.authority.child_areas:
            self.fields[area.pk] = IntegerField(
                label=area.name,
                initial=0
            )

    class Meta:
        model = AuthorityElection
        fields = []

    def clean(self, *args, **kwargs):
        for area, number in self.cleaned_data.items():
            AuthorityElectionPosition.objects.get_or_create(
                authority_election=self.instance,
                user=self.user,
                area_id=area,
                seats=number
            )
        return super().clean(*args, **kwargs)


class AuthorityElectionSkippedForm(ModelForm):
    class Meta:
        model = AuthorityElectionSkipped
        fields = [
            'notes',
            'authority_election',
            'user',
        ]
