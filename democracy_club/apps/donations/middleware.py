from django.http import HttpResponseRedirect

from .forms import DonationForm
from .helpers import GoCardlessHelper


class DonationFormMiddleware(object):
    def get_initial(self):
        return {
            'payment_type': 'bill',
            'amount': '3',
            'payment_interval': 'monthly',
        }

    def form_valid(self, form):
        gc = GoCardlessHelper()
        url = gc.get_payment_url(**form.cleaned_data)
        return HttpResponseRedirect(url)

    def process_request(self, request):
        form_prefix = "donation_form"
        key_to_check = "{}-amount".format(form_prefix)

        if request.method == 'POST' and key_to_check in request.POST:
            form = DonationForm(data=request.POST, prefix=form_prefix)
            if form.is_valid():
                return self.form_valid(form)
        else:
            form = DonationForm(
                initial=self.get_initial(), prefix=form_prefix)
        request.donation_form = form
