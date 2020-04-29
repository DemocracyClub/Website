# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.urls import reverse_lazy
from django.conf.urls.static import static
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth import views as auth_views

from core.views import HomeView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

handler500 = "dc_theme.urls.dc_server_error"

urlpatterns = [
    # Uncomment the next line to enable the admin:
    url(r"^admin/", admin.site.urls),
    url(
        r"^logout/$", auth_views.logout, {"next_page": "/"}, name="auth_logout"
    ),
    url(r"^$", HomeView.as_view(), name="home"),
    url(r"^thanks/$", TemplateView.as_view(template_name="thanks.html")),
    url(
        r"^thanks/finished$",
        TemplateView.as_view(template_name="thanks_finished.html"),
    ),
    # About URLs
    url(
        r"^about/$",
        TemplateView.as_view(template_name="about/index.html"),
        name="about",
    ),
    url(
        r"^about/jobs/$",
        TemplateView.as_view(template_name="about/jobs.html"),
        name="jobs",
    ),
    url(
        r"^about/funding/$",
        TemplateView.as_view(template_name="about/funding.html"),
        name="funding",
    ),
    url(
        r"^about/team/$",
        TemplateView.as_view(template_name="about/team.html"),
        name="team",
    ),
    url(
        r"^privacy/$",
        TemplateView.as_view(template_name="privacy.html"),
        name="privacy",
    ),
    url(
        r"^code-of-conduct/$",
        TemplateView.as_view(template_name="code-of-conduct.html"),
        name="coc",
    ),
    url(r"^projects/", include("projects.urls", namespace="projects")),
    url(
        r"^contact/$",
        TemplateView.as_view(template_name="contact.html"),
        name="contact",
    ),
    url(r"^blog/", include("hermes.urls")),
    url(r"^donate/", include("donations.urls", namespace="donations")),
    url(r"^report_2016/", include("report_2016.urls", namespace="report_2016")),
    url(r"^report_2017/", include("report_2017.urls", namespace="report_2017")),
    url(r"^report_2018/", include("report_2018.urls", namespace="report_2018")),
    url(r"^report_2019/", include("report_2019.urls", namespace="report_2019")),
    url(
        r"^report_parl.2019/",
        include(
            "report_2019_general_election.urls",
            namespace="report_2019_general_election",
        ),
    ),
    url(
        r"^reports/whos_missing/",
        include("report_whos_missing.urls", namespace="report_whos_missing"),
    ),
    url(
        r"^wheredoivote_user_feedback/",
        include(
            "wheredoivote_user_feedback.urls",
            namespace="wheredoivote_user_feedback",
        ),
    ),
    url(r"^quests/", include("backlog.urls", namespace="backlog")),
    url(r"^data/$", RedirectView.as_view(url=reverse_lazy("projects")),),
    url(
        r"^mailing_list/",
        include("mailing_list.urls", namespace="dc_signup_form"),
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
