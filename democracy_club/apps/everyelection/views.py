import random

from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView, UpdateView
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from braces.views import LoginRequiredMixin

from .models import AuthorityElection, AuthorityElectionPosition
from .forms import AuthorityAreaForm, AuthorityElectionSkippedForm


class RandomAuthority(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        authority_elections = list(AuthorityElection.objects.exclude(
            percent_posts=100
        )\
        .annotate(
            position_count=Count('authorityelectionposition')
        ).order_by('position_count').values_list('election_id', flat=True))
        half = authority_elections[0:int(len(authority_elections)/2)]
        authority_election = random.choice(half)

        return reverse('everyelection:authority', kwargs={
            'pk': authority_election})


class AuthorityEdit(LoginRequiredMixin, UpdateView):
    template_name = "everyelection/authority.html"
    form_class = AuthorityAreaForm
    model = AuthorityElection

    def get_success_url(self):
        return reverse('everyelection:random_election')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def post(self, *args, **kwargs):
        if 'skipped_form' in self.request.POST:
            form = AuthorityElectionSkippedForm({
                'user': self.request.user.pk,
                'authority_election': self.get_object().pk,
                'notes': self.request.POST['notes'],
            })
            if form.is_valid():
                form.save()
                url = reverse('everyelection:random_election')
                return redirect(url)
        return super().post(*args, **kwargs)



    def get_context_data(self, **kwargs):
        kwargs['elections_researched'] = \
            AuthorityElectionPosition.objects.filter(
                user=self.request.user)\
            .values('authority_election')\
            .distinct().count()

        kwargs['areas_researched'] = AuthorityElectionPosition.objects.filter(
            user=self.request.user,
            seats__gt=0,
        ).count()

        kwargs['wards_total'] = self.object.authority.child_areas.count()

        kwargs['skip_form'] = AuthorityElectionSkippedForm()

        return super().get_context_data(**kwargs)
