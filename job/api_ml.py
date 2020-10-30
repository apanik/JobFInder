from django.db.models import Q, Count, Max, FilteredRelation
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from job.models import Job
from job.serializers import JobSerializer, JobSerializerAllField, JobUpdateSerializer, JobSerializerAdmin
from p7.models import is_professional, populate_user_info_request
from p7.pagination import P7Pagination
from p7.permissions import StaffPermission
from job.utils import job_slug_generator


class MlJobAPI(RetrieveAPIView):
    required_privilege = 'job.view_job'
    permission_classes = [StaffPermission]
    serializer_class = JobSerializerAllField

    def get_object(self):
        return get_object_or_404(
            Job.objects.filter(
                job_id = self.kwargs['id']
            ).select_related(
                'company'
            ).prefetch_related(
                'job_skills'
            )
        )


class JobCreateView(CreateAPIView):
    required_privilege = 'job.add_job'
    permission_classes = [StaffPermission]
    serializer_class = JobSerializerAdmin

    def post(self, request, *args, **kwargs):
        populate_user_info_request(request, False, False)
        return super().post(request, *args, **kwargs)


class MlJobUpdateView(UpdateAPIView):
    required_privilege = 'job.change_job'
    permission_classes = [StaffPermission]
    serializer_class = JobSerializerAdmin

    def put(self, request, *args, **kwargs):
        populate_user_info_request(request, True, False)
        return super().put(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(
            Job.objects.filter(
                job_id = self.kwargs['id']
            )
        )

class AdminJobList(ListAPIView):
    required_privilege = 'job.view_job'
    permission_classes = [StaffPermission]
    pagination_class = P7Pagination
    serializer_class = JobSerializerAllField

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        datePosted = request.GET.get('datePosted')
        status = request.GET.get('status')
        job_type = request.GET.get('job_type')
        category = request.GET.get('category')

        queryset = Job.objects.filter(
            is_archived=False
        )

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
            queryset = queryset.filter(post_date__gt=datePosted)

        if job_type:
            queryset = queryset.filter(job_type=job_type)

        return queryset

class SlugRegenerateAPI(APIView):
    required_privilege = 'job.change_job'
    permission_classes = [StaffPermission]
    def put(self, request):
        requested_job_ids : list = request.data["job_id"]
        processed_jobs = []
        failed_jobs = []
        for job_id in requested_job_ids:
            try:
                job = Job.objects.get(job_id=job_id)
                generated_slug = job_slug_generator(job)
                job.slug = generated_slug
                job.save()
                processed_jobs.append({
                    "id": job_id,
                    "slug": job.slug
                })
            except:
                failed_jobs.append(job_id)

        return Response({
            'processed_jobs': processed_jobs,
            'failed_jobs': failed_jobs
        })