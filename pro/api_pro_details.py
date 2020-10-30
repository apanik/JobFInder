import base64
import json
import uuid
from decimal import Decimal
from datetime import datetime

from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from rest_framework import generics, serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from job.models import Skill, Company
from job.serializers import SkillSerializer, CompanySerializer
from p7.models import populate_user_info, populate_user_info_request
from p7.permissions import ProfessionalPermission
from pro.models import Membership, Certification, Portfolio, WorkExperience, ProfessionalEducation, Institute, Major, \
    ProfessionalSkill, Reference, Professional, EducationLevel, MembershipOrganization, CertifyingOrganization
from pro.serializers import InstituteNameSerializer, MajorSerializer, ProfessionalSkillSerializer, \
    CertificationSerializer, MembershipSerializer, ReferenceSerializer, ProfessionalEducationSerializer, \
    WorkExperienceSerializer, PortfolioSerializer, EducationLevelSerializer,MembershipOrganizationNameSerializer, \
    CertifyingOrganizationNameSerializer
from resources.strings_pro import ARCHIVED_FALSE, ARCHIVED_TRUE


@api_view(["POST"])
@permission_classes([ProfessionalPermission])
def professional_education_save(request):
    data = json.loads(request.body)
    professional_id = Professional.objects.get(user=request.user).id
    data['professional_id'] = professional_id
    if 'degree_text' not in data or not data['degree_text']:
        raise serializers.ValidationError('Degree is required')
    if 'institution_text' not in data or not data['institution_text']:
        raise serializers.ValidationError('Institute is required')
    if 'enrolled_date' in data and 'graduation_date' in data:
        if datetime.strptime(data['enrolled_date'], '%Y-%m-%d') > datetime.strptime(data['graduation_date'], '%Y-%m-%d'):
            raise serializers.ValidationError('Enrolled date cannot be greater then graduation date')

    key_obj = ProfessionalEducation(**data)
    populate_user_info(request, key_obj, False, False)
    key_obj.save()
    if 'institution_id' in data and data['institution_id'] is not None:
        data['institution_obj'] = InstituteNameSerializer(Institute.objects.get(pk=data['institution_id'])).data
    if 'major_id' in data and data['major_id'] is not None:
        data['major_obj'] = MajorSerializer(Major.objects.get(pk=data['major_id'])).data
    if 'education_level_id' in data and data['education_level_id'] is not None:
        data['education_level_obj'] = EducationLevelSerializer(EducationLevel.objects.get(pk=data['education_level_id'])).data
    data['id'] = key_obj.id
    data['degree_text'] = data["degree_text"]
  #  data['education_level'] = data["education_level"]
    return Response(data)


@api_view(["POST"])
@permission_classes([ProfessionalPermission])
def professional_skill_save(request):
    data = json.loads(request.body)
    professional_id = Professional.objects.get(user=request.user).id
    data['professional_id'] = professional_id
    skill_name_id = data['skill_name_id']
    pro_skill_obj_with_archive = ProfessionalSkill.objects.filter(professional_id=professional_id, skill_name_id=skill_name_id, is_archived=ARCHIVED_TRUE)
    pro_skill_obj_without_archive = ProfessionalSkill.objects.filter(professional_id=professional_id, skill_name_id=skill_name_id, is_archived=ARCHIVED_FALSE)
    key_obj = ProfessionalSkill(**data)
    populate_user_info(request, key_obj, False, False)

    if pro_skill_obj_with_archive.count() > 1 and not pro_skill_obj_without_archive:
        pro_skill_obj_with_archive.delete()
        key_obj.save()
        data['skill_obj'] = SkillSerializer(Skill.objects.get(pk=data['skill_name_id'])).data
        data['id'] = key_obj.id

    elif pro_skill_obj_with_archive.count() == 1 :
        pro_skill_obj = pro_skill_obj_with_archive.first()
        pro_skill_obj.is_archived = ARCHIVED_FALSE
        pro_skill_obj.save()
        data['skill_obj'] = SkillSerializer(Skill.objects.get(pk=data['skill_name_id'])).data
        data['id'] = key_obj.id

    elif not pro_skill_obj_with_archive and not pro_skill_obj_without_archive:
        key_obj.save()
        data['skill_obj'] = SkillSerializer(Skill.objects.get(pk=data['skill_name_id'])).data
        data['id'] = key_obj.id
    else:
        raise serializers.ValidationError("Duplicate Entry")

    return Response(data)


@api_view(["POST"])
@permission_classes([ProfessionalPermission])
def professional_workexperience_save(request):
    data = json.loads(request.body)
    professional_id = Professional.objects.get(user=request.user).id
    data['professional_id'] = professional_id
    key_obj = WorkExperience(**data)
    populate_user_info(request, key_obj, False, False)
    key_obj.save()
    data['id'] = key_obj.id
    if 'company_id' in data and data['company_id'] is not None:
        data['company_obj'] = CompanySerializer(Company.objects.get(pk=data['company_id'])).data
    return Response(data)


@api_view(["POST"])
@permission_classes([ProfessionalPermission])
def professional_portfolio_save(request):
    data = json.loads(request.body)
    professional_id = Professional.objects.get(user=request.user).id
    data['professional_id'] = professional_id
    if 'image' in data:
        img_base64 = data['image']
        if img_base64:
            format, imgstr=img_base64.split(';base64,')
            ext = format.split('/')[-1]
            filename = str(uuid.uuid4()) + '-professional.' + ext
            image_data = ContentFile(base64.b64decode(imgstr), name=filename)
            fs = FileSystemStorage()
            filename = fs.save(filename, image_data)
            uploaded_file_url = fs.url(filename)
            data['image'] = uploaded_file_url
    key_obj = Portfolio(**data)
    populate_user_info(request, key_obj, False, False)
    key_obj.save()
    data['id'] = key_obj.id
    return Response(data)


@api_view(["POST"])
@permission_classes([ProfessionalPermission])
def professional_membership_save(request):
    data = json.loads(request.body)
    professional_id = Professional.objects.get(user=request.user).id
    data['professional_id'] = professional_id
    key_obj = Membership(**data)
    populate_user_info(request, key_obj, False, False)
    key_obj.save()
    if 'organization_key_id' in data and data['organization_key_id'] is not None:
        data['organization_obj'] = MembershipOrganizationNameSerializer(MembershipOrganization.objects.get(pk=data['organization_key_id'])).data
    data['id'] = key_obj.id
    return Response(data)


@api_view(["POST"])
@permission_classes([ProfessionalPermission])
def professional_certification_save(request):
    data = json.loads(request.body)
    professional_id = Professional.objects.get(user=request.user).id
    data['professional_id'] = professional_id
    key_obj = Certification(**data)
    populate_user_info(request, key_obj, False, False)
    key_obj.save()
    if 'organization_key_id' in data and data['organization_key_id'] is not None:
        data['organization_obj'] = CertifyingOrganizationNameSerializer(CertifyingOrganization.objects.get(pk=data['organization_key_id'])).data
    data['id'] = key_obj.id
    return Response(data)


@api_view(["POST"])
@permission_classes([ProfessionalPermission])
def professional_reference_save(request):
    data = json.loads(request.body)
    professional_id = Professional.objects.get(user=request.user).id
    data['professional_id'] = professional_id
    key_obj = Reference(**data)
    populate_user_info(request, key_obj, False, False)
    key_obj.save()
    data['id'] = key_obj.id
    return Response(data)



class ReferenceUpdateDelete(GenericAPIView, UpdateModelMixin):
    permission_classes = [ProfessionalPermission]
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer

    def get_object(self):
        return get_object_or_404(Reference.objects.filter(
            created_by=self.request.user.id, pk=self.kwargs.get('pk')
        ))

    def put(self, request,pk, *args, **kwargs):
        professional_id = Professional.objects.get(user=request.user).id
        request.data['professional_id'] = professional_id
        populate_user_info_request(request, True, request.data.get('is_archived'))
        self.partial_update(request, *args, **kwargs)
        prof_obj = ReferenceSerializer(Reference.objects.get(pk=pk)).data
        return Response(prof_obj)


class EducationUpdateDelete(GenericAPIView, UpdateModelMixin):
    permission_classes = [ProfessionalPermission]
    queryset = ProfessionalEducation.objects.all()
    serializer_class = ProfessionalEducationSerializer

    def get_object(self):
        return get_object_or_404(ProfessionalEducation.objects.filter(
            created_by=self.request.user.id, pk=self.kwargs.get('pk')
        ))

    def put(self, request,pk, *args, **kwargs):
        professional_id = Professional.objects.get(user=request.user).id
        request.data['professional_id'] = professional_id
        if "education_level" in request.data:
            request.data["education_level_id"] = request.data["education_level"]
            del request.data["education_level"]
        if "degree_text" in request.data:
            request.data["degree_text"] = request.data["degree_text"]
            del request.data["degree_text"]
        if "institution_id" in request.data:
            request.data["institution"] = request.data["institution_id"]
            del request.data["institution_id"]
        if "major_id" in request.data:
            request.data["major"] = request.data["major_id"]
            del request.data["major_id"]
        if 'is_ongoing' in request.data and request.data['is_ongoing'] == True:
            request.data['graduation_date'] = None
        populate_user_info_request(request, True, request.data.get('is_archived'))
        if 'institution_text' in request.data:
            try:
                Institute.objects.get(name= request.data['institution_text'])
            except Institute.DoesNotExist:
                request.data['institution'] = None
        self.partial_update(request, *args, **kwargs)
        prof_obj = ProfessionalEducationSerializer(ProfessionalEducation.objects.get(pk=pk)).data
        if 'institution' in request.data and request.data['institution'] is not None:
            prof_obj['institution_obj'] = InstituteNameSerializer(
                Institute.objects.get(pk=request.data['institution'])).data
        else:
            if prof_obj['institution']:
                prof_obj['institution_obj'] = InstituteNameSerializer(
                    Institute.objects.get(pk=prof_obj['institution'])).data
        if 'education_level_id' in request.data and request.data['education_level_id'] is not None:
            prof_obj['education_level_obj'] = EducationLevelSerializer(
                EducationLevel.objects.get(pk=request.data['education_level_id'])).data
        if 'major_id' in request.data and request.data['major_id'] is not None:
            prof_obj['major_obj'] = MajorSerializer(Major.objects.get(pk=request.data['major_id'])).data
        else:
            if prof_obj['major']:
                prof_obj['major_obj'] = MajorSerializer(Major.objects.get(pk=prof_obj['major'])).data

        return Response(prof_obj)


class SkillUpdateDelete(GenericAPIView, UpdateModelMixin):
    permission_classes = [ProfessionalPermission]
    queryset = ProfessionalSkill.objects.all()
    serializer_class = ProfessionalSkillSerializer

    def get_object(self):
        return get_object_or_404(ProfessionalSkill.objects.filter(
            created_by = self.request.user.id, pk = self.kwargs.get('pk')
        ))

    def put(self, request,pk, *args, **kwargs):
        professional_id = Professional.objects.get(user=request.user).id
        request.data['professional_id'] = professional_id
        populate_user_info_request(request, True, request.data.get('is_archived'))
        self.partial_update(request, *args, **kwargs)
        prof_obj = ProfessionalSkillSerializer(ProfessionalSkill.objects.get(pk=pk)).data
        prof_obj['rating'] = Decimal(prof_obj['rating'])
        if 'skill_name_id' in request.data:
            prof_obj['skill_obj'] = SkillSerializer(Skill.objects.get(pk=request.data['skill_name_id'])).data
        else:
            prof_obj['skill_obj'] = SkillSerializer(Skill.objects.get(pk=prof_obj['skill_name'])).data
        return Response(prof_obj)


class WorkExperienceUpdateDelete(GenericAPIView, UpdateModelMixin):
    permission_classes = [ProfessionalPermission]
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer

    def get_object(self):
        return get_object_or_404(WorkExperience.objects.filter(
            created_by=self.request.user.id, pk=self.kwargs.get('pk')
        ))

    def put(self, request,pk, *args, **kwargs):
        professional_id = Professional.objects.get(user=request.user).id
        request.data['professional_id'] = professional_id
        if "company_id" in request.data:
            request.data["company"] = request.data["company_id"]
            del request.data["company_id"]
        populate_user_info_request(request, True, request.data.get('is_archived'))
        if 'company_text' in request.data:
            try:
                Company.objects.get(name= request.data['company_text'])
            except Company.DoesNotExist:
                request.data['company'] = None
        self.partial_update(request, *args, **kwargs)
        prof_obj = WorkExperienceSerializer(WorkExperience.objects.get(pk=pk)).data
        if 'company' in request.data and request.data['company'] is not None:
            prof_obj['company_obj'] = CompanySerializer(Company.objects.get(pk=request.data['company'])).data
        return Response(prof_obj)


class PortfolioUpdateDelete(GenericAPIView, UpdateModelMixin):
    permission_classes = [ProfessionalPermission]
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

    def get_object(self):
        return get_object_or_404(Portfolio.objects.filter(
            created_by=self.request.user.id, pk=self.kwargs.get('pk')
        ))

    def put(self, request,pk, *args, **kwargs):
        professional_id = Professional.objects.get(user=request.user).id
        request.data['professional_id'] = professional_id
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
        self.partial_update(request, *args, **kwargs)
        prof_obj = PortfolioSerializer(Portfolio.objects.get(pk=pk)).data
        return Response(prof_obj)


class MembershipUpdateDelete(GenericAPIView, UpdateModelMixin):
    permission_classes = [ProfessionalPermission]
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer

    def get_object(self):
        return get_object_or_404(Membership.objects.filter(
            created_by=self.request.user.id, pk=self.kwargs.get('pk')
        ))

    def put(self, request, pk, *args, **kwargs):
        professional_id = Professional.objects.get(user=request.user).id
        request.data['professional_id'] = professional_id
        if "organization_key_id" in request.data:
            request.data["organization_key"] = request.data["organization_key_id"]
            del request.data["organization_key_id"]
        populate_user_info_request(request, True, request.data.get('is_archived'))
        if 'organization' in request.data:
            try:
                MembershipOrganization.objects.get(name= request.data['organization'])
            except MembershipOrganization.DoesNotExist:
                request.data['organization_key'] = None
        self.partial_update(request, *args, **kwargs)
        prof_obj = MembershipSerializer(Membership.objects.get(pk=pk)).data
        if 'organization_key' in request.data and request.data['organization_key'] is not None:
            prof_obj['organization_obj'] = MembershipOrganizationNameSerializer(
                MembershipOrganization.objects.get(pk=request.data['organization_key'])).data
        else:
            if prof_obj['organization_key']:
                prof_obj['organization_obj'] = MembershipOrganizationNameSerializer(
                    MembershipOrganization.objects.get(pk=prof_obj['organization_key'])).data
        return Response(prof_obj)


class CertificationUpdateDelete(GenericAPIView, UpdateModelMixin):
    permission_classes = [ProfessionalPermission]
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer

    def get_object(self):
        return get_object_or_404(Certification.objects.filter(
            created_by=self.request.user.id, pk=self.kwargs.get('pk')
        ))

    def put(self, request,pk, *args, **kwargs):
        professional_id = Professional.objects.get(user=request.user).id
        request.data['professional_id'] = professional_id
        if "organization_key_id" in request.data:
            request.data["organization_key"] = request.data["organization_key_id"]
            del request.data["organization_key_id"]
        populate_user_info_request(request, True, request.data.get('is_archived'))
        if 'organization' in request.data:
            try:
                CertifyingOrganization.objects.get(name= request.data['organization'])
            except CertifyingOrganization.DoesNotExist:
                request.data['organization_key'] = None
        self.partial_update(request, *args, **kwargs)
        prof_obj = CertificationSerializer(Certification.objects.get(pk=pk)).data
        if 'organization_key' in request.data and request.data['organization_key'] is not None:
            prof_obj['organization_obj'] = CertifyingOrganizationNameSerializer(
                CertifyingOrganization.objects.get(pk=request.data['organization_key'])).data
        else:
            if prof_obj['organization_key']:
                prof_obj['organization_obj'] = CertifyingOrganizationNameSerializer(
                    CertifyingOrganization.objects.get(pk=prof_obj['organization_key'])).data
        return Response(prof_obj)


class SkillObject(APIView):
    def get(self, request, pk):
        skill = ProfessionalSkillSerializer(get_object_or_404(ProfessionalSkill, pk=pk)).data
        skill_data = {
            'skill_info': skill,
        }
        return Response(skill_data)
