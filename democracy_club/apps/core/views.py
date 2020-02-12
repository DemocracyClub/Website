from django.views.generic import TemplateView

from hermes.models import Post
from backlog.models import Card

class HomeView(TemplateView):
    template_name="home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['latest_posts'] = Post.objects.recent(5)
        context['card'] = Card.objects.filter(published=True).first()

        return context
