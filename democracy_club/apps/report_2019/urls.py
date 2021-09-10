from django.conf.urls import url
from core.report_helpers.views import MarkdownFileView

app_name = "report_2019"

urlpatterns = [
    url(
        r"^$",
        MarkdownFileView.as_view(markdown_file="apps/report_2019/report.md"),
        name="report_2019",
    )
]
