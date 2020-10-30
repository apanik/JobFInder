from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import User
from django.db import connection
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template.response import TemplateResponse
from django.urls import path
from django.utils.html import format_html
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter
from rangefilter.filter import DateRangeFilter

from job.forms import JobModelForm, CompanyModelForm
from job.models import Company, Experience, Qualification, Gender, Industry, Job, Currency, Skill, JobSource, \
    JobCategory, JobGender, ApplicationStatus, City
from job.models import TrendingKeywords, JobApplication
from p7.admin import P7Admin
from p7.models import is_moderator


@admin.register(Job)
class JobAdmin(P7Admin):
    form = JobModelForm
    change_form_template = 'admin/job_change_form.html'
    save_on_top = True
    filter_horizontal = ('job_skills',) # Many to many field
    list_display = ['title', 'company', 'created_at',  'post_date', 'created_by', 'status' ]
    search_fields = ['title__icontains', 'company__name__icontains']
    date_hierarchy = 'post_date' # Top filter
    list_per_page = 15
    list_filter = (
        ('created_at', DateRangeFilter),
        ('post_date', DateRangeFilter),
        ('status', DropdownFilter),
        ('job_source_1', RelatedDropdownFilter),
        ('created_by', DropdownFilter),
        ('is_archived', DropdownFilter)
    )
    fields = [
        'locked_by',
        ('title','status', 'featured'),
        'company',
        ('address','job_category','application_deadline'),
        ('job_gender','vacancy','experience'),
        ('salary','salary_min','salary_max','currency'),
        'salary_option',
        'description','responsibilities','education','qualification',
        'additional_requirements','other_benefits',
        ('job_area','job_city','job_country'),'company_profile',
        ('company_area','company_city','company_country'),
        ('job_site','job_nature','job_type'),'job_skills',
        ('job_source_1','job_url_1'),
        ('job_source_2','job_url_2'),
        ('job_source_3','job_url_3'),
        ('created_by_name', 'created_at', 'created_from'),
        ('modified_by_name', 'modified_at', 'modified_from'),
        ('archived_by_name', 'archived_at', 'archived_from'),
        ('posted_by_name', 'post_date'),
        ('reviewed_by_name', 'review_date'),
        ('approved_by_name', 'approve_date'),
        ('published_by_name', 'publish_date',),
        'raw_content',
        ('slug', 'applied_count', 'favorite_count'),
        'is_archived',
    ]
    readonly_fields = [
        'slug', 'applied_count', 'favorite_count',
        'created_by_name', 'created_at', 'created_from',
        'modified_by_name', 'modified_at', 'modified_from',
        'archived_by_name', 'archived_at', 'archived_from',
        'posted_by_name',
        'reviewed_by_name', 'review_date',
        'approved_by_name', 'approve_date',
        'published_by_name', 'publish_date',
        'job_country', 'company_country'
    ]

    def created_by_name(self, obj):
        try:
            return User.objects.get(id = obj.created_by).get_full_name()
        except:
            return ""

    def modified_by_name(self, obj):
        try:
            return User.objects.get(id = obj.modified_by).get_full_name()
        except:
            return ""

    def archived_by_name(self, obj):
        try:
            return User.objects.get(id = obj.archived_by).get_full_name()
        except:
            return ""

    def posted_by_name(self, obj):
        try:
            return User.objects.get(id = obj.posted_by).get_full_name()
        except:
            return ""

    def reviewed_by_name(self, obj):
        try:
            return User.objects.get(id = obj.reviewed_by).get_full_name()
        except:
            return ""

    def approved_by_name(self, obj):
        try:
            return User.objects.get(id = obj.approved_by).get_full_name()
        except:
            return ""


    def published_by_name(self, obj):
        try:
            return User.objects.get(id = obj.published_by).get_full_name()
        except:
            return ""

    def view_on_site(self, obj):
        return 'https://jobxprss.com/job-detail/' + obj.slug

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('job_post/', self.job_post, name='job_post'),
        ]
        return my_urls + urls

    def job_post(self, request):
        context = dict()
        if request.user.id:
            print(request.user.username )
            return TemplateResponse(request, "admin/job_post.html", context)
        else:
            return redirect('/admin/login/')


@admin.register(Company)
class CompanyAdmin(P7Admin):
    form = CompanyModelForm
    list_display = ['name', 'address', 'basis_membership_no', 'email',
                    'web_address', 'organization_head','year_of_eastablishment',
                    ]
    search_fields = ['name__icontains', 'basis_membership_no__icontains', 'email__icontains', 'web_address__icontains',
                     'organization_head__icontains', 'organization_head_number__icontains'
                     ]
    fields = ['name', 'slug', 'address', 'area', 'city', 'country',
        'company_name_bdjobs', 'company_name_facebook', 'company_name_google',
        'basis_membership_no', 'year_of_eastablishment', 'company_profile',
        'company_contact_no_one', 'company_contact_no_two', 'company_contact_no_three',
        'email', 'web_address', 'organization_head', 'organization_head_designation',
        'organization_head_number', 'legal_structure_of_this_company',
        'total_number_of_human_resources', 'no_of_it_resources', 'contact_person',
        'contact_person_designation', 'contact_person_mobile_no',
        'contact_person_email', 'user', 'profile_picture',
        'latitude', 'longitude', 'featured',
        ('created_by_name', 'created_at', 'created_from'),
        ('modified_by_name', 'modified_at', 'modified_from'),
        ('archived_by_name', 'archived_at', 'archived_from'),
        'is_archived',
    ]
    readonly_fields = [
        'country',
        'created_by_name', 'created_at', 'created_from',
        'modified_by_name', 'modified_at', 'modified_from',
        'archived_by_name', 'archived_at', 'archived_from',
    ]

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ['name']
        return self.readonly_fields

    def created_by_name(self, obj):
        try:
            return User.objects.get(id = obj.created_by).get_full_name()
        except:
            return ""

    def modified_by_name(self, obj):
        try:
            return User.objects.get(id = obj.modified_by).get_full_name()
        except:
            return ""

    def archived_by_name(self, obj):
        try:
            return User.objects.get(id = obj.archived_by).get_full_name()
        except:
            return ""

    def save_model(self, request, obj, form, change):
        if obj.city and len(obj.city.split(',')) == 2:
            obj.country = obj.city.split(',')[0].strip()

        super().save_model(request, obj, form, change)


    def change_name(self, request, queryset):
        if 'apply' in request.POST:
            old_names = request.POST.getlist("_selected_action")
            new_names = request.POST.getlist("new_name")
            for i, old_name in enumerate(old_names):
                new_name = new_names[i]
                with connection.cursor() as cursor:
                    sql = f"""
                        SET foreign_key_checks = 0;
                        update companies set name='{new_name}' where name='{old_name}';
                        update jobs set company_id='{new_name}' where company_id='{old_name}';
                        update work_experiences set company='{new_name}' where company='{old_name}';
                        SET foreign_key_checks = 1;
                    """
                    cursor.execute(sql)
            self.message_user(request, "{} names changed".format(queryset.count()))
            return HttpResponseRedirect(request.get_full_path())
        return render(request, 'admin/change_name.html', context={"models": queryset})

    change_name.short_description = "Change Name"

    actions = ['change_name']

    class Media:
        if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
            css = {
                'all': ('css/admin/location_picker.css',),
            }
            js = (
                'https://maps.googleapis.com/maps/api/js?&libraries=places&key={}'.format(settings.GOOGLE_MAPS_API_KEY),
                'js/admin/location_picker.js',
            )

@admin.register(TrendingKeywords)
class TrendingKeywordsAdmin(P7Admin):
    list_display = ['keyword', 'location', 'device', 'browser', 'operating_system', 'created_at']
    search_fields = ['keyword', 'location', 'device', 'browser', 'operating_system', 'created_at']

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(JobApplication)
class JobApplicationAdmin(P7Admin):
    date_hierarchy = 'created_at' # Top filter
    search_fields = ['pro__full_name__icontains', 'pro__email__icontains', 'job__title__icontains', 'job__company__name__icontains']
    list_filter = (
        ('created_at', DateRangeFilter),
        ('job__job_category', RelatedDropdownFilter)
    )

    def job_link(self, obj: JobApplication):
        return format_html(f'<a target="_blank" href="https://jobxprss.com/job-detail/{obj.job.slug}">{obj.job.title}</a>')

    def pro_link(self, obj):
        return format_html(f'<a target="_blank" href="https://jobxprss.com/pro/{obj.pro.slug}">{obj.pro.full_name}</a>')

    def com_link(self, obj):
        return format_html(f'<a target="_blank" href="https://jobxprss.com/company-details/{obj.job.company}">{obj.job.company}</a>')

    def edit_link(self, obj):
        return "Edit"

    job_link.allow_tags = True
    pro_link.allow_tags = True
    com_link.allow_tags = True

    list_display = ['pro_link', 'job_link', 'com_link', 'created_at', 'is_approved', 'is_shortlisted', 'edit_link']
    list_display_links = ['edit_link']

    def approve(self, request, queryset):
        for application in queryset:
            application.is_approved = True
            application.save()
        self.message_user(request, "{} application(s) approved".format(queryset.count()))
        return HttpResponseRedirect(request.get_full_path())

    approve.short_description = "Approve"

    def shortlist(self, request, queryset):
        for application in queryset:
            application.is_shortlisted = True
            application.save()
        self.message_user(request, "{} application(s) shortlisted".format(queryset.count()))
        return HttpResponseRedirect(request.get_full_path())

    shortlist.short_description = "Shortlist"

    actions = ['approve', 'shortlist']

@admin.register(JobCategory)
class JobCategoryAdmin(P7Admin):
    list_display = ['name', 'created_by', 'created_at']


@admin.register(JobGender)
class JobGenderAdmin(P7Admin):
    list_display = ['name', 'created_by', 'created_at']


@admin.register(JobSource)
class JobSourceAdmin(P7Admin):
    list_display = ['name', 'description', 'url', 'created_by', 'created_at']
    fields = [
        'name', 'description', 'url',
        ('created_by_name', 'created_at', 'created_from'),
        ('modified_by_name', 'modified_at', 'modified_from'),
        ('archived_by_name', 'archived_at', 'archived_from'),
    ]
    readonly_fields = [
        'created_by_name', 'created_at', 'created_from',
        'modified_by_name', 'modified_at', 'modified_from',
        'archived_by_name', 'archived_at', 'archived_from',
    ]

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ['name']
        return self.readonly_fields

    def created_by_name(self, obj):
        try:
            return User.objects.get(id = obj.created_by).get_full_name()
        except:
            return ""

    def modified_by_name(self, obj):
        try:
            return User.objects.get(id = obj.modified_by).get_full_name()
        except:
            return ""

    def archived_by_name(self, obj):
        try:
            return User.objects.get(id = obj.archived_by).get_full_name()
        except:
            return ""

    def change_name(self, request, queryset):
        if 'apply' in request.POST and is_moderator(request.user):
            old_names = request.POST.getlist("_selected_action")
            new_names = request.POST.getlist("new_name")
            for i, old_name in enumerate(old_names):
                new_name = new_names[i]
                with connection.cursor() as cursor:
                    sql = f"""
                        SET foreign_key_checks = 0;
                        update job_sources set name='{new_name}' where name='{old_name}';
                        update jobs set job_source_1='{new_name}' where job_source_1='{old_name}';
                        update jobs set job_source_2='{new_name}' where job_source_2='{old_name}';
                        update jobs set job_source_3='{new_name}' where job_source_3='{old_name}';
                        SET foreign_key_checks = 1;
                    """
                    cursor.execute(sql)
            self.message_user(request, "{} names changed".format(queryset.count()))
            return HttpResponseRedirect(request.get_full_path())
        return render(request, 'admin/change_name.html', context={"models": queryset})

    change_name.short_description = "Change Name"

    actions = ['change_name']

@admin.register(Experience)
class ExperienceAdmin(P7Admin):
    list_display = ['name', 'created_by', 'created_at']


@admin.register(Qualification)
class QualificationAdmin(P7Admin):
    list_display = ['name', 'created_by', 'created_at']


@admin.register(Gender)
class GenderAdmin(P7Admin):
    list_display = ['name', 'created_by', 'created_at']


@admin.register(Industry)
class IndustryAdmin(P7Admin):
    list_display = ['name', 'created_by', 'created_at']


@admin.register(Currency)
class CurrencyAdmin(P7Admin):
    list_display = ['name', 'created_by', 'created_at']


@admin.register(Skill)
class SkillAdmin(P7Admin):
    list_display = ['name', 'created_by', 'created_at']


@admin.register(ApplicationStatus)
class ApplicationStatusAdmin(P7Admin):
    list_display = ['name', 'created_by', 'created_at']


@admin.register(City)
class CityAdmin(P7Admin):
    list_display = ['name', 'created_by', 'created_at']


