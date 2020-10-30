import unittest

import requests

from tests.config_api import MAIN_URL
from tests.test_api.common import signin_as_pro

PRO_SKILL_JOB_CHART_URL = f'{MAIN_URL}/api/pro/dashboard/skill/'
PRO_INFO_BOX_API_URL = f'{MAIN_URL}/api/pro/dashboard/infobox/'


class TestSkillJobChart(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__when_valid__should_pass(self):
        resp = requests.get(PRO_SKILL_JOB_CHART_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        self.assertIsNotNone(data)
        self.assertEqual(resp.status_code, 200)

    def test__when_token_none__should_failed(self):
        resp = requests.get(PRO_SKILL_JOB_CHART_URL)
        self.assertEqual(resp.status_code, 401)


class TestInfoBox(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__when_valid__should_pass(self):
        resp = requests.get(PRO_INFO_BOX_API_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        self.assertIsNotNone(data['favourite_job_count'])
        self.assertIsNotNone(data['applied_job_count'])
        self.assertIsNotNone(data['skills_count'])
        self.assertEqual(resp.status_code,200)

    def test__when_token_none__should_fail(self):
        resp = requests.get(PRO_INFO_BOX_API_URL)
        self.assertEqual(resp.status_code,401)


if __name__ == '__main__':
    unittest.main()
