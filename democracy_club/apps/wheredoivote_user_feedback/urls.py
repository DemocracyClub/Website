from core.report_helpers.views import MarkdownFileView
from django.urls import re_path

app_name = "report_wheredoivote_user_feedback"

urlpatterns = [
    # TODO: once we've got a research/reports list view
    # map this URL to there
    re_path(
        r"^$",
        MarkdownFileView.as_view(
            markdown_file="apps/wheredoivote_user_feedback/templates/wheredoivote_user_feedback/report2017.md"
        ),
        name="wheredoivote_user_feedback",
    ),
    re_path(
        r"^2017/$",
        MarkdownFileView.as_view(
            markdown_file="apps/wheredoivote_user_feedback/templates/wheredoivote_user_feedback/report2017.md"
        ),
        name="wheredoivote_user_feedback_2017",
    ),
    re_path(
        r"^2018/$",
        MarkdownFileView.as_view(
            markdown_file="apps/wheredoivote_user_feedback/templates/wheredoivote_user_feedback/report2018.md"
        ),
        name="wheredoivote_user_feedback_2018",
    ),
]
