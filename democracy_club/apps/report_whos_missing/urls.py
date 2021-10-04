from django.urls import re_path

from core.report_helpers.views import MarkdownFileView

app_name = "report_whos_missing"


urlpatterns = [re_path(r"^$", ReportView.as_view(), name="report_whos_missing")]
