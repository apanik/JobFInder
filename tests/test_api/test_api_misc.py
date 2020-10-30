import unittest

from tests.config_api import MAIN_URL
from tests.test_api.common import *

TOGGLE_FAVOURITE_URL = f'{MAIN_URL}/api/job/favourite/toggle'
GET_ALL_APPLICANTS_URL = f'{MAIN_URL}/api/application/list/'
GET_SHORTLIST_APPLICANTS_URL = f'{MAIN_URL}/api/application/shortlist/'
TRENDING_KEYWORDS_SAVE_URL = f'{MAIN_URL}/api/job/trending_keywords/save/'
JOB_ID = "0711248315e942adbf1c75fa9c64ad66"


class TestToggleFavourite(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']
        self.saved = "Saved"
        self.removed = "Removed"

    def test__when_valid__should__pass(self):
        # With Same data this test case once passed and every second time it failed
        json = {
            'job_id': JOB_ID,
            'status': self.saved
        }
        resp = requests.post(TOGGLE_FAVOURITE_URL, json=json,
                             headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)

    def test__when_status_saved__should_pass(self):
        # With Same data this test case once passed and every second time it failed
        json = {
            'job_id': JOB_ID,
            'status': self.saved
        }
        resp = requests.post(TOGGLE_FAVOURITE_URL, json=json,
                             headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)

    def test__when_status_removed__should_pass(self):
        # With Same data this test case once passed and every second time it failed
        json = {
            'job_id': JOB_ID,
            'status': self.removed
        }
        resp = requests.post(TOGGLE_FAVOURITE_URL, json=json,
                             headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        status = data['code']
        self.assertEqual(status, 200)
        self.assertEqual(resp.status_code, 200)

    def test__when_post_status_as_saved__should_return_response_as_removed(self):
        # With Same data this test case once passed and every second time it failed
        json = {
            'job_id': JOB_ID,
            'status': self.saved
        }
        resp = requests.post(TOGGLE_FAVOURITE_URL, json=json,
                             headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        status = data['code']
        self.assertEqual(status, 200)
        self.assertEqual(resp.status_code, 200)

    def test__when_post_status_as_removed__should_pass(self):
        # With Same data this test case once passed and every second time it failed
        json = {
            'job_id': JOB_ID,
            'status': self.removed
        }
        resp = requests.post(TOGGLE_FAVOURITE_URL, json=json,
                             headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        status = data['code']
        self.assertEqual(status, 200)
        self.assertEqual(resp.status_code, 200)

    def test__when_job_id_is_invalid__should_failed(self):
        json = {
            'job_id': "04855d6f3ace4dab9ffa291415fcb01x",
            'status': self.removed
        }
        resp = requests.post(TOGGLE_FAVOURITE_URL, json=json,
                             headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 500)

    def test__when_job_id_empty__should_failed(self):
        json = {
            'job_id': "",
            'status': self.removed
        }
        resp = requests.post(TOGGLE_FAVOURITE_URL, json=json,
                             headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 500)

    def test__when_job_id_blank__should_failed(self):
        json = {
            'status': self.removed
        }
        resp = requests.post(TOGGLE_FAVOURITE_URL, json=json,
                             headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 500)

    def test__when_status_is_invalid_should_pass(self):
        json = {
            'job_id': JOB_ID,
            'status': "none"
        }
        resp = requests.post(TOGGLE_FAVOURITE_URL, json=json,
                             headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        status = data['code']
        self.assertEqual(status, 200)
        self.assertEqual(resp.status_code, 200)

    def test__when_status_is_empty_should_pass(self):
        # With Same data this test case once passed and every second time it failed
        json = {
            'job_id': JOB_ID,
        }
        resp = requests.post(TOGGLE_FAVOURITE_URL, json=json,
                             headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)

    def test__when_valid_job_id__status_null_should_pass(self):
        # With Same data this test case once passed and every second time it failed
        json = {
            'job_id': JOB_ID
        }
        resp = requests.post(TOGGLE_FAVOURITE_URL, json=json,
                             headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        self.assertEqual(data['code'], 200)
        self.assertEqual(resp.status_code, 200)

    def test__when_job_id_and_status_is_empty_should_failed(self):
        json = {
            'job_id': "",
            'status': ""
        }
        resp = requests.post(TOGGLE_FAVOURITE_URL, json=json,
                             headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 500)

    def test__when_job_id_and_status_both_invalid_should_failed(self):
        json = {
            'job_id': "04855d6f3ace4dab9ffa291415fcb01d",
            'status': "None"
        }
        resp = requests.post(TOGGLE_FAVOURITE_URL, json=json,
                             headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 500)

    def test__when_job_id_and_status_both_null__should_failed(self):
        json = {

        }
        resp = requests.post(TOGGLE_FAVOURITE_URL, json=json,
                             headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        self.assertEqual(str(data), "{}")
        self.assertEqual(resp.status_code, 200)


    def test__when_access_token_in_none_or_invalid_should_failed(self):
        json = {

        }
        resp = requests.post(TOGGLE_FAVOURITE_URL, json=json, )
        self.assertEqual(resp.status_code, 401)


class TestAllApplicants(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__when_valid__should_pass(self):
        resp = requests.get(GET_ALL_APPLICANTS_URL + JOB_ID, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)

    def test__when_job_id_invalid__should_failed(self):
        INVALID_JOB_ID = "04855d6f3ace4dab9ffa291415fcb01x"
        resp = requests.get(GET_ALL_APPLICANTS_URL + INVALID_JOB_ID,
                            headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 500)

    def test__when_access_token_none__should_failed(self):
        resp = requests.get(GET_ALL_APPLICANTS_URL + JOB_ID, )
        self.assertEqual(resp.status_code, 401)

    def test__when_Job_id_empty_none__should_failed(self):
        JOB_ID = ""
        resp = requests.get(GET_ALL_APPLICANTS_URL + JOB_ID, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 404)

    def test__when_Job_id_blank__should_failed(self):
        resp = requests.get(GET_ALL_APPLICANTS_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 404)


class TestShortlistApplicants(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__when_valid__should_pass(self):
        resp = requests.get(GET_SHORTLIST_APPLICANTS_URL + JOB_ID,
                            headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)

    def test__when_job_id_invalid__should_failed(self):
        INVALID_JOB_ID = "04855d6f3ace4dab9ffa291415fcb01x"
        resp = requests.get(GET_SHORTLIST_APPLICANTS_URL + INVALID_JOB_ID,
                            headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 500)

    def test__when_access_token_none__should_failed(self):
        resp = requests.get(GET_SHORTLIST_APPLICANTS_URL + JOB_ID, )
        self.assertEqual(resp.status_code, 401)

    def test__when_Job_id_empty_none__should_failed(self):
        JOB_ID = ""
        resp = requests.get(GET_SHORTLIST_APPLICANTS_URL + JOB_ID,
                            headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 404)

    def test__when_Job_id_blank__should_failed(self):
        resp = requests.get(GET_SHORTLIST_APPLICANTS_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 404)


class TestTrendingKeywordsSave(unittest.TestCase):
    def test__when_valid__user_agent_and_keyword__should_pass(self):
        json = {
           'keyword':'AWS'
        }
        resp = requests.post(TRENDING_KEYWORDS_SAVE_URL, headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}, json=json)
        self.assertEqual(resp.status_code, 200)


if __name__ == '__main__':
    unittest.main()
