import unittest

from tests.config_api import MAIN_URL
from tests.test_api.common import *

COM_JOB_CREATE_URL = f'{MAIN_URL}/api/job/create/'
COM_JOB_UPDATE_URL = f'{MAIN_URL}/api/job/update/'
JOB_ID_FOR_UPDATE = '0711248315e942adbf1c75fa9c64ad66'
JOB_API_URL = f'{MAIN_URL}/api/job/get/'
SLUG = "job-post-example-one-7b147709"
SLUG_GENERATOR_URL = f'{MAIN_URL}/api/slug/generate/'
JOB_ID = ['0711248315e942adbf1c75fa9c64ad66']
COMPANY_NAME = 'Company Example'


class TestJobAPI(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    # def test__when_slug_is_valid__should_pass(self):
    #     resp = requests.get(JOB_API_URL + SLUG, headers={'Authorization': 'Bearer ' + self.access_token})
    #     data = resp.json()
    #     self.assertIsNotNone(data['job_id'])
    #     self.assertIsNotNone(data['company'])
    #     self.assertEqual(resp.status_code, 200)

    # def test__when_slug_is_invalid__should_failed(self):
    #     resp = requests.get(JOB_API_URL + "sr-python-programmer-100abc100",
    #                         headers={'Authorization': 'Bearer ' + self.access_token})
    #     data = resp.json()
    #     if 'job_id' in data:
    #         self.fail()

    def test__when_access_token_is_invalid__should_failed(self):
        invalid_access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIj'
        resp = requests.get(JOB_API_URL + SLUG, headers={'Authorization': 'Bearer ' + invalid_access_token})
        self.assertEqual(resp.status_code, 401)

##TODO
class TestCreateJob(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_com()
        self.access_token = data['access']
        self.company_id = COMPANY_NAME
        self.title = "Automation Testing API"
        self.job_category_id = "Job Category Example Two"
        self.qualification_id = "Qualification Example Two"
        self.experience = "1"
        self.job_gender_id = "Male"
        self.description = "Automation Testing 1,2,3"
        self.vacancy = "2"
        self.status = "DRAFT"
        self.salary = "500000"
        self.salary_min = "0"
        self.salary_max = "200000"
        self.additional_requirements = "Additional Requirements "
        self.application_deadline = "2021-07-09"
        self.company_profile = "Company Profile"
        self.education = "This Is Education"
        self.address = "House 76"
        self.job_area = "Niketan,Gulshan"
        self.job_city = "Dhaka, Bangladesh"
        self.job_type = "PERMANENT"
        self.job_site = "REMOTE"
        self.job_nature = "PARTTIME"
        self.responsibilities = "The is Responsibilities"
        self.other_benefits = "Other Benefits"
        self.skills = "Python,Django"

    def test__when_everything_valid__should_pass(self):
        json = {
            # "company_id": self.company_id,
            "title": self.title,
            "description": self.description,
            "experience": self.experience,
            "salary": self.salary,
            "additional_requirements": self.additional_requirements,
            "address": self.address,
            "application_deadline": self.application_deadline,
            "company_profile": self.company_profile,
            "education": self.education,
            "job_area": self.job_area,
            "job_category_id": self.job_category_id,
            "job_city": self.job_city,
            "job_gender_id": self.job_gender_id,
            "job_nature": self.job_nature,
            "job_site": self.job_site,
            "job_type": self.job_type,
            "other_benefits": self.other_benefits,
            "qualification_id": self.qualification_id,
            "responsibilities": self.responsibilities,
            "salary_max": self.salary_max,
            "salary_min": self.salary_min,
            "skills": self.skills,
            "vacancy": self.vacancy,
            "status": self.status

        }
        resp = requests.post(COM_JOB_CREATE_URL, json=json, headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        self.assertEqual(resp.status_code, 200)

    def test__when_mendatory_field_title_is_empty__should_failed(self):
        json = {
            # "company_id": self.company_id,
            "title": '',
            "description": self.description,
            "experience": self.experience,
            "salary": self.salary,
            "additional_requirements": self.additional_requirements,
            "address": self.address,
            "application_deadline": self.application_deadline,
            "company_profile": self.company_profile,
            "education": self.education,
            "job_area": self.job_area,
            "job_category_id": self.job_category_id,
            "job_city": self.job_city,
            "job_gender_id": self.job_gender_id,
            "job_nature": self.job_nature,
            "job_site": self.job_site,
            "job_type": self.job_type,
            "other_benefits": self.other_benefits,
            "qualification_id": self.qualification_id,
            "responsibilities": self.responsibilities,
            "salary_max": self.salary_min,
            "salary_min": self.salary_max,
            "skills": self.skills,
            "vacancy": self.vacancy
        }
        resp = requests.post(COM_JOB_CREATE_URL, json=json, headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        self.assertNotEqual(resp.status_code, 200)


    def test__when_mendatory_field_of_frontend__title_is_null__should_failed(self):
        json = {
            # "company_id": self.company_id,

            "description": self.description,
            "experience": self.experience,
            "salary": self.salary,
            "additional_requirements": self.additional_requirements,
            "address": self.address,
            "application_deadline": self.application_deadline,
            "company_profile": self.company_profile,
            "education": self.education,
            "job_area": self.job_area,
            "job_category_id": self.job_category_id,
            "job_city": self.job_city,
            "job_gender_id": self.job_gender_id,
            "job_nature": self.job_nature,
            "job_site": self.job_site,
            "job_type": self.job_type,
            "other_benefits": self.other_benefits,
            "qualification_id": self.qualification_id,
            "responsibilities": self.responsibilities,
            "salary_max": self.salary_min,
            "salary_min": self.salary_max,
            "skills": self.skills,
            "vacancy": self.vacancy

        }
        resp = requests.post(COM_JOB_CREATE_URL, json=json, headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        self.assertNotEqual(resp.status_code, 200)

    def test__when_vacancy_is_null__should_pass(self):
        json = {
            # "company_id": self.company_id,
            "title": self.title,
            "description": self.description,
            "experience": self.experience,
            "salary": self.salary,
            "additional_requirements": self.additional_requirements,
            "address": self.address,
            "application_deadline": self.application_deadline,
            "company_profile": self.company_profile,
            "education": self.education,
            "job_area": self.job_area,
            "job_category_id": self.job_category_id,
            "job_city": self.job_city,
            "job_gender_id": self.job_gender_id,
            "job_nature": self.job_nature,
            "job_site": self.job_site,
            "job_type": self.job_type,
            "other_benefits": self.other_benefits,
            "qualification_id": self.qualification_id,
            "responsibilities": self.responsibilities,
            "salary_max": self.salary_min,
            "salary_min": self.salary_max,
            "skills": self.skills,

        }
        resp = requests.post(COM_JOB_CREATE_URL, json=json, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertNotEqual(resp.status_code, 200)

    def test__when__address_is_empty__should_fail(self):
        json = {
            # "company_id": self.company_id,
            "title": self.title,
            "description": self.description,
            "experience": self.experience,
            "salary": self.salary,
            "additional_requirements": self.additional_requirements,
            "address": "",
            "application_deadline": self.application_deadline,
            "company_profile": self.company_profile,
            "education": self.education,
            "job_area": self.job_area,
            "job_category_id": self.job_category_id,
            "job_city": self.job_city,
            "job_gender_id": self.job_gender_id,
            "job_nature": self.job_nature,
            "job_site": self.job_site,
            "job_type": self.job_type,
            "other_benefits": self.other_benefits,
            "qualification_id": self.qualification_id,
            "responsibilities": self.responsibilities,
            "salary_max": self.salary_min,
            "salary_min": self.salary_max,
            "skills": self.skills,
            "vacancy": self.vacancy
        }
        resp = requests.post(COM_JOB_CREATE_URL, json=json, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertNotEqual(resp.status_code, 200)

    def test__when__vacancy_is_blank__should_fail(self):
        json = {
            # "company_id": self.company_id,
            "title": self.title,
            "description": self.description,
            "experience": self.experience,
            "salary": self.salary,
            "additional_requirements": self.additional_requirements,
            "address": self.address,
            "application_deadline": self.application_deadline,
            "company_profile": self.company_profile,
            "education": self.education,
            "job_area": self.job_area,
            "job_category_id": self.job_category_id,
            "job_city": self.job_city,
            "job_gender_id": self.job_gender_id,
            "job_nature": self.job_nature,
            "job_site": self.job_site,
            "job_type": self.job_type,
            "other_benefits": self.other_benefits,
            "qualification_id": self.qualification_id,
            "responsibilities": self.responsibilities,
            "salary_max": self.salary_min,
            "salary_min": self.salary_max,
            "skills": self.skills,
        }
        resp = requests.post(COM_JOB_CREATE_URL, json=json,
                             headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        self.assertNotEqual(resp.status_code, 200)

    def test__when_address_is_null__should_pass(self):
        json = {
            # "company_id": self.company_id,
            "title": self.title,
            "description": self.description,
            "experience": self.experience,
            "salary": self.salary,
            "additional_requirements": self.additional_requirements,

            "application_deadline": self.application_deadline,
            "company_profile": self.company_profile,
            "education": self.education,
            "job_area": self.job_area,
            "job_category_id": self.job_category_id,
            "job_city": self.job_city,
            "job_gender_id": self.job_gender_id,
            "job_nature": self.job_nature,
            "job_site": self.job_site,
            "job_type": self.job_type,
            "other_benefits": self.other_benefits,
            "qualification_id": self.qualification_id,
            "responsibilities": self.responsibilities,
            "salary_max": self.salary_min,
            "salary_min": self.salary_max,
            "skills": self.skills,
            "vacancy": self.vacancy
        }
        resp = requests.post(COM_JOB_CREATE_URL, json=json, headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        self.assertNotEqual(resp.status_code, 200)

    #
    # def test__when_company_id_blank__should_failed(self):
    #     json = {
    #         'title': self.title,
    #         'description': self.description,
    #         'job_category_id': self.job_category_id,
    #         'experience': self.experience,
    #         'qualification_id': self.qualification_id,
    #         'job_gender_id': self.job_gender_id,
    #         'vacancy': self.vacancy,
    #         'salary': self.salary,
    #         'salary_min': self.salary_min,
    #         'salary_max': self.salary_max,
    #         'additional_requirements': self.additional_requirements,
    #         'application_deadline': self.application_deadline,
    #         'company_profile': self.company_profile,
    #         'education': self.education,
    #         'address': self.address,
    #         'job_area': self.job_area,
    #         'job_city': self.job_city,
    #         'job_type': self.job_type,
    #         'job_site': self.job_site,
    #         'job_nature': self.job_nature,
    #         'responsibilities': self.responsibilities,
    #         'other_benefits': self.other_benefits,
    #         'skills': self.skills
    #
    #     }
    #     resp = requests.post(COM_JOB_CREATE_URL, json=json, headers={'Authorization': 'Bearer ' + self.access_token})
    #     self.assertEqual(resp.status_code, 500)

    # def test__when_using_another_company_id__should_failed(self):
    #     json = {
    #         'company_id': '100',
    #         'title': self.title,
    #         'description': self.description,
    #         'job_category_id': self.job_category_id,
    #         'experience': self.experience,
    #         'qualification_id': self.qualification_id,
    #         'job_gender_id': self.job_gender_id,
    #         'vacancy': self.vacancy,
    #         'salary': self.salary,
    #         'salary_min': self.salary_min,
    #         'salary_max': self.salary_max,
    #         'additional_requirements': self.additional_requirements,
    #         'application_deadline': self.application_deadline,
    #         'company_profile': self.company_profile,
    #         'education': self.education,
    #         'address': self.address,
    #         'job_area': self.job_area,
    #         'job_city': self.job_city,
    #         'job_type': self.job_type,
    #         'job_site': self.job_site,
    #         'job_nature': self.job_nature,
    #         'responsibilities': self.responsibilities,
    #         'other_benefits': self.other_benefits,
    #         'skills': self.skills
    #
    #     }
    #     resp = requests.post(COM_JOB_CREATE_URL, json=json, headers={'Authorization': 'Bearer ' + self.access_token})
    #     self.assertEqual(resp.status_code, 500)

    def test__when_access_token_is_invalid_should_failed(self):
        json = {
            # 'company_id': self.company_id,
            'title': self.title,
            'description': self.description,
            'job_category_id': self.job_category_id,
            'experience': self.experience,
            'qualification_id': self.qualification_id,
            'job_gender_id': self.job_gender_id,
            'vacancy': self.vacancy,
            'salary': self.salary,
            'salary_min': self.salary_min,
            'salary_max': self.salary_max,
            'additional_requirements': self.additional_requirements,
            'application_deadline': self.application_deadline,
            'company_profile': self.company_profile,
            'education': self.education,
            'address': self.address,
            'job_area': self.job_area,
            'job_city': self.job_city,
            'job_type': self.job_type,
            'job_site': self.job_site,
            'job_nature': self.job_nature,
            'responsibilities': self.responsibilities,
            'other_benefits': self.other_benefits,
            'skills': self.skills

        }
        invalid_access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIj'
        resp = requests.post(COM_JOB_CREATE_URL, json=json, headers={'Authorization': 'Bearer ' + invalid_access_token})
        self.assertEqual(resp.status_code, 401)

    def test__when_required_field__company_id_vacancy_address_is_empty_should__failed(self):
        json = {
            'company_id': "",
            'description': self.description,
            'job_category_id': self.job_category_id,
            'experience': self.experience,
            'qualification_id': self.qualification_id,
            'job_gender_id': self.job_gender_id,
            'vacancy': "",
            'salary': self.salary,
            'salary_min': self.salary_min,
            'salary_max': self.salary_max,
            'additional_requirements': self.additional_requirements,
            'application_deadline': self.application_deadline,
            'company_profile': self.company_profile,
            'education': self.education,
            'address': "",
            'job_area': self.job_area,
            'job_city': self.job_city,
            'job_type': self.job_type,
            'job_site': self.job_site,
            'job_nature': self.job_nature,
            'responsibilities': self.responsibilities,
            'other_benefits': self.other_benefits,
            'skills': self.skills

        }
        resp = requests.post(COM_JOB_CREATE_URL, json=json, headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        self.assertNotEqual(data, 200)

    def test__when_required_field_is_null__company_id__vacancy_address__should__failed(self):
        json = {
            'description': self.description,
            'job_category_id': self.job_category_id,
            'experience': self.experience,
            'qualification_id': self.qualification_id,
            'job_gender_id': self.job_gender_id,
            'salary': self.salary,
            'salary_min': self.salary_min,
            'salary_max': self.salary_max,
            'additional_requirements': self.additional_requirements,
            'application_deadline': self.application_deadline,
            'company_profile': self.company_profile,
            'education': self.education,
            'job_area': self.job_area,
            'job_city': self.job_city,
            'job_type': self.job_type,
            'job_site': self.job_site,
            'job_nature': self.job_nature,
            'responsibilities': self.responsibilities,
            'other_benefits': self.other_benefits,
            'skills': self.skills

        }
        resp = requests.post(COM_JOB_CREATE_URL, json=json,headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        self.assertNotEqual(resp.status_code, 200)

    def test__when_salary_max_is_less_than_salary_min_should_failed(self):
        json = {
            'company_id': self.company_id,
            'title': self.title,
            'description': self.description,
            'job_category_id': self.job_category_id,
            'experience': self.experience,
            'qualification_id': self.qualification_id,
            'job_gender_id': self.job_gender_id,
            'vacancy': self.vacancy,
            'salary': self.salary,
            'salary_min': "250000",
            'salary_max': "200000",
            'additional_requirements': self.additional_requirements,
            'application_deadline': self.application_deadline,
            'company_profile': self.company_profile,
            'education': self.education,
            'address': self.address,
            'job_area': self.job_area,
            'job_city': self.job_city,
            'job_type': self.job_type,
            'job_site': self.job_site,
            'job_nature': self.job_nature,
            'responsibilities': self.responsibilities,
            'other_benefits': self.other_benefits,
            'skills': self.skills

        }
        resp = requests.post(COM_JOB_CREATE_URL, json=json, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertNotEqual(resp.status_code, 200)

    def test__when_user_type_pro__should_fail(self):
        data = signin_as_pro()
        access_token = data['access']
        json = {
            'company_id': self.company_id,
            'title': self.title,
            'description': self.description,
            'job_category_id': self.job_category_id,
            'experience': self.experience,
            'qualification_id': self.qualification_id,
            'job_gender_id': self.job_gender_id,
            'vacancy': self.vacancy,
            'salary': self.salary,
            'salary_min': self.salary_min,
            'salary_max': self.salary_max,
            'additional_requirements': self.additional_requirements,
            'application_deadline': self.application_deadline,
            'company_profile': self.company_profile,
            'education': self.education,
            'address': self.address,
            'job_area': self.job_area,
            'job_city': self.job_city,
            'job_type': self.job_type,
            'job_site': self.job_site,
            'job_nature': self.job_nature,
            'responsibilities': self.responsibilities,
            'other_benefits': self.other_benefits,
            'skills': self.skills

        }
        resp = requests.post(COM_JOB_CREATE_URL, json=json, headers={'Authorization': 'Bearer ' + access_token})
        self.assertEqual(resp.status_code, 403)


class TestJobUpdateView(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_com()
        self.access_token = data['access']
        self.title = "Title Example"
        self.status = "DRAFT"
        self.job_category_id = "Job Category Example Two"
        self.qualification_id = "Qualification Example Four"
        self.experience = "3"
        self.job_gender_id = "Female"
        self.description = "Updated Description "
        self.vacancy = "20"
        self.salary = "500000"
        self.salary_min = "0"
        self.salary_max = "200000"
        self.additional_requirements = "Updated Additional Requirements "
        self.application_deadline = "2030-07-09"
        self.company_profile = "Updated Company Profile"
        self.education = "This Is Updated Education"
        self.address = "House 76 Updated"
        self.job_area = "Dhanmondi,Dhaka"
        self.job_city = "Dhaka, Bangladesh"
        self.job_country = "Bangladesh"
        self.job_type = "PERMANENT"
        self.job_site = "REMOTE"
        self.job_nature = "PARTTIME"
        self.responsibilities = "The is Updated Responsibilities"
        self.other_benefits = "Updated Other Benefits"
        self.skills = ["1"]

    def test__when_valid__should_pass(self):
        json = {
            'title': self.title,
            'status': self.status,
            'description': self.description,
            'job_category': self.job_category_id,
            'experience': self.experience,
            'qualification': self.qualification_id,
            'job_gender': self.job_gender_id,
            'vacancy': self.vacancy,
            'additional_requirements': self.additional_requirements,
            'application_deadline': self.application_deadline,
            'company_profile': self.company_profile,
            'education': self.education,
            'address': self.address,
            'job_area': self.job_area,
            'job_type': self.job_type,
            'job_city': self.job_city,
            'job_site': self.job_site,
            'job_nature': self.job_nature,
            'responsibilities': self.responsibilities,
            'other_benefits': self.other_benefits,
            'job_skills': self.skills
        }
        resp = requests.put(COM_JOB_UPDATE_URL + JOB_ID_FOR_UPDATE + '/', json=json,
                            headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        self.assertEqual(resp.status_code, 200)


    def test__when_valid__status_draft_to_posted__should_pass(self):
        json = {
            'title': self.title,
            'status': 'POSTED',
            'description': self.description,
            'job_category': self.job_category_id,
            'experience': self.experience,
            'qualification': self.qualification_id,
            'job_gender': self.job_gender_id,
            'vacancy': self.vacancy,
            'additional_requirements': self.additional_requirements,
            'application_deadline': self.application_deadline,
            'company_profile': self.company_profile,
            'education': self.education,
            'address': self.address,
            'job_area': self.job_area,
            'job_type': self.job_type,
            'job_city': self.job_city,
            'job_site': self.job_site,
            'job_nature': self.job_nature,
            'responsibilities': self.responsibilities,
            'other_benefits': self.other_benefits,
            'job_skills': self.skills
        }
        resp = requests.put(COM_JOB_UPDATE_URL + JOB_ID_FOR_UPDATE + '/', json=json,
                            headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        self.assertEqual(resp.status_code, 200)


    def test__when_valid__status_posted_to_draft__should_pass(self):
        json = {
            'title': self.title,
            'status': 'DRAFT',
            'description': self.description,
            'job_category': self.job_category_id,
            'experience': self.experience,
            'qualification': self.qualification_id,
            'job_gender': self.job_gender_id,
            'vacancy': self.vacancy,
            'additional_requirements': self.additional_requirements,
            'application_deadline': self.application_deadline,
            'company_profile': self.company_profile,
            'education': self.education,
            'address': self.address,
            'job_area': self.job_area,
            'job_type': self.job_type,
            'job_city': self.job_city,
            'job_site': self.job_site,
            'job_nature': self.job_nature,
            'responsibilities': self.responsibilities,
            'other_benefits': self.other_benefits,
            'job_skills': self.skills
        }
        resp = requests.put(COM_JOB_UPDATE_URL + JOB_ID_FOR_UPDATE + '/', json=json,
                            headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        self.assertEqual(resp.status_code, 200)

    def test__when_title_empty__should_failed(self):
        json = {
            'title': "",
            'status': self.status,
            'description': self.description,
            'job_category': self.job_category_id,
            'experience': self.experience,
            'qualification': self.qualification_id,
            'job_gender': self.job_gender_id,
            'vacancy': self.vacancy,
            'additional_requirements': self.additional_requirements,
            'application_deadline': self.application_deadline,
            'company_profile': self.company_profile,
            'education': self.education,
            'address': self.address,
            'job_area': self.job_area,
            'job_city': self.job_city,
            'job_type': self.job_type,
            'job_site': self.job_site,
            'job_nature': self.job_nature,
            'responsibilities': self.responsibilities,
            'other_benefits': self.other_benefits,
            'job_skills': self.skills
        }
        resp = requests.put(COM_JOB_UPDATE_URL + JOB_ID_FOR_UPDATE + '/', json=json,
                            headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 400)

    def test__when_title_null__should_fail(self):
        json = {

            'status': self.status,
            'description': self.description,
            'job_category': self.job_category_id,
            'experience': self.experience,
            'qualification': self.qualification_id,
            'job_gender': self.job_gender_id,
            'vacancy': self.vacancy,
            'additional_requirements': self.additional_requirements,
            'application_deadline': self.application_deadline,
            'company_profile': self.company_profile,
            'education': self.education,
            'address': self.address,
            'job_area': self.job_area,
            'job_city': self.job_city,
            'job_type': self.job_type,
            'job_site': self.job_site,
            'job_nature': self.job_nature,
            'responsibilities': self.responsibilities,
            'other_benefits': self.other_benefits,
            'job_skills': self.skills
        }
        resp = requests.put(COM_JOB_UPDATE_URL + JOB_ID_FOR_UPDATE + '/', json=json, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 400)

    def test__when_invalid_access_token_should_failed(self):
        invalid_access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIj'
        json = {
            'status': self.status,
            'description': self.description,
            'job_category': self.job_category_id,
            'experience': self.experience,
            'qualification': self.qualification_id,
            'job_gender': self.job_gender_id,
            'vacancy': self.vacancy,
            'additional_requirements': self.additional_requirements,
            'application_deadline': self.application_deadline,
            'company_profile': self.company_profile,
            'education': self.education,
            'address': self.address,
            'job_area': self.job_area,
            'job_type': self.job_type,
            'job_city': self.job_city,
            'job_site': self.job_site,
            'job_nature': self.job_nature,
            'responsibilities': self.responsibilities,
            'other_benefits': self.other_benefits,
            'job_skills': self.skills
        }
        resp = requests.put(COM_JOB_UPDATE_URL + JOB_ID_FOR_UPDATE + '/', json=json,
                            headers={'Authorization': 'Bearer ' + invalid_access_token})
        self.assertEqual(resp.status_code, 401)

    def test__when_user_type_pro__should_fail(self):
        data = signin_as_pro()
        access_token = data['access']
        json = {
            'company_id': COMPANY_NAME,
            'title': self.title,
            'description': self.description,
            'job_category_id': self.job_category_id,
            'experience': self.experience,
            'qualification_id': self.qualification_id,
            'job_gender_id': self.job_gender_id,
            'vacancy': self.vacancy,
            'salary': self.salary,
            'salary_min': self.salary_min,
            'salary_max': self.salary_max,
            'additional_requirements': self.additional_requirements,
            'application_deadline': self.application_deadline,
            'company_profile': self.company_profile,
            'education': self.education,
            'address': self.address,
            'job_area': self.job_area,
            'job_city': self.job_city,
            'job_type': self.job_type,
            'job_site': self.job_site,
            'job_nature': self.job_nature,
            'responsibilities': self.responsibilities,
            'other_benefits': self.other_benefits,
            'skills': self.skills

        }
        resp = requests.put(COM_JOB_UPDATE_URL + JOB_ID_FOR_UPDATE + '/', json=json,
                            headers={'Authorization': 'Bearer ' + access_token})
        self.assertEqual(resp.status_code, 403)


if __name__ == '__main__':
    unittest.main()
