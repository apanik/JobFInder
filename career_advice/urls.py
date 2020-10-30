from django.urls import path
from django.views.generic import TemplateView
from p7.views import CareerAdviceDetailView
from .api import *

urlpatterns = [
    path('career-advice/details/<int:id>/', CareerAdviceDetailView.as_view(),
         name='career_advice_details'),

]