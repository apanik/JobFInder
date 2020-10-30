import unittest
import requests

from tests.test_api.common import signin_as_pro
from tests.config_api import MAIN_URL

SETTINGS_LIST_URL = f'{MAIN_URL}/api/settings/'


class TestSettingsList(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__when_valid__should__pass(self):
        resp = requests.get(SETTINGS_LIST_URL)
        data = resp.json()
        self.assertIsNotNone(data[0]['id'])
        self.assertIsNotNone(data[0]['created_by'])
        self.assertIsNotNone(data[0]['created_at'])
        self.assertIsNotNone(data[0]['created_from'])
        self.assertIsNotNone(data[0]['facebook_url'])
        self.assertIsNotNone(data[0]['linkedin_url'])
        self.assertIsNotNone(data[0]['twitter_url'])
        self.assertIsNotNone(data[0]['appstore_url'])
        self.assertIsNotNone(data[0]['playstore_url'])
        self.assertIsNotNone(data[0]['logo_url'])
        self.assertIsNotNone(data[0]['admin_email'])
        self.assertIsNotNone(data[0]['support_email'])
        self.assertIsNotNone(data[0]['address'])
        self.assertIsNotNone(data[0]['phone'])

    def test__when_access_token__should__pass(self):
        resp = requests.get(SETTINGS_LIST_URL,headers = {'Authorization':'Bearer' + self.access_token})
        data = resp.json()
        self.assertIsNotNone(data[0]['id'])
        self.assertIsNotNone(data[0]['created_by'])
        self.assertIsNotNone(data[0]['created_at'])
        self.assertIsNotNone(data[0]['created_from'])
        self.assertIsNotNone(data[0]['facebook_url'])
        self.assertIsNotNone(data[0]['linkedin_url'])
        self.assertIsNotNone(data[0]['twitter_url'])
        self.assertIsNotNone(data[0]['appstore_url'])
        self.assertIsNotNone(data[0]['playstore_url'])
        self.assertIsNotNone(data[0]['logo_url'])
        self.assertIsNotNone(data[0]['admin_email'])
        self.assertIsNotNone(data[0]['support_email'])
        self.assertIsNotNone(data[0]['address'])
        self.assertIsNotNone(data[0]['phone'])


if __name__ == '__main__':
    unittest.main()
