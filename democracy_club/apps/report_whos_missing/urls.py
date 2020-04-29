from django.conf.urls import url

from .views import ReportView

urlpatterns = [url(r"^$", ReportView.as_view(), name="report_whos_missing")]
