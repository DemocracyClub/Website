from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^redirect/(?P<url>.*)', views.MemberLinkRedirectView.as_view()),
    url(r'^edit/$', views.MemberUpdateView.as_view(),
        name='edit_member'),
    url(r'^$', views.MemberHomeView.as_view(),
        name='view_member'),
    url(r'^token/(?P<token>.*)/$', views.MemberLoginFromTokenView.as_view(),
            name='member_token_login'),
)