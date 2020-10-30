from datetime import datetime
from pprint import pprint

from django.db import connection
from django.db.models import Count, Q, Sum
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from job.models import TrendingKeywords, JobCategory, Skill, Job, Company
from job.serializers import TrendingKeywordListSerializer, TopCategoriesSerializer, TopSkillSerializer, \
    TopJobSerializer, TopCompanySerializer
from pro.models import Professional


class TrendingKeywordList(generics.ListAPIView):
    permission_classes = []
    queryset = TrendingKeywords.objects.values('keyword').annotate(key_count = Count('keyword')).order_by('-key_count')[:6]
    serializer_class = TrendingKeywordListSerializer

class TopCategoryList(generics.ListAPIView):
    permission_classes = []
    queryset = JobCategory.objects.filter(jobs__status='Published', jobs__is_archived=False
        ).annotate(num_posts=Count('jobs')
        ).order_by('-num_posts')[:16]
    serializer_class = TopCategoriesSerializer

    def get(self, request, *args, **kwargs):
        result = self.list(self, request, *args, **kwargs)
        pprint(connection.queries)
        return result


class TopSkillList(generics.ListAPIView):
    permission_classes = []
    queryset = Skill.objects.filter(skill_set__status='Published', skill_set__is_archived=False
        ).annotate(skills_count=Count('skill_set')
        ).order_by('-skills_count')[:16]
    serializer_class = TopSkillSerializer

class TopFavouriteList(generics.ListAPIView):
    permission_classes = []
    queryset = Job.objects.filter(status='Published', is_archived=False
        ).annotate(favourite_count=Count('fav_jobs')
        ).order_by('-favourite_count')[:16]
    serializer_class = TopJobSerializer

class TopCompanyList(generics.ListAPIView):
    permission_classes = []
    queryset = Company.objects.filter(jobs__status='Published', jobs__is_archived=False
        ).annotate(num_posts=Count('jobs')
        ).order_by('-num_posts')[:16]
    serializer_class = TopCompanySerializer


@api_view(["GET"])
@permission_classes(())
def get_vital_stats(self):
    companies = Company.objects.filter(
        is_archived = False
    ).count()
    num_of_vacancy = Job.objects.filter(
        status='Published'
    ).aggregate(Sum('vacancy'))
    num_of_vacancy = num_of_vacancy['vacancy__sum']

    open_jobs = Job.objects.filter(
        status='Published'
    ).count()
    data ={
        'num_of_vacancy': str(num_of_vacancy),
        'open_job' : str(open_jobs),
        'resume': str(0),
        'company_count': str(companies),
    }
    return Response(data)
