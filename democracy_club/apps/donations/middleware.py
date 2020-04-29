import re
from django.http import HttpResponseRedirect

from .forms import DonationForm
from .helpers import GoCardlessHelper, PAYMENT_UNITS


class DonationFormMiddleware(object):
    def get_initial(self, request):
        form_initial = {
            "payment_type": "subscription",
        }
        default_donation = 3
        suggested_donation = request.GET.get(
            "suggested_donation", default_donation
        )
        if re.search("[^0-9]", str(suggested_donation)):
            suggested_donation = default_donation

        if int(suggested_donation) in [x[0] for x in PAYMENT_UNITS]:
            form_initial["amount"] = suggested_donation
        else:
            form_initial["other_amount"] = suggested_donation

        return form_initial

    def form_valid(self, request, form):
        # Add the form info to the session
        request.session["donation_form"] = form.cleaned_data

        # Start the GoCardless process
        gc = GoCardlessHelper(request)

        # Make a customer object at GC's site first.
        redirect_url = gc.get_redirect_url()

        # Redirect to GoCardless
        return HttpResponseRedirect(redirect_url)

    def process_request(self, request):
        form_prefix = "donation_form"
        key_to_check = "{}-amount".format(form_prefix)

        if request.method == "POST" and key_to_check in request.POST:
            form = DonationForm(data=request.POST, prefix=form_prefix)
            if form.is_valid():
                return self.form_valid(request, form)
        else:
            form = DonationForm(
                initial=self.get_initial(request), prefix=form_prefix
            )
        request.donation_form = form
