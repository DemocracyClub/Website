from django.urls import re_path
from django.views.generic import TemplateView

app_name = "report_2019_general_election"

urlpatterns = [
    re_path(
        r"^$",
        TemplateView.as_view(
            template_name="report_2019_general_election/report.html"
        ),
        name="report_2019_general_election",
    )
]
