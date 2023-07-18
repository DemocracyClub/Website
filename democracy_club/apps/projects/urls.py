from django.urls import path
from django.urls import reverse_lazy
from django.views.generic import RedirectView, TemplateView
from core.report_helpers.views import MarkdownFileView

app_name = "projects"

urlpatterns = [
    path(
        "",
        TemplateView.as_view(template_name="projects/projects_home.html"),
        name="home",
    ),
    path(
        "past/",
        TemplateView.as_view(template_name="projects/past.html"),
        name="past",
    ),
    path(
        "reports/",
        TemplateView.as_view(template_name="projects/reports_home.html"),
        name="reports",
    ),
    path(
        "polling-stations/",
        TemplateView.as_view(
            template_name="projects/polling-stations/home.html"
        ),
        name="polling_one_pager",
    ),
    path(
        "polling-stations/technical/",
        RedirectView.as_view(url=reverse_lazy("projects:polling_data_upload")),
        name="polling_technical_explainer",
    ),
    path(
        "projects/polling-stations/faqs/",
        RedirectView.as_view(url=reverse_lazy("projects:polling_one_pager")),
        name="polling_faqs",
    ),
    path(
        "polling-stations/embed/",
        TemplateView.as_view(
            template_name="projects/polling-stations/embed_code.html"
        ),
        name="polling_embed_code",
    ),
    path(
        "polling-stations/upload/",
        TemplateView.as_view(
            template_name="projects/polling-stations/upload_data.html"
        ),
        name="polling_data_upload",
    ),
    path(
        "election-ids/reference/",
        RedirectView.as_view(
            url="https://elections.democracyclub.org.uk/reference_definition"
        ),
        name="election_ids_reference",
    ),
    path(
        "election-ids/",
        RedirectView.as_view(url=reverse_lazy("projects:every_election")),
        name="election_ids",
    ),
    path(
        "every-election/",
        TemplateView.as_view(template_name="projects/every_election.html"),
        name="every_election",
    ),
    path(
        "election-ids/",
        RedirectView.as_view(url=reverse_lazy("projects:every_election")),
        name="election_ids",
    ),
    path(
        "who-can-i-vote-for/",
        RedirectView.as_view(url=reverse_lazy("projects:candidates")),
        name="whocanivotefor",
    ),
    path(
        "election-widget/",
        TemplateView.as_view(template_name="projects/election-widget.html"),
        name="election_widget",
    ),
    path(
        "candidates-wiki/",
        TemplateView.as_view(template_name="projects/candidates.html"),
        name="candidates",
    ),
    path(
        "data/",
        TemplateView.as_view(template_name="projects/data.html"),
        name="data",
    ),
    path(
        "election-leaflets/",
        TemplateView.as_view(template_name="projects/electionleaflets.html"),
        name="election_leaflets",
    ),
    path(
        "csv/",
        TemplateView.as_view(template_name="projects/cvs.html"),
        name="cvs",
    ),
    path(
        "representatives/",
        TemplateView.as_view(template_name="projects/representatives.html"),
        name="representatives",
    ),
]
