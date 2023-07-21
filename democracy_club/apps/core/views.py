from django.views.generic import TemplateView
from hermes.models import Post


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["latest_posts"] = Post.objects.recent(3)

        return context
