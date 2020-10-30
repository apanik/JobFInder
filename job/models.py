import uuid

from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Max, Min
from django.db.models.signals import pre_save, post_save, post_delete
from django.utils import timezone

from job.utils import job_slug_generator
from p7.models import P7Model, populate_time_info
from resources import strings_job


class Industry(P7Model):
    name = models.CharField(max_length=255, primary_key=True)

    class Meta:
        verbose_name = strings_job.INDUSTRY_VERBOSE_NAME
        verbose_name_plural = strings_job.INDUSTRY_VERBOSE_NAME_PLURAL
        db_table = 'industries'

    def __str__(self):
        return self.name


class JobType(P7Model):
    name = models.CharField(max_length=255, primary_key=True)

    class Meta:
        verbose_name = strings_job.JOB_TYPE_VERBOSE_NAME
        verbose_name_plural = strings_job.JOB_TYPE_VERBOSE_NAME_PLURAL
        db_table = 'job_types'

    def __str__(self):
        return self.name


class Qualification(P7Model):
    name = models.CharField(max_length=255, primary_key=True)

    class Meta:
        verbose_name = strings_job.QUALIFICATION_VERBOSE_NAME
        verbose_name_plural = strings_job.QUALIFICATION_VERBOSE_NAME_PLURAL
        db_table = 'qualifications'

    def __str__(self):
        return self.name


class Experience(P7Model):
    name = models.CharField(max_length=255, primary_key=True)

    class Meta:
        verbose_name = strings_job.EXPERIENCE_VERBOSE_NAME
        verbose_name_plural = strings_job.EXPERIENCE_VERBOSE_NAME_PLURAL
        db_table = 'experiences'

    def __str__(self):
        return self.name


class Gender(P7Model):
    name = models.CharField(max_length=255, primary_key=True)

    class Meta:
        verbose_name = strings_job.GENDER_VERBOSE_NAME
        verbose_name_plural = strings_job.GENDER_VERBOSE_NAME_PLURAL
        db_table = 'genders'

    def __str__(self):
        return self.name


class Currency(P7Model):
    name = models.CharField(max_length=255, primary_key=True)

    class Meta:
        verbose_name = strings_job.CURRENCY_VERBOSE_NAME
        verbose_name_plural = strings_job.CURRENCY_VERBOSE_NAME_PLURAL
        db_table = 'currencies'

    def __str__(self):
        return self.name


class JobSource(P7Model):
    name = models.CharField(max_length=255, primary_key=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = strings_job.JOBSOURCE_VERBOSE_NAME
        verbose_name_plural = strings_job.JOBSOURCE_VERBOSE_NAME_PLURAL
        db_table = 'job_sources'

    def __str__(self):
        return self.name


class JobCategory(P7Model):
    name = models.CharField(max_length=255, primary_key=True)

    class Meta:
        verbose_name = strings_job.JOBCATEGORY_VERBOSE_NAME
        verbose_name_plural = strings_job.JOBCATEGORY_VERBOSE_NAME_PLURAL
        db_table = 'job_categories'

    def __str__(self):
        return self.name


class JobGender(P7Model):
    name = models.CharField(max_length=255, primary_key=True)

    class Meta:
        verbose_name = strings_job.JOBGENDER_VERBOSE_NAME
        verbose_name_plural = strings_job.JOBGENDER_VERBOSE_NAME_PLURAL
        db_table = 'job_genders'

    def __str__(self):
        return self.name


class City(P7Model):
    name = models.CharField(max_length=255, primary_key=True)

    class Meta:
        verbose_name = strings_job.CITY_VERBOSE_NAME
        verbose_name_plural = strings_job.CITY_VERBOSE_NAME_PLURAL
        db_table = 'cities'

    def __str__(self):
        return self.name

class Skill(P7Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = strings_job.SKILLS_VERBOSE_NAME
        verbose_name_plural = strings_job.SKILLS_VERBOSE_NAME_PLURAL
        db_table = 'skills'

    def __str__(self):
        return self.name

class ApplicationStatus(P7Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = strings_job.APPLICATION_STATUS_VERBOSE_NAME
        verbose_name_plural = strings_job.APPLICATION_STATUS_VERBOSE_NAME_PLURAL
        db_table = 'application_statuses'

    def __str__(self):
        return self.name


class TrendingKeywords(P7Model):
    keyword = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True)
    device = models.CharField(max_length=255, default='Unknown')
    browser = models.CharField(max_length=255, default='Unknown')
    operating_system = models.CharField(max_length=255, default='Unknown')


    class Meta:
        verbose_name = strings_job.TRENDING_KEYWORDS_VERBOSE_NAME
        verbose_name_plural = strings_job.TRENDING_KEYWORDS_VERBOSE_NAME_PLURAL
        db_table = 'trending_keywords'

    def __str__(self):
        return self.keyword


class Company(P7Model):
    name = models.CharField(max_length=255, primary_key=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    company_name_bdjobs = models.CharField(max_length=255, blank=True, null=True)
    company_name_facebook = models.CharField(max_length=255, blank=True, null=True)
    company_name_google = models.CharField(max_length=255, blank=True, null=True)
    basis_membership_no = models.CharField(max_length=50, blank=True, null=True)
    year_of_eastablishment = models.DateField(blank=True, null=True)
    company_profile = models.TextField(blank=True, null=True)
    company_contact_no_one = models.CharField(max_length=50, blank=True, null=True)
    company_contact_no_two = models.CharField(max_length=50, blank=True, null=True)
    company_contact_no_three = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    web_address = models.CharField(max_length=255, blank=True, null=True)
    organization_head = models.CharField(max_length=60, blank=True, null=True)
    organization_head_designation = models.CharField(max_length=30, null=True, blank=True)
    organization_head_number = models.CharField(max_length=15, null=True, blank=True)
    legal_structure_of_this_company = models.CharField(max_length=60, null=True, blank=True)
    total_number_of_human_resources = models.PositiveSmallIntegerField(null=True, blank=True)
    no_of_it_resources = models.PositiveSmallIntegerField(null=True, blank=True)
    contact_person = models.CharField(max_length=50, blank=True, null=True)
    contact_person_designation = models.CharField(max_length=50, blank=True, null=True)  # need to recheck (foreign key)
    contact_person_mobile_no = models.CharField(max_length=20, blank=True, null=True)
    contact_person_email = models.CharField(max_length=100, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='images/', blank=True, null=True)
    latitude = models.DecimalField(max_digits=15, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=15, decimal_places=8, blank=True, null=True)
    featured = models.BooleanField(default=False)

    class Meta:
        verbose_name = strings_job.COMPANY_VERBOSE_NAME
        verbose_name_plural = strings_job.COMPANY_VERBOSE_NAME_PLURAL
        db_table = 'companies'

    def load_data(self, json_data):
        self.__dict__ = json_data

    def __str__(self):
        return self.name


class Job(P7Model):
    job_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_column='id')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    job_area = models.CharField(max_length=255, blank=True, null=True)
    job_city = models.CharField(max_length=255, blank=True, null=True)
    locked_by = models.CharField(max_length=255, blank=True, null=True)
    job_country = models.CharField(max_length=255, blank=True, null=True)
    salary_option = models.CharField(max_length=20, blank=False, null=False,
                                  choices=strings_job.SALARY_OPTION, default=strings_job.DEFAULT_SALARY_OPTION)
    salary = models.CharField(max_length=255, blank=True, null=True)
    salary_min = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, blank=True, null=True, db_column='currency')
    other_benefits = RichTextField(blank=True, null=True)
    experience = models.PositiveIntegerField(default=0, blank=True, null=True)
    ## 0080_auto_20200603_1242 migrations.RunSQL("UPDATE jobs SET experience=1 WHERE experience='1 Year'"),
    description = RichTextField(blank=True, null=True)
    qualification = models.ForeignKey(Qualification, on_delete=models.PROTECT, blank=True, null=True,
                                      db_column='qualification')
    responsibilities = RichTextField(blank=True, null=True)
    additional_requirements = RichTextField(blank=True, null=True)
    education = RichTextField(blank=True, null=True)
    vacancy = models.PositiveIntegerField(default=1, null=True)
    application_deadline = models.DateField(null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name='jobs')
    company_profile = RichTextField(blank=True, null=True)
    company_address = models.CharField(max_length=255, blank=True, null=True)
    company_area = models.CharField(max_length=255, blank=True, null=True)
    company_city = models.CharField(max_length=255, blank=True, null=True)
    company_country = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    raw_content = RichTextField(blank=True, null=True)
    favorite_count = models.PositiveIntegerField(default=0)
    applied_count = models.PositiveIntegerField(default=0)
    terms_and_condition = models.BooleanField(default=False)
    job_skills = models.ManyToManyField('Skill', blank=True, related_name='skill_set')
    status = models.CharField(max_length=20, blank=False, null=False, default=strings_job.DEFAULT_JOB_STATUS)
    job_site = models.CharField(max_length=20, blank=False, null=False,
                                choices=strings_job.JOB_SITES, default=strings_job.DEFAULT_JOB_SITE)
    job_nature = models.CharField(max_length=20, blank=False, null=False,
                                  choices=strings_job.JOB_NATURES, default=strings_job.DEFAULT_JOB_NATURE)
    job_type = models.CharField(max_length=20, blank=False, null=False,
                                choices=strings_job.JOB_TYPES, default=strings_job.DEFAULT_JOB_TYPE)
    creator_type = models.CharField(max_length=20, blank=False, null=False,
                                    choices=strings_job.JOB_CREATOR_TYPES, default=strings_job.DEFAULT_JOB_CREATOR_TYPE)
    job_source_1 = models.ForeignKey(JobSource, on_delete=models.PROTECT,
                                     related_name='jobs1', db_column='job_source_1', blank=True, null=True)
    job_url_1 = models.CharField(max_length=255, blank=True, null=True)
    job_source_2 = models.ForeignKey(JobSource, on_delete=models.PROTECT,
                                     related_name='jobs2', db_column='job_source_2', blank=True, null=True)
    job_url_2 = models.CharField(max_length=255, blank=True, null=True)
    job_source_3 = models.ForeignKey(JobSource, on_delete=models.PROTECT,
                                     related_name='jobs3', db_column='job_source_3', blank=True, null=True)
    job_url_3 = models.CharField(max_length=255, blank=True, null=True)
    job_category = models.ForeignKey(JobCategory, on_delete=models.PROTECT,
                                     related_name='jobs', db_column='job_category', blank=True, null=True)
    job_gender = models.ForeignKey(JobGender, on_delete=models.PROTECT,
                                   related_name='jobs', db_column='job_gender', blank=True, null=True)
    post_date = models.DateTimeField(blank=True, null=True)
    review_date = models.DateTimeField(blank=True, null=True)
    approve_date = models.DateTimeField(blank=True, null=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    posted_by = models.CharField(max_length=255, blank=True, null=True)
    reviewed_by = models.CharField(max_length=255, blank=True, null=True)
    approved_by = models.CharField(max_length=255, blank=True, null=True)
    published_by = models.CharField(max_length=255, blank=True, null=True)
    featured = models.BooleanField(default=False)

    class Meta:
        verbose_name = strings_job.JOB_VERBOSE_NAME
        verbose_name_plural = strings_job.JOB_VERBOSE_NAME_PLURAL
        db_table = 'jobs'
        ordering = ['-post_date']

    def load_data(self, json_data):
        self.__dict__ = json_data

    def clean(self):
        super().clean()
        if self.status == "PUBLISHED" and not self.post_date:
            raise ValidationError("Enter post date before publishing")

    def __str__(self):
        return self.title


class FavouriteJob(P7Model):
    job = models.ForeignKey(Job, on_delete=models.PROTECT, db_column='job', related_name='fav_jobs')

    class Meta:
        verbose_name = strings_job.BOOKMARK_JOB_VERBOSE_NAME
        verbose_name_plural = strings_job.BOOKMARK_JOB_VERBOSE_NAME_PLURAL
        db_table = 'favourite_jobs'

    def __str__(self):
        return self.job.title


class JobApplication(P7Model):
    from pro.models import Professional
    job = models.ForeignKey(Job, on_delete=models.PROTECT, db_column='job', related_name='applied_jobs')
    pro = models.ForeignKey(Professional, on_delete=models.PROTECT, db_column='pro', null=True,
                            related_name='applied_pros')
    attachment = models.FileField(upload_to='documents', max_length=100, blank=True, null=True)
    resume = models.FileField(upload_to='documents', max_length=100, blank=True, null=True)
    is_shortlisted = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    application_notes = models.TextField(blank=True, null=True)
    application_status = models.ForeignKey(ApplicationStatus, on_delete=models.PROTECT,
                                           null=True, blank=True)
    class Meta:
        verbose_name = strings_job.JOB_APPLICATION_VERBOSE_NAME
        verbose_name_plural = strings_job.JOB_APPLICATION_VERBOSE_NAME_PLURAL
        db_table = 'job_applications'

    def __str__(self):
        return self.job.title


def before_job_save(sender, instance:Job, *args, **kwargs):
    if instance.job_city and len(instance.job_city.split(',')) == 2:
        instance.job_country = instance.job_city.split(',')[0].strip()

    if instance.company_city and len(instance.company_city.split(',')) == 2:
        instance.company_country = instance.company_city.split(',')[0].strip()

    try:
        old_instance = Job.objects.get(job_id=instance.job_id)
        if old_instance.title != instance.title and old_instance.status != "PUBLISHED":
            instance.slug = job_slug_generator(instance)

        if instance.status == "POSTED" and old_instance.status == "DRAFT":
            instance.post_date = timezone.now()
            instance.posted_by = instance.modified_by
        elif instance.status == "REVIEWED" and old_instance.status != "REVIEWED":
            instance.review_date = timezone.now()
            instance.reviewed_by = instance.modified_by
        elif instance.status == "APPROVED" and old_instance.status != "APPROVED":
            instance.approve_date = timezone.now()
            instance.approved_by = instance.modified_by
        elif instance.status == "PUBLISHED" and old_instance.status != "PUBLISHED":
            instance.publish_date = timezone.now()
            instance.published_by = instance.modified_by

    except Job.DoesNotExist:
        instance.slug = job_slug_generator(instance)
        if instance.status == "POSTED":
            instance.post_date = timezone.now()
            instance.posted_by = instance.created_by


def after_job_save(sender, instance:Job, *args, **kwargs):
    pass
    # queryset = Job.objects.filter(
    #         is_archived=False,
    #         status='Published',
    #     ).aggregate(
    #         Max('salary_max')
    #     ).aggregate(
    #         Max('salary_min')
    #     )
    #
    #
    # print(queryset['salary_max__max'])


def applied_job_counter(sender, instance:JobApplication, *args, **kwargs):
    if instance:
        total_application = JobApplication.objects.filter(job=instance.job, is_approved=True).count()
        job_obj = Job.objects.get(job_id=instance.job.job_id)
        job_obj.applied_count = total_application
        job_obj.save()


pre_save.connect(populate_time_info, sender=Company)
pre_save.connect(populate_time_info, sender=Industry)
pre_save.connect(populate_time_info, sender=JobType)
pre_save.connect(populate_time_info, sender=Qualification)
pre_save.connect(populate_time_info, sender=Experience)
pre_save.connect(populate_time_info, sender=Gender)
pre_save.connect(populate_time_info, sender=Currency)
pre_save.connect(populate_time_info, sender=JobSource)
pre_save.connect(populate_time_info, sender=JobCategory)
pre_save.connect(populate_time_info, sender=JobGender)
pre_save.connect(populate_time_info, sender=Job)
pre_save.connect(before_job_save, sender=Job)
post_save.connect(after_job_save, sender=Job)
pre_save.connect(populate_time_info, sender=Skill)
pre_save.connect(populate_time_info, sender=TrendingKeywords)
pre_save.connect(populate_time_info, sender=FavouriteJob)
pre_save.connect(populate_time_info, sender=JobApplication)
pre_save.connect(populate_time_info, sender=City)
post_save.connect(after_job_save, sender=Job)
post_delete.connect(applied_job_counter, sender=JobApplication)
post_save.connect(applied_job_counter, sender=JobApplication)
