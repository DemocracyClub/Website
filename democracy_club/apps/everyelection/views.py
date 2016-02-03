from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView, UpdateView
from django.core.urlresolvers import reverse

from braces.views import LoginRequiredMixin

from .models import AuthorityElection, AuthorityElectionPosition
from .forms import AuthorityAreaForm


class RandomAuthority(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        authority_election = AuthorityElection.objects.annotate(
            position_count=Count('authorityelectionposition')
        ).order_by('position_count').first()
        return reverse('everyelection:authority', kwargs={
            'pk': authority_election.pk})


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

    def get_context_data(self, **kwargs):
        kwargs['elections_researched'] = \
            AuthorityElectionPosition.objects.filter(
                user=self.request.user)\
            .values('authority_election')\
            .distinct().count()

        kwargs['areas_researched'] = AuthorityElectionPosition.objects.filter(
            user=self.request.user
        ).count()

        return super().get_context_data(**kwargs)
