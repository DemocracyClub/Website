from django.views.generic import TemplateView


class DonateFormView(TemplateView):
    template_name = "donate.html"
