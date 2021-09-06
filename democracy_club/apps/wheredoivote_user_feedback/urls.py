from django.urls import re_path
from django.views.generic import TemplateView

app_name = "report_wheredoivote_user_feedback"

urlpatterns = [
    # TODO: once we've got a research/reports list view
    # map this URL to there
    re_path(
        r"^$",
        TemplateView.as_view(
            template_name="wheredoivote_user_feedback/report2017.html"
        ),
        name="wheredoivote_user_feedback",
    ),
    re_path(
        r"^2017/$",
        TemplateView.as_view(
            template_name="wheredoivote_user_feedback/report2017.html"
        ),
        name="wheredoivote_user_feedback_2017",
    ),
    re_path(
        r"^2018/$",
        TemplateView.as_view(
            template_name="wheredoivote_user_feedback/report2018.html"
        ),
        name="wheredoivote_user_feedback_2018",
    ),
]
