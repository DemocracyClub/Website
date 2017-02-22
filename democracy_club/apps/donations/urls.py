from django.conf.urls import url, include

from .views import DonateFormView

urlpatterns = [
    url(r'', DonateFormView.as_view(), name="donate"),
]
