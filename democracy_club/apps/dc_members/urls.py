from django.conf.urls import patterns, url, include

from rest_framework import routers

from .api import MemberView
from . import views

router = routers.DefaultRouter()
router.register(r'members', MemberView)


urlpatterns = patterns('',
    url(r'^redirect/(?P<url>.*)', views.MemberLinkRedirectView.as_view()),
    url(r'^edit/$', views.MemberUpdateView.as_view(),
        name='edit_member'),
    url(r'^$', views.MemberHomeView.as_view(),
        name='view_member'),
    url(r'^token/(?P<token>.*)/$', views.MemberLoginFromTokenView.as_view(),
            name='member_token_login'),
    url(r'^api/', include(router.urls)),
)