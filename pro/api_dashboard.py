from datetime import datetime, timedelta

from django.db.models import Count
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response

from job.models import Job, FavouriteJob, JobApplication
from p7.auth import ProfessionalAuthentication
from pro.models import ProfessionalSkill, Professional
from resources.strings_pro import ARCHIVED_FALSE


@api_view(["GET"])
@authentication_classes([ProfessionalAuthentication])
def skill_job_chart(request):
    pro = Professional.objects.filter(user = request.user).first()
    last_year = datetime.now() - timedelta(days=365)
    queryset = Job.objects.filter(job_skills__professionalskill__professional_id=pro.id,job_skills__professionalskill__is_archived=ARCHIVED_FALSE, post_date__gte = last_year
    ).values_list('post_date__year', 'post_date__month'
    ).order_by(
    ).annotate(total=Count('*')
    ).order_by('post_date__year', 'post_date__month')
    data = list(queryset)
    return Response(data)


@api_view(["GET"])
@authentication_classes([ProfessionalAuthentication])
def info_box_api(request):
    user = request.user
    favourite_job = FavouriteJob.objects.filter(created_by = user.id).count()
    applied_job = JobApplication.objects.filter(pro__user_id = user.id).count()
    skills_count = ProfessionalSkill.objects.filter(created_by=user.id, is_archived=False).count()
    data ={
        'favourite_job_count': favourite_job,
        'applied_job_count': applied_job,
        'skills_count': skills_count
    }

    return Response(data)