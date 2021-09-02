import pytest
from django.urls import reverse

urls_to_check = [
    "home",
    "about",
    "jobs",
    "team",
    "coc",
    "contact",
    "privacy",
    "dc_signup_form:mailing_list_signup_view",
    "projects:home",
    "projects:cvs",
    "projects:election_leaflets",
    "projects:candidates",
    "projects:data",
    "projects:election_widget",
    "projects:past",
    "projects:polling_one_pager",
    "projects:polling_embed_code",
    "projects:polling_data_upload",
    "projects:reports",
    "projects:reports_registers",
    "report_2016:report_2016",
    "report_2017:report_2017",
    "report_2018:report_2018",
    "report_2019:report_2019",
    "report_2019_general_election:report_2019_general_election",
    "report_2021:report_2021",
    "report_whos_missing:report_whos_missing",
    "wheredoivote_user_feedback:wheredoivote_user_feedback",
    "wheredoivote_user_feedback:wheredoivote_user_feedback_2017",
    "wheredoivote_user_feedback:wheredoivote_user_feedback_2018",
]


@pytest.mark.django_db
@pytest.mark.parametrize("url", urls_to_check)
def test_eval(client, url, subtests):
    assert client.get(reverse(url)).status_code == 200

    # with subtests.test(msg=url):
    #     _, errors = validate_html(client, reverse(url))
    #     if errors:
    #         print(url, errors)
    #     assert errors == ""
