from django.urls import include, re_path
from django.views.decorators.csrf import csrf_exempt


from dc_signup_form.forms import MailingListSignupForm
from dc_signup_form.views import SignupFormView

urlpatterns = [
    re_path(
        r"^signup/$",
        csrf_exempt(
            SignupFormView.as_view(
                template_name="base.html",
                form_class=MailingListSignupForm,
                backend="local_db",
            )
        ),
        name="mailing_list_signup_view",
    ),
    re_path(r"^api_signup/v1/", include("dc_signup_form.signup_server.urls")),
]
