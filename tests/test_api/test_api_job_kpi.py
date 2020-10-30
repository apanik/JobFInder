import unittest

from tests.config_api import MAIN_URL
from tests.test_api.common import *
import requests

TRENDING_KEYWORD_URL = f'{MAIN_URL}/api/job/trending_keywords/'
TOP_CATEGORIES_URL = f'{MAIN_URL}/api/job/top-categories/'
TOP_SKILLS_URL = f'{MAIN_URL}/api/job/top-skills/'
TOP_FAVOURITES_URL = f'{MAIN_URL}/api/job/top-favourites/'
TOP_COMPANIES_URL = f'{MAIN_URL}/api/job/top-companies/'
VITAL_STATS_URL = f'{MAIN_URL}/api/vital_stats/get/'


class TestTrendingKeywordList(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__when_valid__should_pass(self):
        resp = requests.get(TRENDING_KEYWORD_URL)
        self.assertEqual(resp.status_code, 200)

    def test__with_access_token_also__should_pass(self):
        resp = requests.get(TRENDING_KEYWORD_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)


class TestTopCategoryList(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__when_valid__should_pass(self):
        resp = requests.get(TOP_CATEGORIES_URL)
        self.assertEqual(resp.status_code, 200)

    def test__with_access_token_also__should_pass(self):
        resp = requests.get(TOP_CATEGORIES_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)


class TestTopSkillList(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__when_valid__should_pass(self):
        resp = requests.get(TOP_SKILLS_URL)
        self.assertEqual(resp.status_code, 200)

    def test__with_access_token_also__should_pass(self):
        resp = requests.get(TOP_SKILLS_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)


class TestTopFavouriteList(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__when_valid__should_pass(self):
        resp = requests.get(TOP_FAVOURITES_URL)
        self.assertEqual(resp.status_code, 200)

    def test__with_access_token_also__should_pass(self):
        resp = requests.get(TOP_FAVOURITES_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)


class TestTopCompanyList(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__when_valid__should_pass(self):
        resp = requests.get(TOP_COMPANIES_URL)
        self.assertEqual(resp.status_code, 200)

    def test__with_access_token_also__should_pass(self):
        resp = requests.get(TOP_COMPANIES_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)


class TestGetVitalStats(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__when_valid__should_pass(self):
        resp = requests.get(VITAL_STATS_URL)
        data = resp.json()
        self.assertIsNotNone(data['num_of_vacancy'])
        self.assertIsNotNone(data['open_job'])
        self.assertIsNotNone(data['resume'])
        self.assertIsNotNone(data['company_count'])
        self.assertEqual(resp.status_code, 200)

    def test__with_access_token_also__should_pass(self):
        resp = requests.get(VITAL_STATS_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        self.assertIsNotNone(data['num_of_vacancy'])
        self.assertIsNotNone(data['open_job'])
        self.assertIsNotNone(data['resume'])
        self.assertIsNotNone(data['company_count'])
        self.assertEqual(resp.status_code, 200)


if __name__ == '__main__':
    unittest.main()
