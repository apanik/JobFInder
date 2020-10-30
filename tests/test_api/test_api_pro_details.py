import unittest
import requests

from tests.test_api.common import signin_as_pro
from tests.config_api import *

PRO_EDUCATION_URL = f'{MAIN_URL}/api/professional/professional_education/'
PRO_SKILL_URL = f'{MAIN_URL}/api/professional/professional_skill/'


class TestprofessionalEducationSave(unittest.TestCase):

    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']
        self.onging_on = True
        self.onging_off = False
        self.onging_empty = bool('')
        self.degree = "Qualification Example Five"
        self.major = "1"
        self.edu_level = "1"
        self.description = "Example Description here"
        self.graduation_date = "2020-07-02"
        self.enrolled_date = "2019-07-01"
        self.institution = "Example Institution"
        self.cgpa = "3.0"

    def test_save_education__when_valid_all_data__should_pass(self):
        json = {
            'degree_text': self.degree,
            'institution_text': self.institution,
            'cgpa': self.cgpa,
            'major_text': self.major,
            'education_level_id': self.edu_level,
            'description': self.description,
            'enrolled_date': self.enrolled_date,
            'graduation_date': self.graduation_date,
            'is_ongoing': self.onging_off
        }
        resp = requests.post(PRO_EDUCATION_URL, json=json, headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        self.assertIsNotNone(data["id"])
        self.assertEqual(resp.status_code, 200)

    def test_save_education__when_empty_all_data__should_fail(self):
        json = {

            'degree_text': '',
            'institution_text': '',
            'cgpa': '',
            'major_text': '',
            'education_level_id': '',
            'description': '',
            'enrolled_date': '',
            'graduation_date': '',
            'is_ongoing': self.onging_empty
        }
        resp = requests.post(PRO_EDUCATION_URL, json=json, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertNotEqual(resp.status_code, 200)

    def test_save_education__when_empty_degree__should_fail(self):
        json = {
            'degree_text': '',
            'institution_text': self.institution,
            'cgpa': self.cgpa,
            'major_text': self.major,
            'education_level_id': self.edu_level,
            'description': self.description,
            'enrolled_date': self.enrolled_date,
            'graduation_date': self.graduation_date,
            'is_ongoing': self.onging_off
        }
        resp = requests.post(PRO_EDUCATION_URL, json=json, headers={'Authorization': 'Bearer ' + self.access_token})
        # data = resp.json()
        # self.assertIsNotNone(data["id"])
        self.assertNotEqual(resp.status_code, 200)

    def test_save_education__when_empty_institution__should_fail(self):
        json = {
            'degree_text': self.degree,
            'institution_text': '',
            'cgpa': self.cgpa,
            'major_text': self.major,
            'education_level_id': self.edu_level,
            'description': self.description,
            'enrolled_date': self.enrolled_date,
            'graduation_date': self.graduation_date,
            'is_ongoing': self.onging_off
        }
        resp = requests.post(PRO_EDUCATION_URL, json=json, headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        self.assertNotEqual(resp.status_code, 200)


    def test_save_education__when_empty_education_level__should_fail(self):
        json = {
            'degree_text': self.degree,
            'institution_text': '',
            'cgpa': self.cgpa,
            'major_text': self.major,
            'education_level_id': '',
            'description': self.description,
            'enrolled_date': self.enrolled_date,
            'graduation_date': self.graduation_date,
            'is_ongoing': self.onging_off
        }
        resp = requests.post(PRO_EDUCATION_URL, json=json, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertNotEqual(resp.status_code, 200)

    def test_save_education__when_empty_enrolled_date__should_fail(self):
        json = {
            'degree_text': self.degree,
            'institution_text': self.institution,
            'cgpa': self.cgpa,
            'major_text': self.major,
            'education_level_id': self.edu_level,
            'description': self.description,
            'enrolled_date': '',
            'graduation_date': self.graduation_date,
            'is_ongoing': self.onging_off
        }
        resp = requests.post(PRO_EDUCATION_URL, json=json, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertNotEqual(resp.status_code, 200)

    def test_save_education__when_enroll_date_greater_than_graduation_date__should_fail(self):
        json = {
            'degree_text': self.degree,
            'institution_text': self.institution,
            'cgpa': self.cgpa,
            'major_text': self.major,
            'education_level_id': self.edu_level,
            'description': self.description,
            'enrolled_date': '2020-07-01',
            'graduation_date': '2019-07-01',
            'is_ongoing': self.onging_off
        }
        resp = requests.post(PRO_EDUCATION_URL, json=json, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertNotEqual(resp.status_code, 200)

    def test_save_education__when_graduation_date_smaller_than_enroll_date__should_fail(self):
        json = {
            'degree_text': self.degree,
            'institution_text': self.institution,
            'cgpa': self.cgpa,
            'major_text': self.major,
            'education_level_id': self.edu_level,
            'description': self.description,
            'enrolled_date': '2020-07-01',
            'graduation_date': '2019-07-01',
            'is_ongoing': self.onging_off
        }
        resp = requests.post(PRO_EDUCATION_URL, json=json, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertNotEqual(resp.status_code, 200)

    def test_save_education__when_onging_true_and_enroll_graduation_empty__should_fail(self):
        json = {
            'degree_text': self.degree,
            'institution_text': self.institution,
            'cgpa': self.cgpa,
            'major_text': self.major,
            'education_level_id': self.edu_level,
            'description': self.description,
            'enrolled_date': '',
            'graduation_date': '',
            'is_ongoing': self.onging_on

        }
        resp = requests.post(PRO_EDUCATION_URL, json=json, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertNotEqual(resp.status_code, 200)


class TestprofessionalSkillSave(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']


    def test_pro_skill__when_adding_same_skill_twice__should_fail(self):
        json = {
            'skill_name_id': '8',
            'rating': '7'
        }
        resp = requests.post(PRO_SKILL_URL, json=json, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 400)


    def test_pro_skill__when_valid_data__should_pass(self):
        json = {
            'skill_name_id': '2',
            'rating': '7'
        }
        resp = requests.post(PRO_SKILL_URL, json=json, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)


if __name__ == '__main__':
    unittest.main()
