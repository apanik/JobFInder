import time
import unittest

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.color import Color

from tests.config import VALID_PRO_VIEW_USERNAME, VALID_PRO_VIEW_PASSWORD
from tests.config_web import MAIN_URL_HOME, CHROME_DRIVER_LOCATION, DELAY_SHORT, DELAY_LONG
from tests.test_ui.professional.test_signin import signin_helper

LINK_SKILL = f'{MAIN_URL_HOME}/professional/myprofile/'
LINK_APPLIED_JOBS = f'{MAIN_URL_HOME}/professional/applied-jobs/'
LINK_FAVORITE_JOBS = f'{MAIN_URL_HOME}/professional/favorite-jobs/'

COUNT_SKILL = "4"
COUNT_APPLIED_JOBS = "11"
COUNT_FAVORITE_JOBS = "12"

COUNT_APPLIED_JOBS_1 = "10"

INFO_BOX_NAME_SKILL = 'Skills'
INFO_BOX_NAME_APPLIED_JOBS = 'Applied Jobs'
INFO_BOX_NAME_FAVORITE_JOBS = 'Favorite Jobs'

SIDE_MENU_DASHBOARD_NAME = "Dashboard"
SIDE_MENU_SKILL_NAME = "My Profile"
SIDE_MENU_APPLIED_JOBS_NAME = "Favorite Jobs"
SIDE_MENU_FAVORITE_JOBS_NAME = "Applied Jobs"

SUBSCRIBED_CONTENT = 'Unsubscribe job alert.'
UNSUBSCRIBED_CONTENT = 'Subscribe for job alert.'
subscribed_text="You have subscribed for job alert."
unsubscribed_text="You have unsubscribed for job alert."
PROFESSIONAL_DASHBOARD_URL = f'{MAIN_URL_HOME}/professional/profile-dashboard/'

class TestProfessionalInfoBox(unittest.TestCase):

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


    def test__when_info_box_skill_url_and_active_side_menu_name__are_correct__pass(self):
        driver = self.driver
        driver.get(PROFESSIONAL_DASHBOARD_URL)
        try:
            dashboard_btn = driver.find_element_by_link_text('Dashboard')
            dashboard_btn.click()
        except:
            time.sleep(1)
        time.sleep(DELAY_SHORT)
        skill_btn = driver.find_element_by_class_name('skill-statistics')
        skill_btn.click()
        time.sleep(DELAY_SHORT)
        skill_url = driver.current_url
        time.sleep(1)
        side_menu_skill = driver.find_element_by_css_selector(".side-menu.active").text
        driver.execute_script("window.history.go(-1)")
        time.sleep(1)
        side_menu_dashboard = driver.find_element_by_css_selector(".side-menu.active").text
        if skill_url != LINK_SKILL and side_menu_skill != SIDE_MENU_SKILL_NAME and side_menu_dashboard != SIDE_MENU_DASHBOARD_NAME:
            self.fail()

    def test__when_info_box_applied_job_url_and_active_side_menu_name__are_correct__pass(self):
        driver = self.driver
        driver.get(PROFESSIONAL_DASHBOARD_URL)
        time.sleep(DELAY_SHORT)
        applied_jobs_btn = driver.find_element_by_link_text('Applied Jobs')
        applied_jobs_btn.click()
        time.sleep(DELAY_SHORT)
        applied_jobs_url = driver.current_url
        time.sleep(1)
        side_menu_applied_jobs = driver.find_element_by_css_selector(".side-menu.active").text
        driver.execute_script("window.history.go(-1)")
        time.sleep(1)
        side_menu_dashboard = driver.find_element_by_css_selector(".side-menu.active").text
        if applied_jobs_url != LINK_APPLIED_JOBS and side_menu_applied_jobs != SIDE_MENU_APPLIED_JOBS_NAME and side_menu_dashboard != SIDE_MENU_DASHBOARD_NAME:
            self.fail()

    def test__when_info_box_favorite_job_url_and_active_side_menu_name__are_correct__pass(self):
        driver = self.driver
        driver.get(PROFESSIONAL_DASHBOARD_URL)
        time.sleep(DELAY_SHORT)
        favorite_jobs_btn = driver.find_element_by_class_name('favorite-job-statistics')
        favorite_jobs_btn.click()
        time.sleep(DELAY_SHORT)
        favorite_jobs_url = driver.current_url
        time.sleep(1)
        side_menu_favorite_jobs = driver.find_element_by_css_selector(".side-menu.active").text
        driver.execute_script("window.history.go(-1)")
        time.sleep(1)
        side_menu_dashboard = driver.find_element_by_css_selector(".side-menu.active").text
        if favorite_jobs_url != LINK_FAVORITE_JOBS and side_menu_favorite_jobs != SIDE_MENU_FAVORITE_JOBS_NAME and side_menu_dashboard != SIDE_MENU_DASHBOARD_NAME:
            self.fail()

    def test__when_info_box_skill_name_and_count__are_correct__pass(self):
        driver = self.driver
        driver.get(PROFESSIONAL_DASHBOARD_URL)
        time.sleep(DELAY_SHORT)
        skill_name = driver.find_element_by_id('skill-link').text
        time.sleep(1)
        skill_count = driver.find_element_by_id('prof-skills').text
        time.sleep(1)
        if skill_name != INFO_BOX_NAME_SKILL and skill_count != COUNT_SKILL:
            self.fail()

    def test__when_info_box_applied_jobs_name_and_count__are_correct__pass(self):
        driver = self.driver
        driver.get(PROFESSIONAL_DASHBOARD_URL)
        time.sleep(DELAY_SHORT)
        applied_jobs_count = driver.find_element_by_id('applied-jobs').text
        time.sleep(1)
        applied_jobs_name = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[2]/a/span').text
        time.sleep(1)
        if applied_jobs_name != INFO_BOX_NAME_APPLIED_JOBS and applied_jobs_count != COUNT_APPLIED_JOBS and applied_jobs_count != COUNT_APPLIED_JOBS_1:
            self.fail()

    def test__when_info_box_favorite_jobs_name_and_count__are_correct__pass(self):
        driver = self.driver
        driver.get(PROFESSIONAL_DASHBOARD_URL)
        time.sleep(DELAY_SHORT)
        favorite_jobs_count = driver.find_element_by_id('favourite-jobs').text
        time.sleep(1)
        favorite_jobs_name = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[3]/a/span').text
        time.sleep(1)
        if favorite_jobs_name != INFO_BOX_NAME_FAVORITE_JOBS and favorite_jobs_count != COUNT_FAVORITE_JOBS:
            self.fail()

    def test__subscribed_and_unsubscribed__should_pass(self):
        driver = self.driver
        driver.get(PROFESSIONAL_DASHBOARD_URL)
        time.sleep(DELAY_SHORT)
        my_profile_btn = driver.find_element_by_link_text('My Profile')
        my_profile_btn.click()
        time.sleep(DELAY_LONG)
        subscribe_content = driver.find_element_by_id('subscribe-text').text
        if subscribe_content == SUBSCRIBED_CONTENT:
            time.sleep(1)
            subscribe_btn = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[12]/div/label/span')
            subscribe_btn.click()
            time.sleep(DELAY_SHORT)
            success_text_unsubscribed = driver.find_element_by_xpath('//*[@id="swal2-content"]').text
            time.sleep(1)
            ok_btn = driver.find_element_by_css_selector('.swal2-confirm.swal2-styled')
            ok_btn.click()
            time.sleep(1)
            self.assertEquals(success_text_unsubscribed, unsubscribed_text)
            time.sleep(1)
            subscribe_btn = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[12]/div/label/span')
            subscribe_btn.click()
            time.sleep(DELAY_SHORT)
            success_text_subscribed = driver.find_element_by_xpath('//*[@id="swal2-content"]').text
            time.sleep(1)
            ok_btn = driver.find_element_by_css_selector('.swal2-confirm.swal2-styled')
            ok_btn.click()
            time.sleep(1)
            self.assertEquals(success_text_subscribed, subscribed_text)
            time.sleep(1)
        elif subscribe_content == UNSUBSCRIBED_CONTENT:
            time.sleep(1)
            subscribe_btn = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[12]/div/label/span')
            subscribe_btn.click()
            time.sleep(DELAY_SHORT)
            success_text_subscribed = driver.find_element_by_xpath('//*[@id="swal2-content"]').text
            time.sleep(1)
            ok_btn = driver.find_element_by_css_selector('.swal2-confirm.swal2-styled')
            ok_btn.click()
            time.sleep(1)
            self.assertEquals(success_text_subscribed, subscribed_text)
            time.sleep(1)
            subscribe_btn = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[12]/div/label/span')
            subscribe_btn.click()
            time.sleep(DELAY_SHORT)
            success_text_unsubscribed = driver.find_element_by_xpath('//*[@id="swal2-content"]').text
            time.sleep(1)
            ok_btn = driver.find_element_by_css_selector('.swal2-confirm.swal2-styled')
            ok_btn.click()
            time.sleep(1)
            self.assertEquals(success_text_unsubscribed, unsubscribed_text)
            time.sleep(1)
        else:
            self.fail()


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()