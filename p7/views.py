from django.db.models import Prefetch
from django.shortcuts import redirect
from django.views.generic import TemplateView

from p7.settings_dev import SITE_URL
from pro.models import Professional, ProfessionalEducation, ProfessionalSkill, WorkExperience, Portfolio, Membership, \
    Certification, Reference


class HomeView(TemplateView):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        header, footer = get_header_footer(request)
        return super().get(request, *args, **kwargs, header=header, footer=footer)

class GoogleSigninView(TemplateView):
    template_name = "google-signin.html"

    def get(self, request, *args, **kwargs):
        header, footer = get_header_footer(request)
        return super().get(request, *args, **kwargs, header=header, footer=footer)


class AboutUsView(TemplateView):
    template_name = "about_us.html"

    def get(self, request, *args, **kwargs):
        header, footer = get_header_footer(request)
        return super().get(request, *args, **kwargs, header=header, footer=footer)


class CareerAdviceView(TemplateView):
    template_name = "career_advice.html"

    def get(self, request, *args, **kwargs):
        header, footer = get_header_footer(request)
        return super().get(request, *args, **kwargs, header=header, footer=footer)


class CareerAdviceDetailView(TemplateView):
    template_name = "career_advice_details.html"

    def get(self, request, *args, **kwargs):
        header, footer = get_header_footer(request)
        return super().get(request, *args, **kwargs, header=header, footer=footer)


class ContactUsView(TemplateView):
    template_name = "contact_us.html"

    def get(self, request, *args, **kwargs):
        header, footer = get_header_footer(request)
        return super().get(request, *args, **kwargs, header=header, footer=footer)


class JobListView(TemplateView):
    template_name = "job-list.html"

    def get(self, request, *args, **kwargs):
        q = request.GET.get('q', '')
        category = request.GET.get('category', '')
        skill = request.GET.get('skill', '')
        salaryMin = request.GET.get('salaryMin', 0)
        salaryMax = request.GET.get('salaryMax', 1000000)
        experienceMin = request.GET.get('experienceMin', 0)
        experienceMax = request.GET.get('experienceMax', 10)
        unspecified_salary = request.GET.get('unspecified_salary', 1)
        sort = request.GET.get('sort')
        header, footer = get_header_footer(request)
        unspecified_salary = int(unspecified_salary)
        if unspecified_salary == 1:
            unspecified_salary = 'checked'
        else:
            unspecified_salary = ''

        return super().get(request, *args, **kwargs, header=header, footer=footer,
                           q=q, category=category, skill=skill, salaryMin=salaryMin,
                           salaryMax=salaryMax, experienceMin=experienceMin, experienceMax=experienceMax,
                           unspecified_salary=unspecified_salary, sort=sort)


class JobDetailView(TemplateView):
    template_name = "job-details.html"

    def get(self, request, *args, **kwargs):
        header, footer = get_header_footer(request)
        return super().get(request, *args, **kwargs, header=header, footer=footer)


class ProDashboardView(TemplateView):
    template_name = "dashboard.html"

    def get(self, request, *args, **kwargs):
        header, footer = get_header_footer(request)
        return super().get(request, *args, **kwargs, header=header, footer=footer)


class ProEditProfile(TemplateView):
    template_name = "pro_edit_profile.html"

    def get(self, request, *args, **kwargs):
        header, footer = get_header_footer(request)
        return super().get(request, *args, **kwargs, header=header, footer=footer)


class PublicProfileView(TemplateView):
    template_name = "public_view_profile.html"

    def get(self, request, *args, **kwargs):
        header, footer = get_header_footer(request)
        return super().get(request, *args, **kwargs, header=header, footer=footer)

class ApplicantProfileView(TemplateView):
    template_name = "applicant_view_profile.html"

    def get(self, request, *args, **kwargs):
        header, footer = get_header_footer(request)
        return super().get(request, *args, **kwargs, header=header, footer=footer)


class ProProfileView(TemplateView):
    template_name = "pro_view_profile.html"

    def get(self, request, *args, **kwargs):
        header, footer = get_header_footer(request)
        return super().get(request, *args, **kwargs, header=header, footer=footer)


class FavoriteJobsView(TemplateView):
    template_name = "favourite_jobs.html"

    def get(self, request, *args, **kwargs):
        header, footer = get_header_footer(request)
        return super().get(request, *args, **kwargs, header=header, footer=footer)


class AppliedJobsView(TemplateView):
    template_name = "applied_jobs.html"

    def get(self, request, *args, **kwargs):
        header, footer = get_header_footer(request)
        return super().get(request, *args, **kwargs, header=header, footer=footer)


class ProRecentActivity(TemplateView):
    template_name = "pro_recent_activity.html"

    def get(self, request, *args, **kwargs):
        header, footer = get_header_footer(request)
        return super().get(request, *args, **kwargs, header=header, footer=footer)


class PrivacyPolicyView(TemplateView):
    template_name = "privacy_policy.html"

    def get(self, request, *args, **kwargs):
        header, footer = get_header_footer(request)
        return super().get(request, *args, **kwargs, header=header, footer=footer)


class TermsAndConditionsView(TemplateView):
    template_name = "terms-and-condition.html"

    def get(self, request, *args, **kwargs):
        header, footer = get_header_footer(request)
        return super().get(request, *args, **kwargs, header=header, footer=footer)


class FAQView(TemplateView):
    template_name = "FAQ.html"

    def get(self, request, *args, **kwargs):
        header, footer = get_header_footer(request)
        return super().get(request, *args, **kwargs, header=header, footer=footer)


class RequestForAccessView(TemplateView):
    template_name = "request_for_access.html"

    def get(self, request, *args, **kwargs):
        header, footer = get_header_footer(request)
        return super().get(request, *args, **kwargs, header=header, footer=footer)


class CompanyDashboardView(TemplateView):
    template_name = "company_dashboard.html"

    def get(self, request, *args, **kwargs):
        header, footer = get_header_footer(request)
        return super().get(request, *args, **kwargs, header=header, footer=footer)


class CompanyEditProfileView(TemplateView):
    template_name = "company_edit_profile.html"

    def get(self, request, *args, **kwargs):
        header, footer = get_header_footer(request)
        return super().get(request, *args, **kwargs, header=header, footer=footer)


class CompanyManageJobsView(TemplateView):
    template_name = "company_manage_jobs.html"

    def get(self, request, *args, **kwargs):
        header, footer = get_header_footer(request)
        return super().get(request, *args, **kwargs, header=header, footer=footer)


class CompanyJobDetailView(TemplateView):
    template_name = "company-job-details.html"

    def get(self, request, *args, **kwargs):
        header, footer = get_header_footer(request)
        return super().get(request, *args, **kwargs, header=header, footer=footer)


class CompanyManageCandidatesView(TemplateView):
    template_name = "company_manage_candidate.html"

    def get(self, request, *args, **kwargs):
        header, footer = get_header_footer(request)
        return super().get(request, *args, **kwargs, header=header, footer=footer)


class CompanyDetailsView(TemplateView):
    template_name = "company_details.html"

    def get(self, request, *args, **kwargs):
        header, footer = get_header_footer(request)
        return super().get(request, *args, **kwargs, header=header, footer=footer)


class CompanyPostJobView(TemplateView):
    template_name = "post-job.html"

    def get(self, request, *args, **kwargs):
        header, footer = get_header_footer(request)
        return super().get(request, *args, **kwargs, header=header, footer=footer)


class CompanyUpdateJobView(TemplateView):
    template_name = "update-job.html"

    def get(self, request, *args, **kwargs):
        header, footer = get_header_footer(request)
        return super().get(request, *args, **kwargs, header=header, footer=footer)


class ComRecentActivity(TemplateView):
    template_name = "company_recent_activity.html"

    def get(self, request, *args, **kwargs):
        header, footer = get_header_footer(request)
        return super().get(request, *args, **kwargs, header=header, footer=footer)


def get_header_footer(request):
    header = 'layout/_header_anonymous.html'
    footer = 'layout/_footer_anonymous.html'
    if request.COOKIES.get('user_type'):
        if request.COOKIES['user_type'] == 'company':
            header = 'layout/_header_company.html'
            footer = 'layout/_footer_company.html'
        elif request.COOKIES['user_type'] == 'professional':
            header = 'layout/_header_professional.html'
            footer = 'layout/_footer_professional.html'
    return header, footer


# class CompanyMessagesView(TemplateView):
#     template_name = "company_messages.html"
#     def get(self, request, *args, **kwargs):
#         header, footer = get_header_footer(request)
#         return super().get(request, *args, **kwargs, header=header, footer=footer)


def redirct_app_store(request):
    return redirect('https://jobxprss.com/')


def redirct_play_store(request):
    return redirect('https://play.google.com/store/apps/details?id=com.ishraak.jobxprss')
