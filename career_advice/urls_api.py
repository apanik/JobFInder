from django.urls import path
from django.views.generic import TemplateView
from .api import *

urlpatterns = [
    path('career_advice_show/', CareerAdviceShow.as_view()), # Public API
    path('career_advice/', career_advice), # Public API
]