from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase
from job.models import Job, Company, JobType, Qualification, JobGender, Experience, Industry, Currency, TrendingKeywords, \
    Skill, FavouriteJob, JobApplication
from django.contrib.auth.models import User

from pro.models import Professional

exclude = [
    'created_by', 'created_at', 'created_from',
    'modified_by', 'modified_at', 'modified_from',
    'archived_by', 'archived_at', 'archived_from'
]

class CompanyTest(TestCase):
    def setUp(self):
        pass

    def test_when_everything_required_is_given_should_pass(self):
        company = Company(name='Ishraak Solutions', web_address='www.ishraak.com')
        try:
            company.full_clean(exclude=exclude)
        except:
            self.fail()

    def test_when_name_is_null_should_raise_error(self):
        company = Company(web_address='www.ishraak.com')
        with self.assertRaises(ValidationError):
            company.full_clean(exclude=exclude)

    def test_when_name_is_blank_should_raise_error(self):
        company = Company(name='', web_address='www.ishraak.com')
        with self.assertRaises(ValidationError):
            company.full_clean(exclude=exclude)


# INDUSTRY TESTS

class IndustryTest(TestCase):

    def test_when_everything_required_is_given_should_pass(self):
        industry = Industry(name='Information Technology')
        try:
            industry.full_clean(exclude=exclude)
        except:
            self.fail()

    def test_when_name_is_null_should_raise_error(self):
        industry = Industry()
        with self.assertRaises(ValidationError):
            industry.full_clean(exclude=exclude)

    def test_when_name_is_blank_should_raise_error(self):
        industry = Industry(name='')
        with self.assertRaises(ValidationError):
            industry.full_clean(exclude=exclude)

    def test_when_name_is_more_than_max_length_should_raise_error(self):
        industry = Industry(name='Lorem Ipsum is simply dummy text of the printing and typesetting industry. '
                                 'Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, '
                                 'when an unknown printer took a galley of type and scrambled it to make a type '
                                 'specimen book. It has survived not only five centuries, but also the leap into '
                                 'electronic typesetting, remaining essentially unchanged. It was popularised in '
                                 'the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, '
                                 'and more recently with desktop publishing software like Aldus PageMaker '
                                 'including versions of Lorem Ipsum.')
        with self.assertRaises(ValidationError):
            industry.full_clean(exclude=exclude)


# INDUSTRY TESTS

# Currency TESTS

class CurrencyTest(TestCase):

    def test_when_everything_required_is_given_should_pass(self):
        currency = Currency(name='BDT')
        try:
            currency.full_clean(exclude=exclude)
        except:
            self.fail()

    def test_when_name_is_null_should_raise_error(self):
        currency = Currency()
        with self.assertRaises(ValidationError):
            currency.full_clean(exclude=exclude)

    def test_when_name_is_blank_should_raise_error(self):
        currency = Currency(name='')
        with self.assertRaises(ValidationError):
            currency.full_clean(exclude=exclude)

    def test_when_name_is_more_than_max_length_should_raise_error(self):
        currency = Currency(name='Lorem Ipsum is simply dummy text of the printing and typesetting industry. '
                                 'Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, '
                                 'when an unknown printer took a galley of type and scrambled it to make a type '
                                 'specimen book. It has survived not only five centuries, but also the leap into '
                                 'electronic typesetting, remaining essentially unchanged. It was popularised in '
                                 'the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, '
                                 'and more recently with desktop publishing software like Aldus PageMaker '
                                 'including versions of Lorem Ipsum.')
        with self.assertRaises(ValidationError):
            currency.full_clean(exclude=exclude)


# Currency TESTS

# QUALIFICATION TESTS

class QualificationTest(TestCase):

    def test_when_everything_required_is_given_should_pass(self):
        qualification = Qualification(name='Information Technology')
        try:
            qualification.full_clean(exclude=exclude)
        except:
            self.fail()

    def test_when_name_is_null_should_raise_error(self):
        qualification = Qualification()
        with self.assertRaises(ValidationError):
            qualification.full_clean(exclude=exclude)

    def test_when_name_is_blank_should_raise_error(self):
        qualification = Qualification(name='')
        with self.assertRaises(ValidationError):
            qualification.full_clean(exclude=exclude)

    def test_when_name_is_more_than_max_length_should_raise_error(self):
        qualification = Qualification(name='Lorem Ipsum is simply dummy text of the printing and typesetting industry. '
                                           'Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, '
                                           'when an unknown printer took a galley of type and scrambled it to make a type '
                                           'specimen book. It has survived not only five centuries, but also the leap into '
                                           'electronic typesetting, remaining essentially unchanged. It was popularised in '
                                           'the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, '
                                           'and more recently with desktop publishing software like Aldus PageMaker '
                                           'including versions of Lorem Ipsum.')
        with self.assertRaises(ValidationError):
            qualification.full_clean(exclude=exclude)


# QUALIFICATION TESTS

# GENDER TESTS

class JobGenderTest(TestCase):

    def test_when_everything_required_is_given_should_pass(self):
        job_gender = JobGender(name='Male')
        try:
            job_gender.full_clean(exclude=exclude)
        except:
            self.fail()

    def test_when_name_is_null_should_raise_error(self):
        job_gender = JobGender()
        with self.assertRaises(ValidationError):
            job_gender.full_clean(exclude=exclude)

    def test_when_name_is_blank_should_raise_error(self):
        job_gender = JobGender(name='')
        with self.assertRaises(ValidationError):
            job_gender.full_clean(exclude=exclude)

    def test_when_name_is_more_than_max_length_should_raise_error(self):
        job_gender = JobGender(name='Lorem Ipsum is simply dummy text of the printing and typesetting industry. '
                             'Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, '
                             'when an unknown printer took a galley of type and scrambled it to make a type '
                             'specimen book. It has survived not only five centuries, but also the leap into '
                             'electronic typesetting, remaining essentially unchanged. It was popularised in '
                             'the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, '
                             'and more recently with desktop publishing software like Aldus PageMaker '
                             'including versions of Lorem Ipsum.')
        with self.assertRaises(ValidationError):
            job_gender.full_clean(exclude=exclude)


# GENDER TESTS

# JOBTYPE TESTS

class JobTypeTest(TestCase):
    def test_when_everything_required_is_given_should_pass(self):
        job_type = JobType(name='Part Time')
        try:
            job_type.full_clean(exclude=exclude)
        except:
            self.fail()

    def test_when_name_is_null_should_raise_error(self):
        job_type = JobType()
        with self.assertRaises(ValidationError):
            job_type.full_clean(exclude=exclude)

    def test_when_name_is_blank_should_raise_error(self):
        job_type = JobType(name='')
        with self.assertRaises(ValidationError):
            job_type.full_clean(exclude=exclude)


# JOBTYPE TESTS

# Experience TESTS

class ExperienceTest(TestCase):
    def test_when_everything_required_is_given_should_pass(self):
        experience = Experience(name='Part Time')
        try:
            experience.full_clean(exclude=exclude)
        except:
            self.fail()

    def test_when_name_is_null_should_raise_error(self):
        experience = Experience()
        with self.assertRaises(ValidationError):
            experience.full_clean(exclude=exclude)

    def test_when_name_is_blank_should_raise_error(self):
        experience = Experience(name='')
        with self.assertRaises(ValidationError):
            experience.full_clean(exclude=exclude)


# Experience TESTS


# JOB TESTS
class JobTest(TestCase):

    def setUp(self):
        company = Company(name='Ishraak Solutions', web_address='www.ishraak.com')
        company.save()
        self.company = company

        job_gender = JobGender(name='Male')
        job_gender.save()
        self.job_gender = job_gender

        experience = Experience(name='Part Time')
        experience.save()
        self.experience = experience

        qualification = Qualification(name='Graduate')
        qualification.save()
        self.qualification = qualification


    def test_when_everything_is_given_should_pass(self):
        job = Job(title='Software Engineer',
                  experience = 1, salary_min=5000.00, salary_max=10000.00,
                  qualification=self.qualification, job_gender=self.job_gender, application_deadline='',
                  description='Test job', responsibilities='Web developer', education='Computer Science',
                  other_benefits='Apple Watch', company=self.company,
                    latitude=3.00, longitude=4.00,
                  )
        try:
            job.full_clean(exclude=exclude)
        except:
            self.fail()

    def test_when_title_is_null_should_raise_error(self):
        job = Job(experience = 1, salary_min=5000.00, salary_max=10000.00,
                  qualification=self.qualification, job_gender=self.job_gender, application_deadline='',
                  description='Test job', responsibilities='Web developer', education='Computer Science',
                  other_benefits='Apple Watch', company=self.company,
                    latitude=3.00, longitude=4.00,
                  )
        with self.assertRaises(ValidationError):
            job.full_clean(exclude=exclude)

    def test_when_title_is_blank_should_raise_error(self):
        job = Job(title='', experience = 1, salary_min=5000.00, salary_max=10000.00,
                  qualification=self.qualification, job_gender=self.job_gender, application_deadline='',
                  description='Test job', responsibilities='Web developer', education='Computer Science',
                  other_benefits='Apple Watch', company=self.company,
                    latitude=3.00, longitude=4.00,
                  )
        with self.assertRaises(ValidationError):
            job.full_clean(exclude=exclude)

    def test_when_title_is_more_than_max_length_should_raise_error(self):
        job = Job(title='Lorem Ipsum is simply dummy text of the printing and typesetting industry. '
                        'Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, '
                        'when an unknown printer took a galley of type and scrambled it to make a type '
                        'specimen book. It has survived not only five centuries, but also the leap into '
                        'electronic typesetting, remaining essentially unchanged. It was popularised in '
                        'the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, '
                        'and more recently with desktop publishing software like Aldus PageMaker '
                        'including versions of Lorem Ipsum.',
                  experience = 1, salary_min=5000.00, salary_max=10000.00,
                  qualification=self.qualification, job_gender=self.job_gender, application_deadline='',
                  description='Test job', responsibilities='Web developer', education='Computer Science',
                  other_benefits='Apple Watch', company=self.company,
                    latitude=3.00, longitude=4.00,
                  )
        with self.assertRaises(ValidationError):
            job.full_clean(exclude=exclude)

    def test__when_slug_name_duplicate__should_raise_error(self):
        slug = Job(slug='peace-maker-c57fe949')
        slug1 = Job(slug='peace-maker-c57fe949')

        with self.assertRaises(IntegrityError):
            slug.save()
            slug1.save()


    # def test_when_experience_is_null_should_raise_error(self):
    #     s = Job(name='Software Engineer',job_gender='Male')
    #     with self.assertRaises(ValidationError):
    #         s.full_clean(exclude=exclude)
    #
    # def test_when_experience_is_blank_should_raise_error(self):
    #     s = Job(name='Software Engineer',experience='', job_gender='Male')
    #     with self.assertRaises(ValidationError):
    #         s.full_clean(exclude=exclude)
    #
    # def test_when_job_gender_is_null_should_raise_error(self):
    #     s = Job(name='Software Engineer')
    #     with self.assertRaises(ValidationError):
    #         s.full_clean(exclude=exclude)
    #
    # def test_when_job_gender_is_blank_should_raise_error(self):
    #     s = Job(name='Software Engineer',experience='1', job_gender='')
    #     with self.assertRaises(ValidationError):
    #         s.full_clean(exclude=exclude)


# JOB TESTS

# SKILLS TEST
class SkillTest(TestCase):

    def test_when_everything_required_is_given_should_pass(self):
        skill = Skill(name='Programming')
        try:
            skill.full_clean(exclude=exclude)
        except:
            self.fail()

    def test_when_name_is_null_should_raise_error(self):
        skill = Skill()
        with self.assertRaises(ValidationError):
            skill.full_clean(exclude=exclude)

    def test_when_name_is_blank_should_raise_error(self):
        skill = Skill(name='')
        with self.assertRaises(ValidationError):
            skill.full_clean(exclude=exclude)

    def test_when_title_is_more_than_max_length_should_raise_error(self):
        skill = Skill(name='Lorem Ipsum is simply dummy text of the printing and typesetting industry. '
                           'Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, '
                           'when an unknown printer took a galley of type and scrambled it to make a type '
                           'specimen book. It has survived not only five centuries, but also the leap into '
                           'electronic typesetting, remaining essentially unchanged. It was popularised in '
                           'the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, '
                           'and more recently with desktop publishing software like Aldus PageMaker '
                           'including versions of Lorem Ipsum.')
        with self.assertRaises(ValidationError):
            skill.full_clean(exclude=exclude)

    def test__when_skills_name_duplicate__should_raise_error(self):
        s = Skill(name="Programming")
        s1 = Skill(name="Programming")
        with self.assertRaises(IntegrityError):
            s.save()
            s1.save()

#SKILLS TEST

#TRENDING_KEYWORDS_TEST#
class TrendingKeywordsTest(TestCase):
    def test_when_everything_required_is_given_should_pass(self):
        trending_keywords = TrendingKeywords(keyword='XYZ',location='This is a comment')
        try:
            trending_keywords.full_clean(exclude=exclude)
        except:
            self.fail()

    def test_when_keyword_is_null_should_raise_error(self):
        trendingkeywords = TrendingKeywords(location = "Niketan")
        with self.assertRaises(ValidationError):
            trendingkeywords.full_clean(exclude=exclude)


    def test_when_keyword_and_location_both_is_null_should_raise_error(self):
        trendingkeywords = TrendingKeywords()
        with self.assertRaises(ValidationError):
            trendingkeywords.full_clean(exclude=exclude)

    def test_when_keyword_is_blank_should_raise_error(self):
        trendingkeywords = TrendingKeywords(keyword='',location='Niketan')
        with self.assertRaises(ValidationError):
            trendingkeywords.full_clean(exclude=exclude)


    def test_when_keyword_and_location_both_is_blank_should_raise_error(self):
        trendingkeywords = TrendingKeywords(keyword='', location='')
        with self.assertRaises(ValidationError):
            trendingkeywords.full_clean(exclude=exclude)


    def test_when_keyword_is_more_than_max_length_should_raise_error(self):
        trendingkeywords = TrendingKeywords(keyword='Lorem Ipsum is simply dummy text of the printing and typesetting industry. '
                           'Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, '
                           'when an unknown printer took a galley of type and scrambled it to make a type '
                           'specimen book. It has survived not only five centuries, but also the leap into '
                           'electronic typesetting, remaining essentially unchanged. It was popularised in '
                           'the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, '
                           'and more recently with desktop publishing software like Aldus PageMaker '
                           'including versions of Lorem Ipsum.', location='Niketan')
        with self.assertRaises(ValidationError):
            trendingkeywords.full_clean(exclude=exclude)

    def test_when_location_is_more_than_max_length_should_raise_error(self):
        trendingkeywords = TrendingKeywords(keyword='Python3',location='Lorem Ipsum is simply dummy text of the printing and typesetting industry. '
                           'Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, '
                           'when an unknown printer took a galley of type and scrambled it to make a type '
                           'specimen book. It has survived not only five centuries, but also the leap into '
                           'electronic typesetting, remaining essentially unchanged. It was popularised in '
                           'the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, '
                           'and more recently with desktop publishing software like Aldus PageMaker '
                           'including versions of Lorem Ipsum.')
        with self.assertRaises(ValidationError):
            trendingkeywords.full_clean(exclude=exclude)


#TRENDING_KEYWORDS_TEST#


#BOOKMARK_JOB_TEST#


class FavouriteJobTest(TestCase):
    def setUp(self) :
        company = Company(name='Ishraak Solutions', web_address='www.ishraak.com')
        company.save()
        self.company = company

        job_gender = JobGender(name='Male')
        job_gender.save()
        self.job_gender = job_gender

        experience = Experience(name='Part Time')
        experience.save()
        self.experience = experience

        qualification = Qualification(name='Graduate')
        qualification.save()
        self.qualification = qualification

        job = Job(title='Software Engineer',
                  experience = 1, salary_min=5000.00, salary_max=10000.00,
                  qualification=self.qualification, job_gender=self.job_gender, application_deadline='2020-03-29',
                  description='Test job', responsibilities='Web developer', education='Computer Science',
                  other_benefits='Apple Watch', company=self.company,
                    latitude=3.00, longitude=4.00,
                  )
        job.save()
        self.jb = job

        user = User(username='Admin', password='123')
        user.save()
        self.usr = user

    def test__when_everything_required_is_given__should_pass(self):
        favouritejob = FavouriteJob(job=self.jb, user=self.usr)
        try:
            favouritejob.full_clean(exclude=exclude)
        except:
            self.fail()

    def test__when_job_is_blank__should__raise_error(self):
        with self.assertRaises(ValueError):
            favouritejob = FavouriteJob(job='', user=self.usr)

    def test__when_job_is_null_should__raise_error(self):
        favouritejob = FavouriteJob(user=self.usr)
        with self.assertRaises(ValidationError):
            favouritejob.full_clean(exclude=exclude)

    def test__when_user_is_blank_should__raise_error(self):
        with self.assertRaises(ValueError):
            favouritejob = FavouriteJob(job=self.jb, user='')

    def test__when_user_is_null_should__raise_error(self):
        favouritejob = FavouriteJob(job=self.jb)
        with self.assertRaises(ValidationError):
            favouritejob.full_clean(exclude=exclude)

#BOOKMARK_JOB_TEST#
