# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from core.views import HomeView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('allauth.urls')),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/'}, name='auth_logout'),
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'thanks/$', TemplateView.as_view(template_name="thanks.html")),
    url(r'thanks/finished$', TemplateView.as_view(template_name="thanks_finished.html")),
    url(r'^about/$', TemplateView.as_view(template_name="about.html")),
    url(r'^projects/$', TemplateView.as_view(template_name="projects.html")),
    url(r'^contact/$', TemplateView.as_view(template_name="contact.html")),
    url(r'^members/', include('dc_members.urls')),
    url(r'^blog/', include('hermes.urls')),
    url(r'^research/', include('research.urls', namespace="research")),
    url(r'^donate/', include('donations.urls', namespace="donations")),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
