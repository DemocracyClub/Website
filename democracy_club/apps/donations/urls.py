from django.conf.urls import url

from .views import DonateFormView, DonateThanksView, ProcessDonationView

urlpatterns = [
    url(r"thanks", DonateThanksView.as_view(), name="donate_thanks"),
    url(r"process", ProcessDonationView.as_view(), name="donate_process"),
    url(r"", DonateFormView.as_view(), name="donate"),
]
