import time
import unittest

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.color import Color

from tests.config import VALID_PRO_VIEW_USERNAME, VALID_PRO_VIEW_PASSWORD
from tests.config_web import MAIN_URL_HOME, CHROME_DRIVER_LOCATION, DELAY_SHORT
from tests.test_ui.professional.test_signin import signin_helper

TOTAL_ACTIVITY_COUNT = "23"
TOTAL_ACTIVITY_COUNT_1 = "21"
TOTAL_ACTIVITY_COUNT_2 = "24"
TOTAL_ACTIVITY_COUNT_3 = "25"



TOTAL_ACTIVITY = [
    'Applied job',
    'Applied job',
    'Applied job',
    'Profile Updated',
    'Profile Updated',
    'Applied job',
    'Applied job',
    'Applied job',
    'Profile Updated',
    'Applied job',
    'Applied job',
    'Profile Updated',
    'Profile Updated',
    'Applied job',
    'Applied job',
    'Applied job',
    'Applied job',
    'Applied job',
    'Profile Updated',
    'Profile Updated',
    'Profile Updated',
    'Profile Updated',
    'Profile Updated']

TOTAL_ACTIVITY_1 = [
'Applied job',
 'Profile Updated',
 'Profile Updated',
 'Applied job',
 'Applied job',
 'Applied job',
 'Profile Updated',
 'Applied job',
 'Applied job',
 'Profile Updated',
 'Profile Updated',
 'Applied job',
 'Applied job',
 'Applied job',
 'Applied job',
 'Applied job',
 'Profile Updated',
 'Profile Updated',
 'Profile Updated',
 'Profile Updated',
 'Profile Updated']

TOTAL_ACTIVITY_2 = [
    'Applied job',
    'Applied job',
    'Applied job',
    'Applied job',
    'Profile Updated',
    'Profile Updated',
    'Applied job',
    'Applied job',
    'Applied job',
    'Profile Updated',
    'Applied job',
    'Applied job',
    'Profile Updated',
    'Profile Updated',
    'Applied job',
    'Applied job',
    'Applied job',
    'Applied job',
    'Applied job',
    'Profile Updated',
    'Profile Updated',
    'Profile Updated',
    'Profile Updated',
    'Profile Updated']


TOTAL_ACTIVITY_3 = ['Applied job', 'Applied job', 'Applied job', 'Applied job', 'Applied job', 'Profile Updated', 'Profile Updated', 'Applied job', 'Applied job', 'Applied job', 'Profile Updated', 'Applied job', 'Applied job', 'Profile Updated', 'Profile Updated', 'Applied job', 'Applied job', 'Applied job', 'Applied job', 'Applied job', 'Profile Updated', 'Profile Updated', 'Profile Updated', 'Profile Updated', 'Profile Updated']

class TestProfessionalActivity(unittest.TestCase):

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


    def test__when_recent_activity_list_is_valid__should_pass(self):
        driver = self.driver
        time.sleep(1)
        recent_activity_btn = driver.find_element_by_link_text('Recent Activity')
        time.sleep(1)
        recent_activity_btn.click()
        time.sleep(DELAY_SHORT)
        try:
            titles = []
            total_activities = driver.find_elements_by_class_name('activity-list').__len__()
            if str(total_activities) != TOTAL_ACTIVITY_COUNT and str(total_activities) != TOTAL_ACTIVITY_COUNT_1 and str(total_activities) != TOTAL_ACTIVITY_COUNT_2 and str(total_activities) != TOTAL_ACTIVITY_COUNT_3:
                self.fail()
            time.sleep(1)
            activity_list = driver.find_elements_by_class_name('activity-list')
            for activity in activity_list:
                try:
                    title = activity.find_element_by_tag_name('h5').text
                except:
                    title = ''
                if title != '':
                    titles.append(title)

                # --------------- KEEP THIS SECTION FOR PAGINATION START--------
                # if i != page_count-3:
                #     time.sleep(1)
                #     page_next = driver.find_element_by_link_text('Next')
                #     page_next.click()
                # time.sleep(DELAY_SHORT)
                # --------------- KEEP THIS SECTION FOR PAGINATION END--------

            if titles != TOTAL_ACTIVITY and titles != TOTAL_ACTIVITY_1 and titles != TOTAL_ACTIVITY_2 and titles != TOTAL_ACTIVITY_3:
                self.fail()
        except NoSuchElementException:
            self.fail('Not ok')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()