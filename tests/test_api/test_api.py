import unittest
import requests

from tests.config import SERVER_PROTOCOL, SERVER_ADDRESS, VALID_PRO_USERNAME
from tests.test_api.common import signin_as_com, signin_as_pro

IS_LOGGED_IN_URL = f'{SERVER_PROTOCOL}://{SERVER_ADDRESS}/log/'
PROFESSIONAL_INFO_URL = f'{SERVER_PROTOCOL}://{SERVER_ADDRESS}/api/profile-info/'
SEND_EMAIL_TO_ADMIN_URL = f'{SERVER_PROTOCOL}://{SERVER_ADDRESS}/api/send_email_to_admin_contact_us/'
USER_ID_FOR_TEST = 4
INVALID_ID_FOR_TEST = 999


class TestisLoggedIn(unittest.TestCase):
    def setUp(self) -> None:
        pro_data = signin_as_pro()
        self.pro_access_token = pro_data['access']
        com_data = signin_as_com()
        self.com_access_token = com_data['access']

    def test__pro_user_logged_in__should_pass(self):
        resp = requests.get(IS_LOGGED_IN_URL, headers={'Authorization': 'Bearer ' + self.pro_access_token})
        data = resp.json()
        user = data[0]['user']
        name = user['name']
        email = user['email']
        id = user['id']
        self.assertIsNotNone(user)
        self.assertIsNotNone(name)
        self.assertIsNotNone(email)
        self.assertIsNotNone(id)
        self.assertEqual(resp.status_code, 200)

    def test__com_user_logged_in__should_pass(self):
        resp = requests.get(IS_LOGGED_IN_URL,
                            headers={'Authorization': 'Bearer ' + self.com_access_token})
        data = resp.json()
        user = data[0]['user']
        name = user['name']
        email = user['email']
        id = user['id']
        self.assertIsNotNone(user)
        self.assertIsNotNone(name)
        self.assertIsNotNone(email)
        self.assertIsNotNone(id)
        self.assertEqual(resp.status_code, 200)

    def test__user_not_logged_in__should_fail(self):
        resp = requests.get(IS_LOGGED_IN_URL)
        data = resp.json()
        self.assertEqual(data, 401)


class TestSendEmailToAdminContactUs(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']
        self.name = "Example"
        self.email = VALID_PRO_USERNAME
        self.phone = "01774116712"  # Test Number
        self.subject = "For Company Registration"
        self.message = "Example Message"

    def test__when_name_empty__should_fail(self):
        json = {
            "name": "",
            "email": self.email,
            "phone": self.phone,
            "subject": self.subject,
            "message": self.message
        }
        resp = requests.post(SEND_EMAIL_TO_ADMIN_URL, json=json)
        self.assertNotEqual(resp.text, 200)

    def test__when_email_empty__should_fail(self):
        json = {
            "name":self.name,
            "email": "",
            "phone": self.phone,
            "subject": self.subject,
            "message": self.message
        }
        resp = requests.post(SEND_EMAIL_TO_ADMIN_URL, json=json)
        self.assertNotEqual(resp.text, 200)

    def test__when_phone_empty__should_fail(self):
        json = {
            "name": self.name,
            "email": self.email,
            "phone": "",
            "subject": self.subject,
            "message": self.message
        }
        resp = requests.post(SEND_EMAIL_TO_ADMIN_URL, json=json)
        self.assertNotEqual(resp.text, 200)

    def test__when_subject_empty__should_fail(self):
        json = {
            "name":self.name,
            "email": self.email,
            "phone": self.phone,
            "subject": "",
            "message": self.message
        }
        resp = requests.post(SEND_EMAIL_TO_ADMIN_URL, json=json)
        self.assertNotEqual(resp.text, 200)

    def test__when_message_empty__should_fail(self):
        json = {
            "name": self.name,
            "email": self.email,
            "phone": self.email,
            "subject": self.subject,
            "message": ""
        }
        resp = requests.post(SEND_EMAIL_TO_ADMIN_URL, json=json)
        self.assertNotEqual(resp.text, 200)

    def test__when_fields_empty__should_fail(self):
        json = {
            "name": "",
            "email": "",
            "phone": "",
            "subject": "",
            "message": ""
        }
        resp = requests.post(SEND_EMAIL_TO_ADMIN_URL, json=json)
        self.assertNotEqual(resp.text, 200)

    def test__when_name_blank__should_fail(self):
        json = {
            "email": self.email,
            "phone": self.phone,
            "subject": self.subject,
            "message": self.message
        }
        resp = requests.post(SEND_EMAIL_TO_ADMIN_URL, json=json)
        self.assertEqual(resp.status_code, 500)

    def test__when_email_blank__should_fail(self):
        json = {
            "name": self.name,
            "phone": self.phone,
            "subject": self.subject,
            "message": self.message
        }
        resp = requests.post(SEND_EMAIL_TO_ADMIN_URL, json=json)
        self.assertEqual(resp.status_code, 500)

    def test__when_phone_blank__should_fail(self):
        json = {
            "name": self.name,
            "email": self.email,
            "subject": self.subject,
            "message": self.message
        }
        resp = requests.post(SEND_EMAIL_TO_ADMIN_URL, json=json)
        self.assertEqual(resp.status_code, 500)

    def test__when_subject_blank__should_fail(self):
        json = {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "message": self.message
        }
        resp = requests.post(SEND_EMAIL_TO_ADMIN_URL, json=json)
        self.assertEqual(resp.status_code, 500)

    def test__when_message_blank__should_fail(self):
        json = {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "subject": self.subject
        }
        resp = requests.post(SEND_EMAIL_TO_ADMIN_URL, json=json)
        self.assertEqual(resp.status_code, 500)

    def test__when_all_fields_blank__should_fail(self):
        json = {

        }
        resp = requests.post(SEND_EMAIL_TO_ADMIN_URL, json=json)
        self.assertEqual(resp.status_code, 500)


    def test__when_valid_data__send_email_to_admin_contact_us__should_pass(self):
        json = {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "subject": self.subject,
            "message": self.message
        }
        resp = requests.post(SEND_EMAIL_TO_ADMIN_URL, json=json)
        data = resp.json()
        self.assertEqual(resp.status_code, 200)


if __name__ == '__main__':
    unittest.main()
