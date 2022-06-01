import pytest
from dc_utils.tests.helpers import validate_html
from django.urls import reverse


class TestHtml:
    @pytest.fixture
    def urls(self):
        return [
            reverse("home"),
            reverse("about"),
            reverse("jobs"),
            reverse("team"),
            reverse("coc"),
            reverse("contact"),
            reverse("privacy"),
            reverse("dc_signup_form:mailing_list_signup_view"),
            reverse("projects:home"),
            reverse("projects:cvs"),
            reverse("projects:election_leaflets"),
            reverse("projects:candidates"),
            reverse("projects:data"),
            reverse("projects:election_widget"),
            reverse("projects:past"),
            reverse("projects:polling_one_pager"),
            reverse("projects:polling_embed_code"),
            reverse("projects:polling_data_upload"),
            reverse("projects:reports"),
            reverse("projects:reports_registers"),
            reverse("report_2016:report_2016"),
            reverse("report_2017:report_2017"),
            reverse("report_2018:report_2018"),
            reverse("report_2019:report_2019"),
            reverse(
                "report_2019_general_election:report_2019_general_election"
            ),
            reverse("report_2021:report_2021"),
            reverse("report_whos_missing:report_whos_missing"),
            reverse("wheredoivote_user_feedback:wheredoivote_user_feedback"),
            reverse(
                "wheredoivote_user_feedback:wheredoivote_user_feedback_2017"
            ),
            reverse(
                "wheredoivote_user_feedback:wheredoivote_user_feedback_2018"
            ),
            reverse("projects:every_election"),
        ]

    @pytest.mark.django_db
    def test_html_valid(self, client, subtests, urls):
        for url in urls:
            with subtests.test(msg=url):
                assert client.get(url).status_code == 200
                _, errors = validate_html(client, url)
                assert errors == ""

    @pytest.mark.django_db
    def test_page_title(self, client, urls):
        """test every page has a page title in the
        block title tag"""
        for url in urls:
            response = client.get(url)
            assert "<title>" in response.content.decode("utf-8")
            assert "</title>" in response.content.decode("utf-8")

    def test_report_page_title(self, client):
        """test report page has a page title in the
        block title tag that is equal to the report title"""
        response = client.get("/report_2016/")
        assert (
            "<title>Towards better elections | Democracy Club</title>"
            in response.content.decode("utf-8")
        )
        assert (
            "<title> | Democracy Club</title>"
            not in response.content.decode("utf-8")
        )
