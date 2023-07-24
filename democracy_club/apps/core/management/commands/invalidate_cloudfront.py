from core.cloudfront import invalidate_paths
from django.core.management import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        super().add_arguments(parser)

        parser.add_argument(
            "--paths", dest="paths", help="URL paths to invalidate", type=list
        )

    def handle(self, *args, **options):
        return invalidate_paths(options["paths"])
