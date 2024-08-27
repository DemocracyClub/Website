from core.report_helpers.views import MarkdownFileView
from django.urls import path

app_name = "reports"

urlpatterns = [
    path(
        "report_2016/",
        MarkdownFileView.as_view(markdown_file="apps/reports/report_2016.md"),
        name="report_2016",
    ),
    path(
        r"report_2017/",
        MarkdownFileView.as_view(markdown_file="apps/reports/report_2017.md"),
        name="report_2017",
    ),
    path(
        r"report_2018/",
        MarkdownFileView.as_view(markdown_file="apps/reports/report_2018.md"),
        name="report_2018",
    ),
    path(
        r"report_2019/",
        MarkdownFileView.as_view(markdown_file="apps/reports/report_2019.md"),
        name="report_2019",
    ),
    path(
        r"report_2019_general_election/",
        MarkdownFileView.as_view(
            markdown_file="apps/reports/report_2019_general_election.md"
        ),
        name="report_2019_general_election",
    ),
    path(
        r"report_2021/",
        MarkdownFileView.as_view(markdown_file="apps/reports/report_2021.md"),
        name="report_2021",
    ),
    path(
        r"report_2022/",
        MarkdownFileView.as_view(markdown_file="apps/reports/report_2022.md"),
        name="report_2022",
    ),
    path(
        r"report_2023/",
        MarkdownFileView.as_view(markdown_file="apps/reports/report_2023.md"),
        name="report_2023",
    ),
    path(
        r"report_2024/",
        MarkdownFileView.as_view(markdown_file="apps/reports/report_2024.md"),
        name="report_2024",
    ),
    path(
        r"reports/whos_missing/",
        MarkdownFileView.as_view(
            markdown_file="apps/reports/report_whos_missing.md"
        ),
        name="report_whos_missing",
    ),
    path(
        "projects/reports/registers/",
        MarkdownFileView.as_view(
            markdown_file="apps/reports/report_odi_registers.md"
        ),
        name="reports_registers",
    ),
]
