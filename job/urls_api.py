from django.urls import path

from job.api_company import list_company_by_name, CompanyList, CompanyUpdateView, company_info_box_api, \
    company_recent_activity, company_job_application_chart, CompanyListWithoutPagination, FeaturedCompanyList, \
    CompanyRetrieveView
from job.api_job_core import JobAPI, CompanyJobUpdateView, CompanyJobCreateAPI, CompanyJobAPI, \
    CompanyJobUnpublishAPI, CompanyJobPublishAPI, CompanyJobPostAPI
from job.api_job_kpi import TopFavouriteList, TopCategoryList, TopSkillList, TopCompanyList, TrendingKeywordList, \
    get_vital_stats
from job.api_job_list import similar_jobs, applied_jobs, favourite_jobs, recent_jobs, JobSearchAPI, CompanyJobSearchAPI
from job.api_job_related import get_job_site_list, JobSourceList, get_job_nature_list, get_job_type_list, \
    get_job_status_list, get_job_creator_type_list, JobCategoryList, JobGenderList, IndustryList, JobTypeList, \
    ExperienceList, CurrencyList, QualificationList, GenderList, SkillList, get_salary_range, \
    ApplicationStatusList, CityList, SkillSearch
from job.api_misc import apply_online, save_trending_keywords, \
    toggle_favourite, MarkShortlistUpdateView, JobApplicationQuickApply, get_all_applicants, get_shortlisted_applicants, \
    JobApply, request_for_access, JobApplicationAPI
from job.api_ml import MlJobAPI, AdminJobList, JobCreateView, MlJobUpdateView, SlugRegenerateAPI

urlpatterns = [
    path('job/search/', JobSearchAPI.as_view()), # Public API
    path('company/job/search/', CompanyJobSearchAPI.as_view()),
    path('job/recent/', recent_jobs), # Public API
    path('job/applied/', applied_jobs),
    path('job/favourite/', favourite_jobs),
    path('job/similar/<str:identifier>/', similar_jobs), # Public API
    path('job/get/<slug:slug>/', JobAPI.as_view()), # Public API
    path('company/job/get/<slug:slug>/', CompanyJobAPI.as_view()),

    path('job-source/list/', JobSourceList.as_view()),
    path('job-category/list/', JobCategoryList.as_view()),
    path('job-gender/list/', JobGenderList.as_view()), # Public API
    path('job-site/list/', get_job_site_list),
    path('job-nature/list/', get_job_nature_list),
    path('job-type/list/', get_job_type_list),
    path('job-status/list/', get_job_status_list),
    path('job-creator-type/list', get_job_creator_type_list),
    path('city/list/', CityList.as_view()), # Public API
    path('company-shortlist/mark/<str:pk>/', MarkShortlistUpdateView.as_view()),
    path('application_status/list/', ApplicationStatusList.as_view()),
    path('application/list/<str:job_id>/', get_all_applicants),
    path('application/shortlist/<str:job_id>/', get_shortlisted_applicants),

    path('company/update/', CompanyUpdateView.as_view()),
    path('company/list', CompanyList.as_view()),
    path('company/list/featured', FeaturedCompanyList.as_view()),
    path('company/list/without-pagination/', CompanyListWithoutPagination.as_view()),
    path('company/search/', list_company_by_name),  # Public API
    path('company/get/', CompanyRetrieveView.as_view()),  # Public API
    path('company/dashboard/infobox/', company_info_box_api),
    path('company/dashboard/chart/', company_job_application_chart),
    path('company/dashboard/recent_activity/', company_recent_activity),
    path('company/request_for_access/', request_for_access), # Public API

    path('industry/list', IndustryList.as_view()), # Public API
    path('job_type/list', JobTypeList.as_view()), # Public API
    path('experience/list', ExperienceList.as_view()), # Public API
    path('currency/list', CurrencyList.as_view()), # Public API
    path('qualification/list', QualificationList.as_view()), # Public API
    path('gender/list', GenderList.as_view()), # Public API

    path('job/apply/', apply_online),
    path('job/favourite/toggle', toggle_favourite),

    path('job/top-favourites/', TopFavouriteList.as_view()), # Public API
    path('job/top-categories/', TopCategoryList.as_view()), # Public API
    path('job/top-skills/', TopSkillList.as_view()), # Public API
    path('job/top-companies/', TopCompanyList.as_view()), # Public API
    path('job/trending_keywords/', TrendingKeywordList.as_view()), # Public API

    path('skill/list/', SkillList.as_view()), # Public API
    path('skill/search/', SkillSearch.as_view()), # Public API
    path('job/salary-range/', get_salary_range), # Public API

    path('job/update/<str:pk>/', CompanyJobUpdateView.as_view()),
    path('job/update/unpublish/<str:pk>/', CompanyJobUnpublishAPI.as_view()),
    path('job/update/publish/<str:pk>/', CompanyJobPublishAPI.as_view()),
    path('job/update/post/<str:pk>/', CompanyJobPostAPI.as_view()),
    path('job/create/', CompanyJobCreateAPI.as_view()),
    path('job/trending_keywords/save/', save_trending_keywords), # Public API
    path('vital_stats/get/', get_vital_stats), # Public API
    # TODO: will be removed later
    path('apply/', JobApply.as_view()),  # Public API
    path('job_apply/', JobApplicationAPI.as_view()),  # Public API
    path('slug/generate/', SlugRegenerateAPI.as_view()),

    path('admin/job/list/', AdminJobList.as_view()),
    path('admin/job/get/<str:id>/', MlJobAPI.as_view()),
    path('admin/job/create/', JobCreateView.as_view()),
    path('admin/job/update/<str:id>/', MlJobUpdateView.as_view()),
]

