"""Server Side FCM sample.
Firebase Cloud Messaging (FCM) can be used to send messages to clients on iOS,
Android and Web.
This sample uses FCM to send two types of messages to clients that are subscribed
to the `news` topic. One type of message is a simple notification message (display message).
The other is a notification message (display notification) with platform specific
customizations. For example, a badge is added to messages that are sent to iOS devices.
"""

import argparse
import json
import requests
import os
from oauth2client.service_account import ServiceAccountCredentials
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ID = 'p7app-df2de'
BASE_URL = 'https://fcm.googleapis.com'
FCM_ENDPOINT = 'v1/projects/' + PROJECT_ID + '/messages:send'
FCM_URL = BASE_URL + '/' + FCM_ENDPOINT
SCOPES = ['https://www.googleapis.com/auth/firebase.messaging']


# [START retrieve_access_token]
def _get_access_token():
    """Retrieve a valid access token that can be used to authorize requests.
    :return: Access token.
    """
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        BASE_DIR + '/static/service-account.json', SCOPES)
    access_token_info = credentials.get_access_token()
    print(access_token_info)
    return access_token_info.access_token


# [END retrieve_access_token]

def _send_fcm_message(fcm_message):
    """Send HTTP request to FCM with given message.
    Args:
      fcm_message: JSON object that will make up the body of the request.
    """
    # [START use_access_token]
    headers = {
        'Authorization': 'Bearer ' + _get_access_token(),
        'Content-Type': 'application/json; UTF-8',
    }
    # [END use_access_token]
    resp = requests.post(FCM_URL, data=json.dumps(fcm_message), headers=headers)

    if resp.status_code == 200:
        print('Message sent to Firebase for delivery, response:')
        print(resp.text)
    else:
        print('Unable to send message to Firebase')
        print(resp.text)


def _build_common_message():
    """Construct common notifiation message.
    Construct a JSON object that will be used to define the
    common parts of a notification message that will be sent
    to any app instance subscribed to the news topic.
    """
    return {
        'message': {
            'topic': 'news_dev',
            'notification': {
                'title': 'FCM Notification',
                'body': 'Notification from FCM'
            }
        }
    }


def _build_single_message(token, message):
    """Construct single notifiation message for specific device.
    token must be taken form user and must be saved to database!
    """
    return {
        'message': {
            'token': token,
            'notification': {
                #'title': 'FCM Notification For user',
                'body': message
            },
            "android": {
                "ttl": "86400s",
                "priority" : 'high',
                "notification" : {
                    'click_action': 'FLUTTER_NOTIFICATION_CLICK'
                }
            },
            "apns": {
                "headers": {
                    "apns-priority": "5",
                },
                "payload": {
                    "aps": {
                        "category": "NEW_MESSAGE_CATEGORY"
                    }
                }
            },
            "data": {
                "Nick": "Mario",
                "Room": "PortugalVSDenmark"
            }
        },
    }


def _build_override_message():
    """Construct common notification message with overrides.
    Constructs a JSON object that will be used to customize
    the messages that are sent to iOS and Android devices.
    """
    fcm_message = _build_common_message()

    apns_override = {
        'payload': {
            'aps': {
                'badge': 1
            }
        },
        'headers': {
            'apns-priority': '10'
        }
    }

    android_override = {
        'notification': {
            'click_action': 'FLUTTER_NOTIFICATION_CLICK'
        }
    }

    fcm_message['message']['android'] = android_override
    fcm_message['message']['apns'] = apns_override

    return fcm_message
