import unittest

from tests.config_api import MAIN_URL
from tests.test_api.common import *

JOB_SOURCE_LIST_URL = f'{MAIN_URL}/api/job-source/list/'
JOB_CATEGORY_LIST_URL = f'{MAIN_URL}/api/job-category/list/'
JOB_GENDER_LIST_URL = f'{MAIN_URL}/api/job-gender/list/'
JOB_SITE_LIST_URL = f'{MAIN_URL}/api/job-site/list/'
JOB_NATURE_LIST_URL = f'{MAIN_URL}/api/job-nature/list/'
JOB_TYPE_LIST_URL = f'{MAIN_URL}/api/job-type/list/'
JOB_STATUS_LIST_URL = f'{MAIN_URL}/api/job-status/list/'
JOB_CREATOR_TYPE_LIST_URL = f'{MAIN_URL}/api/job-creator-type/list'
CITY_LIST_URL = f'{MAIN_URL}/api/city/list/'
SALARY_RANGE_URL = f'{MAIN_URL}/api/job/salary-range/'
INDUSTRY_LIST_URL = f'{MAIN_URL}/api/industry/list'
JOB_TYPE_LIST_URL_TWO = f'{MAIN_URL}/api/job_type/list'
CURRENCY_LIST_URL = f'{MAIN_URL}/api/currency/list'
EXPERIENCE_LIST_URL = f'{MAIN_URL}/api/experience/list'
QUALIFICATION_LIST_URL = f'{MAIN_URL}/api/qualification/list'
GENDER_LIST_URL = f'{MAIN_URL}/api/gender/list'
SKILL_LIST_URL = f'{MAIN_URL}/api/skill/list/'


class TestJobSourceList(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__when_access_token_valid__job_source_list__should_pass(self):
        resp = requests.get(JOB_SOURCE_LIST_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)

    def test__when_access_token_empty__job_source_list__should_failed(self):
        resp = requests.get(JOB_SOURCE_LIST_URL)
        self.assertEqual(resp.status_code, 401)


class TestJobCategoryList(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__when_access_token_valid__job_category_list__should_pass(self):
        resp = requests.get(JOB_CATEGORY_LIST_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)

    def test__when_access_token_empty__job_category_list__should_failed(self):
        resp = requests.get(JOB_CATEGORY_LIST_URL)
        self.assertEqual(resp.status_code, 401)


class TestJobGenderList(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__when_access_token_valid__job_gender_list__should_pass(self):
        resp = requests.get(JOB_GENDER_LIST_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)

    def test__when_access_token_empty__job_gender_list__should_pass(self):
        resp = requests.get(JOB_GENDER_LIST_URL)
        self.assertEqual(resp.status_code, 200)


class TestJobSiteList(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__when_valid__should_pass(self):
        resp = requests.get(JOB_SITE_LIST_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)

    def test__when_access_token_invalid_or_none__should_failed(self):
        resp = requests.get(JOB_SITE_LIST_URL)
        self.assertEqual(resp.status_code, 401)


class TestJobNatureList(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__when_valid__should_pass(self):
        resp = requests.get(JOB_NATURE_LIST_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)

    def test__when_access_token_invalid_or_none__should_failed(self):
        resp = requests.get(JOB_NATURE_LIST_URL)
        self.assertEqual(resp.status_code, 401)


class TestJobTypeList(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__when_valid__should_pass(self):
        resp = requests.get(JOB_TYPE_LIST_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)

    def test__when_access_token_invalid_or_none__should_failed(self):
        resp = requests.get(JOB_TYPE_LIST_URL)
        self.assertEqual(resp.status_code, 401)


class TestJobStatusList(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__when_valid__should_pass(self):
        resp = requests.get(JOB_STATUS_LIST_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)

    def test__when_access_token_invalid_or_none__should_failed(self):
        resp = requests.get(JOB_STATUS_LIST_URL)
        self.assertEqual(resp.status_code, 401)


class TestJobCreatorTypeList(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__when_valid__should_pass(self):
        resp = requests.get(JOB_CREATOR_TYPE_LIST_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)

    def test__when_access_token_invalid_or_none__should_failed(self):
        resp = requests.get(JOB_CREATOR_TYPE_LIST_URL)
        self.assertEqual(resp.status_code, 401)


class TestCityList(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__when_valid__city_list__should_pass(self):
        resp = requests.get(CITY_LIST_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)

    def test__when_access_token_none__city_list__should_pass(self):
        resp = requests.get(CITY_LIST_URL)
        self.assertEqual(resp.status_code, 200)


class TestSalaryRange(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__when_valid__should_pass(self):
        resp = requests.get(SALARY_RANGE_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        self.assertIsNotNone(data['sr_min'])
        self.assertIsNotNone(data['sr_max'])
        self.assertEqual(resp.status_code, 200)

    def test__when_access_token_none__salary_range__should_pass(self):
        resp = requests.get(SALARY_RANGE_URL)
        data = resp.json()
        self.assertIsNotNone(data['sr_min'])
        self.assertIsNotNone(data['sr_max'])
        self.assertEqual(resp.status_code, 200)


class TestIndustryList(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__when_access_token_valid__should_pass(self):
        resp = requests.get(INDUSTRY_LIST_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)

    def test__when_no_access_token_provided__valid__should_pass(self):
        resp = requests.get(INDUSTRY_LIST_URL)
        self.assertEqual(resp.status_code, 200)




class TestJobTypeListTwo(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__when_access_token_valid__should_pass(self):
        resp = requests.get(JOB_TYPE_LIST_URL_TWO, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)

    def test__when_access_token_empty__should_pass(self):
        resp = requests.get(JOB_TYPE_LIST_URL_TWO)
        self.assertEqual(resp.status_code, 200)


class TestCurrencyList(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__when_access_token__currency_list__should_also_pass(self):
        resp = requests.get(CURRENCY_LIST_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)

    def test__when_access_token_empty__currency_list__should_pass(self):
        resp = requests.get(CURRENCY_LIST_URL)
        self.assertEqual(resp.status_code, 200)




class TestExperienceList(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__when_valid__should_pass(self):
        resp = requests.get(EXPERIENCE_LIST_URL)
        self.assertEqual(resp.status_code, 200)

    def test__when_access_token__should_also_pass(self):
        resp = requests.get(EXPERIENCE_LIST_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)


class TestQualificationList(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__when_valid__should_pass(self):
        resp = requests.get(QUALIFICATION_LIST_URL)
        self.assertEqual(resp.status_code, 200)

    def test__when_access_token__should_also_pass(self):
        resp = requests.get(QUALIFICATION_LIST_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)


class TestGenderList(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__when_access_token_valid__gender_list__should_pass(self):
        resp = requests.get(GENDER_LIST_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)

    def test__when_access_token_empty__gender_list__should_pass(self):
        resp = requests.get(GENDER_LIST_URL)
        self.assertEqual(resp.status_code, 200)



class TestSkillList(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__when_valid__should_pass(self):
        resp = requests.get(SKILL_LIST_URL)
        self.assertEqual(resp.status_code, 200)

    def test__when_access_token__should_also_pass(self):
        resp = requests.get(SKILL_LIST_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)


if __name__ == '__main__':
    unittest.main()
