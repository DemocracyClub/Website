import os

from django.core.management.base import BaseCommand

from report_2016 import graphs


class Command(BaseCommand):
    def handle(self, **options):
        includes_path = os.path.join(
            os.path.dirname(graphs.__file__),
            'templates',
            'report_2016',
            'includes',
        )

        for graph in graphs.GRAPHS:
            include_name = os.path.join(
                includes_path,
                "_{}_graph.html".format(graph.name)
            )
            html = graph().html
            with open(include_name, 'w') as include_file:
                include_file.write(html)
