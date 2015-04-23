from django.views.generic import FormView

from .forms import DonationForm
from .helpers import GoCardlessHelper

class DonateFormView(FormView):
    form_class = DonationForm
    template_name = "donate.html"

    def get_initial(self):
        return {
            'payment_type': 'bill',
            'amount': '10',
            'payment_interval': 'once',
        }

    def form_valid(self, form):
        gc = GoCardlessHelper()
        self.success_url =  gc.get_payment_url(**form.cleaned_data)
        return super(DonateFormView, self).form_valid(form)
