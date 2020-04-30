from django.urls import path

from .views import DonateFormView, DonateThanksView, ProcessDonationView

app_name = "donations"

urlpatterns = [
    path("thanks", DonateThanksView.as_view(), name="donate_thanks"),
    path("process", ProcessDonationView.as_view(), name="donate_process"),
    path("", DonateFormView.as_view(), name="donate"),
]
