from django.conf.urls import url
from django.views.generic import TemplateView

app_name = "report_2021"

urlpatterns = [
    url(
        r"^$",
        TemplateView.as_view(template_name="report_2021/report.html"),
        name="report_2021",
    )
]
