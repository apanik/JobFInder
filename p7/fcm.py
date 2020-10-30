import os

from p7.settings_dev import FIREBASE_CLOUD_MESSAGING_TOPIC

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import firebase_admin
from firebase_admin import credentials, messaging

cred = credentials.Certificate(BASE_DIR + '/static/service-account.json')
firebase_admin.initialize_app(cred)

# This registration token comes from the client FCM SDKs.

# See documentation on defining a message payload.

def build_single_message(token, msg):
    registration_token = token
    message = messaging.Message(
        data={
            'type': 'notification'
        },
        notification=messaging.Notification('', msg),
        android=messaging.AndroidConfig(
            priority='high',
            notification=messaging.AndroidNotification(
                click_action='FLUTTER_NOTIFICATION_CLICK'
            ),
        ),
        apns=messaging.APNSConfig(
            payload=messaging.APNSPayload(
                aps=messaging.Aps(badge=42),
            ),
        ),
        token=registration_token,
    )
    return message

def build_topic_message(msg):

    topic = FIREBASE_CLOUD_MESSAGING_TOPIC
    message = messaging.Message(
        data={
            'type': 'notification'
        },
        notification=messaging.Notification('', msg),
        android=messaging.AndroidConfig(
            priority='high',
            notification=messaging.AndroidNotification(
                click_action='FLUTTER_NOTIFICATION_CLICK'
            ),
        ),
        topic=topic,
    )
    return message

def build_multiple_message(token, msg):
    registration_token = token
    message = messaging.Message(
        data={
            'type': 'notification'
        },
        notification=messaging.Notification('', msg),
        android=messaging.AndroidConfig(
            priority='high',
            notification=messaging.AndroidNotification(
                click_action='FLUTTER_NOTIFICATION_CLICK'
            ),
        ),
        apns=messaging.APNSConfig(
            payload=messaging.APNSPayload(
                aps=messaging.Aps(badge=42),
            ),
        ),
        token=registration_token,
    )
    return message


# Send a message to the device corresponding to the provided
# registration token.
#response = messaging.send(build_single_message())
# Response is a message ID string.
#print('Successfully sent message:', response)