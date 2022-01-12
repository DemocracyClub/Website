import datetime
from django.conf import settings


def days_to_election(request):
    end_timestamp = 1430959200
    end_date = datetime.datetime.fromtimestamp(end_timestamp)
    if datetime.datetime.now() < end_date:
        delta = end_date - datetime.datetime.now()
        days = delta.days

        return {"days_to_election": days + 1}
    else:
        return {}


def canonical_url(request):
    return {"CANONICAL_URL": f"{request.scheme}://{request.get_host()}"}


def site_title(request):
    return {"SITE_TITLE": settings.SITE_TITLE}
