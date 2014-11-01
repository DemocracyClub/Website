from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^edit/(?P<slug>.+)/$', views.MemberUpdateView.as_view(), name='edit_member'),
    url(r'^(?P<slug>.+)/$', views.MemberHomeView.as_view(), name='view_member'),
)