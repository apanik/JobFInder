from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter
from django_filters import Filter
from rangefilter.filter import DateRangeFilter

from job.models import JobApplication
from p7.admin import P7Admin
from pro.models import Professional, WorkExperience, Institute, Nationality, Religion, Major, Organization, \
    CertificateName, ProfessionalEducation, ProfessionalSkill, Portfolio, Membership, Reference, Certification, \
    RecentActivity, EducationLevel, MembershipOrganization, CertifyingOrganization


@admin.register(Professional)
class ProfesssionalAdmin(P7Admin):
    date_hierarchy = 'created_at' # Top filter
    search_fields = ['full_name__icontains', 'email__icontains']
    list_filter = (
        ('created_at', DateRangeFilter),
        ('industry_expertise', RelatedDropdownFilter)
    )

    def total_applied(self, obj):
        try:
            return JobApplication.objects.filter(pro__id=obj.id).count()
        except:
            return ""

    list_display = ['full_name', 'email','total_applied', 'created_at']


@admin.register(Institute)
class InstituteAdmin(P7Admin):
    list_display = ['name', 'created_by', 'created_at']


@admin.register(Nationality)
class NationalityAdmin(P7Admin):
    list_display = ['name', 'created_by', 'created_at']


@admin.register(Religion)
class ReligionAdmin(P7Admin):
    list_display = ['name', 'created_by', 'created_at']


@admin.register(Major)
class MajorAdmin(P7Admin):
    list_display = ['name', 'created_by', 'created_at']


@admin.register(EducationLevel)
class EducationLevelAdmin(P7Admin):
    list_display = ['name', 'created_by', 'created_at']


@admin.register(Organization)
class OrganizationAdmin(P7Admin):
    list_display = ['name', 'created_by', 'created_at']


@admin.register(MembershipOrganization)
class MembershipOrganizationAdmin(P7Admin):
    list_display = ['name', 'created_by', 'created_at']


@admin.register(CertifyingOrganization)
class CertifyingOrganizationAdmin(P7Admin):
    list_display = ['name', 'created_by', 'created_at']


@admin.register(CertificateName)
class CertificateNameAdmin(P7Admin):
    list_display = ['name', 'created_by', 'created_at']


@admin.register(ProfessionalEducation)
class ProfessionalEducationAdmin(P7Admin):
    def pro_email(self, obj):
        return obj.professional.email

    list_display = ['professional', 'pro_email', 'degree_text', 'institution_text', 'created_at']


@admin.register(ProfessionalSkill)
class ProfessionalSkillAdmin(P7Admin):
    def pro_email(self, obj):
        return obj.professional.email

    list_display = ['professional',  'pro_email', 'skill_name', 'created_at']


@admin.register(Portfolio)
class PortfolioAdmin(P7Admin):
    def pro_email(self, obj):
        return obj.professional.email

    list_display = ['professional', 'pro_email', 'name', 'created_at']


@admin.register(Membership)
class MembershipAdmin(P7Admin):
    def pro_email(self, obj):
        return obj.professional.email

    list_display = ['professional', 'pro_email', 'organization', 'position_held', 'created_at']


@admin.register(Reference)
class ReferenceAdmin(P7Admin):
    def pro_email(self, obj):
        return obj.professional.email

    list_display = ['professional', 'pro_email', 'description', 'created_at']


@admin.register(Certification)
class CertificationAdmin(P7Admin):
    def pro_email(self, obj):
        return obj.professional.email

    list_display = ['professional', 'pro_email', 'certificate_name', 'created_at']


# @admin.register(RecentActivity)
# class RecentActivityAdmin(P7Admin):
#     pass


@admin.register(WorkExperience)
class WorkExperienceAdmin(P7Admin):
    def pro_email(self, obj):
        return obj.professional.email

    list_display = ['professional',  'pro_email', 'company_text', 'created_at']




