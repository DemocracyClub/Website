from django.forms import (ModelForm, CheckboxSelectMultiple,
                          MultipleChoiceField)

from .models import (AuthorityElection, AuthorityElectionPosition,
                     AuthorityElectionSkipped)


class AuthorityAreaForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.fields['areas'] = MultipleChoiceField(
            choices=[
                (a.pk, a.name) for a in self.instance.authority.child_areas],
            label="Wards",
            widget=CheckboxSelectMultiple
        )

    class Meta:
        model = AuthorityElection
        fields = []

    def clean(self, *args, **kwargs):
        if 'areas' in self.cleaned_data:
            for area in self.cleaned_data['areas']:
                AuthorityElectionPosition.objects.get_or_create(
                    authority_election=self.instance,
                    user=self.user,
                    area_id=area
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
