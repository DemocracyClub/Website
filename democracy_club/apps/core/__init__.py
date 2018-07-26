import storages
from django.apps import apps
from django.core.checks import Error, register

@register()
def check_django_storage_version(app_configs, **kwargs):
    errors = []
    if (app_configs is None or apps.get_app_config('core') in app_configs):
        if storages.__version__ != '1.6.5':
            errors.append(
                Error(
                    'django-storages must be at version 1.6.5',
                    hint='See https://github.com/DemocracyClub/Website/pull/117',
                    obj='core',
                    id='core.E001'
                )
            )
    return errors
