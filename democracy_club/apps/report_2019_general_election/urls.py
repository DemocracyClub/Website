from django.urls import re_path
from core.report_helpers.views import MarkdownFileView

app_name = "report_2019_general_election"

urlpatterns = [
    re_path(
        r"^$",
        MarkdownFileView.as_view(
            markdown_file="apps/report_2019_general_election/report.md"
        ),
        name="report_2019_general_election",
    )
]
