from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from testimonial.api import *

urlpatterns = [
    path('testimonial_show/',testimonial_list) # Public API
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)