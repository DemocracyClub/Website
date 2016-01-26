from django.contrib.gis import admin

from .models import (Authority, AuthorityGeo,
                     AuthorityServiceCategory, AuthorityServiceDetails)

class AuthorityGeoInline(admin.StackedInline):
    model = AuthorityGeo
    def has_delete_permission(self, request, obj=None):
            return False


class AuthorityAdmin(admin.OSMGeoAdmin):
    exclude = ('authority_geo',)
    inlines = (AuthorityGeoInline,)

class AuthorityServiceDetailsAdmin(admin.OSMGeoAdmin):
    list_filter = [
        'LGSL',
    ]

admin.site.register(Authority, AuthorityAdmin)
admin.site.register(AuthorityGeo)
admin.site.register(AuthorityServiceCategory)
admin.site.register(AuthorityServiceDetails, AuthorityServiceDetailsAdmin)
