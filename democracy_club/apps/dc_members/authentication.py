from django.contrib.auth.models import User

from .models import Member

class MemberTokenBackend(object):
    def authenticate(self, token):

        try:
            member = Member.objects.get(token=token)
        except Member.DoesNotExist:
            return None
        return member.user

    def get_user(self, user_id):
           try:
              return User.objects.get(pk=user_id)
           except User.DoesNotExist:
              return None