from django.urls import path,include

from pro.api import professional_signup_email_verification, job_alert, job_alert_notification, EducationObject, \
    recent_activity
from pro.api_dashboard import skill_job_chart, info_box_api
from pro.api_pro_core import change_password, profile_completeness, check_professional_exist, \
    profile_create_with_user_create, ProfessionalDetail, ProfessionalPublicRetrieve, ProfessionalUpdateView, \
    ProfessionalUpdatePartial, ApplicantDetail
from pro.api_pro_details import professional_education_save, EducationUpdateDelete, professional_skill_save, \
    SkillUpdateDelete, professional_workexperience_save, WorkExperienceUpdateDelete, professional_portfolio_save, \
    PortfolioUpdateDelete, professional_membership_save, MembershipUpdateDelete, professional_certification_save, \
    CertificationUpdateDelete, professional_reference_save, ReferenceUpdateDelete, SkillObject
from pro.api_pro_related import EmailSubscriptionUpdateView, ReligionList, NationalityList, OrganizationList, MajorList, \
    InstituteList, CertificateNameList, InstituteSearch, EducationLevelList, MembershipOrganizationList, \
    CertifyingOrganizationList, MembershipOrganizationSearch, CertifyingOrganizationSearch

urlpatterns = [
    path('pro/change-password/', change_password),
    path('pro/dashboard/skill/', skill_job_chart),
    path('pro/dashboard/infobox/', info_box_api),
    path('pro/profile-completeness/', profile_completeness),
    path('pro/check-professional-exist/', check_professional_exist),  # Public API

    path('professional/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('professional/signup-email-verification/<str:token>', professional_signup_email_verification , name='code-verify'),

    path('professional/create_with_user/', profile_create_with_user_create), # Public API
    path('professional/profile/', ProfessionalDetail.as_view()),
    path('applicant/profile/<str:slug>/', ApplicantDetail.as_view()),
    path('pro/public-profile/<str:slug>/', ProfessionalPublicRetrieve.as_view()),  # Public API

    path('professional/profile_update/<str:pk>/', ProfessionalUpdateView.as_view()),
    path('professional/job_alert/', job_alert),
    path('professional/job_alert_notification/', job_alert_notification), # Public API
    path('professional/profile_update_partial/', ProfessionalUpdatePartial.as_view()),
    path('professional/professional_education/', professional_education_save),
    path('professional/professional_education/<str:pk>/', EducationUpdateDelete.as_view()),
    path('professional/professional_skill/', professional_skill_save, name='professional-skill'),
    path('professional/professional_skill/<str:pk>/', SkillUpdateDelete.as_view()),
    path('professional/professional_work_experience/', professional_workexperience_save),
    path('professional/professional_work_experience/<str:pk>/', WorkExperienceUpdateDelete.as_view()),
    path('professional/professional_portfolio/', professional_portfolio_save),
    path('professional/professional_portfolio/<str:pk>/', PortfolioUpdateDelete.as_view()),
    path('professional/professional_membership/', professional_membership_save),
    path('professional/professional_membership/<str:pk>/', MembershipUpdateDelete.as_view()),
    path('professional/professional_certification/', professional_certification_save),
    path('professional/professional_certification/<str:pk>/', CertificationUpdateDelete.as_view()),
    path('professional/professional_reference/', professional_reference_save),
    path('professional/professional_reference/<str:pk>/', ReferenceUpdateDelete.as_view()),
    path('professional/professional_education_object/<str:pk>/', EducationObject.as_view()),
    path('professional/religion/', ReligionList.as_view()),
    path('professional/nationality/', NationalityList.as_view()),
    path('professional/organization/', OrganizationList.as_view()),
    path('professional/membership-organization/', MembershipOrganizationList.as_view()),
    path('professional/certifying-organization/', CertifyingOrganizationList.as_view()),
    path('professional/major/', MajorList.as_view()),
    path('professional/education_level/', EducationLevelList.as_view()),
    path('professional/institute/list/', InstituteList.as_view()),
    path('professional/institute/search/', InstituteSearch.as_view()),
    path('professional/membership_organization/search/', MembershipOrganizationSearch.as_view()),
    path('professional/certifying_organization/search/', CertifyingOrganizationSearch.as_view()),
    path('professional/certificate_name/', CertificateNameList.as_view()),
    path('professional/professional_skill_object/<str:pk>/', SkillObject.as_view()),
    path('professional/pro_recent_activity/', recent_activity),
    path('professional/email-subscription-on-off/', EmailSubscriptionUpdateView.as_view())
]