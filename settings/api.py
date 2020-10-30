# from .serializers import DistrictSerializer
from rest_framework import generics

from .models import Settings
from .serializers import SettingsSerializer


class SettingsList(generics.ListAPIView):
    permission_classes = []
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer
