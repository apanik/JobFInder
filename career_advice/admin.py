from career_advice.models import CareerAdvice
from django.contrib import admin

from p7.admin import P7Admin


@admin.register(CareerAdvice)
class CareerAdviceAdmin(P7Admin):
    list_display = ['title', 'author', 'posted_at']
    search_fields = ['title', 'author', 'posted_at']


