import uuid

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone

from job.models import Industry, Gender, JobType, Experience, Qualification, Company, Skill
from p7.models import P7Model, populate_time_info
from p7.utils import uuid_slug_generator
from p7.validators import check_valid_password, MinLengthValidator, \
    check_valid_phone_number
from resources import strings_pro


class Nationality(P7Model):
    name = models.CharField(max_length=255, )

    class Meta:
        db_table = 'nationalities'


class Institute(P7Model):
    name = models.CharField(max_length=255, )
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    class Meta:
        db_table = 'institutes'


class Organization(P7Model):
    name = models.CharField(max_length=255, )

    class Meta:
        db_table = 'organizations'


class MembershipOrganization(P7Model):
    name = models.CharField(max_length=255, )
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    class Meta:
        db_table = 'membership_organizations'


class CertifyingOrganization(P7Model):
    name = models.CharField(max_length=255, )
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    class Meta:
        db_table = 'certifying_organizations'


class Major(P7Model):
    name = models.CharField(max_length=255, )

    class Meta:
        db_table = 'majors'


class EducationLevel(P7Model):
    name = models.CharField(max_length=255, )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'education_level'


class Religion(P7Model):
    name = models.CharField(max_length=255, )

    class Meta:
        db_table = 'religions'


class CertificateName(P7Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'certificate_names'

class Professional(P7Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_column='id')
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    professional_id = models.CharField(max_length=255, blank=True, null=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=255, validators=[check_valid_phone_number], blank=True, null=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    industry_expertise = models.ForeignKey(Industry, on_delete=models.PROTECT, blank=True, null=True)
    about_me = models.TextField(null=True, blank=True)
    image = models.CharField(blank=True, null=True, max_length=500)
    terms_and_condition_status = models.BooleanField(default=False)
    password = models.CharField(max_length=255, validators=[check_valid_password, MinLengthValidator(8)])
    user = models.OneToOneField(User, on_delete=models.PROTECT, null=True, blank=True)
    signup_verification_code = models.CharField(max_length=200, blank=True, null=True)
    job_alert_status = models.BooleanField(default=False)

    father_name = models.CharField(max_length=255, blank=True, null=True)
    mother_name = models.CharField(max_length=255, blank=True, null=True)
    facebook_id = models.CharField(max_length=255, blank=True, null=True)
    twitter_id = models.CharField(max_length=255, blank=True, null=True)
    linkedin_id = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    blood_group = models.CharField(max_length=5, null=True, blank=True)
    gender = models.ForeignKey(Gender, on_delete=models.PROTECT, null=True, blank=True)
    status = models.ForeignKey(JobType, on_delete=models.PROTECT, null=True, blank=True)
    experience = models.ForeignKey(Experience, on_delete=models.PROTECT, null=True, blank=True)
    qualification = models.ForeignKey(Qualification, on_delete=models.PROTECT, null=True, blank=True)
    expected_salary_min = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    expected_salary_max = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    nationality = models.ForeignKey(Nationality, on_delete=models.PROTECT, null=True, blank=True)
    religion = models.ForeignKey(Religion, on_delete=models.PROTECT, null=True, blank=True)
    permanent_address = models.CharField(max_length=255, null=True, blank=True)
    current_location = models.CharField(max_length=255, null=True, blank=True)
    current_company = models.CharField(max_length=255, null=True, blank=True)
    current_designation = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = strings_pro.PROFESSIONAL_VERBOSE_NAME
        verbose_name_plural = strings_pro.PROFESSIONAL_VERBOSE_NAME_PLURAL
        db_table = 'professionals'
        ordering = ['-created_at']



class ProfessionalEducation(P7Model):
    professional = models.ForeignKey(Professional, on_delete=models.PROTECT, related_name='educations')
    education_level = models.ForeignKey(EducationLevel, on_delete=models.PROTECT, null=True)
    degree = models.ForeignKey(Qualification, on_delete=models.PROTECT, null=True, blank=True)
    degree_text = models.CharField(max_length=255, blank=True, null=True)
    institution = models.ForeignKey(Institute, on_delete=models.PROTECT, null=True, blank=True)
    institution_text = models.CharField(max_length=255, blank=True, null=True)
    cgpa = models.CharField(max_length=255, blank=True, null=True)
    major = models.ForeignKey(Major, on_delete=models.PROTECT, null=True, blank=True)
    major_text = models.CharField(max_length=255, blank=True, null=True)
    is_ongoing = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    enrolled_date = models.DateField(null=True, blank=True)
    graduation_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'professional_educations'


class ProfessionalSkill(P7Model):
    professional = models.ForeignKey(Professional, on_delete=models.PROTECT, related_name='skills')
    skill_name = models.ForeignKey(Skill, on_delete=models.PROTECT)
    rating = models.DecimalField(default=0, decimal_places=2, max_digits=4)
    verified_by_skillcheck = models.BooleanField(default=False)

    class Meta:
        db_table = 'professional_skills'

""" 
ProfessionalWorkExperience
"""
class WorkExperience(P7Model):
    professional = models.ForeignKey(Professional, on_delete=models.PROTECT, related_name='work_experiences')
    company_text = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, blank=True, null=True, related_name='company_pic')
    designation = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_currently_working = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'work_experiences'

""" 
ProfessionalPortfolio
"""
class Portfolio(P7Model):
    professional = models.ForeignKey(Professional, on_delete=models.PROTECT, related_name='portfolios')
    name = models.CharField(max_length=255)
    image = models.CharField(blank=True, null=True, max_length=500)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'portfolios'

""" 
ProfessionalMembership
"""
class Membership(P7Model):
    professional = models.ForeignKey(Professional, on_delete=models.PROTECT, related_name='memberships')
    organization = models.CharField(max_length=255)
    organization_key = models.ForeignKey(MembershipOrganization, on_delete=models.PROTECT, blank=True, null=True, related_name='members')
    position_held = models.CharField(max_length=255, blank=True, null=True)
    membership_ongoing = models.BooleanField(default=False)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'memberships'


""" 
ProfessionalCertification
"""
class Certification(P7Model):
    professional = models.ForeignKey(Professional, on_delete=models.PROTECT, related_name='certifications')
    certificate_name = models.CharField(max_length=255)
    organization = models.CharField(max_length=255, blank=True, null=True)
    organization_key = models.ForeignKey(CertifyingOrganization, on_delete=models.PROTECT, blank=True, null=True, related_name='members')
    has_expiry_period = models.BooleanField(default=True)
    issue_date = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    credential_id = models.CharField(max_length=255, null=True, blank=True)
    credential_url = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'certifications'

""" 
ProfessionalReference
"""
class Reference(P7Model):
    professional = models.ForeignKey(Professional, on_delete=models.PROTECT, related_name='references')
    description = models.TextField(blank=False, null=False)

    class Meta:
        db_table = 'references'


class RecentActivity(P7Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='recent_activities')
    description = models.TextField(blank=False, null=False)
    time = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'recent_activities'


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = uuid_slug_generator(instance)

pre_save.connect(populate_time_info, sender=Nationality)
pre_save.connect(populate_time_info, sender=Institute)
pre_save.connect(populate_time_info, sender=Organization)
pre_save.connect(populate_time_info, sender=CertifyingOrganization)
pre_save.connect(populate_time_info, sender=MembershipOrganization)
pre_save.connect(populate_time_info, sender=Major)
pre_save.connect(populate_time_info, sender=Religion)
pre_save.connect(slug_generator, sender=Professional)
pre_save.connect(populate_time_info, sender=Professional)
pre_save.connect(populate_time_info, sender=ProfessionalEducation)
pre_save.connect(populate_time_info, sender=ProfessionalSkill)
pre_save.connect(populate_time_info, sender=WorkExperience)
pre_save.connect(populate_time_info, sender=Portfolio)
pre_save.connect(populate_time_info, sender=Membership)
pre_save.connect(populate_time_info, sender=CertificateName)
pre_save.connect(populate_time_info, sender=Certification)
pre_save.connect(populate_time_info, sender=Reference)
pre_save.connect(populate_time_info, sender=RecentActivity)
