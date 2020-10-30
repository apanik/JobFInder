from django.contrib import admin

from messaging.models import Notification, EmployerMessage, FcmCloudMessaging
from p7.admin import P7Admin

# Register your models here.
@admin.register(Notification)
class NotificationAdmin(P7Admin):
    list_per_page = 15
    list_display = ['title','message','recipient','is_read', 'created_by', 'created_at']
    fields = ['title','message','recipient','is_read', 'created_by', 'created_at', 'modified_by', 'modified_at']

@admin.register(EmployerMessage)
class EmployerMessageAdmin(P7Admin):
    list_per_page = 15
    list_display = ['message', 'receiver', 'is_read', 'created_by', 'created_at']
    fields = ['message', 'receiver', 'is_read', 'created_by', 'created_at', 'modified_by', 'modified_at']

@admin.register(FcmCloudMessaging)
class EmployerMessageAdmin(P7Admin):
    list_per_page = 15