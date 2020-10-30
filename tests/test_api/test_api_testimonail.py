import unittest
import requests
from tests.config_api import MAIN_URL
from tests.test_api.common import signin_as_pro,signin_as_com


TESTIMONIAL_LIST_URL = f'{MAIN_URL}/api/testimonial_show/'


class TestTestimonialList(unittest.TestCase):
    def setUp(self) -> None:
        data = signin_as_pro()
        self.access_token = data['access']

    def test__when_valid__should__pass(self):
        resp = requests.get(TESTIMONIAL_LIST_URL)
        data = resp.json()
        self.assertIsNotNone(data[0]['client_name'])
        self.assertIsNotNone(data[0]['comment'])
        self.assertIsNotNone(data[0]['profile_picture'])
        self.assertEqual(resp.status_code,200)

    def test__when_with_access_token__should_pass(self):
        resp = requests.get(TESTIMONIAL_LIST_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        data = resp.json()
        self.assertIsNotNone(data[0]['client_name'])
        self.assertIsNotNone(data[0]['comment'])
        self.assertIsNotNone(data[0]['profile_picture'])
        self.assertEqual(resp.status_code, 200)


if __name__ == '__main__':
    unittest.main()
