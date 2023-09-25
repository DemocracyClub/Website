from dc_signup_form.forms import MailingListSignupForm
from dc_signup_form.views import SignupFormView
from django.conf import settings
from django.urls import include, re_path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    re_path(
        r"^signup/$",
        csrf_exempt(
            SignupFormView.as_view(
                template_name="base.html",
                form_class=MailingListSignupForm,
                backend=settings.EMAIL_SIGNUP_BACKEND,
                backend_kwargs=settings.EMAIL_SIGNUP_BACKEND_KWARGS,
            )
        ),
        name="mailing_list_signup_view",
    ),
    re_path(r"^api_signup/v1/", include("dc_signup_form.signup_server.urls")),
]
