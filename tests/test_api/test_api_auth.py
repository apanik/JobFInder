import unittest
import requests

from tests.config import VALID_PRO_USERNAME, VALID_PRO_PASSWORD, VALID_COM_USERNAME, VALID_COM_PASSWORD
from tests.config_api import PRO_SIGNIN_URL, COM_SIGNIN_URL

BLANK_FIELD = ''
WRONG_PRO_PASSWORD = '12121212b'
INVALID_PRO_USERNAME = 'invalid_example@ishraak.com'


class TestProfessionalSignIn(unittest.TestCase):

    def setUp(self) -> None:
        self.url = PRO_SIGNIN_URL


    def test_signin__when_valid__should_signin(self):
        json = {
            'email': VALID_PRO_USERNAME,
            'password': VALID_PRO_PASSWORD
        }
        resp = requests.post(self.url, json=json)
        data = resp.json()
        self.assertIsNotNone(data['access'])
        self.assertIsNotNone(data['refresh'])
        self.assertIsNotNone(data['user'])
        self.assertIsNotNone(data['pro'])
        self.assertIsNotNone(data['pro']['id'])
        self.assertEqual(resp.status_code, 200)


    def test_signin__when_empty_username__should_fail(self):
        json = {
            'email': BLANK_FIELD,
            'password': BLANK_FIELD
        }
        resp = requests.post(self.url, json=json)
        data = resp.json()
        self.assertNotEqual(resp.status_code, 200)


    def test_signin__when_empty_password__should_fail(self):
        json = {
            'email': VALID_PRO_USERNAME,
            'password': BLANK_FIELD
        }
        resp = requests.post(self.url, json=json)
        self.assertNotEqual(resp.status_code, 200)


    def test_signin__when_invalid_username__should_fail(self):
        json = {
            'email': INVALID_PRO_USERNAME,
            'password': VALID_PRO_PASSWORD
        }

        resp = requests.post(self.url, json=json)
        self.assertNotEqual(resp.status_code, 200)


    def test_signin__when_wrong_password__should_fail(self):
        json = {
            'email': VALID_PRO_USERNAME,
            'password': WRONG_PRO_PASSWORD
        }

        resp = requests.post(self.url, json=json)
        self.assertNotEqual(resp.status_code, 200)


    def test_signin__when_no_data__should_fail(self):
        json = {

        }
        resp = requests.post(self.url, json=json)
        self.assertNotEqual(resp.status_code, 200)


    def test_signin__when_no_username__should_fail(self):
        json = {
            'password': VALID_PRO_PASSWORD
        }
        resp = requests.post(self.url, json=json)
        self.assertNotEqual(resp.status_code, 200)


    def test_signin__when_no_password__should_fail(self):
        json = {
            'email': VALID_PRO_USERNAME
        }
        resp = requests.post(self.url, json=json)
        self.assertNotEqual(resp.status_code, 200)

    def test__sign_in_with_company_credentials__should_fail(self):
        json = {
            'email': VALID_COM_USERNAME,
            'password': VALID_COM_PASSWORD
        }
        resp = requests.post(self.url, json=json)
        self.assertNotEqual(resp.status_code, 200)


class TestCompanySignIn(unittest.TestCase):

    def setUp(self) -> None:
        self.url = COM_SIGNIN_URL


    def test_signin__when_valid__should_signin(self):
        json = {
            'email': VALID_COM_USERNAME,
            'password': VALID_COM_PASSWORD
        }
        resp = requests.post(self.url, json=json)

        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertIsNotNone(data['access'])
        self.assertIsNotNone(data['refresh'])
        self.assertIsNotNone(data['user'])
        self.assertIsNotNone(data['company'])
        self.assertIsNotNone(data['company']['name'])


    def test_signin__when_empty_username__should_fail(self):
        json = {
            'email': BLANK_FIELD,
            'password': VALID_COM_PASSWORD
        }
        resp = requests.post(self.url, json=json)
        data = resp.json()
        self.assertNotEqual(data, 401)


    def test_signin__when_empty_password__should_fail(self):
        json = {
            'email': VALID_COM_USERNAME,
            'password': BLANK_FIELD
        }
        resp = requests.post(self.url, json=json)
        data = resp.json()
        self.assertNotEqual(data, 401)


    def test_signin__when_invalid_username__should_fail(self):
        json = {
            'email': INVALID_PRO_USERNAME,
            'password': VALID_COM_PASSWORD
        }
        resp = requests.post(self.url, json=json)
        data = resp.json()
        self.assertNotEqual(data, 401)


    # def test_signin__when_invalid_password__should_fail(self):
    #     json = {
    #         'email': VALID_COM_USERNAME,
    #         'password': WRONG_PRO_PASSWORD
    #     }
    #     resp = requests.post(self.url, json=json)
    #     data = resp.json()
    #     self.assertNotEqual(data, 401)
    #
    #
    # def test_signin__when_no_data__should_fail(self):
    #     json = {
    #
    #     }
    #     resp = requests.post(self.url, json=json)
    #     data = resp.json()
    #     self.assertNotEqual(data, 500)


    # def test_signin__when_no_username__should_fail(self):
    #     json = {
    #         'password': VALID_COM_PASSWORD
    #     }
    #     resp = requests.post(self.url, json=json)
    #     data = resp.json()
    #     # self.assertNotEqual(data, 500)


    def test_signin__when_no_password__should_fail(self):
        json = {
            'email': VALID_COM_USERNAME
        }
        resp = requests.post(self.url, json=json)
        self.assertNotEqual(resp.status_code, 200)

    def test__sign_in__when_with_pro_credentials__should_fail(self):
        json = {
            'email': VALID_PRO_USERNAME,
            'password': VALID_PRO_PASSWORD
        }
        resp = requests.post(self.url, json=json)
        self.assertEqual(resp.status_code, 401)


if __name__ == '__main__':
    unittest.main()