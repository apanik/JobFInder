import json

from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes

from .models import Testimonial

@api_view(["GET"])
@permission_classes(())
def testimonial_list(request):
    queryset = Testimonial.objects.all()[:6]
    for testimonials in queryset:
        if not testimonials.profile_picture:
            testimonials.profile_picture = "static/images/alternate.jpg"
        else:
            testimonials.profile_picture = "media/" + str(testimonials.profile_picture)
    data=[{
        'client_name': str(testimonial.client_name),
        'comment' : str(testimonial.comment),
        'profile_picture': str(testimonial.profile_picture),
    } for testimonial in queryset
    ]
    return HttpResponse(json.dumps(data), content_type='application/json')
