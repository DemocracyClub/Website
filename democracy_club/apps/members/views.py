from django.views.generic.edit import UpdateView
from django.views.generic import DetailView

from .models import Member


# TODO rate limit
class MemberUpdateView(UpdateView):
    """
    Take a token and find a Member object that matches it.

    Render an update form for Member object.
    """
    template_name = 'members/edit.html'
    queryset = Member.objects.all()
    slug_field = 'token'


class MemberHomeView(DetailView):
    """
    Page for displaying a single member
    """
    template_name = 'members/detail.html'
    queryset = Member.objects.all()
    slug_field = 'token'

