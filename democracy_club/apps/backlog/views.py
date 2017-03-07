from django.views.generic import ListView

from backlog.models import Card


class BacklogView(ListView):
    queryset = Card.objects.filter(published=True)
