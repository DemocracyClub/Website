from django.views.generic import TemplateView

from .helpers import GoCardlessHelper


class DonateFormView(TemplateView):
    template_name = "donate.html"


class DonateThanksView(TemplateView):

    def get(self, request, *args, **kwargs):
        resource_uri = request.GET.get('resource_uri')
        resource_id = request.GET.get('resource_id')
        resource_type = request.GET.get('resource_type')
        if resource_id and resource_type and resource_uri:
            GoCardlessHelper().confirm_payment(
                resource_uri,
                resource_id,
                resource_type
            )
        return super(DonateThanksView, self).get(request, *args, **kwargs)


    template_name = "donate_thanks.html"
