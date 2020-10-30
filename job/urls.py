from django.urls import path
from django.views.generic import TemplateView
from p7.views import JobListView, JobDetailView, CompanyDashboardView, CompanyEditProfileView, CompanyPostJobView, \
    CompanyJobDetailView, CompanyUpdateJobView, ComRecentActivity
from .api_misc import DownloadAttachmentAPIView, DownloadResumeAPIView
from .views import *

urlpatterns = [
    path('company/update-job/<slug:slug>/', CompanyUpdateJobView.as_view(), name='update_job'),
    path('company/post-job/', CompanyPostJobView.as_view(), name='post_job'),
    path('validation-test', TemplateView.as_view(template_name='company-create.html')),
    path('job-detail/<slug:slug>/', JobDetailView.as_view()),
    path('company/job-detail/<slug:slug>/', CompanyJobDetailView.as_view()),
    path('jobs/', JobListView.as_view(), name='jobs'),
    path('company/sign-in/', TemplateView.as_view(template_name='company_sign_in_yellow_design.html'), name='company_sign'),
    path('company/reset-password/', TemplateView.as_view(template_name='company_forget_password.html'), name='company_forgot'),
    path('company/password-reset/<str:token>/', TemplateView.as_view(template_name='company_reset_password.html'), name='company_reset'),
    path('company/reset-password-successful/', TemplateView.as_view(template_name='company-reset-password-successful.html'), name='reset_success'),
    path('company/edit-profile/', CompanyEditProfileView.as_view(), name='company_edit'),
    path('company/dashboard/', CompanyDashboardView.as_view(), name='company_dashboard'),
    path('company/download-attachment/<int:id>/', DownloadAttachmentAPIView.as_view()),
    path('company/download-resume/<int:id>/', DownloadResumeAPIView.as_view()),
    path('company/recent-activity/',ComRecentActivity.as_view(),name='com_recent_activity'),
]