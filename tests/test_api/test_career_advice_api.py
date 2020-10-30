import unittest

import requests


from tests.test_api.common import signin_as_pro
from tests.config_api import MAIN_URL

# BOTH PUBLIC API
CAREER_ADVICE_DETAILS_URL = f'{MAIN_URL}/api/career_advice_show'
CAREER_ADVICE_URL = f'{MAIN_URL}/api/career_advice'


class TestCareerAdviseDetail(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__when_no_access_token__show_detail__should_pass(self):
        resp = requests.get(CAREER_ADVICE_DETAILS_URL)
        data = resp.json()
        # Testing First Element from Data and also checking Must have key's
        if len(data) > 0:
           self.assertIsNotNone(data[0]['id'])
           self.assertIsNotNone(data[0]['created_by'])
           self.assertIsNotNone(data[0]['created_at'])
           self.assertIsNotNone(data[0]['created_from'])
           self.assertIsNotNone(data[0]['title'])
           self.assertIsNotNone(data[0]['short_description'])
           self.assertIsNotNone(data[0]['author'])
           self.assertEqual(resp.status_code, 200)

    def test__when_valid_access_token__show_detail__should_pass(self):
        resp = requests.get(CAREER_ADVICE_DETAILS_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        # Testing First Element from Data and also checking Must have key's
        self.assertEqual(resp.status_code, 200)
        if len(data)>0:
            self.assertIsNotNone(data[0]['id'])
            self.assertIsNotNone(data[0]['created_by'])
            self.assertIsNotNone(data[0]['created_at'])
            self.assertIsNotNone(data[0]['created_from'])
            self.assertIsNotNone(data[0]['title'])
            self.assertIsNotNone(data[0]['short_description'])
            self.assertIsNotNone(data[0]['author'])



class TestCareerAdviseShow(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__when_valid__should_pass(self):
        resp = requests.get(CAREER_ADVICE_URL)
        data = resp.json()
        self.assertIsNotNone(data['count'])
        self.assertIsNotNone(data['start_index'])
        self.assertIsNotNone(data['end_index'])
        self.assertIsNotNone(data['page_number'])
        self.assertIsNotNone(data['page_size'])
        self.assertIsNotNone(data['pages'])
        self.assertIsNotNone(data['results'])
        self.assertEqual(resp.status_code,200)

    def test__when_access_token__should__pass(self):
        resp = requests.get(CAREER_ADVICE_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        self.assertIsNotNone(data['count'])
        self.assertIsNotNone(data['start_index'])
        self.assertIsNotNone(data['end_index'])
        self.assertIsNotNone(data['page_number'])
        self.assertIsNotNone(data['page_size'])
        self.assertIsNotNone(data['pages'])
        self.assertIsNotNone(data['results'])
        self.assertEqual(resp.status_code, 200)


if __name__ == '__main__':
    unittest.main()
