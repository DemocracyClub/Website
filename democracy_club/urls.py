# -*- coding: utf-8 -*-

from django.conf import settings
from django.urls import include, path
from django.urls import reverse_lazy
from django.conf.urls.static import static
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth import views as auth_views

from core.views import HomeView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin


admin.autodiscover()

handler500 = "dc_utils.urls.dc_server_error"


def trigger_error(request):
    division_by_zero = 1 / 0
    return division_by_zero


urlpatterns = [
    # Uncomment the next line to enable the admin:
    path("admin/", admin.site.urls),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="/"),
        name="auth_logout",
    ),
    path("", HomeView.as_view(), name="home"),
    path(
        "data_apis/data/",
        TemplateView.as_view(template_name="data_apis/data.html"),
        name="data",
    ),
    path(
        "data_apis/voting_information_api/",
        TemplateView.as_view(
            template_name="data_apis/voting_information_api.html"
        ),
        name="voting_information_api",
    ),
    path(
        "voters/",
        TemplateView.as_view(template_name="for_voters.html"),
        name="voters",
    ),
    path("thanks/", TemplateView.as_view(template_name="thanks.html")),
    path(
        "thanks/finished/",
        TemplateView.as_view(template_name="thanks_finished.html"),
    ),
    # About URLs
    path(
        "about/",
        TemplateView.as_view(template_name="about/index.html"),
        name="about",
    ),
    path(
        "about/jobs/",
        TemplateView.as_view(template_name="about/jobs.html"),
        name="jobs",
    ),
    path(
        "research/case_studies/",
        TemplateView.as_view(template_name="research/case_studies.html"),
        name="case_studies",
    ),
    path(
        "research/impact/",
        TemplateView.as_view(template_name="research/impact.html"),
        name="impact",
    ),
    path(
        "research/index/",
        RedirectView.as_view(url=reverse_lazy("research/impact.html")),
    ),
    path(
        "about/team/",
        TemplateView.as_view(template_name="about/team.html"),
        name="team",
    ),
    path(
        "about/funding/",
        TemplateView.as_view(template_name="about/funding.html"),
        name="funding",
    ),
    path(
        "privacy/",
        TemplateView.as_view(template_name="privacy.html"),
        name="privacy",
    ),
    path(
        "code-of-conduct/",
        TemplateView.as_view(template_name="code-of-conduct.html"),
        name="coc",
    ),
    path("projects/", include("projects.urls", "projects")),
    path(
        "contact/",
        TemplateView.as_view(template_name="contact.html"),
        name="contact",
    ),
    path("blog/", include("hermes.urls")),
    path(
        "donate/",
        TemplateView.as_view(template_name="donate.html"),
        name="donate",
    ),
    path("report_2016/", include("report_2016.urls", namespace="report_2016")),
    path("report_2017/", include("report_2017.urls", namespace="report_2017")),
    path("report_2018/", include("report_2018.urls", namespace="report_2018")),
    path("report_2019/", include("report_2019.urls", namespace="report_2019")),
    path(
        "report_2019_general_election/",
        include(
            "report_2019_general_election.urls",
            namespace="report_2019_general_election",
        ),
    ),
    path("report_2021/", include("report_2021.urls", namespace="report_2021")),
    path("report_2022/", include("report_2022.urls", namespace="report_2022")),
    path(
        "reports/whos_missing/",
        include("report_whos_missing.urls", namespace="report_whos_missing"),
    ),
    path(
        "wheredoivote_user_feedback/",
        include(
            "wheredoivote_user_feedback.urls",
            namespace="wheredoivote_user_feedback",
        ),
    ),
    path(
        "mailing_list/",
        include(("mailing_list.urls", "dc_signup_form")),
    ),
    path("sentry-debug/", trigger_error),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Tuple of URLs to redirect to. Maintained for backwards compatibility / old links
url_redirects = (
    path(
        "data/",
        RedirectView.as_view(url=reverse_lazy("projects")),
    ),
    path(
        "donate/",
        RedirectView.as_view(url=reverse_lazy("funding")),
    ),
    path(
        "support-us/",
        RedirectView.as_view(url=reverse_lazy("donate")),
    ),
    path(
        "about/support-us/",
        RedirectView.as_view(url=reverse_lazy("donate")),
    ),
    path(
        "about/impact/",
        RedirectView.as_view(url=reverse_lazy("impact")),
    ),
    path(
        "data_apis/index/",
        RedirectView.as_view(url=reverse_lazy("voter_information_api")),
    ),
    path(
        "impact/",
        RedirectView.as_view(url=reverse_lazy("impact")),
    ),
)

urlpatterns += url_redirects


if settings.DEBUG:
    from dc_utils.urls import dc_utils_testing_patterns

    urlpatterns += dc_utils_testing_patterns
