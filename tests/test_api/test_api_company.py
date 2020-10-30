import unittest

from tests.config_api import MAIN_URL
from tests.test_api.common import *

COMPANY_NAME = 'Company Example'
COMPANY_LIST_URL = f'{MAIN_URL}/api/company/list'
COMPANY_SEARCH_BY_NAME = f'{MAIN_URL}/api/company/search/?name='
COMPANY_UPDATE_URL = f'{MAIN_URL}/api/company/update/'
COMPANY_JOB_APPLICATION_CHART_URL = f'{MAIN_URL}/api/company/dashboard/chart/'
COMPANY_DASHBOARD_RECENT_ACTIVITY_URL = f'{MAIN_URL}/api/company/dashboard/recent_activity/'
COMPANY_INFO_BOX_URL = f'{MAIN_URL}/api/company/dashboard/infobox/'


class TestCompanyList(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__when_valid__should_pass(self):
        resp = requests.get(COMPANY_LIST_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        self.assertIsNotNone(data['count'])
        self.assertIsNotNone(data['start_index'])
        self.assertIsNotNone(data['end_index'])
        self.assertIsNotNone(data['page_number'])
        self.assertIsNotNone(data['page_size'])
        self.assertIsNotNone(data['page_count'])
        self.assertIsNotNone(data['page_data_count'])
        self.assertEqual(resp.status_code, 200)

    def test__when_access_token_none__should_failed(self):
        resp = requests.get(COMPANY_LIST_URL)
        self.assertEqual(resp.status_code, 401)


class TestGetCompanyByName(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__when_valid__should__pass(self):
        resp = requests.get(COMPANY_SEARCH_BY_NAME + COMPANY_NAME,
                            headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        self.assertIsNotNone(data['count'])
        self.assertIsNotNone(data['start_index'])
        self.assertIsNotNone(data['end_index'])
        self.assertIsNotNone(data['page_number'])
        self.assertIsNotNone(data['page_size'])
        self.assertIsNotNone(data['page_count'])
        self.assertIsNotNone(data['page_data_count'])
        self.assertIsNotNone(data['pages'])
        self.assertEqual(resp.status_code, 200)

    def test__when_access_token_none__should_pass(self):
        resp = requests.get(COMPANY_SEARCH_BY_NAME + COMPANY_NAME)
        data = resp.json()
        self.assertIsNotNone(data['count'])
        self.assertIsNotNone(data['start_index'])
        self.assertIsNotNone(data['end_index'])
        self.assertIsNotNone(data['page_number'])
        self.assertIsNotNone(data['page_size'])
        self.assertIsNotNone(data['page_count'])
        self.assertIsNotNone(data['page_data_count'])
        self.assertIsNotNone(data['pages'])
        self.assertEqual(resp.status_code, 200)


class TestCompanyUpdateView(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_com()
        self.access_token = data['access']
        self.company_name = "Company Example"
        self.address = "Niketan, Gulshan"
        self.basis_membership_no = "1200"
        self.company_profile = "Updated Company Profile"
        self.year_of_eastablishment = "2000-06-07"
        self.legal_structure_of_this_company = "Head Based"
        self.total_number_of_human_resources = 100
        self.no_of_it_resources = 200
        self.area = "Gulshan"
        self.city = "Dhaka, Bangladesh"
        self.company_contact_no_one = "0178400800"
        self.company_contact_no_two = "01642552313"
        self.company_contact_no_three = "01642552314"
        self.organization_head = "Mr. X"
        self.organization_head_designation = "CEO"
        self.organization_head_number = "01910910901"
        self.contact_person = "Mr. Y"
        self.contact_person_designation = "Executive"
        self.contact_person_mobile_no = "016686666777"
        self.contact_person_email = "contact@xmail.com"
        self.company_name_bdjobs = "Moto X"
        self.company_name_facebook = "Moto X"
        self.company_name_google = "Moto X"
        self.latitude = "20.000"
        self.longitude = "30.000"


        # with open('/home/ap/Desktop/Office/jobXpress/static/images/company/company-logo-10.png',
        #           'r') as profile_picture:
        #     self.profile_picture = json.loads(profile_picture)

    def test__when_valid__should_pass(self):
        json = {
            "name": "Blank Company Example",
            "address": self.address,
            "basis_membership_no": self.basis_membership_no,
            "company_profile": self.company_profile,
            "year_of_eastablishment": self.year_of_eastablishment,
            "legal_structure_of_this_company": self.legal_structure_of_this_company,
            "total_number_of_human_resources": self.total_number_of_human_resources,
            "no_of_it_resources": self.no_of_it_resources,
            "area": self.area,
            "city": self.city,
            "company_contact_no_one": self.company_contact_no_one,
            "company_contact_no_two": self.company_contact_no_two,
            "company_contact_no_three": self.company_contact_no_three,
            "organization_head": self.organization_head,
            "organization_head_designation": self.organization_head_designation,
            "organization_head_number": self.organization_head_number,
            "contact_person": self.contact_person,
            "contact_person_designation": self.contact_person_designation,
            "contact_person_mobile_no": self.contact_person_mobile_no,
            "contact_person_email": self.contact_person_email,
            "company_name_bdjobs": self.company_name_bdjobs,
            "company_name_facebook": self.company_name_facebook,
            "company_name_google": self.company_name_google,
            "latitude": self.latitude,
            "longitude": self.longitude
            # "profile_picture": self.profile_picture,
        }
        resp = requests.put(COMPANY_UPDATE_URL, json=json,
                            headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)

    def test__when_latitude_and_longitude_empty__should_pass(self):
        json = {
            "address": "",
            "company_contact_no_one": "",
            "organization_head": "",
            "contact_person": "",
            "contact_person_designation": "",
        }
        resp = requests.put(COMPANY_UPDATE_URL, json=json,
                            headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)


class TestCompanyApplicationChart(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_com()
        self.access_token = data['access']

    def test__when_valid__should_pass(self):
        resp = requests.get(COMPANY_JOB_APPLICATION_CHART_URL,
                            headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)

    def test__when_access_token_none__should_fail(self):
        resp = requests.get(COMPANY_JOB_APPLICATION_CHART_URL)
        self.assertNotEqual(resp.status_code, 200)


class TestCompanydashboardRecentActivity(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_com()
        self.access_token = data['access']

    def test__when_valid__should_pass(self):
        resp = requests.get(COMPANY_DASHBOARD_RECENT_ACTIVITY_URL,
                            headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)

    def test__when_access_token_none__should_fail(self):
        resp = requests.get(COMPANY_DASHBOARD_RECENT_ACTIVITY_URL)
        self.assertEqual(resp.status_code, 401)


class TestCompanyInfoBox(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_com()
        self.access_token = data['access']

    def test__when_valid__should_pass(self):
        resp = requests.get(COMPANY_INFO_BOX_URL,
                            headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        self.assertIsNotNone(data['company_number_of_job'])
        self.assertIsNotNone(data['company_appilcation_count'])
        self.assertIsNotNone(data['company_application_shortlist_count'])
        self.assertEqual(resp.status_code, 200)

    def test__when_access_token_none__should_fail(self):
        resp = requests.get(COMPANY_INFO_BOX_URL)
        self.assertNotEqual(resp.status_code, 200)


if __name__ == '__main__':
    unittest.main()
