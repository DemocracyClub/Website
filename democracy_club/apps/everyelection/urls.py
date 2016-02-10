from django.conf.urls import patterns, url, include

from django.views.generic import TemplateView

from .views import AuthorityEdit, RandomAuthority, SkippedAuthoritiesView

urlpatterns = [
    url(r'^$',
        TemplateView.as_view(template_name='everyelection/home.html'),
        name="home"),
    url(r'random_election', RandomAuthority.as_view(), name="random_election"),
    url(r'election/(?P<pk>.*)/', AuthorityEdit.as_view(), name="authority"),
    url(
        r'admin/skipped/',
        SkippedAuthoritiesView.as_view(),
        name="skipped_elections"
    ),
]
