from datetime import datetime, timedelta
from pprint import pprint

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import connection
from django.db.models import Q, Count, Max, FilteredRelation
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from job.models import Job
from job.serializers import JobSerializer, CompanyJobSerializer
from p7.models import is_professional, is_company
from p7.pagination import P7Pagination
from p7.permissions import CompanyPermission
from pro.utils import similar  # TODO: Why from pro


class JobSearchAPI(ListAPIView):
    permission_classes = ()
    pagination_class = P7Pagination
    serializer_class = JobSerializer
    def get_queryset(self):
        request = self.request
        if not request.user.is_authenticated:
            if request.GET.get('page') and request.GET.get('page') != "1":
                raise AuthenticationFailed()
        query = request.GET.get('q')
        featured = request.GET.get('featured')
        unspecified_salary = request.GET.get('unspecified_salary', 1)
        sorting = request.GET.get('sort')
        category = request.GET.get('category')
        company = request.GET.get('company')
        skill = request.GET.get('skill')
        job_city = request.GET.get('job_city')
        salaryMin = request.GET.get('salaryMin')
        salaryMax = request.GET.get('salaryMax')
        experienceMin = request.GET.get('experienceMin')
        experienceMax = request.GET.get('experienceMax')
        datePosted = request.GET.get('datePosted')
        gender = request.GET.get('gender')
        job_type = request.GET.get('job_type')
        qualification = request.GET.get('qualification')

        if request.user.is_authenticated and is_professional(request.user):
            current_user_id = request.user.id
        else:
            current_user_id = 0

        queryset = Job.objects.annotate(
            applied = FilteredRelation(
                'applied_jobs', condition=Q(applied_jobs__created_by=current_user_id)
            )
        ).annotate(
            favourite = FilteredRelation(
                'fav_jobs', condition=Q(fav_jobs__created_by=current_user_id)
            )
        ).filter(
            is_archived=False,
            status='Published',
        ).select_related(
            'company'
        ).annotate(
            is_favourite=Count('favourite')
        ).annotate(
            is_applied=Count('applied')
        ).annotate(
            applied_at=Max('applied__created_at')
        ).annotate(favourite_at=Max('favourite__created_at'))

        if sorting == 'most-applied':
            queryset = queryset.order_by('-applied_count')
        elif sorting == 'top-rated':
            queryset = queryset.order_by('-favorite_count')
        else:
            queryset = queryset.order_by('-post_date')

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(description__icontains=query) |
                Q(company_id__name__icontains=query) |
                Q(additional_requirements__icontains=query)
            )

        if featured:
            queryset = queryset.filter(featured=featured)

        if salaryMin and salaryMax:
            if unspecified_salary=='1':
                queryset = queryset.filter(
                    Q(salary_min__isnull=True, salary_max__isnull=True) |
                    Q(salary_min__range=(salaryMin, salaryMax)) |
                    Q(salary_max__range=(salaryMin, salaryMax))
                )
            else:
                queryset = queryset.filter(salary_min__gte=salaryMin, salary_min__lte=salaryMax)


        if category:
            queryset = queryset.filter(job_category=category)

        if datePosted:
            if datePosted == 'Last hour':
                queryset = queryset.filter(post_date__gt=datetime.now() - timedelta(hours=1))
            elif datePosted == 'Last 24 hour':
                queryset = queryset.filter(post_date__gt=datetime.now() - timedelta(hours=24))
            elif datePosted == 'Last 7 days':
                queryset = queryset.filter(post_date__gt=datetime.now() - timedelta(days=7))
            elif datePosted == 'Last 14 days':
                queryset = queryset.filter(post_date__gt=datetime.now() - timedelta(days=14))
            elif datePosted == 'Last 30 days':
                queryset = queryset.filter(post_date__gt=datetime.now() - timedelta(days=30))

        if gender and gender != 'Any':
            queryset = queryset.filter(job_gender=gender)

        if job_type:
            queryset = queryset.filter(job_type=job_type)

        if company:
            queryset = queryset.filter(company=company)

        if qualification:
            queryset = queryset.filter(qualification_id=qualification)

        if skill:
            queryset = queryset.filter(job_skills__name__in = [skill])

        if experienceMin and  experienceMax:
            queryset = queryset.filter(
                Q(experience__isnull=True) |
                Q(experience__gte=experienceMin, experience__lte = experienceMax)
            )

        if job_city:
            queryset = queryset.filter(job_city__icontains=job_city)

        return queryset


class CompanyJobSearchAPI(ListAPIView):
    permission_classes = [CompanyPermission]
    pagination_class = P7Pagination
    serializer_class = CompanyJobSerializer
    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        datePosted = request.GET.get('datePosted')
        status = request.GET.get('status')
        job_type = request.GET.get('job_type')
        category = request.GET.get('category')

        current_user_id = request.user.id

        queryset = Job.objects.filter(
            company__user_id = current_user_id,
            is_archived=False,
        ).select_related(
            'company'
        ).order_by('-post_date')

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(description__icontains=query) |
                Q(company_id__name__icontains=query) |
                Q(additional_requirements__icontains=query)
            )

        if category:
            queryset = queryset.filter(job_category=category)

        if status:
            queryset = queryset.filter(status=status)

        if datePosted:
            if datePosted == 'Last hour':
                queryset = queryset.filter(post_date__gt=datetime.now() - timedelta(hours=1))
            elif datePosted == 'Last 24 hour':
                queryset = queryset.filter(post_date__gt=datetime.now() - timedelta(hours=24))
            elif datePosted == 'Last 7 days':
                queryset = queryset.filter(post_date__gt=datetime.now() - timedelta(days=7))
            elif datePosted == 'Last 14 days':
                queryset = queryset.filter(post_date__gt=datetime.now() - timedelta(days=14))
            elif datePosted == 'Last 30 days':
                queryset = queryset.filter(post_date__gt=datetime.now() - timedelta(days=30))

        if job_type:
            queryset = queryset.filter(job_type=job_type)

        return queryset


@api_view(["GET"])
@permission_classes(())
def similar_jobs(request, identifier, limit = 5):
    try:
        selected_job = Job.objects.get(job_id=identifier)
    except Job.DoesNotExist:
        return JsonResponse(Job.DoesNotExist)

    if request.user.is_authenticated and is_professional(request.user):
        current_user_id = request.user.id
    else:
        current_user_id = 0

    queryset = Job.objects.annotate(
        applied = FilteredRelation(
            'applied_jobs', condition=Q(applied_jobs__created_by=current_user_id)
        )
    ).annotate(
        favourite = FilteredRelation(
            'fav_jobs', condition=Q(fav_jobs__created_by=current_user_id)
        )
    ).filter(
        is_archived=False,
        status='Published',
    ).exclude(
        job_id=identifier
    ).select_related('company'
                     ).annotate(is_favourite=Count('favourite')
                                ).annotate(is_applied=Count('applied')
                                           ).annotate(applied_at=Max('applied__created_at')
                                                      ).annotate(favourite_at=Max('favourite__created_at')
                                                                 ).order_by('-post_date')

    data = []
    for job in queryset:
        if(similar(selected_job.title, job.title) > 0.8 ): # TODO: Read from settings)
            data.append(job)
        if len(data) >= limit:
            break

    data = JobSerializer(data, many=True).data
    return Response(data)


@api_view(["GET"])
@permission_classes(())
def recent_jobs(request, limit:int = 6):
    if request.user.is_authenticated and is_professional(request.user):
        current_user_id = request.user.id
    else:
        current_user_id = 0

    queryset = Job.objects.annotate(
        applied = FilteredRelation(
            'applied_jobs', condition=Q(applied_jobs__created_by=current_user_id)
        )
    ).annotate(
        favourite = FilteredRelation(
            'fav_jobs', condition=Q(fav_jobs__created_by=current_user_id)
        )
    ).filter(
        is_archived=False,
        status='Published',
    ).select_related('company'
                     ).annotate(is_favourite=Count('favourite')
                                ).annotate(is_applied=Count('applied')
                                           ).annotate(applied_at=Max('applied__created_at')
                                                      ).annotate(favourite_at=Max('favourite__created_at')
                                                                 ).order_by('-post_date')[:limit]

    data = JobSerializer(queryset, many=True).data
    return Response(data)


@api_view(["GET"])
def favourite_jobs(request):
    if request.user.is_authenticated and is_professional(request.user):
        current_user_id = request.user.id
    else:
        current_user_id = 0

    queryset = Job.objects.annotate(
        applied = FilteredRelation(
            'applied_jobs', condition=Q(applied_jobs__created_by=current_user_id)
        )
    ).filter(
        is_archived=False,
        status='Published',
        fav_jobs__created_by = current_user_id
    ).select_related('company'
                     ).annotate(is_favourite=Count('fav_jobs')
                                ).annotate(is_applied=Count('applied')
                                           ).annotate(applied_at=Max('applied__created_at')
                                                      ).annotate(favourite_at=Max('fav_jobs__created_at')
                                                                 ).order_by('-fav_jobs__created_at')
    paginator = P7Pagination()
    result_page = paginator.paginate_queryset(queryset, request)
    serializer = JobSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(["GET"])
def applied_jobs(request):
    if request.user.is_authenticated and is_professional(request.user):
        current_user_id = request.user.id
    else:
        current_user_id = 0

    queryset = Job.objects.annotate(
        favourite = FilteredRelation(
            'fav_jobs', condition=Q(fav_jobs__created_by=current_user_id)
        )
    ).filter(
        is_archived=False,
        status='Published',
        applied_jobs__created_by = current_user_id
    ).select_related('company'
                     ).annotate(is_favourite=Count('favourite')
                                ).annotate(is_applied=Count('applied_jobs')
                                           ).annotate(applied_at=Max('applied_jobs__created_at')
                                                      ).annotate(favourite_at=Max('favourite__created_at')
                                                                 ).order_by('-applied_jobs__created_at')
    paginator = P7Pagination()
    result_page = paginator.paginate_queryset(queryset, request)
    serializer = JobSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


