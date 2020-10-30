import unittest

from tests.config_api import MAIN_URL
from tests.test_api.common import *

JOB_LIST_URL = f'{MAIN_URL}/api/job/search/?'
COMPANY_NAME = "Company Example"
Q = "python"
UNSPECIFIED_SALARY = "1"
CATEGORY = "Job Category Example Two"
SKILL = "1"
JOB_CITY = "Dhaka, Bangladesh"
SALARY_RANGE = "salaryMin=100000&salaryMax=300000"
EXPERIENCE_RANGE = "experienceMin=1&experienceMax=2"

SIMILAR_JOBS_URL = f'{MAIN_URL}/api/job/similar/'
JOB_ID = '0711248315e942adbf1c75fa9c64ad66'
RECENT_JOBS_URL = f'{MAIN_URL}/api/job/recent/'
FAVOURITE_JOBS_URL = f'{MAIN_URL}/api/job/favourite/'
APPLIED_JOBS_URL = f'{MAIN_URL}/api/job/applied/'


class TestJobList(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__when_company_name_valid__should_pass(self):
        resp = requests.get(JOB_LIST_URL + 'company=' + COMPANY_NAME)
        self.assertEqual(resp.status_code, 200)

    def test__with_access_token_also__should_pass(self):
        resp = requests.get(JOB_LIST_URL + 'company=' + "None",
                            headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)

    def test__when_company_name_invalid__should_pass(self):
        resp = requests.get(JOB_LIST_URL + 'company=' + 'FingerCross')
        self.assertEqual(resp.status_code, 200)

    def test__when_query_is_valid__should_pass(self):
        resp = requests.get(JOB_LIST_URL + 'q=' + Q)
        self.assertEqual(resp.status_code, 200)

    def test__when_query_is_invalid__should_pass(self):
        resp = requests.get(JOB_LIST_URL + 'q=' + "Unknown Query")
        self.assertEqual(resp.status_code, 200)

    def test__when_query_is_invalid__count_and_result_should_zero(self):
        resp = requests.get(JOB_LIST_URL + 'q=' + "Unknown Query")
        data = resp.json()
        if data['count'] and data['results'] != 0:
            raise self.fail()

    def test__when_salary_is_specified__should_pass(self):
        resp = requests.get(JOB_LIST_URL + 'unspecified_salary=' + "0")
        self.assertEqual(resp.status_code, 200)

    def test__when_salary_is_unspecified__should_pass(self):
        resp = requests.get(JOB_LIST_URL + 'unspecified_salary=' + UNSPECIFIED_SALARY)
        self.assertEqual(resp.status_code, 200)

    def test__when_sort_is_descending__should_pass(self):
        resp = requests.get(JOB_LIST_URL + 'sort=' + 'descending')
        self.assertEqual(resp.status_code, 200)

    def test__when_descending_sort_value_ascending_sort_value_same__should_fail(self):
        # Ascending and Descending is not working
        resp1 = requests.get(JOB_LIST_URL + 'sort=' + 'descending')
        data1 = resp1.json()
        resp2 = requests.get(JOB_LIST_URL + 'sort=' + 'ascending')
        data2 = resp2.json()
        if data1 == data2:
            self.fail("Ascending and Descending sorting value can't be same when data is more than one")

    def test__when_category_is_valid__should_pass(self):
        resp = requests.get(JOB_LIST_URL + 'category=' + CATEGORY)
        self.assertEqual(resp.status_code, 200)

    def test__when_Skill_is_valid_id__should_pass(self):
        resp = requests.get(JOB_LIST_URL + 'skill=' + SKILL)
        self.assertEqual(resp.status_code, 200)

    def test__when_Skill_is_invalid__should_pass(self):
        resp = requests.get(JOB_LIST_URL + 'skill=' + 'NoSkill')
        data = resp.json()
        self.assertEqual(data['count'], 0)

    def test__when_job_city_is_valid__should_return_data(self):
        resp = requests.get(JOB_LIST_URL + 'job_city=' + JOB_CITY)
        data = resp.json()
        if data['count'] == 0:
            self.fail("Job City Filter Should Return Data")

    def test__when_Salary_Min_and_Salary_Max_is_valid__should_pass(self):
        resp = requests.get(JOB_LIST_URL + SALARY_RANGE)
        self.assertEqual(resp.status_code, 200)

    def test__when_Salary_Min_is_Greater_than_Salary_Max__should_fail(self):
        SALARY_RANGE_INVALID = "salaryMin=300000&salaryMax=1000"
        resp = requests.get(JOB_LIST_URL + SALARY_RANGE_INVALID)
        data = resp.json()
        self.assertEqual(resp.status_code, 200)
        if data['count'] > 0:
            self.fail("Salary Min Can't be greater than Salary Max")

    def test__when_Experience_Min_and_Experience_Max_is_valid__should_pass(self):
        resp = requests.get(JOB_LIST_URL + EXPERIENCE_RANGE)
        self.assertEqual(resp.status_code, 200)

    def test__when_datePosted_Last_hour__should_pass(self):
        resp = requests.get(JOB_LIST_URL + 'datePosted=Last hour')
        self.assertEqual(resp.status_code, 200)

    def test__when_datePosted_Last_24hour__should_pass(self):
        resp = requests.get(JOB_LIST_URL + 'datePosted=Last 24 hour')
        self.assertEqual(resp.status_code, 200)

    def test__when_datePosted_Last_7days__should_pass(self):
        resp = requests.get(JOB_LIST_URL + 'datePosted=Last 7 days')
        self.assertEqual(resp.status_code, 200)

    def test__when_datePosted_Last_14days__should_pass(self):
        resp = requests.get(JOB_LIST_URL + 'datePosted=Last 14 days')
        self.assertEqual(resp.status_code, 200)

    def test__when_datePosted_Last_30days__should_pass(self):
        resp = requests.get(JOB_LIST_URL + 'datePosted=Last 30 days')
        self.assertEqual(resp.status_code, 200)

    def test__when_gender_Male_should__pass(self):
        resp = requests.get(JOB_LIST_URL + 'gender=Male')
        self.assertEqual(resp.status_code, 200)

    def test__when_gender_Female_should__pass(self):
        resp = requests.get(JOB_LIST_URL + 'gender=Female')
        self.assertEqual(resp.status_code, 200)

    def test__when_gender_Any_should__pass(self):
        resp = requests.get(JOB_LIST_URL + 'gender=Any')
        self.assertEqual(resp.status_code, 200)

    def test__when_job_type_Contractual__should_pass(self):
        resp = requests.get(JOB_LIST_URL + 'job_type=Contractual')
        self.assertEqual(resp.status_code, 200)

    def test__when_job_type_Internship__should_pass(self):
        resp = requests.get(JOB_LIST_URL + 'job_type=Internship')
        self.assertEqual(resp.status_code, 200)

    def test__when_job_type_Permanent_full_time__should_pass(self):
        resp = requests.get(JOB_LIST_URL + 'job_type=Permanent (Full-time)')
        self.assertEqual(resp.status_code, 200)

    def test__when_job_type_Permanent_part_time__should_pass(self):
        resp = requests.get(JOB_LIST_URL + 'job_type=Permanent (Part-time)')
        self.assertEqual(resp.status_code, 200)

    def test__when_top_skills_is_Valid__should_pass(self):
        resp = requests.get(JOB_LIST_URL + 'top-skill=1')
        self.assertEqual(resp.status_code, 200)

    def test__when_top_qualification_is_valid__should_pass(self):
        resp = requests.get(JOB_LIST_URL + 'qualification=BSc in CSE')
        self.assertEqual(resp.status_code, 200)


class TestSimilarJobs(unittest.TestCase):
    def test__when_valid__should_pass(self):
        resp = requests.get(SIMILAR_JOBS_URL + JOB_ID)
        self.assertEqual(resp.status_code, 200)

    def test__when_id_invalid__should_fail(self):
        resp = requests.get(SIMILAR_JOBS_URL + '04855d6f3ace4dab9ffa29')
        self.assertEqual(resp.status_code, 500)


class TestRecentJobs(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__when_valid__should_pass(self):
        resp = requests.get(RECENT_JOBS_URL)
        self.assertEqual(resp.status_code, 200)

    def test__with_access_token__should_pass(self):
        resp = requests.get(RECENT_JOBS_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)


class TestFavouriteJobs(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__when_valid__should_pass(self):
        resp = requests.get(FAVOURITE_JOBS_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        self.assertEqual(resp.status_code, 200)

    def test__without_access_token__should_failed(self):
        resp = requests.get(FAVOURITE_JOBS_URL)
        self.assertEqual(resp.status_code, 401)


class TestAppliedJobs(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__when_valid__should_pass(self):
        resp = requests.get(APPLIED_JOBS_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)

    def test__without_access_token__should_failed(self):
        resp = requests.get(FAVOURITE_JOBS_URL)
        self.assertEqual(resp.status_code, 401)

if __name__ == '__main__':
    unittest.main()
