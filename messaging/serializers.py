from rest_framework import serializers

from job.models import Company
from messaging.models import Notification, EmployerMessage, FcmCloudMessaging
from pro.models import Professional


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class NotificationReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['is_read']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'profile_picture']


class ProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional
        fields = ['full_name', 'image']


class EmployerMessageListSerializer(serializers.ModelSerializer):
    receiver_pro = ProfessionalSerializer(many=False)
    sender_pro = ProfessionalSerializer(many=False)
    receiver_company = CompanySerializer(many=False)
    sender_company = CompanySerializer(many=False)

    class Meta:
        model = EmployerMessage
        fields = ['message', 'receiver', 'receiver_type', 'receiver_company', 'receiver_pro',
                  'sender', 'sender_type', 'sender_company', 'sender_pro','created_at']

class EmployerMessageCreateSerializer(serializers.ModelSerializer):
    # receiver = serializers.CharField(source='receiver.id')
    # receiver_company = serializers.CharField(source='receiver_company.name')
    #receiver_company_profile_pic = serializers.CharField(source='com_received_msgs.profile_pic')

    class Meta:
        model = EmployerMessage
        fields = ['message', 'receiver', 'receiver_type', 'receiver_company', 'receiver_pro', 'sender',
                  'sender_type', 'sender_company', 'sender_pro', 'created_by', 'created_from', 'sender_type']

class EmployerMessageReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployerMessage
        fields = ['is_read']


class OtherPartySerializer(serializers.ModelSerializer):
    other_party_user_id = serializers.CharField()
    other_party_type = serializers.CharField()
    other_party_name = serializers.CharField()
    other_party_image = serializers.CharField()
    class Meta:
        model = EmployerMessage
        fields = ['other_party_user_id', 'other_party_type', 'other_party_name', 'other_party_image']


class FcmCloudMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FcmCloudMessaging
        fields = '__all__'


