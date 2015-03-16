# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('allauth.urls')),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/'}, name='auth_logout'),
    url(r'^$', TemplateView.as_view(template_name="home.html"), name="home"),
    url(r'thanks/$', TemplateView.as_view(template_name="thanks.html")),
    url(r'thanks/finished$', TemplateView.as_view(template_name="thanks_finished.html")),
    url(r'^about/$', TemplateView.as_view(template_name="about.html")),
    url(r'^data/$', TemplateView.as_view(template_name="data.html")),
    url(r'^contact/$', TemplateView.as_view(template_name="contact.html")),
    url(r'^help_out/$', TemplateView.as_view(template_name="help_out.html")),
    url(r'^members/', include('dc_members.urls')),
    url(r'^blog/', include('hermes.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
