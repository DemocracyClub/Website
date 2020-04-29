from django.views.generic import TemplateView, RedirectView
from django.urls import reverse

from .helpers import GoCardlessHelper


class DonateFormView(TemplateView):
    template_name = "donate.html"


class ProcessDonationView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        redirect_flow_id = self.request.GET.get("redirect_flow_id")
        if redirect_flow_id:
            gc = GoCardlessHelper(self.request)
            gc.confirm_redirect_flow()
            gc.create_payment()
        return reverse("donations:donate_thanks")


class DonateThanksView(TemplateView):
    template_name = "donate_thanks.html"
