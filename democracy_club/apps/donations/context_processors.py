from .forms import DonationForm


def donation_form(request):
    return {
        'donation_form': DonationForm(initial={
            'source_url': request.path
        })
}