from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$',
        TemplateView.as_view(template_name="report_2016/report.html"),
        name="report_2016")

]
