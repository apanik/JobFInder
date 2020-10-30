import time
import unittest

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.color import Color

from tests.config import VALID_PRO_VIEW_USERNAME, VALID_PRO_VIEW_PASSWORD
from tests.config_web import MAIN_URL_HOME, CHROME_DRIVER_LOCATION, DELAY_SHORT
from tests.test_ui.professional.test_signin import signin_helper


APPLIED_COUNT = "13"
APPLIED_COUNT_1 = "12"
APPLIED_COUNT_2 = "14"

COUNT_APPLIED_JOBS = f'Showing 1 - 10 of {APPLIED_COUNT} Jobs'
COUNT_APPLIED_JOBS_1 = f'Showing 1 - 10 of {APPLIED_COUNT_1} Jobs'
COUNT_APPLIED_JOBS_2 = f'Showing 1 - 10 of {APPLIED_COUNT_2} Jobs'

TOTAL_APPLIED_JOBS_RESULT = [
    'Job Post Example Twenty One',
    'Job Post Example Fourteen',
    'Job Post Example Four',
    'Job Post Example Company Two',
    'Job Post Example Twenty',
    'Job Post Example Seventeen',
    'Job Post Example Fourteen Single',
    'Job Post Example Fourteen',
    'Job Post Example Three',
    'Job Post Example Five']


TOTAL_APPLIED_JOBS_RESULT_12 = [
    'Job Post Example Twenty One',
    'Job Post Example Fourteen',
    'Job Post Example Company Two',
    'Job Post Example Twenty',
    'Job Post Example Seventeen',
    'Job Post Example Fourteen Single',
    'Job Post Example Fourteen',
    'Job Post Example Three',
    'Job Post Example Five',
    'Job Post Example Nine',
    'Job Post Example Eleven',
    'Job Post Example Fourteen Double']


TOTAL_APPLIED_JOBS_RESULT_1 = [
 'Job Post Example Company Two',
 'Job Post Example Twenty',
 'Job Post Example Seventeen',
 'Job Post Example Fourteen Single',
 'Job Post Example Fourteen',
 'Job Post Example Three',
 'Job Post Example Five',
 'Job Post Example Nine',
 'Job Post Example Eleven',
 'Job Post Example Fourteen Double']

TOTAL_APPLIED_JOBS_RESULT_13 = [
    'Job Post Example Nineteen',
    'Job Post Example Twenty One',
    'Job Post Example Fourteen',
    'Job Post Example Company Two',
    'Job Post Example Twenty',
    'Job Post Example Seventeen',
    'Job Post Example Fourteen Single',
    'Job Post Example Fourteen',
    'Job Post Example Three',
    'Job Post Example Five',
    'Job Post Example Nine',
    'Job Post Example Eleven',
    'Job Post Example Fourteen Double']

TOTAL_APPLIED_JOBS_RESULT_13_1 = [
    'Job Post Example Twenty One',
    'Job Post Example Fourteen',
    'Job Post Example Four',
    'Job Post Example Company Two',
    'Job Post Example Twenty',
    'Job Post Example Seventeen',
    'Job Post Example Fourteen Single',
    'Job Post Example Fourteen',
    'Job Post Example Three',
    'Job Post Example Five',
    'Job Post Example Nine',
    'Job Post Example Eleven',
    'Job Post Example Fourteen Double']


TOTAL_APPLIED_JOBS_RESULT_14 = [
    'Job Post Example Twenty Four',
    'Job Post Example Nineteen',
    'Job Post Example Twenty One',
    'Job Post Example Fourteen',
    'Job Post Example Company Two',
    'Job Post Example Twenty',
    'Job Post Example Seventeen',
    'Job Post Example Fourteen Single',
    'Job Post Example Fourteen',
    'Job Post Example Three',
    'Job Post Example Five',
    'Job Post Example Nine',
    'Job Post Example Eleven',
    'Job Post Example Fourteen Double']

TOTAL_APPLIED_JOBS_RESULT_12 = [
    'Job Post Example Twenty One',
    'Job Post Example Fourteen',
    'Job Post Example Company Two',
    'Job Post Example Twenty',
    'Job Post Example Seventeen',
    'Job Post Example Fourteen Single',
    'Job Post Example Fourteen',
    'Job Post Example Three',
    'Job Post Example Five',
    'Job Post Example Nine',
    'Job Post Example Eleven',
    'Job Post Example Fourteen Double']




class TestProfessionalAppliedJobs(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        data_signin = {
            "email": VALID_PRO_VIEW_USERNAME,
            "password": VALID_PRO_VIEW_PASSWORD,
        }
        signin_helper(cls.driver, data_signin)
        time.sleep(DELAY_SHORT)


    def test__when_applied_jobs_is_showing_valid_list__should_pass(self):
        driver = self.driver
        time.sleep(1)
        applied_jobs_btn = driver.find_element_by_id('applied-jobs')
        time.sleep(1)
        applied_jobs_btn.click()
        time.sleep(DELAY_SHORT)
        try:
            total_applied_jobs_count_show = driver.find_element_by_css_selector('.apply-title.float-right').text
            if total_applied_jobs_count_show != COUNT_APPLIED_JOBS and total_applied_jobs_count_show != COUNT_APPLIED_JOBS_1 and total_applied_jobs_count_show != COUNT_APPLIED_JOBS_2:
                self.fail()

            titles = []

            i = 0;
            page_count = driver.find_elements_by_class_name('page-item ').__len__()
            for i in range(i, page_count - 2):
                if i <= page_count - 3:
                    page = driver.find_element_by_css_selector('.page-item.active').text

                    time.sleep(1)
                    self.assertEqual(page, str(i + 1))
                else:
                    time.sleep(1)
                job_list = driver.find_elements_by_class_name('job-list')

                for job in job_list:

                    # .  not all companies have review
                    try:
                        title = job.find_element_by_tag_name('h4').text
                    except:
                        title = ''
                    if title != '':
                        titles.append(title)
                if i != page_count - 3:
                    time.sleep(1)
                    page_next = driver.find_element_by_class_name('fa-arrow-right')
                    page_next.click()
                    time.sleep(DELAY_SHORT)
                time.sleep(1)

            if titles != TOTAL_APPLIED_JOBS_RESULT and titles != TOTAL_APPLIED_JOBS_RESULT_12 and titles != TOTAL_APPLIED_JOBS_RESULT_1 and titles != TOTAL_APPLIED_JOBS_RESULT_13 and titles != TOTAL_APPLIED_JOBS_RESULT_13_1 and titles != TOTAL_APPLIED_JOBS_RESULT_14:
                    self.fail()
        except NoSuchElementException:
            self.fail('Not ok')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()