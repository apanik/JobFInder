from django.urls import path, include
from django.views.generic import TemplateView
from p7.views import PublicProfileView, ProDashboardView, ProEditProfile, ProProfileView, FavoriteJobsView, \
    AppliedJobsView, ProRecentActivity, ApplicantProfileView
from pro.api import *


urlpatterns = [
    path('professional/profile-layout/', TemplateView.as_view(template_name='layout_professional.html')),
    path('professional/applicant-profile/', ProProfileView.as_view(), name='myprofile'),
    path('professional/profile-dashboard/', ProDashboardView.as_view()),
    path('professional/signup/', TemplateView.as_view(template_name='register.html'), name='register'),
    path('professional/reset-password-successful/', TemplateView.as_view(template_name='reset-password-successful.html')),
    path('sign-out/', logout),
    path('professional/sign-in/', TemplateView.as_view(template_name='sign-in.html'), name='sign-in'),
    path('professional/reset-password/', TemplateView.as_view(template_name='forget_password.html')),
    path('professional/reset-password-email/', TemplateView.as_view(template_name='reset_email_successful.html')),
    path('professional/password-reset/<str:token>/', TemplateView.as_view(template_name='reset_password.html')),
    path('professional/terms-and-condition/', TemplateView.as_view(template_name='terms-and-condition.html')),
    path('professional/myprofile/', ProEditProfile.as_view() ,name='profile'),
    path('professional/static_urls/', StaticUrl),
    path('professional/applied-jobs/', AppliedJobsView.as_view(),name='applied_jobs'),
    path('professional/favorite-jobs/', FavoriteJobsView.as_view(),name='favourite_jobs'),
    path('change-password/', TemplateView.as_view(template_name='change_password.html'), name='change_password'),
    path('pro/<str:slug>/', PublicProfileView.as_view(), name='public_myprofile'),
    path('applicant/<str:slug>/', ApplicantProfileView.as_view(), name='public_myprofile'),
    path('professional/recent-activity/',ProRecentActivity.as_view() , name='pro_recent_activity'),
]