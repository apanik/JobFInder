import unittest
import requests

from tests.test_api.common import signin_as_pro
from tests.config_api import *

RELIGION_URL = f'{MAIN_URL}/api/professional/religion/'
NATIONALITY_URL = f'{MAIN_URL}/api/professional/nationality/'
INSTITUTE_URL = f'{MAIN_URL}/api/professional/institute/list/'
ORGANIZATION_URL = f'{MAIN_URL}/api/professional/organization/'
MAJOR_URL = f'{MAIN_URL}/api/professional/major/'
CERTIFICATE_URL = f'{MAIN_URL}/api/professional/certificate_name/'
EMAIL_SUBS_URL = f'{MAIN_URL}/api/professional/email-subscription-on-off/'


class TestReligionList(unittest.TestCase):

    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']
        self.invalid_token = data['refresh']

    def test_token__when_valid__should_pass(self):
        resp = requests.get(RELIGION_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)

    def test_token__when_in_valid__should_fail(self):
        resp = requests.get(RELIGION_URL, headers={'Authorization': 'Bearer ' + self.invalid_token})
        self.assertEqual(resp.status_code, 401)


class TestNationalityList(unittest.TestCase):

    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']
        self.invalid_token = data['refresh']

    def test_token__when_valid__should_pass(self):
        resp = requests.get(NATIONALITY_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)

    def test_token__when_in_valid__should_fail(self):
        resp = requests.get(NATIONALITY_URL, headers={'Authorization': 'Bearer ' + self.invalid_token})
        self.assertEqual(resp.status_code, 401)


class TestInstituteList(unittest.TestCase):

    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']
        self.invalid_token = data['refresh']

    def test_token__when_valid__should_pass(self):
        resp = requests.get(INSTITUTE_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)

    def test_token__when_in_valid__should_fail(self):
        resp = requests.get(INSTITUTE_URL, headers={'Authorization': 'Bearer ' + self.invalid_token})
        self.assertEqual(resp.status_code, 401)


class TestOrganizationList(unittest.TestCase):

    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']
        self.invalid_token = data['refresh']

    def test_token__when_valid__should_pass(self):
        resp = requests.get(ORGANIZATION_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)

    def test_token__when_in_valid__should_fail(self):
        resp = requests.get(ORGANIZATION_URL, headers={'Authorization': 'Bearer ' + self.invalid_token})
        self.assertEqual(resp.status_code, 401)


class TestMajorList(unittest.TestCase):

    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']
        self.invalid_token = data['refresh']

    def test_token__when_valid__should_pass(self):
        resp = requests.get(MAJOR_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)

    def test_token__when_in_valid__should_fail(self):
        resp = requests.get(MAJOR_URL, headers={'Authorization': 'Bearer ' + self.invalid_token})
        self.assertEqual(resp.status_code, 401)


class TestCertificateNameList(unittest.TestCase):

    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']
        self.invalid_token = data['refresh']

    def test_token__when_valid__should_pass(self):
        resp = requests.get(CERTIFICATE_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)

    def test_token__when_in_valid__should_fail(self):
        resp = requests.get(CERTIFICATE_URL, headers={'Authorization': 'Bearer ' + self.invalid_token})
        self.assertEqual(resp.status_code, 401)


class TestEmailSubscriptionUpdateView(unittest.TestCase):

    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']
        self.invalid_token = data['refresh']
        self.user_id = data['pro']['id']
        self.assertIsNotNone(data['pro']['id'])

    def test_token__when_true__should_pass(self):
        json = {
            'job_alert_status': 'true'
        }
        resp = requests.put(EMAIL_SUBS_URL, json=json, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)

    def test_token__when_false__should_pass(self):
        json = {
            'job_alert_status': 'false'
        }
        resp = requests.put(EMAIL_SUBS_URL, json=json, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)

    def test__when_token_none__should_pass(self):
        json = {
            'job_alert_status': 'false'
        }
        resp = requests.put(EMAIL_SUBS_URL, json=json)
        self.assertEqual(resp.status_code, 401)


if __name__ == '__main__':
    unittest.main()
