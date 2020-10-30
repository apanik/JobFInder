from django.urls import path
from django.views.generic import TemplateView
from .api import *
urlpatterns = [
    path('settings/', SettingsList.as_view()), # Public API
]