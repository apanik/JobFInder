from django.contrib import admin

from p7.admin import P7Admin
from .models import Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(P7Admin):
    list_display = ['client_name', 'created_by', 'created_at']
