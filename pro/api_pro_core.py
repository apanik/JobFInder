import base64
import datetime
import uuid

import rest_framework
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import Group, User
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.core.mail import EmailMultiAlternatives
from django.db.models import Prefetch
from django.dispatch import receiver
from django.http import Http404, HttpRequest
from django.template.loader import render_to_string
from django_rest_passwordreset.signals import reset_password_token_created
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
from rest_framework.utils import json
from rest_framework.views import APIView

from job.models import JobApplication
from job.serializers import SkillSerializer
from p7.auth import ProfessionalAuthentication
from p7.models import is_professional_registered, get_user_address, populate_user_info_request
from p7.permissions import ProfessionalPermission, CompanyPermission
from p7.settings_dev import SITE_URL
from p7.utils import send_email
from resources.strings_pro import EMAIL_EXIST_ERROR_MSG, USER_ID_NOT_EXIST, WRONG_OLD_PASSWORD_MSG, SITE_SHORTCUT_NAME, \
    ON_TXT, PASSWORD_CHANGED_SUCCESS_MSG, FAILED_TXT, EMAIL_BLANK_ERROR_MSG, MOBILE_BLANK_ERROR_MSG, \
    PASSWORD_BLANK_ERROR_MSG, FULL_NAME_BLANK_ERROR_MSG, TAC_BLANK_ERROR_MSG
from settings.models import Settings
from .models import ProfessionalEducation, ProfessionalSkill, WorkExperience, Portfolio, Membership, Certification, \
    Reference, Religion, Nationality, Professional
from .serializers import ProfessionalSerializer, ReligionSerializer, NationalitySerializer, \
    WorkExperienceDetailSerializer, InstituteNameSerializer, MajorSerializer, ProfessionalPublicSerializer, \
    EducationLevelSerializer,MembershipOrganizationNameSerializer, CertifyingOrganizationNameSerializer
from .utils import sendSignupEmail, save_recent_activity


@api_view(["POST"])
@permission_classes(())
def profile_create_with_user_create(request):
    profile_data = request.data
    data_error = {
        'status': FAILED_TXT,
        'code': 500,
        "result": None
    }
    if 'email' not in profile_data or not profile_data['email']:
        data_error["message"] = EMAIL_BLANK_ERROR_MSG
        return Response(data_error)
    if 'phone' not in profile_data or not profile_data['phone']:
        data_error["message"] = MOBILE_BLANK_ERROR_MSG
        return Response(data_error)
    if 'password' not in profile_data or not profile_data['password']:
        data_error["message"] = PASSWORD_BLANK_ERROR_MSG
        return Response(data_error)
    if 'full_name' not in profile_data or not profile_data['full_name']:
        data_error["message"] = FULL_NAME_BLANK_ERROR_MSG
        return Response(data_error)
    if 'terms_and_condition_status' not in profile_data or profile_data['terms_and_condition_status'] != ON_TXT:
        data_error["message"] = TAC_BLANK_ERROR_MSG
        return Response(data_error)
    try:
        user = User.objects.get(email=profile_data['email'])
        user_exist = True
        user_active = user.is_active
    except User.DoesNotExist:
        user_exist = False
        user_active = False
    try:
        pro = Professional.objects.get(email=profile_data['email'])
        pro_exist = True
    except Professional.DoesNotExist:
        pro_exist = False

    if user_exist and user_active:
        data_error["message"] = EMAIL_EXIST_ERROR_MSG
        return Response(data_error)
    hash_password = make_password(profile_data['password'])
    if not user_exist:
        user = User(email=profile_data['email'], password=hash_password, username=profile_data['email'], is_active=0)
        user.save()
        pro_group = Group.objects.get(name='Professional')
        user.groups.add(pro_group) # or using reverse relation pro_group.user_set.add(user)
    if not pro_exist:
        pro = Professional(
            full_name=profile_data["full_name"],
            email=profile_data["email"],
            password=hash_password,
            phone=profile_data['phone'],
            terms_and_condition_status=1 if profile_data['terms_and_condition_status'] == ON_TXT else 0
        )
        pro.user_id = user.id
        pro.created_by = user.id
        pro.created_from = get_user_address(request)
        if 'alert' in profile_data:
            pro.job_alert_status = True
        pro.save()
    sendSignupEmail(profile_data['email'],pro.id, datetime.date.today)
    data = {
        'status': 'success',
        'code': HTTP_200_OK,
        "message": 'An verification link has been sent to your email address. Please open it to confirm your email '
                   'account.',
        "result": {
            "user": {
                "email": profile_data['email'],
                "user_id": user.id,
                "professional_id": pro.id
            }
        }
    }
    return Response(data)


class ProfessionalDetail(generics.ListAPIView):
    permission_classes = [ProfessionalPermission]
    def get(self, request):
        profile = get_object_or_404(Professional, user_id=request.user.id)
        pk = profile.id
        education = ProfessionalEducation.objects.filter(professional=pk ,is_archived=False).order_by('-enrolled_date')
        skills = ProfessionalSkill.objects.filter(professional=pk, is_archived=False)
        experience = WorkExperience.objects.filter(professional=pk, is_archived=False).order_by("-start_date")
        portfolio = Portfolio.objects.filter(professional=pk, is_archived=False)
        membership = Membership.objects.filter(professional_id=pk, is_archived=False)
        certification = Certification.objects.filter(professional=pk, is_archived=False).order_by("-issue_date")
        reference = Reference.objects.filter(professional=pk, is_archived=False)

        info_data = ProfessionalSerializer(profile).data
        info_data['religion_obj'] = ReligionSerializer(profile.religion).data
        info_data['nationality_obj'] = NationalitySerializer(profile.nationality).data

        work_experience_data = WorkExperienceDetailSerializer(experience, many=True).data

        edu_data = [{
            'id': edu.id,
            'degree_text': edu.degree_text,
            'institution_obj': InstituteNameSerializer(edu.institution).data,
            'institution_text': edu.institution_text,
            'education_level_obj': EducationLevelSerializer(edu.education_level).data,
            'cgpa': edu.cgpa,
            'major_obj':MajorSerializer(edu.major).data,
            'major_text':edu.major_text,
            'enrolled_date': edu.enrolled_date,
            'graduation_date': edu.graduation_date,
            'description': edu.description,
            'is_ongoing' :edu.is_ongoing
        } for edu in education]

        skill_data = [{
            'id':skill.id,
            'skill_obj': SkillSerializer(skill.skill_name).data,
            'rating': skill.rating,
            'verified_by_skillcheck': skill.verified_by_skillcheck,
        } for skill in skills]

        portfolio_data = [{
            'id': pf.id,
            'name': pf.name,
            'image': pf.image,
            'description': pf.description,
        } for pf in portfolio]

        membership_data = [{
            'id':ms.id,
            'organization': ms.organization,
            'organization_obj': MembershipOrganizationNameSerializer(ms.organization_key).data,
            'position_held': ms.position_held,
            'membership_ongoing': ms.membership_ongoing,
            'start_date': ms.start_date,
            'end_date': ms.end_date,
            'description': ms.description,
        } for ms in membership]

        certification_data = [{
            'id': cert.id,
            'certificate_name': cert.certificate_name,
            'organization': cert.organization,
            'organization_obj': CertifyingOrganizationNameSerializer(cert.organization_key).data,
            'has_expiry_period': cert.has_expiry_period,
            'issue_date': cert.issue_date,
            'expiry_date': cert.expiry_date,
            'credential_id': cert.credential_id,
            'credential_url': cert.credential_url,
        } for cert in certification]

        reference_data = [{
            'id':ref.id,
            'description':ref.description
        } for ref in reference]

        prof_data = {
            'personal_info': info_data,
            'edu_info': edu_data,
            'skill_info': skill_data,
            'experience_info': work_experience_data,
            'portfolio_info': portfolio_data,
            'membership_info': membership_data,
            'certification_info': certification_data,
            'reference_data': reference_data
        }
        return Response(prof_data)

class ApplicantDetail(APIView):
    permission_classes = [CompanyPermission]
    #todo Check if the person has applied atleast one job of this compnay.
    def get(self, request, slug):
        pro = get_object_or_404(Professional, slug=slug)
        pk = pro.id
        num_jobs = JobApplication.objects.filter(job__company__user_id=request.user.id, pro__id=pk).count()
        if num_jobs == 0:
            raise AuthenticationFailed()
        education = ProfessionalEducation.objects.filter(professional=pk ,is_archived=False).order_by('-enrolled_date')
        skills = ProfessionalSkill.objects.filter(professional=pk, is_archived=False)
        experience = WorkExperience.objects.filter(professional=pk, is_archived=False).order_by("-start_date")
        portfolio = Portfolio.objects.filter(professional=pk, is_archived=False)
        membership = Membership.objects.filter(professional_id=pk, is_archived=False)
        certification = Certification.objects.filter(professional=pk, is_archived=False).order_by("-issue_date")
        reference = Reference.objects.filter(professional=pk, is_archived=False)

        info_data = ProfessionalSerializer(pro).data
        info_data['religion_obj'] = ReligionSerializer(pro.religion).data
        info_data['nationality_obj'] = NationalitySerializer(pro.nationality).data

        work_experience_data = WorkExperienceDetailSerializer(experience, many=True).data

        edu_data = [{
            'id': edu.id,
            'degree_text': edu.degree_text,
            'institution_obj': InstituteNameSerializer(edu.institution).data,
            'institution_text': edu.institution_text,
            'education_level_obj': EducationLevelSerializer(edu.education_level).data,
            'cgpa': edu.cgpa,
            'major_obj':MajorSerializer(edu.major).data,
            'major_text':edu.major_text,
            'enrolled_date': edu.enrolled_date,
            'graduation_date': edu.graduation_date,
            'description': edu.description,
            'is_ongoing' :edu.is_ongoing
        } for edu in education]

        skill_data = [{
            'id':skill.id,
            'skill_obj': SkillSerializer(skill.skill_name).data,
            'rating': skill.rating,
            'verified_by_skillcheck': skill.verified_by_skillcheck,
        } for skill in skills]

        portfolio_data = [{
            'id': pf.id,
            'name': pf.name,
            'image': pf.image,
            'description': pf.description,
        } for pf in portfolio]

        membership_data = [{
            'id':ms.id,
            'organization': ms.organization,
            'organization_obj': MembershipOrganizationNameSerializer(ms.organization_key).data,
            'position_held': ms.position_held,
            'membership_ongoing': ms.membership_ongoing,
            'start_date': ms.start_date,
            'end_date': ms.end_date,
            'description': ms.description,
        } for ms in membership]

        certification_data = [{
            'id': cert.id,
            'certificate_name': cert.certificate_name,
            'organization': cert.organization,
            'organization_obj': CertifyingOrganizationNameSerializer(cert.organization_key).data,
            'has_expiry_period': cert.has_expiry_period,
            'issue_date': cert.issue_date,
            'expiry_date': cert.expiry_date,
            'credential_id': cert.credential_id,
            'credential_url': cert.credential_url,
        } for cert in certification]

        reference_data = [{
            'id':ref.id,
            'description':ref.description
        } for ref in reference]

        prof_data = {
            'personal_info': info_data,
            'edu_info': edu_data,
            'skill_info': skill_data,
            'experience_info': work_experience_data,
            'portfolio_info': portfolio_data,
            'membership_info': membership_data,
            'certification_info': certification_data,
            'reference_data': reference_data
        }
        return Response(prof_data)


class ProfessionalPublicRetrieve(generics.RetrieveAPIView):
    permission_classes = (())
    serializer_class = ProfessionalPublicSerializer
    def get_object(self):
        queryset = Professional.objects.filter(
            slug = self.kwargs['slug']
        ).prefetch_related(
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
        return get_object_or_404(queryset)

class ProfessionalUpdateView(APIView):
    authentication_classes = [ProfessionalAuthentication]
    def get_object(self, pk):
        try:
            return Professional.objects.get(pk=pk)
        except Professional.DoesNotExist:
            raise Http404
    def put(self, request, pk, format=None):
        profile = self.get_object(pk)
        # image uploading code start here
        if 'image' in request.data:
            img_base64 = request.data['image']
            if img_base64:
                format, imgstr = img_base64.split(';base64,')
                ext = format.split('/')[-1]
                filename = str(uuid.uuid4()) + '-professional.' + ext
                data = ContentFile(base64.b64decode(imgstr), name=filename)
                fs = FileSystemStorage()
                filename = fs.save(filename, data)
                uploaded_file_url = fs.url(filename)
                request.data['image'] = uploaded_file_url
        # end of image uploading code

        serializer = ProfessionalSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfessionalUpdatePartial(GenericAPIView, UpdateModelMixin):
    permission_classes = [ProfessionalPermission]
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer
    current_user = None

    def get_object(self):
        return get_object_or_404(Professional.objects.filter(
            user_id = self.current_user.id
        ))

    def put(self,request, *args, **kwargs,):
        self.current_user = request.user
        if 'image' in request.data:
            img_base64 = request.data['image']
            if img_base64:
                format, imgstr = img_base64.split(';base64,')
                ext = format.split('/')[-1]
                filename = str(uuid.uuid4()) + '-professional.' + ext
                data = ContentFile(base64.b64decode(imgstr), name=filename)
                fs = FileSystemStorage()
                filename = fs.save(filename, data)
                uploaded_file_url = fs.url(filename)
                request.data['image'] = uploaded_file_url
        populate_user_info_request(request, True, request.data.get('is_archived'))
        prof_obj = self.partial_update(request, *args, **kwargs).data
        save_recent_activity(request.user.id, 'profile_pro')
        if prof_obj['religion']:
            prof_obj['religion_obj'] = ReligionSerializer(Religion.objects.get(pk = prof_obj['religion'])).data
        if prof_obj['nationality']:
            prof_obj['nationality_obj'] = NationalitySerializer(Nationality.objects.get(pk = prof_obj['nationality'])).data
        return Response(prof_obj)



class CustomPasswordResetView:
    @receiver(reset_password_token_created)
    def password_reset_token_created(sender, reset_password_token, *args, **kwargs):
        """
          Handles password reset tokens
          When a token is created, an e-mail needs to be sent to the user
        """
        # send an e-mail to the user
        # Checking User Type For sending User ype in Verification URL
        try:
            if reset_password_token.user.company:
                user_type = "company"
        except:
            user_type = "professional"
        context = {
            'current_user': reset_password_token.user,
            'username': reset_password_token.user.username,
            'email': reset_password_token.user.email,
            'reset_password_url': "{}/{}/password-reset/{}".format(SITE_URL,user_type, reset_password_token.key),
            'site_name': SITE_SHORTCUT_NAME,
            'site_domain': SITE_URL
        }

        # render email text
        email_html_message = render_to_string('user_reset_password.html', context)
        email_plaintext_message = render_to_string('user_reset_password.txt', context)
        settingsObj = Settings.objects.all().first()
        recipient_list = reset_password_token.user.email
        subject_text = "Password Reset for {}".format(SITE_SHORTCUT_NAME)
        send_email(recipient_list, subject_text, email_html_message, settingsObj.sender_email_host, settingsObj.sender_email_port,
               settingsObj.no_reply_sender_host_user, settingsObj.no_reply_sender_host_password)


@api_view(["POST"])
def change_password(request):
    received_json_data = json.loads(request.body)
    user = request.user.id
    old_password = received_json_data["old_password"]
    new_password = received_json_data["new_password"]

    try:
        user_obj = User.objects.get(id=user)
    except User.DoesNotExist:
        data = {
            'status': 'failed',
            'code': HTTP_401_UNAUTHORIZED,
            "message": USER_ID_NOT_EXIST,
            "result": ''
        }
        return Response(data, HTTP_401_UNAUTHORIZED)
    status = check_password(old_password, user_obj.password)

    if not status :
        data = {
            'status': 'failed',
            'code': HTTP_401_UNAUTHORIZED,
            "message": WRONG_OLD_PASSWORD_MSG,
            "result": ''
        }
        return Response(data, HTTP_401_UNAUTHORIZED)
    else:
        new_password = make_password(new_password)
        user_obj.password = new_password
        user_obj.save()

        data = {
            'status': 'success',
            'code': HTTP_200_OK,
            "message": PASSWORD_CHANGED_SUCCESS_MSG,
            "result": {
                "user": {
                    "username": user_obj.username,
                    'user_id': user_obj.id
                }
            }
        }
    return Response(data, HTTP_200_OK)


@api_view(["GET","POST"])
def profile_completeness(request):
    pro:Professional = Professional.objects.filter(
        user = request.user
    ).prefetch_related('educations', 'work_experiences', 'skills',
        'portfolios', 'certifications', 'memberships'
    ).first()
    point = 0
    if pro.full_name: point += 10
    if pro.experience: point += 5
    if pro.facebook_id or pro.linkedin_id: point += 5
    if pro.email: point += 10
    if pro.phone: point += 10
    if pro.image: point += 10
    if pro.date_of_birth: point += 5
    if pro.job_alert_status: point += 5
    if pro.educations.filter(is_archived=False).count() > 0: point += 10
    if pro.work_experiences.filter(is_archived=False).count() > 0: point += 10
    if pro.skills.filter(is_archived=False).count() > 0: point += 10
    if pro.portfolios.filter(is_archived=False).count() > 0: point += 5
    if pro.certifications.filter(is_archived=False).count() > 0: point += 3
    if pro.memberships.filter(is_archived=False).count() > 0: point += 2

    data = {
        'percent_of_profile_completeness': point
    }
    return Response(data)


@api_view(["GET"])
@permission_classes(())
def check_professional_exist(request):
    email = request.GET.get('email')
    if is_professional_registered(email):
        status = True
    else:
        status = False
    data = {
        'email_exist': status
    }
    return Response(data)



