from datetime import datetime, timedelta
from pprint import pprint

from django.db import connection
from django.db.models import QuerySet, FilteredRelation, Max
from django.http import Http404
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404, GenericAPIView, CreateAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.utils import json
from rest_framework.views import APIView
from django.db.models import Q, Count
from job.models import Job, FavouriteJob, JobApplication, Skill, Company
from job.serializers import JobSerializerAllField, JobSerializer, JobUpdateSerializer, CompnayJobCreateSerializer, \
    CompanyJobSerializer, JobUpdateStatusSerializer
from job.utils import job_slug_generator
from p7.models import populate_user_info, is_professional, populate_user_info_request, populate_user_info_querydict

# TODO Handle try catch
from p7.permissions import StaffPermission, CompanyPermission


class JobAPI(APIView):
    permission_classes = ()

    def get(self, request, slug):
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
            slug=slug,
        ).select_related('company'
        ).prefetch_related('job_skills'
        ).annotate(is_favourite=Count('favourite')
        ).annotate(is_applied=Count('applied')
        ).annotate(applied_at=Max('applied__created_at')
        ).annotate(favourite_at=Max('favourite__created_at')
        ).first()
        data = JobSerializerAllField(queryset, many=False).data
        return Response(data)

class CompanyJobAPI(APIView):
    permission_classes = [CompanyPermission]
    def get(self, request, slug):
        queryset = Job.objects.filter(
            is_archived=False,
            slug=slug,
            company__user_id = request.user.id
        ).select_related('company'
        ).prefetch_related('job_skills'
        ).first()
        data = CompanyJobSerializer(queryset, many=False).data
        return Response(data)


class CompanyJobCreateAPI(CreateAPIView):
    permission_classes = [CompanyPermission]
    serializer_class = CompnayJobCreateSerializer

    def post(self, request, *args, **kwargs):
        job_data = json.loads(request.body)
        if 'company_id' in job_data or 'company' in job_data:
            raise serializers.ValidationError('Unexpected Company/Company Id.')
        if 'title' not in job_data or not job_data['title'] :
            raise serializers.ValidationError('Title is required.')
        if 'vacancy' not in job_data or not job_data['vacancy'] :
            raise serializers.ValidationError('Vacancy is required.')
        if 'address' not in job_data or not job_data['address'] :
            raise serializers.ValidationError('Address is required.')
        if 'job_site' not in job_data or not job_data['job_site'] :
            raise serializers.ValidationError('Job site is required.')
        if 'job_nature' not in job_data or not job_data['job_nature'] :
            raise serializers.ValidationError('Job nature is required.')
        if 'job_type' not in job_data or not job_data['job_type'] :
            raise serializers.ValidationError('Job type is required.')
        if 'status' in job_data:
            if job_data['status'] != 'DRAFT' and job_data['status'] != 'POSTED' and job_data['status'] != '':
                raise serializers.ValidationError('Invalid status.')
        if 'salary_min' in job_data and job_data['salary_min'] and 'salary_max' in job_data and job_data['salary_max']:
            if int(job_data['salary_min']) > int(job_data['salary_max']):
                raise serializers.ValidationError('Minimum salary cannot be greater than maximum salary')

        company = Company.objects.get(user_id = request.user.id)
        job_data['company'] = company
        try:
            skills = job_data['skills']
            del job_data['skills']
        except KeyError:
            skills = None

        job_obj = Job(**job_data)
        populate_user_info(request, job_obj, False, False)
        job_obj.save()
        if skills:
            skill_list = skills.split(',')
            for skill in skill_list:
                try:
                    skill_obj = Skill.objects.get(name=skill)
                except Skill.DoesNotExist:
                    skill_obj = None
                if skill_obj:
                    job_obj.job_skills.add(skill_obj)
        return Response(HTTP_200_OK)


class CompanyJobUpdateView(GenericAPIView, UpdateModelMixin):
    permission_classes = [CompanyPermission]
    serializer_class = JobUpdateSerializer

    def get_queryset(self):
        return Job.objects.filter(company__user_id=self.request.user.id)

    def put(self, request, *args, **kwargs):
        req_data = request.data.copy()
        populate_user_info_querydict(request, req_data, False, False)
        if 'title' not in req_data or not req_data['title'] :
            raise serializers.ValidationError('Title is required.')
        if 'vacancy' not in req_data or not req_data['vacancy'] :
            raise serializers.ValidationError('Vacancy is required.')
        if 'address' not in req_data or not req_data['address'] :
            raise serializers.ValidationError('Address is required.')
        if 'job_site' not in req_data or not req_data['job_site'] :
            raise serializers.ValidationError('Job site is required.')
        if 'job_nature' not in req_data or not req_data['job_nature'] :
            raise serializers.ValidationError('Job nature is required.')
        if 'job_type' not in req_data or not req_data['job_type'] :
            raise serializers.ValidationError('Job type is required.')
        if 'status' in req_data:
            if req_data['status'] != 'DRAFT' and req_data['status'] != 'POSTED' and req_data['status'] != '':
                raise serializers.ValidationError('Invalid status.')
        if 'salary_min' in req_data and req_data['salary_min']  and 'salary_max' in req_data and req_data['salary_max']:
            if int(req_data['salary_min']) > int(req_data['salary_max']):
                raise serializers.ValidationError('Minimum salary cannot be greater than maximum salary')
        try:
            skills = req_data['skills']
            del req_data['skills']
        except KeyError:
            skills = None

        instance = self.get_object()
        job_skill_list = []
        if skills:
            skill_list = skills.split(',')
            for skill in skill_list:
                try:
                    skill_obj = Skill.objects.get(name=skill)
                except Skill.DoesNotExist:
                    skill_obj = None
                if skill_obj:
                    job_skill_list.append(skill_obj.id)
        req_data['job_skills'] = job_skill_list
        serializer = self.get_serializer(instance, data=req_data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(HTTP_200_OK)

class CompanyJobUnpublishAPI(GenericAPIView, UpdateModelMixin):
    permission_classes = [CompanyPermission]
    serializer_class = JobUpdateStatusSerializer

    def get_queryset(self):
        return Job.objects.filter(company__user_id=self.request.user.id,status__exact='PUBLISHED')

    def put(self, request, *args, **kwargs):
        req_data = {'status': 'UNPUBLISHED'}
        populate_user_info_querydict(request, req_data, False, False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=req_data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(HTTP_200_OK)

class CompanyJobPublishAPI(GenericAPIView, UpdateModelMixin):
    permission_classes = [CompanyPermission]
    serializer_class = JobUpdateStatusSerializer

    def get_queryset(self):
        return Job.objects.filter(company__user_id=self.request.user.id,status__exact='UNPUBLISHED')

    def put(self, request, *args, **kwargs):
        req_data = {'status': 'PUBLISHED'}
        populate_user_info_querydict(request, req_data, False, False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=req_data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(HTTP_200_OK)

class CompanyJobPostAPI(GenericAPIView, UpdateModelMixin):
    permission_classes = [CompanyPermission]
    serializer_class = JobUpdateStatusSerializer

    def get_queryset(self):
        return Job.objects.filter(company__user_id=self.request.user.id,status__exact='DRAFT')

    def put(self, request, *args, **kwargs):
        req_data = {'status': 'POSTED'}
        populate_user_info_querydict(request, req_data, False, False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=req_data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(HTTP_200_OK)


def get_company_latlng(job):
    if type(job) is QuerySet:
        job = job[0]
    if job.company_name:
        latitude = job.company_name.latitude
        longitude = job.company_name.longitude
    return latitude, longitude

def get_company_logo(job):
    # TODO: read from string file/ settings
    if type(job) is QuerySet:
        job = job[0]
    if job.company_name:
        if job.company_name.profile_picture:
            profile_picture = '/media/' + str(job.company_name.profile_picture)
        else:
            profile_picture = '/static/images/job/company-logo-2.png'
    else:
        profile_picture = '/static/images/job/company-logo-2.png'

    return profile_picture

def get_favourite_status(job : Job, user):
    if type(job) is QuerySet:
        job = job[0]
    if user.is_authenticated:
        try:
            favourite_job = FavouriteJob.objects.get(job=job, created_by=user)
        except FavouriteJob.DoesNotExist:
            favourite_job = None
    else:
        favourite_job = None

    return favourite_job != None

def get_applied_status(job : Job, user):
    if type(job) is QuerySet:
        job = job[0]
    if user.is_authenticated:
        try:
            applied_job = JobApplication.objects.get(job=job, created_by=user)
        except JobApplication.DoesNotExist:
            applied_job = None
    else:
        applied_job = None

    return applied_job != None
