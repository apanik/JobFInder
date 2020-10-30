from django.db.models import Min, Max
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django_countries import countries
from job.models import JobSource, JobCategory, JobGender, Industry, JobType, Currency, Qualification, Gender, \
    Experience, Skill, Job, ApplicationStatus, City
from job.serializers import JobSourceSerializer, CurrencySerializer, JobTypeSerializer, IndustrySerializer, \
    QualificationSerializer, GenderSerializer, ExperienceSerializer, SkillSerializer, ApplicationStatusSerializer, \
    CitySerializer
from job.utils import sendAccessRequestToEmail
from resources import strings_job
from resources.strings_location import CITY_COUNTRIES


class JobSourceList(generics.ListAPIView):
    queryset = JobSource.objects.filter(
        is_archived=False
    ).order_by('name')
    serializer_class = JobSourceSerializer


class JobCategoryList(generics.ListAPIView):
    queryset = JobCategory.objects.filter(
        is_archived=False
    ).order_by('name')
    serializer_class = JobSourceSerializer


class JobGenderList(generics.ListAPIView):
    permission_classes = ()
    queryset = JobGender.objects.filter(
        is_archived=False
    ).order_by('name')
    serializer_class = JobSourceSerializer


@api_view(["GET"])
def get_job_site_list(request):
    data = [{'id': item[0], 'text': item[1]} for item in strings_job.JOB_SITES]
    return Response(data)

@api_view(["GET"])
def get_job_nature_list(request):
    data = [{'id': item[0], 'text': item[1]} for item in strings_job.JOB_NATURES]
    return Response(data)

@api_view(["GET"])
def get_job_type_list(request):
    data = [{'id': item[0], 'text': item[1]} for item in strings_job.JOB_TYPES]
    return Response(data)

@api_view(["GET"])
def get_job_status_list(request):
    data = [{'id': item[0],'text': item[1]} for item in strings_job.JOB_STATUSES]
    return Response(data)

@api_view(["GET"])
def get_job_creator_type_list(request):
    data = [{'id': item[0],'text': item[1]} for item in strings_job.JOB_CREATOR_TYPES]
    return Response(data)


class CityList(generics.ListAPIView):
    permission_classes = []
    queryset = City.objects.filter(
        is_archived=False
    ).order_by('name')
    serializer_class = CitySerializer


@api_view(["GET"])
@permission_classes(())
def get_salary_range(self):
    range_min = Job.objects.all().aggregate(Min('salary_min'))
    range_max = Job.objects.all().aggregate(Max('salary_max'))
    min_v = range_min['salary_min__min']
    max_v = range_max['salary_max__max']
    data ={
        'sr_min': str(min_v),
        'sr_max': str(max_v),
    }
    return Response(data)


class IndustryList(generics.ListAPIView):
    permission_classes = ()
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer

class JobTypeList(generics.ListAPIView):
    permission_classes = ()
    queryset = JobType.objects.all()
    serializer_class = JobTypeSerializer

class CurrencyList(generics.ListAPIView):
    permission_classes = ()
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

class ExperienceList(generics.ListAPIView):
    permission_classes = ()
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class QualificationList(generics.ListAPIView):
    permission_classes = ()
    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer

    def get_queryset(self):
        name = self.request.GET.get('name')
        if name:
            return Qualification.objects.filter(name__icontains=name).order_by('name')
        else:
            return Qualification.objects.all().order_by('name')

class GenderList(generics.ListAPIView):
    permission_classes = ()
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer

class SkillList(generics.ListCreateAPIView):
    permission_classes = ()
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ApplicationStatusList(generics.ListCreateAPIView):
    permission_classes = ()
    queryset = ApplicationStatus.objects.all()
    serializer_class = ApplicationStatusSerializer

class SkillSearch(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    def get_queryset(self):
        name = self.request.GET.get('name')
        if name:
            return Skill.objects.filter(name__icontains=name).order_by('name')
