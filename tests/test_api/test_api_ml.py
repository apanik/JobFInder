import unittest
from datetime import datetime

from tests.config_api import MAIN_URL, COM_SIGNIN_URL
from tests.test_api.common import signin_as_pro, signin_as_com, signin_as_staff
import requests

ML_JOB_API_URL = f'{MAIN_URL}/api/admin/job/get/'
JOB_ID_UPDATE = "528731050c7d4809a0f361db7136a87e"
JOB_ID = "0711248315e942adbf1c75fa9c64ad66"
ML_JOB_CREATE_URL = f'{MAIN_URL}/api/admin/job/create/'
ML_JOB_UPDATE_URL = f'{MAIN_URL}/api/admin/job/update/'
ML_ADMIN_JOB_LIST = f'{MAIN_URL}/api/admin/job/list/'
COMPANY_NAME = 'Company Example'


class TestMlJobAPI(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_staff()
        self.access_token = data['access']

    def test__when_valid__should_pass(self):
        resp = requests.get(ML_JOB_API_URL + JOB_ID, headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        self.assertIsNotNone(data['job_id'])
        self.assertIsNotNone(data['company'])
        self.assertEqual(resp.status_code, 200)

    def test__when_Job_Id_is_invalid__should_fail(self):
        INVALID_JOB_ID = "f1d94f74-d55c-4612-abee-13a877c576aX"
        resp = requests.get(ML_JOB_API_URL + INVALID_JOB_ID, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 500)

    def test__when_Job_Id_is_empty__should_fail(self):
        INVALID_JOB_ID = ""
        resp = requests.get(ML_JOB_API_URL + INVALID_JOB_ID, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 404)

    def test__when_Job_Id_is_null__should_fail(self):
        resp = requests.get(ML_JOB_API_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 404)

    def test__when_access_token_none_or_invalid__should_fail(self):
        resp = requests.get(ML_JOB_API_URL + JOB_ID)
        self.assertEqual(resp.status_code, 401)


class TestJobCreateView(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_com()
        self.access_token = data['access']
        # TITLE HERE: REQUIRED
        self.title = "Testing Machine Learning Team's API"
        self.address = "Example"
        self.job_area = "Dhanmondi"
        self.job_city = "Dhaka, Bangladesh"
        # self.job_country = ""
        self.salary = "30000"
        self.salary_min = "25000.00"
        self.salary_max = "50000.00"
        self.currency = "BDT"
        self.other_benefits = "2 times Meal, 50% Bonus On Festival"
        self.experience = 1
        self.qualification = "Qualification Example Two"
        self.description = "Employee have to hard worker and .......& so on"
        self.responsibilities = "Problem Solving Responsibility"
        self.additional_requirements = "Experience in Java and Spring will be added advantage"
        self.education = "Graduate"
        self.vacancy = 2
        self.application_deadline = "2022-06-07"
        # COMPANY NAME HERE: REQUIRED
        self.company = COMPANY_NAME
        self.company_profile = "Almost 10 years in IT Industry.....& so on"
        self.company_address = "Voot er Goli"
        self.company_area = "dhanmondi"
        self.company_city = "Dhaka, Bangladesh"
        # self.company_country = data['access']
        self.latitude = "23.68"
        self.longitude = "90.35"
        self.raw_content = "Raw Content Here....."
        # self.favorite_count = data['access']
        # self.applied_count = data['access']
        self.terms_and_condition = True
        self.job_skills = ["1"]
        self.status = "DRAFT"
        self.job_site = "REMOTE"
        self.job_nature = "PARTTIME"
        self.job_type = "PERMANENT"
        self.creator_type = "OPERATOR"
        self.job_source_1 = "Job Source One"
        self.job_url_1 = "https://www.exampleOne.com/"
        self.job_source_2 = "Job Source Two"
        self.job_url_2 = "https://www.exampleTwo.com/"
        self.job_source_3 = "Job Source Three"
        self.job_url_3 = "https://www.exampleThree.com/"
        self.job_category = "Job Category Example Two"
        self.job_gender = "Male"
        self.post_date = datetime.now()
        # self.review_date = data['access']
        # self.approve_date = data['access']
        # self.publish_date = data['access']
        self.featured = True

    def test__when_valid__job_create_view__should_pass(self):
        json = {
            'title': self.title,
            'address': self.address,
            'job_area': self.job_area,
            'job_city': self.job_city,
            'salary': self.salary,
            'salary_min': self.salary_min,
            'salary_max': self.salary_max,
            'currency': self.currency,
            'other_benefits': self.other_benefits,
            'experience': self.experience,
            'description': self.description,
            'qualification': self.qualification,
            'responsibilities': self.responsibilities,
            'additional_requirements': self.additional_requirements,
            'education': self.education,
            'vacancy': self.vacancy,
            'application_deadline': self.application_deadline,
            'company': self.company,
            'company_profile': self.company_profile,
            'company_address': self.company_address,
            'company_area': self.company_area,
            'company_city': self.company_city,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'raw_content': self.raw_content,
            'terms_and_condition': self.terms_and_condition,
            'job_skills': self.job_skills,
            'status': self.status,
            'job_site': self.job_site,
            'job_nature': self.job_nature,
            'job_type': self.job_type,
            'creator_type': self.creator_type,
            'job_source_1': self.job_source_1,
            'job_url_1': self.job_url_1,
            'job_source_2': self.job_source_2,
            'job_url_2': self.job_url_2,
            'job_source_3': self.job_source_3,
            'job_url_3': self.job_url_3,
            'job_category': self.job_category,
            'job_gender': self.job_gender,
            'post_date': str(self.post_date),
            'featured': self.featured,

        }
        resp = requests.post(ML_JOB_CREATE_URL, json=json, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 403)

    def test__when_required_filed_title_and_company_empty__should_fail(self):
        json = {
            'title': "",
            'address': self.address,
            'job_area': self.job_area,
            'job_city': self.job_city,
            'salary': self.salary,
            'salary_min': self.salary_min,
            'salary_max': self.salary_max,
            'currency': self.currency,
            'other_benefits': self.other_benefits,
            'experience': self.experience,
            'description': self.description,
            'qualification': self.qualification,
            'responsibilities': self.responsibilities,
            'additional_requirements': self.additional_requirements,
            'education': self.education,
            'vacancy': self.vacancy,
            'application_deadline': self.application_deadline,
            'company': "",
            'company_profile': self.company_profile,
            'company_address': self.company_address,
            'company_area': self.company_area,
            'company_city': self.company_city,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'raw_content': self.raw_content,
            'terms_and_condition': self.terms_and_condition,
            'job_skills': self.job_skills,
            'status': self.status,
            'job_site': self.job_site,
            'job_nature': self.job_nature,
            'job_type': self.job_type,
            'creator_type': self.creator_type,
            'job_source_1': self.job_source_1,
            'job_url_1': self.job_url_1,
            'job_source_2': self.job_source_2,
            'job_url_2': self.job_url_2,
            'job_source_3': self.job_source_3,
            'job_url_3': self.job_url_3,
            'job_category': self.job_category,
            'job_gender': self.job_gender,
            'post_date': str(self.post_date),
            'featured': self.featured,

        }
        resp = requests.post(ML_JOB_CREATE_URL, json=json, headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        self.assertEqual(resp.status_code, 403)

    def test__when_required_field_title_and_company_null__should_fail(self):
        json = {
            'address': self.address,
            'job_area': self.job_area,
            'job_city': self.job_city,
            'salary': self.salary,
            'salary_min': self.salary_min,
            'salary_max': self.salary_max,
            'currency': self.currency,
            'other_benefits': self.other_benefits,
            'experience': self.experience,
            'description': self.description,
            'qualification': self.qualification,
            'responsibilities': self.responsibilities,
            'additional_requirements': self.additional_requirements,
            'education': self.education,
            'vacancy': self.vacancy,
            'application_deadline': self.application_deadline,
            'company_profile': self.company_profile,
            'company_address': self.company_address,
            'company_area': self.company_area,
            'company_city': self.company_city,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'raw_content': self.raw_content,
            'terms_and_condition': self.terms_and_condition,
            'job_skills': self.job_skills,
            'status': self.status,
            'job_site': self.job_site,
            'job_nature': self.job_nature,
            'job_type': self.job_type,
            'creator_type': self.creator_type,
            'job_source_1': self.job_source_1,
            'job_url_1': self.job_url_1,
            'job_source_2': self.job_source_2,
            'job_url_2': self.job_url_2,
            'job_source_3': self.job_source_3,
            'job_url_3': self.job_url_3,
            'job_category': self.job_category,
            'job_gender': self.job_gender,
            'post_date': str(self.post_date),
            'featured': self.featured,

        }
        resp = requests.post(ML_JOB_CREATE_URL, json=json, headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        self.assertEqual(resp.status_code, 403)

    def test__when_access_token_none__should_fail(self):
        json = {
            'title': self.title,
            'address': self.address,
            'job_area': self.job_area,
            'job_city': self.job_city,
            'salary': self.salary,
            'salary_min': self.salary_min,
            'salary_max': self.salary_max,
            'currency': self.currency,
            'other_benefits': self.other_benefits,
            'experience': self.experience,
            'description': self.description,
            'qualification': self.qualification,
            'responsibilities': self.responsibilities,
            'additional_requirements': self.additional_requirements,
            'education': self.education,
            'vacancy': self.vacancy,
            'application_deadline': self.application_deadline,
            'company': self.company,
            'company_profile': self.company_profile,
            'company_address': self.company_address,
            'company_area': self.company_area,
            'company_city': self.company_city,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'raw_content': self.raw_content,
            'terms_and_condition': self.terms_and_condition,
            'job_skills': self.job_skills,
            'status': self.status,
            'job_site': self.job_site,
            'job_nature': self.job_nature,
            'job_type': self.job_type,
            'creator_type': self.creator_type,
            'job_source_1': self.job_source_1,
            'job_url_1': self.job_url_1,
            'job_source_2': self.job_source_2,
            'job_url_2': self.job_url_2,
            'job_source_3': self.job_source_3,
            'job_url_3': self.job_url_3,
            'job_category': self.job_category,
            'job_gender': self.job_gender,
            'post_date': str(self.post_date),
            'featured': self.featured,

        }
        resp = requests.post(ML_JOB_CREATE_URL, json=json)
        data = resp.json()
        self.assertEqual(resp.status_code, 401)


class TestMlJobUpdateAPI(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_staff()
        self.access_token = data['access']
        # TITLE HERE: REQUIRED
        self.title = "Testing Machine Learning Team's API [updated]"
        self.address = "Address [updated]"
        self.job_area = "Dhanmondi [updated]"
        self.job_city = "Dhaka, Bangladesh"
        # self.job_country = ""
        self.salary = "30000"
        self.salary_min = "25000.00"
        self.salary_max = "50000.00"
        self.currency = "BDT"
        self.other_benefits = "2 times Meal, 50% Bonus On Festival [updated]"
        self.experience = 1
        self.qualification = "Qualification Example Five"
        self.description = "Employee have to hard worker and .......& so on [updated]"
        self.responsibilities = "Problem Solving Responsibility [updated]"
        self.additional_requirements = "Experience in Java and Spring will be added advantage [updated]"
        self.education = "Graduate [updated]"
        self.vacancy = 1
        self.application_deadline = "2022-06-07"
        # COMPANY NAME HERE: REQUIRED
        self.company = COMPANY_NAME
        self.company_profile = "Almost 10 years in IT Industry.....& so on [updated]"
        self.company_address = "Address [updated]"
        self.company_area = "dhanmondi"
        self.company_city = "Dhaka, Bangladesh"
        # self.company_country = data['access']
        self.latitude = "23.68"
        self.longitude = "90.35"
        self.raw_content = "Raw Content Here....."
        # self.favorite_count = data['access']
        # self.applied_count = data['access']
        self.terms_and_condition = True
        self.job_skills = ["1"]
        self.status = "DRAFT"
        self.job_site = "REMOTE"
        self.job_nature = "PARTTIME"
        self.job_type = "PERMANENT"
        self.creator_type = "OPERATOR"
        self.job_source_1 = "Job Source One"
        self.job_url_1 = "https://www.exampleOne.com/"
        self.job_source_2 = "Job Source Two"
        self.job_url_2 = "https://www.exampleTwo.com/"
        self.job_source_3 = "Job Source One"
        self.job_url_3 = "https://www.exampleThree.com/"
        self.job_category = "Job Category Example Two"
        self.job_gender = "Male"
        self.post_date = datetime.now()
        # self.review_date = data['access']
        # self.approve_date = data['access']
        # self.publish_date = data['access']
        self.featured = True

    def test__when_valid__auth_and_data_job_update__should_pass(self):
        json = {
            'title': self.title,
            'address': self.address,
            'job_area': self.job_area,
            'job_city': self.job_city,
            'salary': self.salary,
            'salary_min': self.salary_min,
            'salary_max': self.salary_max,
            'currency': self.currency,
            'other_benefits': self.other_benefits,
            'experience': self.experience,
            'description': self.description,
            'qualification': self.qualification,
            'responsibilities': self.responsibilities,
            'additional_requirements': self.additional_requirements,
            'education': self.education,
            'vacancy': self.vacancy,
            'application_deadline': self.application_deadline,
            'company': self.company,
            'company_profile': self.company_profile,
            'company_address': self.company_address,
            'company_area': self.company_area,
            'company_city': self.company_city,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'raw_content': self.raw_content,
            'terms_and_condition': self.terms_and_condition,
            'job_skills': self.job_skills,
            'status': self.status,
            'job_site': self.job_site,
            'job_nature': self.job_nature,
            'job_type': self.job_type,
            'creator_type': self.creator_type,
            'job_source_1': self.job_source_1,
            'job_url_1': self.job_url_1,
            'job_source_2': self.job_source_2,
            'job_url_2': self.job_url_2,
            'job_source_3': self.job_source_3,
            'job_url_3': self.job_url_3,
            'job_category': self.job_category,
            'job_gender': self.job_gender,
            'post_date': str(self.post_date),
            'featured': self.featured

        }
        resp = requests.put(ML_JOB_UPDATE_URL + JOB_ID_UPDATE + '/', json=json,
                            headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        self.assertEqual(resp.status_code, 200)

    def test__when_required_filed__title_and_company_empty__should_fail(self):
        json = {
            'title': "",
            'address': self.address,
            'job_area': self.job_area,
            'job_city': self.job_city,
            'salary': self.salary,
            'salary_min': self.salary_min,
            'salary_max': self.salary_max,
            'currency': self.currency,
            'other_benefits': self.other_benefits,
            'experience': self.experience,
            'description': self.description,
            'qualification': self.qualification,
            'responsibilities': self.responsibilities,
            'additional_requirements': self.additional_requirements,
            'education': self.education,
            'vacancy': self.vacancy,
            'application_deadline': self.application_deadline,
            'company': "",
            'company_profile': self.company_profile,
            'company_address': self.company_address,
            'company_area': self.company_area,
            'company_city': self.company_city,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'raw_content': self.raw_content,
            'terms_and_condition': self.terms_and_condition,
            'job_skills': self.job_skills,
            'status': self.status,
            'job_site': self.job_site,
            'job_nature': self.job_nature,
            'job_type': self.job_type,
            'creator_type': self.creator_type,
            'job_source_1': self.job_source_1,
            'job_url_1': self.job_url_1,
            'job_source_2': self.job_source_2,
            'job_url_2': self.job_url_2,
            'job_source_3': self.job_source_3,
            'job_url_3': self.job_url_3,
            'job_category': self.job_category,
            'job_gender': self.job_gender,
            'post_date': str(self.post_date),
            'featured': self.featured,

        }
        resp = requests.post(ML_JOB_CREATE_URL, json=json, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 400)

    #
    def test__when_required_field__title_and_company_null__should_fail(self):
        json = {
            'address': self.address,
            'job_area': self.job_area,
            'job_city': self.job_city,
            'salary': self.salary,
            'salary_min': self.salary_min,
            'salary_max': self.salary_max,
            'currency': self.currency,
            'other_benefits': self.other_benefits,
            'experience': self.experience,
            'description': self.description,
            'qualification': self.qualification,
            'responsibilities': self.responsibilities,
            'additional_requirements': self.additional_requirements,
            'education': self.education,
            'vacancy': self.vacancy,
            'application_deadline': self.application_deadline,
            'company_profile': self.company_profile,
            'company_address': self.company_address,
            'company_area': self.company_area,
            'company_city': self.company_city,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'raw_content': self.raw_content,
            'terms_and_condition': self.terms_and_condition,
            'job_skills': self.job_skills,
            'status': self.status,
            'job_site': self.job_site,
            'job_nature': self.job_nature,
            'job_type': self.job_type,
            'creator_type': self.creator_type,
            'job_source_1': self.job_source_1,
            'job_url_1': self.job_url_1,
            'job_source_2': self.job_source_2,
            'job_url_2': self.job_url_2,
            'job_source_3': self.job_source_3,
            'job_url_3': self.job_url_3,
            'job_category': self.job_category,
            'job_gender': self.job_gender,
            'post_date': str(self.post_date),
            'featured': self.featured,

        }
        resp = requests.post(ML_JOB_CREATE_URL, json=json, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 400)

    #
    def test__when_access_token_none__should_fail(self):
        json = {
            'title': self.title,
            'address': self.address,
            'job_area': self.job_area,
            'job_city': self.job_city,
            'salary': self.salary,
            'salary_min': self.salary_min,
            'salary_max': self.salary_max,
            'currency': self.currency,
            'other_benefits': self.other_benefits,
            'experience': self.experience,
            'description': self.description,
            'qualification': self.qualification,
            'responsibilities': self.responsibilities,
            'additional_requirements': self.additional_requirements,
            'education': self.education,
            'vacancy': self.vacancy,
            'application_deadline': self.application_deadline,
            'company': self.company,
            'company_profile': self.company_profile,
            'company_address': self.company_address,
            'company_area': self.company_area,
            'company_city': self.company_city,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'raw_content': self.raw_content,
            'terms_and_condition': self.terms_and_condition,
            'job_skills': self.job_skills,
            'status': self.status,
            'job_site': self.job_site,
            'job_nature': self.job_nature,
            'job_type': self.job_type,
            'creator_type': self.creator_type,
            'job_source_1': self.job_source_1,
            'job_url_1': self.job_url_1,
            'job_source_2': self.job_source_2,
            'job_url_2': self.job_url_2,
            'job_source_3': self.job_source_3,
            'job_url_3': self.job_url_3,
            'job_category': self.job_category,
            'job_gender': self.job_gender,
            'post_date': str(self.post_date),
            'featured': self.featured,

        }
        resp = requests.post(ML_JOB_CREATE_URL, json=json)
        self.assertEqual(resp.status_code, 401)


class TestMlAdminJobLst(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_staff()
        self.access_token = data['access']

    def test__when_valid__admin_job_list__should_pass(self):
        resp = requests.get(ML_ADMIN_JOB_LIST, headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        # self.assertIsNotNone(data['count'])
        # self.assertIsNotNone(data['start_index'])
        # self.assertIsNotNone(data['end_index'])
        # self.assertIsNotNone(data['page_number'])
        # self.assertIsNotNone(data['page_size'])
        # self.assertIsNotNone(data['page_count'])
        # self.assertIsNotNone(data['page_data_count'])
        # self.assertIsNotNone(data['pages'])
        self.assertEqual(resp.status_code, 200)

    def test__when_access_token_none__should_pass(self):
        resp = requests.get(ML_ADMIN_JOB_LIST)
        self.assertEqual(resp.status_code, 401)


if __name__ == '__main__':
    unittest.main()
