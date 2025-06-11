import json

from core.cloudfront import invalidate_paths
from django.core.management import BaseCommand
from django.core.management.base import CommandError


class Command(BaseCommand):
    def add_arguments(self, parser):
        super().add_arguments(parser)

        parser.add_argument(
            "--paths", dest="paths", help="URL paths to invalidate", type=list
        )

    def handle(self, *args, **options):
        resp = invalidate_paths(options["paths"])
        if resp["ResponseMetadata"]["HTTPStatusCode"] != 201:
            raise CommandError(f"Invalidation failed: {json.dumps(resp)}")
