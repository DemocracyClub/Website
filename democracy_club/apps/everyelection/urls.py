from django.conf.urls import patterns, url, include

from django.views.generic import TemplateView

from .views import AuthorityEdit, RandomAuthority

urlpatterns = [
    url(r'^$',
        TemplateView.as_view(template_name='everyelection/home.html'),
        name="home"),
    url(r'random_election', RandomAuthority.as_view(), name="random_election"),
    url(r'authority/(?P<pk>.*)/', AuthorityEdit.as_view(), name="authority"),
]
