import datetime

def days_to_election(request):
    end_timestamp = 1430956800
    end_date = datetime.datetime.fromtimestamp(end_timestamp)
    if datetime.datetime.now() < end_date:
        delta = end_date - datetime.datetime.now()
        days = delta.days

        return {
            'days_to_election': days+1
        }
    else:
        return {}