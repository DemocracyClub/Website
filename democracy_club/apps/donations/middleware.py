from django.http import HttpResponseRedirect

from .forms import DonationForm
from .helpers import GoCardlessHelper


class DonationFormMiddleware(object):
    def get_initial(self):
        return {
            'payment_type': 'subscription',
            'amount': 10,
        }

    def form_valid(self, request, form):
        # Add the form info to the session
        request.session['donation_form'] = form.cleaned_data

        # Start the GoCardless process
        gc = GoCardlessHelper(request)

        # Make a customer object at GC's site first.
        redirect_url = gc.get_redirect_url()

        # Redirect to GoCardless
        return HttpResponseRedirect(redirect_url)

    def process_request(self, request):
        form_prefix = "donation_form"
        key_to_check = "{}-amount".format(form_prefix)

        if request.method == 'POST' and key_to_check in request.POST:
            form = DonationForm(data=request.POST, prefix=form_prefix)
            if form.is_valid():
                return self.form_valid(request, form)
        else:
            form = DonationForm(
                initial=self.get_initial(), prefix=form_prefix)
        request.donation_form = form
