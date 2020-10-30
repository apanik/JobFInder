from rest_framework import serializers

from pro.models import Institute
from .models import Company, Job, Industry, JobType, Experience, Qualification, Gender, Currency, TrendingKeywords, \
    Skill, JobSource, JobCategory, JobGender, JobApplication, ApplicationStatus, City
from rest_framework.validators import *

class CompanyUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['address', 'basis_membership_no', 'company_profile', 'year_of_eastablishment', 'legal_structure_of_this_company',
                  'total_number_of_human_resources', 'no_of_it_resources', 'address', 'area', 'city',
                  'company_contact_no_one', 'company_contact_no_two', 'company_contact_no_three', 'organization_head',
                  'organization_head_designation','organization_head_number','contact_person','contact_person_designation','contact_person_mobile_no',
                  'contact_person_email','company_name_bdjobs','company_name_facebook','company_name_google','latitude','longitude','profile_picture']

class CompanyNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name']

class FeaturedCompanySerializer(serializers.ModelSerializer):
    num_posts = serializers.IntegerField(read_only=True)

    class Meta:
        model = Company
        fields = '__all__'

    def to_representation(self, instance):
            response = super(FeaturedCompanySerializer, self).to_representation(instance)
            if instance.profile_picture:
                response['profile_picture'] = instance.profile_picture.url
            return response


class JobListCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

    def to_representation(self, instance):
        response = super(JobListCompanySerializer, self).to_representation(instance)
        if instance.profile_picture:
            response['profile_picture'] = instance.profile_picture.url
        return response


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class CompanyProfilePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['profile_picture']

class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ['name']

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['name']

class JobTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobType
        fields = ['name']

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['name']

class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = '__all__'

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = ['name']


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']


class ApplicationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationStatus
        fields = ['id', 'name']


class CompanyJobSerializer(serializers.ModelSerializer):
    company = CompanySerializer(many=False)
    job_skills = SkillSerializer(many=True)
    class Meta:
        model = Job
        fields = ('job_id', 'title', 'status', 'company', 'job_category',
                  'application_deadline', 'job_area', 'job_city', 'job_country',
                  'job_site', 'job_nature', 'job_type' , 'address', 'vacancy','salary',
                  'created_at', 'post_date', 'slug', 'applied_count', 'favorite_count',
                  'publish_date','other_benefits', 'responsibilities', 'additional_requirements', 'description',
                  'education','job_gender','job_skills','experience','salary_min','salary_max','company_profile','salary_option','currency'
        )

class JobSerializer(serializers.ModelSerializer):
    is_favourite = serializers.BooleanField(read_only=True)
    is_applied = serializers.BooleanField(read_only=True)
    company = JobListCompanySerializer(many=False)
    applied_at = serializers.DateTimeField(read_only=True)
    favourite_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Job
        fields = ('job_id', 'title', 'status', 'company', 'job_category',
                  'application_deadline', 'job_area', 'job_city', 'job_country',
                  'job_site', 'job_nature', 'job_type' , 'address', 'vacancy',
                  'created_at', 'post_date', 'slug', 'applied_count', 'favorite_count',
                  'is_applied', 'applied_at', 'is_favourite', 'favourite_at','salary','salary_min','salary_max')

class CompnayJobCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('title', 'status', 'job_category','qualification','responsibilities','education','additional_requirements',
                  'application_deadline', 'job_area', 'job_city', 'job_country', 'description', 'experience','job_gender',
                  'job_site', 'other_benefits','company_profile', 'job_nature', 'job_type', 'vacancy','address','job_skills','salary_option')

class JobUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('title', 'status', 'job_category','qualification','responsibilities','education','additional_requirements',
                  'application_deadline', 'job_area', 'job_city', 'job_country', 'description', 'experience','job_gender',
                  'job_site', 'other_benefits','company_profile', 'job_nature', 'job_type', 'vacancy','address','job_skills','salary_min',
                  'salary_max','salary','salary_option')
class JobUpdateStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('status',)

class JobSerializerAllField(serializers.ModelSerializer):
    is_favourite = serializers.CharField(read_only=True)
    is_applied = serializers.CharField(read_only=True)
    company = CompanySerializer(many=False)
    job_skills = SkillSerializer(many=True)
    applied_at = serializers.DateTimeField(read_only=True)
    favourite_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Job
        fields = '__all__'

class JobSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

class JobSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSource
        fields = ['name']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name']

class JobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = ['name']

class JobGenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobGender
        fields = ['name']

# TODO: remove if not needed
class RecentJobSerializer(serializers.ModelSerializer):
    status = serializers.CharField()

    class Meta:
        model = Job
        fields = ['job_location', 'job_id', 'company', 'employment_status', 'title', 'created_date', 'status']


class CompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'web_address', 'company_profile']

class TrendingKeywordListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrendingKeywords
        fields = ['keyword']

class TopCategoriesSerializer(serializers.ModelSerializer):
    num_posts = serializers.IntegerField(read_only=True)
    class Meta:
        model = JobCategory
        fields= ['name', 'num_posts']

class TopCompanySerializer(serializers.ModelSerializer):
    num_posts = serializers.IntegerField(read_only=True)
    class Meta:
        model = Company
        fields= ['name', 'num_posts']



class TopSkillSerializer(serializers.ModelSerializer):
    skills_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Skill
        fields= '__all__'

class TopJobSerializer(serializers.ModelSerializer):
    favourite_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Job
        fields= ['title','favourite_count']


class JobApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = ['job', 'pro', 'attachment', 'created_by', 'created_from', 'resume', 'application_notes']

class JobApplicationUpdateSerializer(serializers.ModelSerializer):
    application_status_name = serializers.CharField(required=False)
    class Meta:
        model = JobApplication
        fields = ['id', 'is_shortlisted', 'application_notes','application_status', 'application_status_name']


