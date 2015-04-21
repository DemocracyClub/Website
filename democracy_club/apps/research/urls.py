from django.conf.urls import patterns, url, include

from rest_framework import routers

from .api import AnswerView

router = routers.DefaultRouter()
router.register(r'answers', AnswerView)


urlpatterns = patterns('',
    url(r'', include(router.urls)),
)
