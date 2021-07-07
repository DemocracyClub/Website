from django.conf.urls import url
from django.views.generic import TemplateView

from core.report_helpers.views import MarkdownFileView

app_name = "report_2021"

urlpatterns = [
    url(
        r"^$",
        MarkdownFileView.as_view(markdown_file="apps/report_2021/report.md"),
        name="report_2021",
    )
]
