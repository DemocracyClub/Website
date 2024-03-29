from django.urls import path, re_path

from .feeds import LatestPostFeed
from .views import (
    ArchivePostListView,
    PostDetail,
    PostListView,
    TagPostListView,
)

urlpatterns = [
    re_path(
        r"^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<slug>[\w-]+)/$",
        view=PostDetail.as_view(),
        name="hermes_post_detail",
    ),
    re_path(
        r"^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$",
        view=ArchivePostListView.as_view(),
        name="hermes_archive_year_month_day",
    ),
    re_path(
        r"^(?P<year>\d+)/(?P<month>\d+)/$",
        view=ArchivePostListView.as_view(),
        name="hermes_archive_year_month",
    ),
    re_path(
        r"^(?P<year>\d+)/$",
        view=ArchivePostListView.as_view(),
        name="hermes_archive_year",
    ),
    re_path(
        r"^$",
        view=PostListView.as_view(),
        name="hermes_post_list",
    ),
    re_path(r"^feed/$", view=LatestPostFeed(), name="hermes_post_feed"),
    path(
        "tag/<slug:tag>/",
        view=TagPostListView.as_view(),
        name="hermes_post_list_by_tag",
    ),
]
