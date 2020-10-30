from django.contrib.auth.models import User
from django.db.models import Q, F, Max, Case, When, CharField
from rest_framework import generics
from rest_framework.response import Response

from job.models import Company
from messaging.models import EmployerMessage, Notification
from messaging.serializers import NotificationSerializer, NotificationReadSerializer, \
    EmployerMessageReadSerializer, OtherPartySerializer, EmployerMessageCreateSerializer, EmployerMessageListSerializer, \
    FcmCloudMessageSerializer
from p7.models import populate_user_info_request, is_company
from p7.pagination import P7Pagination
from pro.models import Professional


class NotificationListCreate(generics.ListCreateAPIView):
    serializer_class = NotificationSerializer
    pagination_class = P7Pagination
    def get_queryset(self):
        user = self.request.user
        userwithcomma = str(user.id) + ','
        commawithuser = ',' + str(user.id)
        commawithuserwithcomma = ',' + str(user.id) + ','
        queryset = Notification.objects.filter(
            Q(recipient=user.id) | Q(recipient='*') | Q(recipient__startswith=userwithcomma)
            | Q(recipient__endswith=commawithuser) | Q(recipient__icontains=commawithuserwithcomma)
        ).filter( is_archived = False).order_by('-created_at')
        return queryset

    def post(self, request, *args, **kwargs):
        populate_user_info_request(request, False, False)
        return super(NotificationListCreate, self).post(request, *args, **kwargs)


class MarkNotificationUpdateView(generics.UpdateAPIView):
    serializer_class = NotificationReadSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Notification.objects.filter(
            recipient = user.id
        )
        return queryset

    def put(self, request, *args, **kwargs):
        populate_user_info_request(request, True, False)
        return super(MarkNotificationUpdateView, self).put(request, *args, **kwargs)


class MessageCreate(generics.CreateAPIView):
    serializer_class = EmployerMessageCreateSerializer
    pagination_class = P7Pagination

    def post(self, request, *args, **kwargs):
        populate_user_info_request(request, False, False)
        request.data['sender'] = request.user.id
        if is_company(request.user):
            request.data['sender_type'] = 'Company'
            company_obj = Company.objects.filter(user_id=request.user.id).first()
            request.data['sender_company'] = company_obj.name
        else:
            request.data['sender_type'] = 'Professional'
            pro_obj = Professional.objects.filter(user_id=request.user.id).first()
            request.data['sender_pro'] = pro_obj.id

        user_obj = User.objects.filter(id = request.data['receiver']).first()
        if is_company(user_obj):
            request.data['receiver_type'] = 'Company'
            company_obj = Company.objects.filter(user_id=user_obj.id).first()
            request.data['receiver_company'] = company_obj.name
        else:
            request.data['receiver_type'] = 'Professional'
            pro_obj = Professional.objects.filter(user_id=user_obj.id).first()
            request.data['receiver_pro'] = pro_obj.id

        return super(MessageCreate, self).post(request, *args, **kwargs)


class SenderMessageList(generics.ListAPIView):
    serializer_class = EmployerMessageListSerializer
    pagination_class = P7Pagination

    def get_queryset(self):
        user = self.request.user
        sender = self.request.GET.get('sender')
        queryset = EmployerMessage.objects.filter(
            Q(receiver=user.id, sender=sender) |
            Q(sender=user.id, receiver=sender),
            is_archived=False
        ).order_by('-created_at')
        return queryset


class SenderList(generics.ListAPIView):
    serializer_class = OtherPartySerializer

    def list(self, request, *args, **kwargs):
        user = self.request.user
        q1 = EmployerMessage.objects.filter(
            created_by=user.id,
            is_archived=False
        ).values(
            'receiver', 'receiver_type', 'receiver_pro__full_name', 'receiver_company', 'created_at'
        ).annotate(
            other_party_user_id=F('receiver'),
            other_party_type=F('receiver_type'),
            other_party_name=Case(
                When(receiver_type='Professional', then= F('receiver_pro__full_name')),
                default=F('receiver_company')),
            other_party_image=Case(
                When(receiver_type='Professional', then= F('receiver_pro__image')),
                default=F('receiver_company__profile_picture'),
                output_field = CharField()
            ),
        ).annotate(
            last_date=Max('created_at')
        )

        q2 = EmployerMessage.objects.filter(
            receiver=user.id,
            is_archived=False
        ).values(
            'sender', 'sender_type', 'sender_pro', 'sender_company', 'created_at'
        ).annotate(
            other_party_user_id=F('sender'),
            other_party_type=F('sender_type'),
            other_party_name=Case(
                When(sender_type='Professional', then=F('sender_pro__full_name')),
                default=F('sender_company')),
            other_party_image=Case(
                When(sender_type='Professional', then=F('sender_pro__image')),
                default=F('sender_company__profile_picture'),
                output_field=CharField()
            ),
        ).annotate(
            last_date=Max('created_at')
        )

        queryset = (q1.union(q2)).order_by('-last_date')

        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        data_unique = [i for n, i in enumerate(data) if i not in data[n + 1:]]
        return Response(data_unique)


class MarkMessageUpdateView(generics.UpdateAPIView):
    serializer_class = EmployerMessageReadSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = EmployerMessage.objects.filter(
            receiver = user.id
        )
        return queryset

    def put(self, request, *args, **kwargs):
        populate_user_info_request(request, True, False)
        return super(MarkMessageUpdateView, self).put(request, *args, **kwargs)


class FcmCloudMessageCreate(generics.CreateAPIView):
    serializer_class = FcmCloudMessageSerializer
    pagination_class = P7Pagination

    def post(self, request, *args, **kwargs):
        populate_user_info_request(request, False, False)
        request.data['user'] = self.request.user.id



        return super(FcmCloudMessageCreate, self).post(request, *args, **kwargs)

