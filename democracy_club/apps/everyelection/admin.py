from django.contrib import admin

from .models import AuthorityElection, AuthorityElectionPosition


admin.site.register(AuthorityElection)
admin.site.register(AuthorityElectionPosition)
