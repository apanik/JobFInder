from django.urls import path,include

from messaging.api import *
from pro.api_dashboard import skill_job_chart
from pro.api_pro_core import *

urlpatterns = [
    path('notification/mark-read/<str:pk>/', MarkNotificationUpdateView.as_view()),
    path('notification/', NotificationListCreate.as_view()),
    path('fcm-cloud-message/', FcmCloudMessageCreate.as_view()),
    path('employer-message/mark-read/<str:pk>/', MarkMessageUpdateView.as_view()),
    path('sender-message-list/', SenderMessageList.as_view()),
    path('employer-message-create/', MessageCreate.as_view()),
    path('sender-list/', SenderList.as_view()),
]