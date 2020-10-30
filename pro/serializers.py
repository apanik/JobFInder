from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from rest_framework import exceptions
from rest_framework import serializers
from rest_framework_simplejwt.serializers import PasswordField
from rest_framework_simplejwt.tokens import RefreshToken

from job.serializers import CompanyProfilePictureSerializer, CompanySerializer
from pro.models import *
from resources.strings_pro import *


class WorkExperienceDetailSerializer(serializers.ModelSerializer):
    # company = serializers.RelatedField(
    #     source='company.profile_picture', read_only=True
    # )
    company = CompanyProfilePictureSerializer(many=False)
    class Meta:
        model = WorkExperience
        fields = ('id','professional','company_text','company','designation','start_date','end_date','is_currently_working', 'description')

class ProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional
        exclude = ('password','terms_and_condition_status','signup_verification_code',)


class ProfessionalEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalEducation
        fields = '__all__'

class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = '__all__'

class ProfessionalSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalSkill
        fields = '__all__'

class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'

class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = '__all__'

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = '__all__'


class ReligionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Religion
        fields = '__all__'

class NationalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Nationality
        fields = '__all__'

class CertificateNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificateName
        fields = '__all__'

class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = '__all__'

class EducationLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationLevel
        fields = '__all__'

class OrganizationNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class CertifyingOrganizationNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertifyingOrganization
        fields = '__all__'

class MembershipOrganizationNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipOrganization
        fields = '__all__'

class InstituteNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institute
        fields = '__all__'

class InstituteSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institute
        fields = '__all__'



class CustomTokenSerializer(serializers.Serializer):
    token = serializers.CharField()

class TokenObtainCustomSerializer(serializers.Serializer):
    username_field = User.USERNAME_FIELD

    default_error_messages = {
        'no_active_account': _(ACTIVE_ACCOUNT_ERROR)
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'] = serializers.CharField()
        self.fields['password'] = PasswordField()

    def validate(self, attrs):
        authenticate_kwargs = {
            self.username_field: attrs['email'],
            'password': attrs['password'],
        }
        try:
            authenticate_kwargs['request'] = self.context['request']
        except KeyError:
            pass

        self.user = authenticate(**authenticate_kwargs)

        # Prior to Django 1.10, inactive users could be authenticated with the
        # default `ModelBackend`.  As of Django 1.10, the `ModelBackend`
        # prevents inactive users from authenticating.  App designers can still
        # allow inactive users to authenticate by opting for the new
        # `AllowAllUsersModelBackend`.  However, we explicitly prevent inactive
        # users from authenticating to enforce a reasonable policy and provide
        # sensible backwards compatibility with older Django versions.
        if self.user is None or not self.user.is_active:
            raise exceptions.AuthenticationFailed(
                self.error_messages['no_active_account'],
                'no_active_account',
            )

        return {}

class ProfessionalEducationPublicSerializer(serializers.ModelSerializer):
    institution = InstituteNameSerializer(many=False)
    class Meta:
        model = ProfessionalEducation
        fields = (['degree_text', 'institution_text', 'cgpa', 'major_text', 'enrolled_date', 'institution',
        'graduation_date','description', 'is_ongoing'])


class ProfessionalSkillPublicSerializer(serializers.ModelSerializer):
    skill =  serializers.CharField(source='skill_name.name')
    class Meta:
        model = ProfessionalSkill
        fields = (['skill', 'rating', 'verified_by_skillcheck'])


class JobApplicantSkillSerializer(serializers.ModelSerializer):
    skill =  serializers.CharField(source='skill_name.name')
    class Meta:
        model = ProfessionalSkill
        fields = (['skill'])


class WorkExperiencePublicSerializer(serializers.ModelSerializer):
    company = CompanyProfilePictureSerializer()
    class Meta:
        model = WorkExperience
        fields = (["company_text", "company", "designation", "start_date", "end_date", "is_currently_working", "description"])


class PortfolioPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = (["name", "image", "description"])


class MembershipPublicSerializer(serializers.ModelSerializer):
    organization_key = MembershipOrganizationNameSerializer(many=False)
    class Meta:
        model = Membership
        fields = (["organization", "organization_key", "position_held", "start_date", "end_date", "membership_ongoing", "description"])


class CertificationPublicSerializer(serializers.ModelSerializer):
    organization_key = CertifyingOrganizationNameSerializer(many=False)
    class Meta:
        model = Certification
        fields = (["organization_key", "organization", "certificate_name", "has_expiry_period", "issue_date", "expiry_date", "credential_id", "credential_url"])


class ReferencePublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = (["description"])

class ProfessionalPublicSerializer(serializers.ModelSerializer):
    educations = ProfessionalEducationPublicSerializer(many=True)
    skills = ProfessionalSkillPublicSerializer(many=True)
    work_experiences = WorkExperiencePublicSerializer(many=True)
    portfolios = PortfolioPublicSerializer(many=True)
    memberships = MembershipPublicSerializer(many=True)
    certifications = CertificationPublicSerializer(many=True)
    references = ReferencePublicSerializer(many=True)
    class Meta:
        model = Professional
        fields = (['full_name', 'about_me', 'image', 'facebook_id', 'twitter_id', 'linkedin_id',
                   'industry_expertise', 'address', 'status', 'experience', 'gender', 'qualification',
                   'educations', 'skills', 'work_experiences', 'portfolios', 'memberships',
                   'certifications', 'references', 'current_designation', 'current_company'])


class JobApplicantSerializer(serializers.ModelSerializer):
    application_notes = serializers.CharField()
    application_status = serializers.CharField()
    application_status_name = serializers.CharField()
    application_id = serializers.CharField()
    is_shortlisted = serializers.BooleanField()
    skills = JobApplicantSkillSerializer(many=True)
    class Meta:
        model = Professional
        fields = ('application_id','full_name','image','application_notes','application_status','application_status_name',
                  'is_shortlisted', 'user', 'current_designation', 'current_company', 'experience', 'skills', 'slug')

class TokenObtainCustomPairSerializer(TokenObtainCustomSerializer):
    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)
        professional = Professional.objects.get(user=self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['email'] = self.user.email
        data['user_id'] = self.user.id
        data['full_name'] = professional.full_name
        data['professional_id'] = professional.id
        data['professional_image'] = professional.image

        return data


class SkillJobChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalSkill
        fields = ['skill_name',]

class NationalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Nationality
        fields = '__all__'


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class EmailSubscriptionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional
        fields = ['job_alert_status']

