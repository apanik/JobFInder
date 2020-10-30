"""p7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include
from django.views.generic import TemplateView

# from p7.api import *
from django_rest_passwordreset.models import ResetPasswordToken
from rest_framework.authtoken.models import Token

from p7.settings_dev import BASE_DIR
from p7.views import HomeView, AboutUsView, CareerAdviceView, ContactUsView, PrivacyPolicyView, TermsAndConditionsView, \
    FAQView, CompanyManageJobsView, CompanyManageCandidatesView, RequestForAccessView, CompanyDetailsView, \
    redirct_play_store, redirct_app_store, GoogleSigninView
from testimonial.urls import *


def firebase_messaging_sw_js(request):
    filename = '/static/firebase-messaging-sw.js'
    jsfile = open(BASE_DIR + filename, 'rb')
    response = HttpResponse(content=jsfile)
    response['Content-Type'] = 'text/javascript'
    response['Content-Disposition'] = 'attachment; filename="firebase-messaging-sw.js"'
    return response

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('', include('job.urls')),
    path('', include('pro.urls')),
    path('', include('messaging.urls')),
    path('', include('career_advice.urls')),
    path('', include('p7.urls_api')),
    path('firebase-messaging-sw.js', firebase_messaging_sw_js),

    path('android', redirct_play_store),
    path('ios', redirct_app_store),

    path('career-advice/', CareerAdviceView.as_view(), name='career_advice'),
    path('skill-check/', TemplateView.as_view(template_name='skill_check.html'), name='skill_check'),
    path('about-us/', AboutUsView.as_view(), name='about_us'),
    path('contact-us/', ContactUsView.as_view(), name='contact_us'),
    path('request-for-access/', RequestForAccessView.as_view(), name='request_for_access'),
    path('privacy-policy/', PrivacyPolicyView.as_view(), name='privacy_policy'),
    path('terms-of-use/', TermsAndConditionsView.as_view(), name='terms-of-use'),
    path('FAQ/', FAQView.as_view(), name='FAQ'),
    path('company/manage-jobs/', CompanyManageJobsView.as_view(), name='company_manage_jobs'),
    path('company-manage-candidates/', CompanyManageCandidatesView.as_view(),name='company_manage_candidates'),
    path('company-shortlisted-candidates/', TemplateView.as_view(template_name='company_shortlisted_candidates.html'),name='company_shortlisted_candidates'),
    path('about-us-app/', TemplateView.as_view(template_name='app/about_us.html')),
    path('contact-us-app/', TemplateView.as_view(template_name='app/contact_us.html')),
    path('career-advice-app/', TemplateView.as_view(template_name='app/career_advice.html')),
    path('FAQ-app/', TemplateView.as_view(template_name='app/FAQ.html')),
    path('company-details/<str:name>/', CompanyDetailsView.as_view(),name='company_details'),
]

admin.site.unregister(Token)
admin.site.unregister(ResetPasswordToken)


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)