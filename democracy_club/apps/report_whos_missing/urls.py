from django.conf.urls import url

from .views import ReportView

app_name = "report_whos_missing"


urlpatterns = [url(r"^$", ReportView.as_view(), name="report_whos_missing")]
