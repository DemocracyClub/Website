import json

from django.views.generic import View
from django.http import HttpResponse
from django.db.models import Count

from .models import Answer

class StatsView(View):
    def get(self, request):
        data = {}

        data['number_of_answers'] = Answer.objects\
                    .order_by().values_list('answer_set').distinct().count()

        q = "Did the information on this site make you feel more informed?"
        data['more_informed'] = {
            'question': q,
        }
        data['more_informed']['yes'] = Answer.objects\
            .filter(question=q, answer="Yes").count()
        data['more_informed']['no'] = Answer.objects\
            .filter(question=q, answer="No").count()

        q = "Do you plan to vote?"
        data['plan_to_vote'] = {
            'question': q,
        }
        data['plan_to_vote']['yes'] = Answer.objects\
            .filter(question=q, answer="Yes").count()
        data['plan_to_vote']['no'] = Answer.objects\
            .filter(question=q, answer="No").count()

        q = "Having used this website, how do you feel about your own power over candidates or parties?"
        data['power_over_candidates'] = {
            'question': q,
        }
        data['power_over_candidates']['more'] = Answer.objects\
            .filter(question=q, answer="More powerful").count()
        data['power_over_candidates']['same'] = Answer.objects\
            .filter(question=q, answer="About the same").count()
        data['power_over_candidates']['less'] = Answer.objects\
            .filter(question=q, answer="Less powerful").count()

        q = "What is your age?"
        data['age'] = {
            'question': q,
        }
        data['age'] = dict(Answer.objects\
            .filter(question=q)\
            .values_list('answer',)\
            .annotate(count=Count('id'))\
            .order_by())

        return HttpResponse(json.dumps(data), content_type='application/json')