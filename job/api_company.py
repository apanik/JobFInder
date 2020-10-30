import base64
import uuid

from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from job.models import Company, Job, JobApplication
from job.serializers import CompanySerializer, CompanyUpdateSerializer, FeaturedCompanySerializer
from p7.auth import CompanyAuthentication
from p7.models import populate_user_info_request, populate_user_info_querydict
from p7.pagination import P7Pagination
from datetime import datetime, timedelta
from django.db.models import Count, Q
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from job.models import Job, FavouriteJob, JobApplication
from p7.auth import ProfessionalAuthentication
from p7.permissions import CompanyPermission
from pro.models import ProfessionalSkill, Professional, RecentActivity
from resources.strings_pro import ARCHIVED_FALSE


class CompanyList(generics.ListAPIView):
    pagination_class = P7Pagination
    queryset = Company.objects.all().order_by('name')
    serializer_class = CompanySerializer

class FeaturedCompanyList(generics.ListAPIView):
    pagination_class = P7Pagination
    permission_classes = ()
    queryset = Company.objects.filter(
        featured=True
    ).annotate(num_posts=Count(
        'jobs', filter=Q(jobs__status='Published', jobs__is_archived=False))
    ).order_by('name')[0:9]
    serializer_class = FeaturedCompanySerializer


class CompanyListWithoutPagination(generics.ListAPIView):
    queryset = Company.objects.all().order_by('name')
    serializer_class = CompanySerializer


@api_view(["GET"])
@permission_classes([])
def list_company_by_name(request):
    comp_name = request.GET.get('name')
    if comp_name:
        queryset = Company.objects.filter(name__icontains=comp_name).order_by('name')
    else:
        queryset = Company.objects.all().order_by('name')

    paginator = P7Pagination()
    result_page = paginator.paginate_queryset(queryset, request)
    serializer = CompanySerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


class CompanyRetrieveView(generics.RetrieveAPIView):
    authentication_classes = [CompanyAuthentication]
    permission_classes = [CompanyPermission]
    serializer_class = CompanySerializer
    def get_object(self):
        user = self.request.user
        queryset = Company.objects.filter(
            ~Q(user_id=None),
            user_id = user.id,
        )
        return get_object_or_404(queryset)

class CompanyUpdateView(generics.UpdateAPIView):
    authentication_classes = [CompanyAuthentication]
    permission_classes = [CompanyPermission]
    serializer_class = CompanyUpdateSerializer

    def get_object(self):
        user = self.request.user
        queryset = Company.objects.filter(
            ~Q(user_id=None),
            user_id = user.id
        )
        return get_object_or_404(queryset)

    def put(self, request, *args, **kwargs):

        if 'image' in request.data:
            img_base64 = request.data['image']
            if img_base64:
                format, imgstr = img_base64.split(';base64,')
                ext = format.split('/')[-1]
                filename = str(uuid.uuid4()) + '-company.' + ext
                data = ContentFile(base64.b64decode(imgstr), name=filename)
                request.data['profile_picture'] = data

        req_data = request.data.copy()
        populate_user_info_querydict(request, req_data, False, False)

        instance = self.get_object()
        serializer = self.get_serializer(instance, data=req_data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


@api_view(["GET"])
@permission_classes([CompanyPermission])
def company_job_application_chart(request):
    com = Company.objects.filter(user = request.user).first()
    last_year = datetime.now() - timedelta(days=365)
    queryset = JobApplication.objects.filter(job__company_id=com.name, created_at__gte = last_year
    ).values_list('created_at__year', 'created_at__month'
    ).order_by(
    ).annotate(total=Count('*')
    ).order_by('created_at__year', 'created_at__month')
    data = list(queryset)
    return Response(data)



@api_view(["GET"])
@permission_classes([CompanyPermission])
def company_info_box_api(request):
    user = request.user.id
    company = Company.objects.filter(user_id=user).first()
    company_number_of_job = Job.objects.filter(company = company).count()
    company_appilcation_count = JobApplication.objects.filter(job__company = company).count()
    company_application_shortlist_count = JobApplication.objects.filter(job__company=company, is_shortlisted=True).count()

    data ={
        'company_number_of_job': company_number_of_job,
        'company_appilcation_count': company_appilcation_count,
        'company_application_shortlist_count': company_application_shortlist_count
    }

    return Response(data)



@api_view(["GET"])
@permission_classes([CompanyPermission])
def company_recent_activity(request):
    user = request.user
    activity = RecentActivity.objects.filter(user = user).order_by('-time')
    for obj in activity:
        if (timezone.now() - obj.time).days >=1:
            obj.activity_time = '{} days ago'.format((timezone.now() - obj.time).days)
        elif (((timezone.now() - obj.time).seconds)//3600) >=1:
            obj.activity_time = '{} hour ago'.format(((timezone.now() - obj.time).seconds) //3600)
        elif (((timezone.now() - obj.time).seconds)//60) >=1:
            obj.activity_time = '{} min ago'.format(((timezone.now() - obj.time).seconds) //60)
        else:
            obj.activity_time = '{} sec ago'.format(((timezone.now() - obj.time).seconds))
    activity_list =[{
        'description': act.description,
        'time': act.activity_time,
        'type': act.type
    } for act in activity]
    return Response(activity_list)

