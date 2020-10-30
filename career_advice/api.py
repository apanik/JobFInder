from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import HTTP_200_OK
from career_advice.models import *
from career_advice.serializers import CareerAdviceSerializer
from rest_framework.response import Response

from p7.pagination import P7Pagination


class CareerAdviceShow(generics.ListCreateAPIView):
    permission_classes = []
    queryset = CareerAdvice.objects.filter().order_by('-posted_at')[:3]
    serializer_class = CareerAdviceSerializer

@api_view(["GET"])
@permission_classes(())
def career_advice(request):
    queryset = CareerAdvice.objects.filter().order_by('-posted_at')
    paginator = P7Pagination()
    result_page = paginator.paginate_queryset(queryset, request)
    serializer = CareerAdviceSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)




