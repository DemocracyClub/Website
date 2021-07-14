from dc_utils.tests import validate_html
from django.urls import reverse

urls = (
    "/",
    "/about/",
    "/about/index",
    "/about/jobs",
    "/about/funding",
    "/about/team",
    "/privacy",
    "code-of-conduct/",
    "projects/",
    "contact/",
    "/admin",
    "/feedback",
    "blog/",
    "report_2016/",
    "report_2017/",
    "report_2018/",
    "report_2019/",
    "report_2019_general_election/",
    "report_2021/",
    "reports/whos_missing/",
    "wheredoivote_user_feedback/",
    "data/",
)


@pytest.mark.parametrize("url", urls)
def test_urls(url):
    assert validate_html(url)
