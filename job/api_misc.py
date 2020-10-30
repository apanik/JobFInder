import mimetypes
import uuid
from random import randint
import pdfkit
from django.contrib.auth.models import User
from django.core.files import File
from django.core.files.base import ContentFile
from django.db.models import Count, F, Prefetch
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.utils import json
from rest_framework.views import APIView

from messaging.models import Notification
from p7.models import populate_user_info, is_professional, populate_user_info_request, populate_user_info_querydict
from p7.pagination import P7Pagination
from p7.settings_dev import SITE_URL
from pro.api_pro_core import profile_create_with_user_create, profile_completeness
from pro.models import Professional, ProfessionalSkill, ProfessionalEducation, WorkExperience, Portfolio, Membership, \
    Certification, Reference
from pro.serializers import ProfessionalSerializer, JobApplicantSerializer
from pro.utils import save_recent_activity
from resources.strings_pro import EMAIL_EXIST_ERROR_MSG
from .models import FavouriteJob
from settings.models import Settings
from .serializers import *
from .utils import favourite_job_counter, applied_job_counter, sendAccessRequestToEmail, sendVerificationRequestToEmail
from rest_framework.parsers import FileUploadParser
from rest_framework import status


@api_view(["POST"])
def toggle_favourite(request):
    data = {}
    job_data = json.loads(request.body)

    if job_data:
        try:
            job = Job.objects.select_related('company').get(job_id=job_data['job_id'])
        except Job.DoesNotExist:
            job = None
        try:
            favourite_jobs = FavouriteJob.objects.filter(created_by=request.user.id, job=job_data['job_id'])
        except FavouriteJob.DoesNotExist:
            favourite_jobs = None
        if not favourite_jobs:
            favourite_job = FavouriteJob(job_id=job_data['job_id'])
            populate_user_info(request, favourite_job, False, False)
            favourite_job.save()
            favourite_job_counter(job)

            save_recent_activity(request.user.id, 'apply_com', )
            if job.company.user_id:
                save_recent_activity(job.company.user_id, 'apply_com')

            data = {
                'code': HTTP_200_OK,
                "result": {
                    "user": {
                        "job": job_data['job_id'],
                        "status": 'Saved'
                    }
                }
            }
        elif favourite_jobs:
            favourite_jobs.delete()
            favourite_job_counter(job)
            data = {
                'code': HTTP_200_OK,
                "result": {
                    "user": {
                        "job": job_data['job_id'],
                        "status": 'Removed'
                    }
                }
            }
    return Response(data)


class JobApplicationQuickApply(APIView):  # No Uses. Will be reviewed
    permission_classes = ()
    parser_class = (FileUploadParser)

    def post(self, request, *args, **kwargs):
        file_serializer = JobApplySerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobApply(APIView):
    permission_classes = ()
    parser_class = (FileUploadParser)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and is_professional(request.user):
            current_user_id = request.user.id
            pro_id = Professional.objects.get(user_id=current_user_id).id
        else:
            resp = profile_create_with_user_create(request._request)
            if resp.data["code"] == 500:
                return resp
            current_user_id = resp.data["result"]['user']['user_id']
            user = User.objects.get(id=current_user_id)
            user.is_active = True
            user.save()
            pro_id = resp.data["result"]['user']['professional_id']
            request.user.id = current_user_id
        req_data = request.data.copy()
        req_data['pro'] = pro_id
        populate_user_info_querydict(request, req_data, False, False)
        job_application_serializer = JobApplySerializer(data=req_data)
        if job_application_serializer.is_valid():
            job_application_serializer.save()
            # TODO
            # save_recent_activity(request.user.id, 'apply', 'Job applied')
            job = Job.objects.select_related('company__user').get(job_id=request.data["job"])
            applied_job_counter(job)

            save_recent_activity(request.user.id, 'apply_pro', )
            if job.company.user_id:
                save_recent_activity(job.company.user_id, 'apply_com')

            return Response(job_application_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(job_application_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobApplicationAPI(APIView):
    permission_classes = ()
    parser_class = (FileUploadParser)
    template = get_template('public_profile_pdf.html')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and is_professional(request.user):
            current_user_id = request.user.id
        else:
            current_user_id = None

        pro_obj = Professional.objects.get(user_id=current_user_id)
        resp = profile_completeness(request._request)
        user_profile_completeness = resp.data['percent_of_profile_completeness']
        settings_minimum_profile_completeness = Settings.objects.values('minimum_profile_completeness')[0][
            'minimum_profile_completeness']

        if user_profile_completeness < settings_minimum_profile_completeness:
            return Response({'details': 'Please complete your profile with necessary and authentic information.'},status=status.HTTP_400_BAD_REQUEST)

        if JobApplication.objects.filter(job=request.data['job'], pro=pro_obj):
            return Response({'details': 'Already applied for this job'}, status=status.HTTP_400_BAD_REQUEST)

        queryset = Professional.objects.filter(user_id=current_user_id).prefetch_related(
            Prefetch('educations',
                     queryset=ProfessionalEducation.objects.filter(is_archived=False).order_by('-enrolled_date')),
            Prefetch('skills',
                     queryset=ProfessionalSkill.objects.filter(is_archived=False).order_by('skill_name')),
            Prefetch('work_experiences',
                     queryset=WorkExperience.objects.filter(is_archived=False).order_by('-start_date')),
            Prefetch('portfolios',
                     queryset=Portfolio.objects.filter(is_archived=False).order_by('created_at')),
            Prefetch('memberships',
                     queryset=Membership.objects.filter(is_archived=False).order_by('created_at')),
            Prefetch('certifications',
                     queryset=Certification.objects.filter(is_archived=False).order_by('-issue_date')),
            Prefetch('references',
                     queryset=Reference.objects.filter(is_archived=False).order_by('created_at'))
        )
        html = self.template.render({'data': queryset, 'SITE_URL': SITE_URL})
        options = {
            'page-size': "A4",
            'encoding': "UTF-8",
            "enable-local-file-access": None,
            "viewport-size": "1024x768",
        }

        resume = pdfkit.from_string(html, False, options=options)
        filename = 'resume-' + str(uuid.uuid4()) + '.pdf'
        req_data = request.data.copy()
        company = Job.objects.get(job_id=req_data['job']).company
        req_data['pro'] = pro_obj.id
        req_data['resume'] = ContentFile(resume, name=filename)
        populate_user_info_querydict(request, req_data, False, False)
        job_application_serializer = JobApplySerializer(data=req_data)

        if job_application_serializer.is_valid():
            job_application_obj = job_application_serializer.save()
            # TODO
            # save_recent_activity(request.user.id, 'apply', 'Job applied')
            job = Job.objects.select_related('company__user').get(job_id=request.data["job"])
            # applied_job_counter(job)

            ##Create notification
            # if (company.user):
            #     notification = Notification()
            #     notification.title = 'job notification'
            #     notification.message = job_application_obj.id
            #     notification.recipient = company.user.id
            #     notification.is_read = False
            #     populate_user_info(request, notification, False, False)
            #     notification.save()

            save_recent_activity(request.user.id, 'apply_pro', )
            if job.company.user_id:
                save_recent_activity(job.company.user_id, 'apply_com')

            return Response(job_application_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(job_application_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# No Uses. Will be reviewed
@api_view(["POST"])
def apply_online(request):
    job_data = json.loads(request.body)

    try:
        job = Job.objects.get(job_id=job_data['job_id'])
    except Job.DoesNotExist:
        return HTTP_404_NOT_FOUND

    try:
        JobApplication(JobApplication.objects.get(created_by=request.user.id, job=job))
    except JobApplication.DoesNotExist:
        pro = Professional.objects.get(user_id=request.user.id)
        job_application = JobApplication(job=job, pro=pro)
        populate_user_info(request, job_application, False, False)
        job_application.save()
        applied_job_counter(job)
        data = {
            "job": job_data['job_id'],
            "status": 'Saved'
        }
    return Response(data)


class MarkShortlistUpdateView(generics.UpdateAPIView):
    serializer_class = JobApplicationUpdateSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = JobApplication.objects.filter(
            job__company__user_id=user.id
        ).annotate(application_status_name=F('application_status__name'))
        return queryset


@api_view(["GET"])
def get_shortlisted_applicants(request, job_id):
    queryset = Professional.objects.filter(
        applied_pros__job_id=job_id,
        applied_pros__is_shortlisted=True
    ).annotate(is_shortlisted=F('applied_pros__is_shortlisted')
               ).annotate(application_notes=F('applied_pros__application_notes')
                          ).annotate(application_status=F('applied_pros__application_status')
                                     ).annotate(application_status_name=F('applied_pros__application_status__name')
                                                ).annotate(application_id=F('applied_pros__id')
                                                           ).prefetch_related(Prefetch('skills',
                                                                                       queryset=ProfessionalSkill.objects.filter(
                                                                                           is_archived=False).order_by(
                                                                                           'skill_name'))
                                                                              ).order_by('-created_at')

    paginator = P7Pagination()
    result_page = paginator.paginate_queryset(queryset, request)
    serializer = JobApplicantSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(["GET"])
def get_all_applicants(request, job_id):
    queryset = Professional.objects.filter(
        applied_pros__job_id=job_id,
        applied_pros__is_approved=True
        # Q(applied_jobs__created_by=current_user_id),
    ).annotate(is_shortlisted=F('applied_pros__is_shortlisted')
               ).annotate(application_notes=F('applied_pros__application_notes')
                          ).annotate(application_status=F('applied_pros__application_status')
                                     ).annotate(application_status_name=F('applied_pros__application_status__name')
                                                ).annotate(application_id=F('applied_pros__id')
                                                           ).prefetch_related(Prefetch('skills',
                                                                                       queryset=ProfessionalSkill.objects.filter(
                                                                                           is_archived=False).order_by(
                                                                                           'skill_name'))
                                                                              ).order_by('-created_at')

    paginator = P7Pagination()
    result_page = paginator.paginate_queryset(queryset, request)
    serializer = JobApplicantSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


# TODO: call as private method in job search
@api_view(["POST"])
@permission_classes(())
def save_trending_keywords(request):
    search_data = json.loads(request.body)

    if request.user_agent.is_mobile is True:
        device_name = 'Mobile'
    elif request.user_agent.is_tablet is True:
        device_name = 'Tablet'
    elif request.user_agent.is_pc is True:
        device_name = 'Computer'
    browser_name = request.user_agent.browser.family
    os_name = request.user_agent.os.family

    search_data.update([('device', device_name), ('browser', browser_name), ('operating_system', os_name)])

    if search_data['keyword']:
        key_obj = TrendingKeywords(**search_data)
        key_obj.save()
        return Response(HTTP_200_OK)


@api_view(["POST"])
@permission_classes(())
def request_for_access(request):
    req_data = request.data
    support_response = sendAccessRequestToEmail(req_data['email'], req_data['company_name'], req_data['phone'],
                                                req_data['person_name'], req_data['company_role'],
                                                req_data['contact_info'])
    verification_code = randint(100000, 999999)
    company_response = sendVerificationRequestToEmail(req_data['email'], verification_code, req_data['person_name'],
                                                      req_data['company_name'])
    if support_response.status_code and company_response.status_code:
        data = {
            'status': 'success',
            'code': 200
        }
    return HttpResponse(json.dumps(data), content_type='application/json')


class DownloadAttachmentAPIView(generics.RetrieveAPIView):
    permission_classes = ()

    def get(self, request, id, format=None):
        job_application_obj = JobApplication.objects.get(id=id)
        if job_application_obj.attachment:
            fl_path = job_application_obj.attachment.path
            filename = job_application_obj.attachment.name
            fl = open(fl_path, 'rb')
            mime_type, _ = mimetypes.guess_type(fl_path)
            response = HttpResponse(fl, content_type=mime_type)
            response['Content-Disposition'] = "attachment; filename=%s" % filename
            return response
        else:
            return Response({'details': 'File Not Found'}, status=status.HTTP_404_NOT_FOUND)


class DownloadResumeAPIView(generics.RetrieveAPIView):
    permission_classes = ()

    def get(self, request, id, format=None):
        job_application_obj = JobApplication.objects.get(id=id)
        if job_application_obj.resume:
            fl_path = job_application_obj.resume.path
            filename = job_application_obj.resume.name
            fl = open(fl_path, 'rb')
            mime_type, _ = mimetypes.guess_type(fl_path)
            response = HttpResponse(fl, content_type=mime_type)
            response['Content-Disposition'] = "attachment; filename=%s" % filename
            return response
        else:
            return Response({'details': 'File Not Found'}, status=status.HTTP_404_NOT_FOUND)
