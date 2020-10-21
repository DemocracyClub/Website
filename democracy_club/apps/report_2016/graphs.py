from datetime import datetime
from collections import defaultdict
import csv
import os

from plotly.offline import plot as plotly_plot
from plotly.graph_objs import Scatter


class BaseGraph(object):
    def __init__(self):
        self.reports_root = os.path.dirname(__file__)
        self.make_figure_or_data()
        self.html = self.plot()

    def plot(self):
        return plotly_plot(
            self.figure_or_data,
            show_link=False,
            output_type="div",
            include_plotlyjs=False,
        )


class TestGraph(BaseGraph):
    name = "test"

    def make_figure_or_data(self):
        self.figure_or_data = [
            Scatter(x=[1, 2, 3, 5, 6, 7], y=[3, 1, 6, 3, 23, 23, 2, 12])
        ]


class YNREditsOverTimeGraph(BaseGraph):
    name = "ynr_edits_over_time"

    def make_figure_or_data(self):
        interesting_days = {
            "2016-04-08": "SOPNs out",
            "2016-04-09": "Crowd sourcing party",
            "2016-05-06": "Results coming in overnight",
        }
        data_file = os.path.join(
            self.reports_root,
            "data",
            "logged_actions.csv",
        )
        data = defaultdict(int)
        for line in csv.reader(open(data_file)):
            if line[1].startswith("2016-04") or line[1].startswith("2016-05"):
                day = line[1].split(" ")[0]
                data[day] += 1

        grouped_list = []
        for day, count in data.items():
            label = interesting_days.get(day, None)
            grouped_list.append((day, count, label))
        grouped_list = sorted(grouped_list, key=lambda day: day[0])

        self.figure_or_data = [
            Scatter(
                x=[x[0] for x in grouped_list],
                y=[x[1] for x in grouped_list],
                name="Edits to Democracy Club candidates over 2016",
                text=[x[2] for x in grouped_list],
                mode="lines+markers+text",
                textposition="top",
            )
        ]


class YNRPagesOverTime(BaseGraph):
    name = "ynr_page_views_over_time"

    def make_figure_or_data(self):
        def _parse_date(date):
            return datetime.strptime(date, "%d/%b/%Y")

        interesting_days = {
            _parse_date("5/May/2016"): "Election day",
            _parse_date("6/May/2016"): "Results & Telegraph embedded map",
        }

        data_file = os.path.join(
            self.reports_root,
            "data",
            "ynr_pages_over_time.log",
        )
        data = defaultdict(int)
        for line in csv.reader(open(data_file)):
            date = _parse_date(line[0].split(":")[0])
            data[date] += 1

        grouped_list = []
        for day, count in data.items():
            label = interesting_days.get(day, None)
            grouped_list.append((day, count, label))
        grouped_list = sorted(grouped_list, key=lambda day: day[0])

        self.figure_or_data = [
            Scatter(
                x=[x[0] for x in grouped_list],
                y=[x[1] for x in grouped_list],
                name="Edits to Democracy Club candidates over 2016",
                text=[x[2] for x in grouped_list],
                mode="lines+markers+text",
                textposition="top",
            )
        ]


GRAPHS = [
    # TestGraph,
    # YNREditsOverTimeGraph
    YNRPagesOverTime
]
