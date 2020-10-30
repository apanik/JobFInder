import unittest
import requests
import socketio

from tests.test_api.common import signin_as_pro
from tests.config_api import MAIN_URL

ALL_MESSAGE_CREATE = f'{MAIN_URL}/api/employer-message-create/'
ALL_MESSAGE_LIST = f'{MAIN_URL}/api/employer-message-list/'
SENDER_LIST_URL = f'{MAIN_URL}/api/sender-list/'
SENDER_MESSAGE_LIST = f'{MAIN_URL}/api/sender-message-list/'
NOTIFICATION_GET_URL = f'{MAIN_URL}/api/notification/get/'
NOTIFICATION_CREATE_URL = f'{MAIN_URL}/api/notification/'
NOTIFICATION_MARK_READ = f'{MAIN_URL}/api/notification/mark-read/'
MARK_MESSAGE_UPDATE_VIEW_URL = f'{MAIN_URL}/api/employer-message/mark-read/'
EMPLOYYER_MESAGE_URL = f'{MAIN_URL}/api/employer-message/get/'
USER_ID = "1"
BLANK_FIELD = ""
RECIEVER_ID = "2"



# Create your tests here.

class SocketClientTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_socket_client_connection(self):
        socket = socketio.Client(ssl_verify=False)
        socket.connect(
            "https://iss.ishraak.com:443?server_token=xNTk3ODk0ODE5LCJqdGkiOiJiMGYxODEyOWI0Mjk0OGU4YmFjMmQwMWRmNDdlNTM0YyIsInVzZXJfaWQiOjUwfQ")

class TestSenderList(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__when_val_user_token__should_pass(self):
        resp = requests.get(SENDER_LIST_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        self.assertIsNotNone(data[0]['other_party_user_id'])
        self.assertIsNotNone(data[0]['other_party_type'])
        self.assertIsNotNone(data[0]['other_party_name'])
        # self.assertIsNotNone(data[0]['other_party_image'])
        self.assertEqual(resp.status_code, 200)

    def test__when_val_user_token__and__other_party_type__is_not_professional__should_pass(self):
        resp = requests.get(SENDER_LIST_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        self.assertIsNotNone(data[0]['other_party_user_id'])
        self.assertIsNotNone(data[0]['other_party_type'])
        self.assertIsNotNone(data[0]['other_party_name'])
        # self.assertIsNotNone(data[0]['other_party_image'])
        self.assertEqual(resp.status_code, 200)
        other_party_user_all_id = []
        other_party_all_type = []
        for item in data:
            other_party_user_all_id = item.get('other_party_user_id'),
            other_party_all_type = item.get('other_party_type'),
        if 'Professional' in other_party_all_type:
            self.fail()

    def test__when_val_user_token__and__other_party_user_id__are_as_expected__should_pass(self):
        resp = requests.get(SENDER_LIST_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        other_party_user_all_id = []
        other_party_all_type = []
        for item in data:
            other_party_user_all_id.append(item.get('other_party_user_id'))
            other_party_all_type.append(item.get('other_party_type'))
        self.failUnless('7' in other_party_user_all_id)
        self.failUnless('5' in other_party_user_all_id)


    def test__when_invalid_user_token__should_fail(self):
        resp = requests.get(SENDER_LIST_URL)
        self.assertEqual(resp.status_code, 401)


class TestSenderMessageList(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']
        resp = requests.get(SENDER_LIST_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        data_sender = resp.json()
        data_sender_length = len(data_sender)-1
        self.other_party_user_id = data_sender[data_sender_length]['other_party_user_id']
        self.other_party_invalid_user_id = '0'
        self.other_party_type = data_sender[data_sender_length]['other_party_type']

    def test__when_valid_other_party_user_id__should_pass(self):
        resp = requests.get(SENDER_MESSAGE_LIST, params={'sender': self.other_party_user_id},
                            headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        self.assertIsNotNone(data['count'])
        self.assertIsNotNone(data['start_index'])
        self.assertIsNotNone(data['end_index'])
        self.assertIsNotNone(data['page_number'])
        self.assertIsNotNone(data['page_size'])
        self.assertIsNotNone(data['page_count'])
        self.assertIsNotNone(data['page_data_count'])
        self.assertIsNotNone(data['pages'])
        self.assertIsNotNone(data['pages']['page_links'])
        self.assertIsNotNone(data['results'])
        self.assertEqual(resp.status_code, 200)


    def test__when_invalid_other_party_user_id__should_fail(self):
        resp = requests.get(SENDER_MESSAGE_LIST, params={'sender': self.other_party_invalid_user_id},
                            headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        self.assertEqual(data['count'], 0)

    def test__when_valid_but_company_other_party_user_id__should_fail(self):
        resp = requests.get(SENDER_MESSAGE_LIST, params={'sender': '0'},
                            headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        self.assertEqual(data['count'], 0)


    def test__when_access_token_invalid__should_fail(self):
        resp = requests.get(SENDER_MESSAGE_LIST)
        self.assertEqual(resp.status_code, 401)


    def test__when_access_token_inval_USER_ID__should_fail(self):
        resp = requests.get(SENDER_MESSAGE_LIST)
        self.assertEqual(resp.status_code, 401)


class TestAlMessageCreateProfessional(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']
        self.receiver = RECIEVER_ID
        self.message = "How you are doing?"

    def test__when_val_USER_ID__should_pass(self):
        json = {
            "receiver": self.receiver,
            "message": self.message
        }
        resp = requests.post(ALL_MESSAGE_CREATE, json=json, headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        print(data)
        self.assertEqual(resp.status_code, 201)

    def test__when_access_token_none__should_fail(self):
        json = {
            "receiver": self.receiver,
            "message": self.message
        }
        resp = requests.post(ALL_MESSAGE_CREATE, json=json)
        self.assertEqual(resp.status_code, 401)

    def test_when_receiver_empty_should_fail(self):
        json = {
            "receiver": BLANK_FIELD,
            "message": self.message
        }
        resp = requests.post(ALL_MESSAGE_CREATE, json=json, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertNotEqual(resp.status_code, 201)

    def test_when_receiver_blank_should_fail(self):
        json = {
            "message": self.message
        }
        resp = requests.post(ALL_MESSAGE_CREATE, json=json, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertNotEqual(resp.status_code, 201)

    def test__when_message_empty_should_pass(self):
        json = {
            "receiver": self.receiver,
            "message": BLANK_FIELD
        }
        resp = requests.post(ALL_MESSAGE_CREATE, json=json, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertNotEqual(resp.status_code, 201)

    def test__when_message_blank_should_pass(self):
        json = {
            "receiver": self.receiver
        }
        resp = requests.post(ALL_MESSAGE_CREATE, json=json, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertNotEqual(resp.status_code, 201)

    def test__when_both_empty_should_fail(self):
        json = {
            "receiver": BLANK_FIELD,
            "message": BLANK_FIELD
        }
        resp = requests.post(ALL_MESSAGE_CREATE, json=json, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertNotEqual(resp.status_code, 201)

    def test__when_both_blank_should_fail(self):
        json = {

        }
        resp = requests.post(ALL_MESSAGE_CREATE, json=json, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertNotEqual(resp.status_code, 201)



# class TestEmployerMessageList(unittest.TestCase):
#     def setUp(self) -> None:
#         data = signin_as_pro()
#         self.access_token = data['access']
#
#     def test__when_val_USER_ID__should_pass(self):
#         resp = requests.get(ALL_MESSAGE_LIST, headers={'Authorization': 'Bearer ' + self.access_token})
#         data = resp.json()
#         self.assertIsNotNone(data['count'])
#         self.assertIsNotNone(data['start_index'])
#         self.assertIsNotNone(data['end_index'])
#         self.assertIsNotNone(data['page_number'])
#         self.assertIsNotNone(data['page_size'])
#         self.assertIsNotNone(data['page_count'])
#         self.assertIsNotNone(data['page_data_count'])
#         self.assertIsNotNone(data['pages'])
#         self.assertIsNotNone(data['results'])
#         self.assertEqual(resp.status_code, 200)
#
#     def test__when_inval_USER_ID_token__should_fail(self):
#         resp = requests.get(ALL_MESSAGE_LIST)
#         self.assertEqual(resp.status_code, 401)


# class TestNotificationCreate(unittest.TestCase):
#     def setUp(self) -> None:
#         data = signin_as_pro()
#         self.access_token = data['access']
#         self.title = "Example Title Notification"
#         self.message = "Example Message"
#         self.recipient = RECIEVER_ID
#
#     def test__when_val_USER_ID__should_pass(self):
#         json = {
#             "title": self.title,
#             "message": self.message,
#             "recipient": self.recipient
#         }
#         resp = requests.post(NOTIFICATION_CREATE_URL, json=json,
#                              headers={'Authorization': 'Bearer ' + self.access_token})
#         data = resp.json()
#         self.assertIsNotNone(data['title'])
#         self.assertIsNotNone(data['message'])
#         self.assertIsNotNone(data['recipient'])
#
#     def test__when_recipient_empty__should_fail(self):
#         json = {
#             "title": self.title,
#             "message": self.message,
#             "recipient": BLANK_FIELD
#         }
#         resp = requests.post(NOTIFICATION_CREATE_URL, json=json,
#                              headers={'Authorization': 'Bearer ' + self.access_token})
#         self.assertNotEqual(resp.status_code, 201)
#
#     def test__when_recipient_blank__should_fail(self):
#         json = {
#             "title": self.title,
#             "message": self.message
#
#         }
#         resp = requests.post(NOTIFICATION_CREATE_URL, json=json,
#                              headers={'Authorization': 'Bearer ' + self.access_token})
#         self.assertNotEqual(resp.status_code, 201)
#
#     def test__when_message_empty__should_fail(self):
#         json = {
#             "title": self.title,
#             "message": BLANK_FIELD,
#             "recipient": self.recipient
#         }
#         resp = requests.post(NOTIFICATION_CREATE_URL, json=json,
#                              headers={'Authorization': 'Bearer ' + self.access_token})
#         self.assertNotEqual(resp.status_code, 201)
#
#     def test__when_message_blank__should_fail(self):
#         json = {
#             "title": self.title,
#             "recipient": self.recipient
#
#         }
#         resp = requests.post(NOTIFICATION_CREATE_URL, json=json,
#                              headers={'Authorization': 'Bearer ' + self.access_token})
#         self.assertNotEqual(resp.status_code, 201)
#
#     def test__when_title_empty__should_fail(self):
#         json = {
#             "title": BLANK_FIELD,
#             "message": self.message,
#             "recipient": self.recipient
#         }
#         resp = requests.post(NOTIFICATION_CREATE_URL, json=json,
#                              headers={'Authorization': 'Bearer ' + self.access_token})
#         self.assertNotEqual(resp.status_code, 201)
#
#     def test__when_title_blank__should_fail(self):
#         json = {
#             "message": self.message,
#             "recipient": self.recipient
#         }
#         resp = requests.post(NOTIFICATION_CREATE_URL, json=json,
#                              headers={'Authorization': 'Bearer ' + self.access_token})
#         self.assertNotEqual(resp.status_code, 201)
#
#     def test__when_all_field_empty__should_fail(self):
#         json = {
#             "title": BLANK_FIELD,
#             "message": BLANK_FIELD,
#             "recipient": BLANK_FIELD
#         }
#         resp = requests.post(NOTIFICATION_CREATE_URL, json=json,
#                              headers={'Authorization': 'Bearer ' + self.access_token})
#         self.assertNotEqual(resp.status_code, 201)
#
#     def test__when_all_field_blank__should_fail(self):
#         json = {
#
#         }
#         resp = requests.post(NOTIFICATION_CREATE_URL, json=json,
#                              headers={'Authorization': 'Bearer ' + self.access_token})
#         self.assertNotEqual(resp.status_code, 201)
#
#     def test__when_sender_and_recipient_same__should_fail(self):
#         json = {
#             "title": self.title,
#             "message": self.message,
#             "recipient": "4"
#         }
#         resp = requests.post(NOTIFICATION_CREATE_URL, json=json,
#                              headers={'Authorization': 'Bearer ' + self.access_token})
#         self.assertNotEqual(resp.status_code, 201)


# class TestNotificationGet(unittest.TestCase):
#     def setUp(self) -> None:
#         data = signin_as_pro()
#         self.access_token = data['access']
#
#     def test__when_val_USER_ID__should_pass(self):
#         resp = requests.get(NOTIFICATION_GET_URL + USER_ID + '/',
#                             headers={'Authorization': 'Bearer ' + self.access_token})
#         self.assertEqual(resp.status_code, 200)

#
# class TestNotificationMarkRead(unittest.TestCase):
#     def setUp(self) -> None:
#         data = signin_as_pro()
#         self.access_token = data['access']
#         self.IS_READ_TRUE = True
#         self.IS_READ_FALSE = False
#
#     def test__when_val_USER_ID__should_pass(self):
#         json = {
#             "is_read": self.IS_READ_TRUE
#         }
#         resp = requests.put(NOTIFICATION_MARK_READ + USER_ID + '/', json=json,
#                             headers={'Authorization': 'Bearer ' + self.access_token})
#         self.assertEqual(resp.status_code, 200)
#
#     def test__when_is_read_false__should_pass(self):
#         json = {
#             "is_read": self.IS_READ_FALSE
#         }
#         resp = requests.put(NOTIFICATION_MARK_READ + USER_ID + '/', json=json,
#                             headers={'Authorization': 'Bearer ' + self.access_token})
#         self.assertEqual(resp.status_code, 200)
#
#     def test__when_access_token_inval_USER_ID__should_pass(self):
#         json = {
#             "is_read": self.IS_READ_TRUE
#         }
#         resp = requests.put(NOTIFICATION_MARK_READ + USER_ID + '/', json=json)
#         self.assertEqual(resp.status_code, 401)
#
#
# class TestMarkMessageUpdateView(unittest.TestCase):
#     def setUp(self) -> None:
#         data = signin_as_pro()
#         self.access_token = data['access']
#
#     def test__when_val_USER_ID__should_pass(self):
#         resp = requests.put(MARK_MESSAGE_UPDATE_VIEW_URL + USER_ID + '/',
#                             headers={'Authorization': 'Bearer ' + self.access_token})
#         self.assertEqual(resp.status_code, 200)
#
#     def test__when_access_token_inval_USER_ID__should_fail(self):
#         resp = requests.put(MARK_MESSAGE_UPDATE_VIEW_URL + USER_ID + '/')
#         self.assertEqual(resp.status_code, 401)
#
#
# class TestEmployerMessage(unittest.TestCase):
#     def setUp(self) -> None:
#         data = signin_as_pro()
#         self.access_token = data['access']
#
#     def test__when_val_USER_ID__should_pass(self):
#         resp = requests.get(EMPLOYYER_MESAGE_URL + USER_ID + '/',
#                             headers={'Authorization': 'Bearer ' + self.access_token})
#         self.assertEqual(resp.status_code, 200)
#
#     def test__when_access_token_inval_USER_ID__should_fail(self):
#         resp = requests.get(EMPLOYYER_MESAGE_URL + USER_ID + '/')
#         self.assertEqual(resp.status_code, 401)


if __name__ == '__main__':
    unittest.main()
