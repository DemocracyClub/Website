from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView, TemplateView

urlpatterns = [
    url(
        r"^$",
        TemplateView.as_view(template_name="projects/projects_home.html"),
        name="projects",
    ),
    url(
        r"^projects/polling-stations/$",
        TemplateView.as_view(
            template_name="projects/polling-stations/home.html"
        ),
        name="polling_one_pager",
    ),
    url(
        r"^projects/polling-stations/technical/$",
        RedirectView.as_view(url=reverse_lazy("polling_data_upload")),
        name="polling_technical_explainer",
    ),
    url(
        r"^projects/polling-stations/faqs/$",
        RedirectView.as_view(url=reverse_lazy("polling_one_pager")),
        name="polling_faqs",
    ),
    url(
        r"^projects/polling-stations/embed/$",
        TemplateView.as_view(
            template_name="projects/polling-stations/embed_code.html"
        ),
        name="polling_embed_code",
    ),
    url(
        r"^projects/polling-stations/upload/$",
        TemplateView.as_view(
            template_name="projects/polling-stations/upload_data.html"
        ),
        name="polling_data_upload",
    ),
    url(
        r"^projects/polling-stations/techincal/$",
        RedirectView.as_view(url=reverse_lazy("polling_technical_explainer")),
    ),
    url(
        r"^projects/election-ids/reference/$",
        RedirectView.as_view(
            url="https://elections.democracyclub.org.uk/reference_definition"
        ),
        name="election_ids_reference",
    ),
    url(
        r"^projects/election-ids/$",
        TemplateView.as_view(template_name="projects/election-ids/home.html"),
        name="election_ids",
    ),
]
