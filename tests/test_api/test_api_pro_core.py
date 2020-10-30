import unittest
import requests

from tests.config import VALID_PRO_USERNAME, VALID_PRO_PASSWORD
from tests.test_api.common import signin_as_pro
from tests.config_api import *

PRO_CHANGE_PASSWORD_URL = f'{MAIN_URL}/api/pro/change-password/'
PRO_CHECK_EXIST_URL = f'{MAIN_URL}/api/pro/check-professional-exist/'
PRO_PROFILE_COMPLETENESS_URL = f'{MAIN_URL}/api/pro/profile-completeness/'
PRO_CREATE_WITH_USER_URL = f'{MAIN_URL}/api/professional/create_with_user/'


class TestProfileCreateWithUserCreate(unittest.TestCase):

    def setUp(self) -> None:
        self.url = PRO_CREATE_WITH_USER_URL
        self.full_name = "ExampleUser"
        self.email = VALID_PRO_USERNAME
        self.phone = "01781008090"
        self.password = VALID_PRO_PASSWORD
        self.confirm_password = "12345678a"
        self.terms_and_condition = "on"

    def test__create_user__when_all_data_is_valid__should_create(self):
        json = {
            'full_name': self.full_name,
            'email': "new@email.com",
            'phone': self.phone,
            'password': self.password,
            'confirm_password': self.confirm_password,
            'terms_and_condition_status': self.terms_and_condition
        }
        resp = requests.post(self.url, json=json)
        data = resp.text
        data = resp.json()
        self.assertEqual(data['code'], 200)
        self.assertIsNotNone(data['message'])
        self.assertEqual(resp.status_code, 200)

    def test__create_user__when_all_fields_are_empty__should_not_create(self):
        json = {
            'full_name': '',
            'email': '',
            'phone': '',
            'password': '',
            'confirm_password': '',
            'terms_and_condition_status': ''
        }
        resp = requests.post(self.url, json=json)
        data = resp.json()
        self.assertEqual(data['code'], 500)

    def test__create_user__when_name_field_is_empty__should_not_create(self):
        json = {
            'full_name': '',
            'email': self.email,
            'phone': self.phone,
            'password': self.password,
            'confirm_password': self.confirm_password,
            'terms_and_condition_status': self.terms_and_condition
        }
        resp = requests.post(self.url, json=json)
        data = resp.json()
        self.assertEqual(data['code'], 500)

    def test__create_user__when_email_field_is_empty__should_not_create(self):
        json = {
            'full_name': 'Tanvir Ahmed',
            'email': '',
            'phone': '01921069797',
            'password': '12345678a',
            'confirm_password': '12345678a',
            'terms_and_condition_status': 'on'
        }
        resp = requests.post(self.url, json=json)
        data = resp.json()
        self.assertEqual(data['code'], 500)

    def test__create_user__when_phone_field_is_empty__should_not_create(self):
        json = {
            'full_name': self.full_name,
            'email': self.email,
            'phone':self.phone,
            'password': self.password,
            'confirm_password': self.confirm_password,
            'terms_and_condition_status': self.terms_and_condition
        }
        resp = requests.post(self.url, json=json)
        data = resp.json()
        self.assertEqual(data['code'], 500)

    def test__create_user__when_password_field_is_empty__should_not_create(self):
        json = {
            'full_name': self.full_name,
            'email': self.email,
            'phone': self.email,
            'password': '',
            'confirm_password': self.confirm_password,
            'terms_and_condition_status': self.terms_and_condition
        }
        resp = requests.post(self.url, json=json)
        data = resp.json()
        self.assertEqual(data['code'], 500)

    def test__create_user__when_confirm_password_is_empty__should_not_create(self):
        json = {
            'full_name': self.full_name,
            'email': self.email,
            'phone': self.email,
            'password': self.password,
            'confirm_password': '',
            'terms_and_condition_status': self.terms_and_condition
        }
        resp = requests.post(self.url, json=json)
        data = resp.json()
        self.assertEqual(data['code'], 500)

    def test__create_user__when_terms_and_condition_is_not_checked__should_not_create(self):
        json = {
            'full_name': self.full_name,
            'email': self.email,
            'phone': self.phone,
            'password': self.password,
            'confirm_password': self.confirm_password,
            'terms_and_condition_status': ''
        }
        resp = requests.post(self.url, json=json)
        data = resp.json()
        self.assertEqual(data['code'], 500)

    def test__create_user__when_only_name_field_has_value__should_not_create(self):
        json = {
            'full_name': self.full_name,
            'email': '',
            'phone': '',
            'password': '',
            'confirm_password': '',
            'terms_and_condition_status': ''
        }
        resp = requests.post(self.url, json=json)
        data = resp.json()
        self.assertEqual(data['code'], 500)

    def test__create_user__when_only_email_field_has_value__should_not_create(self):
        json = {
            'full_name': '',
            'email': self.email,
            'phone': '',
            'password': '',
            'confirm_password': '',
            'terms_and_condition_status': ''
        }
        resp = requests.post(self.url, json=json)
        data = resp.json()
        self.assertEqual(data['code'], 500)

    def test__create_user__when_only_phone_field_has_value__should_not_create(self):
        json = {
            'full_name': '',
            'email': '',
            'phone': self.phone,
            'password': '',
            'confirm_password': '',
            'terms_and_condition_status': ''
        }
        resp = requests.post(self.url, json=json)
        data = resp.json()
        self.assertEqual(data['code'], 500)

    def test__create_user__when_only_password_field_has_value__should_not_create(self):
        json = {
            'full_name': '',
            'email': '',
            'phone': '',
            'password': self.password,
            'confirm_password': '',
            'terms_and_condition_status': ''
        }
        resp = requests.post(self.url, json=json)
        data = resp.json()
        self.assertEqual(data['code'], 500)

    def test__create_user__when_only_confirm_password_field_has_value__should_not_create(self):
        json = {
            'full_name': '',
            'email': '',
            'phone': '',
            'password': '',
            'confirm_password': self.confirm_password,
            'terms_and_condition_status': ''
        }
        resp = requests.post(self.url, json=json)
        data = resp.json()
        self.assertEqual(data['code'], 500)

    def test__create_user__when_only_terms_and_condition_is_checked__should_not_create(self):
        json = {
            'full_name': '',
            'email': '',
            'phone': '',
            'password': '',
            'confirm_password': '',
            'terms_and_condition_status': self.terms_and_condition
        }
        resp = requests.post(self.url, json=json)
        data = resp.json()
        self.assertEqual(data['code'], 500)

    def test__create_user__when_email_is_invalid__should_not_create(self):
        json = {
            'full_name': '',
            'email': 'invalid',
            'phone': '',
            'password': self.password,
            'confirm_password': self.confirm_password,
            'terms_and_condition_status': self.terms_and_condition
        }
        resp = requests.post(self.url, json=json)
        data = resp.json()
        self.assertEqual(data['code'], 500)

    def test__create_user__when_password_is_invalid__should_not_create(self):
        json = {
            'full_name': self.full_name,
            'email': self.email,
            'phone': self.phone,
            'password': self.password,
            'confirm_password': self.confirm_password,
            'terms_and_condition_status': self.terms_and_condition
        }
        resp = requests.post(self.url, json=json)
        data = resp.json()
        self.assertEqual(data['code'], 500)

    def test__create_user__when_password_and_confirm_password_mismatched__should_not_create(self):
        json = {
            'full_name': '',
            'email': self.email,
            'phone': self.phone,
            'password': self.password,
            'confirm_password': self.confirm_password,
            'terms_and_condition_status': self.terms_and_condition
        }
        resp = requests.post(self.url, json=json)
        data = resp.json()
        self.assertEqual(data['code'], 500)

    def test__create_user__when_name_key_is_not_provided__should_not_create(self):
        json = {

            'email': self.email,
            'phone': self.phone,
            'password': self.password,
            'confirm_password': self.confirm_password,
            'terms_and_condition_status': self.terms_and_condition
        }
        resp = requests.post(self.url, json=json)
        data = resp.json()
        self.assertEqual(data['code'], 500)

    def test__create_user__when_email_key_is_not_provided__should_not_create(self):
        json = {
            'full_name': self.full_name,

            'phone':self.phone,
            'password': self.password,
            'confirm_password': self.confirm_password,
            'terms_and_condition_status': self.terms_and_condition
        }
        resp = requests.post(self.url, json=json)
        data = resp.json()
        self.assertEqual(data['code'], 500)

    def test__create_user__when_mobile_key_is_not_provided__should_not_create(self):
        json = {
            'full_name': self.full_name,
            'email': self.email,

            'password': self.password,
            'confirm_password': self.confirm_password,
            'terms_and_condition_status': self.terms_and_condition
        }
        resp = requests.post(self.url, json=json)
        data = resp.json()
        self.assertNotEqual(str(data['code']), 500)

    def test__create_user__when_password_key_is_not_provided__should_not_create(self):
        json = {
            'full_name': self.full_name,
            'email': self.email,
            'phone': self.phone,

            'confirm_password': self.confirm_password,
            'terms_and_condition_status': self.terms_and_condition
        }
        resp = requests.post(self.url, json=json)
        data = resp.json()
        self.assertNotEqual(str(data['code']), 500)

    def test__create_user__when_confirm_password_key_is_not_provided__should_not_create(self):
        json = {
            'full_name': self.full_name,
            'email': self.email,
            'phone': self.phone,
            'password': self.password,

            'terms_and_condition_status': self.terms_and_condition
        }
        resp = requests.post(self.url, json=json)
        data = resp.json()
        self.assertNotEqual(str(data['code']), 500)

    def test__create_user__when_terms_and_condition_key_is_not_provided__should_not_create(self):
        json = {
            'full_name': self.full_name,
            'email': self.email,
            'phone': self.phone,
            'password': self.password,
            'confirm_password': self.confirm_password,

        }
        resp = requests.post(self.url, json=json)
        data = resp.json()
        self.assertNotEqual(str(data['code']), 500)


class TestProfessionalChangePassword(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__change_password__when_valid__should_pass(self):
        json = {
            'old_password': '12345678a',
            'new_password': '12345678a',
            'confirm_password': '12345678a'
        }
        resp = requests.post(PRO_CHANGE_PASSWORD_URL, json=json,
                             headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        self.assertEqual(data['code'], 200)

    def test__change_password__when_empty__should_failed(self):
        json = {
            'old_password': '',
            'new_password': '',
            'confirm_password': ''
        }
        resp = requests.post(PRO_CHANGE_PASSWORD_URL, json=json,
                             headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 401)

    def test__change_password__when_old_pass_and_new_pass_empty__should_failed(self):
        json = {
            'old_password': '',
            'new_password': '',
            'confirm_password': 'anik12345'
        }
        resp = requests.post(PRO_CHANGE_PASSWORD_URL, json=json,
                             headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 401)

    def test__change_password__when_old_pass_and_new_pass_null__should_failed(self):
        json = {
            'confirm_password': 'qwer12345'
        }
        resp = requests.post(PRO_CHANGE_PASSWORD_URL, json=json,
                             headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 500)

    def test__change_password__when_old_pass_and_confirm_pass_empty__should_failed(self):
        json = {
            'old_password': '',
            'new_password': 'qwer12345',
            'confirm_password': ''
        }
        resp = requests.post(PRO_CHANGE_PASSWORD_URL, json=json,
                             headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 401)

    def test__change_password__when_old_pass_and_confirm_pass_null__should_failed(self):
        json = {
            'new_password': 'qwer12345'
        }
        resp = requests.post(PRO_CHANGE_PASSWORD_URL, json=json,
                             headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 500)

    def test__change_password__when_new_pass_and_confirm_pass_null__should_failed(self):
        json = {
            'old_password': 'qwer12345'
        }
        resp = requests.post(PRO_CHANGE_PASSWORD_URL, json=json,
                             headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 500)

    def test__change_password__when_old_password_wrong__should_failed(self):
        json = {
            'old_password': 'wrongpassword',
            'new_password': 'qwer12345',
            'confirm_password': 'qwer12345'
        }
        resp = requests.post(PRO_CHANGE_PASSWORD_URL, json=json,
                             headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 401)


class TestCheckProExist(unittest.TestCase):
    def test__when_valid_email__should_pass(self):
        params = {
            'email': VALID_PRO_USERNAME
        }
        resp = requests.get(PRO_CHECK_EXIST_URL, params=params)
        data = resp.json()
        self.assertEqual(data['email_exist'], True)

    def test__when_invalid_email__should_failed(self):
        params = {
            'email': "Invalid_Email@Ishraak.com"
        }
        resp = requests.get(PRO_CHECK_EXIST_URL, params=params)
        data = resp.json()
        self.assertEqual(data['email_exist'], False)

    def test__when_email_empty__should_failed(self):
        params = {
            'email': ""
        }
        resp = requests.get(PRO_CHECK_EXIST_URL, params=params)
        data = resp.json()
        self.assertEqual(data['email_exist'], False)

# ####### OUR SYSTEM IS NOT USING THIS API NOW
# class TestSendCredentialToEmail(unittest.TestCase):
#     def setUp(self) -> None:
#         self.email = VALID_PRO_USERNAME
#         self.password = VALID_PRO_PASSWORD
#     def test__when_valid_data__should_pass(self):
#         json = {
#             "email": self.email,
#             "password": self.password
#         }
#         resp = requests.post(PRO_SEND_CREDENTIAL_URL, json=json)
#         data = resp.json()
#         self.assertEqual(resp.status_code, 200)
#         self.assertIsNotNone(data["id"])
#
#     def test__when_invalid__should_fail(self):
#         json = {
#             "email": "invalid_Example@Ishraak.com",
#             "password": "a2ecsx1"
#         }
#         resp = requests.post(PRO_SEND_CREDENTIAL_URL, json=json)
#         data = resp.json()
#         self.assertEqual(data, 404)
#
#     def test__when_invalid_email__should_fail(self):
#         json = {
#             "email": "xyz@hotmail.com",
#             "password": self.password
#         }
#         resp = requests.post(PRO_SEND_CREDENTIAL_URL, json=json)
#         data = resp.json()
#         self.assertEqual(data, 404)
#
#     def test__when_invalid_password__should_fail(self):
#         json = {
#             "email": self.email,
#             "password": "a2ecsx1"
#         }
#         resp = requests.post(PRO_SEND_CREDENTIAL_URL, json=json)
#         self.assertEqual(resp.status_code, 500)
#
#     def test__when_email_empty__should_fail(self):
#         json = {
#             "email": "",
#             "password": "a2ecsx1"
#         }
#         resp = requests.post(PRO_SEND_CREDENTIAL_URL, json=json)
#         data = resp.json()
#         self.assertEqual(data, 404)
#
#     def test__when_email_blank__should_fail(self):
#         json = {
#             "password": self.password
#         }
#         resp = requests.post(PRO_SEND_CREDENTIAL_URL, json=json)
#         # self.assertEqual(data, 500)
#
#     def test__when_password_null__should_fail(self):
#         json = {
#             "email": self.email
#
#         }
#         resp = requests.post(PRO_SEND_CREDENTIAL_URL, json=json)
#         self.assertEqual(resp.status_code, 500)
#
#     def test__when_password_empty__should_fail(self):
#         json = {
#             "email": self.email,
#             "password": ""
#         }
#         resp = requests.post(PRO_SEND_CREDENTIAL_URL, json=json)
#         self.assertEqual(resp.status_code, 500)
#
#
#     def test__when_both_field_empty__should_fail(self):
#         json = {
#             "email": "",
#             "password": ""
#         }
#         resp = requests.post(PRO_SEND_CREDENTIAL_URL, json=json)
#         data = resp.json()
#         self.assertEqual(data, 404)
#
#     def test__when_both_field_blank__should_fail(self):
#         json = {
#
#         }
#         resp = requests.post(PRO_SEND_CREDENTIAL_URL, json=json)
#         self.assertEqual(resp.status_code, 500)


class TestProfessionalProfileCompleteness(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']
        self.invalid_token = data['refresh']

    def test__token__when_valid__should_pass(self):
        resp = requests.get(PRO_PROFILE_COMPLETENESS_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)

    def test__token__when_invalid__should_fail(self):
        resp = requests.get(PRO_PROFILE_COMPLETENESS_URL, headers={'Authorization': 'Bearer ' + self.invalid_token})
        self.assertEqual(resp.status_code, 401)


if __name__ == '__main__':
    unittest.main()

