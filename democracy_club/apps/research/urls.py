from django.conf.urls import url, include

from rest_framework import routers

from .api import AnswerView
from .views import StatsView

router = routers.DefaultRouter()
router.register(r'answers', AnswerView)


urlpatterns = [
    url(r'stats', StatsView.as_view()),
    url(r'', include(router.urls)),
]
