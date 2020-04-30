from django.urls import re_path

from .views import BacklogView

app_name = "backlog"

urlpatterns = [
    re_path(r"^$", BacklogView.as_view(), name="backlog_view"),
    # url(
    #     r'^(?P<pk>[^/]+)/(?P<ignored_slug>.*)$',
    #     PartyView.as_view(),
    #     name='party_view'),
]
