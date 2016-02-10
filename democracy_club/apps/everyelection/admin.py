from django.contrib import admin

from .models import (AuthorityElection, AuthorityElectionPosition,
                     AuthorityElectionSkipped)

class AuthorityElectionSkippedAdmin(admin.ModelAdmin):
    list_display = ('authority_election', 'user', 'notes')

admin.site.register(AuthorityElection)
admin.site.register(AuthorityElectionPosition)
admin.site.register(AuthorityElectionSkipped, AuthorityElectionSkippedAdmin)
