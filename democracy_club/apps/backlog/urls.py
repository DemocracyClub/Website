from django.conf.urls import url

from .views import BacklogView

urlpatterns = [
    url(
        r'^$',
        BacklogView.as_view(),
        name='backlog_view'
    ),
    # url(
    #     r'^(?P<pk>[^/]+)/(?P<ignored_slug>.*)$',
    #     PartyView.as_view(),
    #     name='party_view'),
]

