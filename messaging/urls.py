from django.urls import path
from messaging.views import CompanyMessagesView, ProfessionalMessagesView, CompanyNotificationView, \
    ProfessionalNotificationView

urlpatterns = [
    path('company/messages/', CompanyMessagesView.as_view(), name='messages-company'),
    path('professional/messages/', ProfessionalMessagesView.as_view(), name='messages-professional'),
    path('company/notifications/',CompanyNotificationView.as_view(),name= 'company_notification'),
    path('professional/notifications/',ProfessionalNotificationView.as_view(),name= 'company_notification'),
]