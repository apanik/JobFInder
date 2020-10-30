import json

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save, post_save
from firebase_admin import messaging

from job.models import Company
from p7.fcm import build_single_message, build_topic_message
from p7.messaging import _build_single_message, _send_fcm_message
from p7.models import P7Model, populate_time_info
from p7.socket_client import SocketClient
from pro.models import Professional
from resources import strings_messaging


class Notification(P7Model) :
    title = models.CharField(max_length=255)
    message = models.TextField()
    recipient = models.CharField(max_length=255, null=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = strings_messaging.NOTIFICATION_VERBOSE_NAME
        verbose_name_plural = strings_messaging.NOTIFICATION_VERBOSE_NAME_PLURAL

    def __str__(self):
        return self.title

class EmployerMessage(P7Model):
    message = models.TextField()
    receiver = models.ForeignKey(User, on_delete=models.PROTECT, related_name='received_msgs', null=True)
    receiver_type = models.CharField(max_length=30, null=True)
    receiver_company = models.ForeignKey(Company, on_delete=models.PROTECT, null=True, related_name='com_received_msgs')
    receiver_pro = models.ForeignKey(Professional, on_delete=models.PROTECT, null=True, related_name='pro_received_msgs')
    sender = models.ForeignKey(User, on_delete=models.PROTECT, related_name='sent_msgs', null=True)
    sender_type = models.CharField(max_length=30, null=True)
    sender_company = models.ForeignKey(Company, on_delete=models.PROTECT, null=True, related_name='com_sent_msgs')
    sender_pro = models.ForeignKey(Professional, on_delete=models.PROTECT, null=True, related_name='pro_sent_msgs')
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = strings_messaging.EMPLOYER_MESSAGE_VERBOSE_NAME
        verbose_name_plural = strings_messaging.EMPLOYER_MESSAGE_VERBOSE_NAME_PLURAL

    def __str__(self):
        return self.message

class FcmCloudMessaging(P7Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    fcm_token = models.CharField(max_length=500)
    device_id = models.CharField(max_length=255)
    device_os_type = models.CharField(max_length=255, null=True, blank=True)
    device_os_version = models.CharField(max_length=255, null=True, blank=True)
    device_model = models.CharField(max_length=255, null=True, blank=True)
    device_brand = models.CharField(max_length=255, null=True, blank=True)
    app_version = models.CharField(max_length=255, null=True, blank=True)
    is_company = models.BooleanField(null=True, blank=True)
    is_professional = models.BooleanField(null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=True, blank=True)
    professional = models.ForeignKey(Professional, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        unique_together = ('user', 'fcm_token', 'device_id')

def after_notification_save(sender, instance: Notification, *args, **kwargs):
    from messaging.serializers import NotificationSerializer
    SocketClient.send({
        "type": "notification",
        "text": json.dumps(NotificationSerializer(instance, many=False).data),
        "from": "",
        "to": instance.recipient
    })
    userid = instance.recipient
    message = instance.message

    if userid == '*':
        param = build_topic_message(message)
        response = messaging.send(param)
    else:
        try:
            messaging_obj = FcmCloudMessaging.objects.get(user_id=userid)
            param  = build_single_message(messaging_obj.fcm_token, message)
            response = messaging.send(param)

        except FcmCloudMessaging.DoesNotExist:
            pass


def after_employer_message_save(sender, instance: EmployerMessage, *args, **kwargs):
    from messaging.serializers import EmployerMessageListSerializer
    SocketClient.send({
        "type": "message",
        "text": json.dumps(EmployerMessageListSerializer(instance, many=False).data),
        "from": instance.sender,
        "to": instance.receiver
    })



pre_save.connect(populate_time_info, sender=Notification)
post_save.connect(after_notification_save, sender=Notification)
pre_save.connect(populate_time_info, sender=EmployerMessage)
post_save.connect(after_employer_message_save, sender=EmployerMessage)

