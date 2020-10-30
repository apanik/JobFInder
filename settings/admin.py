from django.contrib import admin

from p7.admin import P7Admin
from .models import Settings

@admin.register(Settings)
class SettingsAdmin(P7Admin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True


