from django.conf.urls import patterns, url, include

from rest_framework import routers

from .api import AnswerView
from .views import StatsView

router = routers.DefaultRouter()
router.register(r'answers', AnswerView)


urlpatterns = patterns('',
    url(r'stats', StatsView.as_view()),
    url(r'', include(router.urls)),
)
