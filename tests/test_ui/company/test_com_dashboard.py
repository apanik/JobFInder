import time
import unittest

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.color import Color

from tests.config import VALID_PRO_VIEW_USERNAME, VALID_PRO_VIEW_PASSWORD, VALID_COM_VIEW_USERNAME, \
    VALID_COM_VIEW_PASSWORD
from tests.config_web import MAIN_URL_HOME, CHROME_DRIVER_LOCATION, DELAY_SHORT, DELAY_LONG
from tests.test_ui.company.test_signin import signin_helper_company
from tests.test_ui.professional.test_signin import signin_helper


COMPANY_DASHBOARD_URL = f'{MAIN_URL_HOME}/company/dashboard/'
SIDE_MENU_DASHBOARD_NAME = "Dashboard"

MANAGE_JOBS_URL = f'{MAIN_URL_HOME}/company/manage-jobs/'
SIDE_MENU_MANAGE_JOBS_NAME = "Manage Jobs"

MANAGE_CANDIDATES_URL = f'{MAIN_URL_HOME}/company-manage-candidates/'
MANAGE_CANDIDATES_IS_SHORTLISTED_URL = f'{MAIN_URL_HOME}/company-manage-candidates/?is_shortlisted'
SIDE_MENU_MANAGE_CANDIDATES_NAME = "Manage Candidates"

EDIT_PROFILE_URL = f'{MAIN_URL_HOME}/company/edit-profile/'
SIDE_MENU_EDIT_PROFILE_NAME = "Edit Profile"

POST_JOB_URL = f'{MAIN_URL_HOME}/company/post-job/'
SIDE_MENU_POST_JOB_NAME = "Post Job"

MESSAGES_URL = f'{MAIN_URL_HOME}/company/messages/'
SIDE_MENU_MESSAGES_NAME = "Messages"

RECENT_ACTIVITY_URL = f'{MAIN_URL_HOME}/company/recent-activity/'
SIDE_MENU_RECENT_ACTIVITY_NAME = "Recent Activity"

NOTIFICATIONS_URL = f'{MAIN_URL_HOME}/company/notifications/'
SIDE_MENU_NOTIFICATIONS_NAME = "Notifications"

BREAD_CRUMB_HOME = 'Home'
BREAD_CRUMB_HOME_URL = f'{MAIN_URL_HOME}/'


JOB_POSTED_BTN_ICON_DATA = 'M18 3a3 3 0 0 0-3 3v12a3 3 0 0 0 3 3 3 3 0 0 0 3-3 3 3 0 0 0-3-3H6a3 3 0 0 0-3 3 3 3 0 0 0 3 3 3 3 0 0 0 3-3V6a3 3 0 0 0-3-3 3 3 0 0 0-3 3 3 3 0 0 0 3 3h12a3 3 0 0 0 3-3 3 3 0 0 0-3-3z'
JOB_POSTED_ICON_WIDTH = '24'
JOB_POSTED_ICON_HEIGHT = '24'
JOB_POSTED_COUNT_DATA = '11'
JOB_POSTED_TEXT_DATA = 'Job(s) Posted'

APPLICATIONS_BTN_ICON_DATA = 'M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z'
APPLICATIONS_ICON_WIDTH = '24'
APPLICATIONS_ICON_HEIGHT = '24'
APPLICATIONS_COUNT_DATA = '5'
APPLICATIONS_TEXT_DATA = 'Application(s)'

SHORTLISTED_BTN_ICON_DATA = 'M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z'
SHORTLISTED_ICON_WIDTH = '24'
SHORTLISTED_ICON_HEIGHT = '24'
SHORTLISTED_COUNT_DATA = '1'
SHORTLISTED_TEXT_DATA = 'Shortlisted'

COMPANY_NAME_DATA = 'Company Example View'
COMPANY_IMAGE_DATA = f'{MAIN_URL_HOME}/media/images/portfolio.png'
PROGRESS_DATA = '70%'
ACCOUNT_EMAIL = VALID_COM_VIEW_USERNAME

NAV_ITEM_NAME_LIST = [' Dashboard', ' Change Password', ' Sign out']
NAV_ITEMS_URL_LIST = [f'{MAIN_URL_HOME}/company/dashboard/', f'{MAIN_URL_HOME}/change-password/', f'{MAIN_URL_HOME}/sign-out']


class TestCompanyInfoBox(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        data_signin = {
            "email": VALID_COM_VIEW_USERNAME,
            "password": VALID_COM_VIEW_PASSWORD,
        }
        signin_helper_company(cls.driver, data_signin)
        time.sleep(DELAY_SHORT)


    def test__when_info_box__jobs_posted_data__is_correct__pass(self):
        driver = self.driver
        driver.get(COMPANY_DASHBOARD_URL)
        try:
            dashboard_btn = driver.find_element_by_link_text('Dashboard')
            dashboard_btn.click()
        except:
            time.sleep(1)
        time.sleep(DELAY_SHORT)
        job_posted_btn = driver.find_element_by_class_name('posted-jobs-statistics')
        job_posted_btn_icon = job_posted_btn.find_element_by_tag_name('path').get_attribute('d')
        job_posted_btn_icon_width = job_posted_btn.find_element_by_tag_name('svg').get_attribute('width')
        job_posted_btn_icon_height = job_posted_btn.find_element_by_tag_name('svg').get_attribute('height')
        job_posted_count = job_posted_btn.find_element_by_id('posted-jobs-count').text
        job_posted_text = job_posted_btn.find_element_by_id('total-jobs').text

        if job_posted_btn_icon != JOB_POSTED_BTN_ICON_DATA:
            self.fail()
        if job_posted_btn_icon_width != JOB_POSTED_ICON_WIDTH:
            self.fail()
        if job_posted_btn_icon_height != JOB_POSTED_ICON_HEIGHT:
            self.fail()
        if job_posted_count != JOB_POSTED_COUNT_DATA:
            self.fail()
        if job_posted_text != JOB_POSTED_TEXT_DATA:
            self.fail()

        job_posted_btn.click()
        time.sleep(DELAY_SHORT)

        page_header = driver.find_element_by_css_selector('.container.mb-2')
        page_title = page_header.find_element_by_class_name('page-title').text
        bread_crumb_home = page_header.find_element_by_tag_name('a').text
        bread_crumb_home_url = page_header.find_element_by_tag_name('a').get_attribute('href')
        bread_crumb_title = page_header.find_element_by_tag_name('span').text

        if page_title != SIDE_MENU_MANAGE_JOBS_NAME:
            self.fail()
        if bread_crumb_home != BREAD_CRUMB_HOME:
            self.fail()
        if bread_crumb_home_url != BREAD_CRUMB_HOME_URL:
            self.fail()
        if bread_crumb_title != SIDE_MENU_MANAGE_JOBS_NAME:
            self.fail()

        job_posted_url = driver.current_url
        time.sleep(1)
        side_menu_job_posted = driver.find_element_by_css_selector(".managejobs.active").text
        driver.execute_script("window.history.go(-1)")
        time.sleep(DELAY_SHORT)
        side_menu_dashboard = driver.find_element_by_css_selector(".dashboard.active").text
        if job_posted_url != MANAGE_JOBS_URL:
            self.fail()
        if side_menu_job_posted != SIDE_MENU_MANAGE_JOBS_NAME:
            self.fail()
        if side_menu_dashboard != SIDE_MENU_DASHBOARD_NAME:
            self.fail()


    def test__when_info_box__applications_data__is_correct__pass(self):
        driver = self.driver
        driver.get(COMPANY_DASHBOARD_URL)
        try:
            dashboard_btn = driver.find_element_by_link_text('Dashboard')
            dashboard_btn.click()
        except:
            time.sleep(1)
        time.sleep(DELAY_SHORT)
        applications_btn = driver.find_element_by_class_name('applications-statistics')
        applications_btn_icon = applications_btn.find_element_by_tag_name('path').get_attribute('d')
        applications_btn_icon_width = applications_btn.find_element_by_tag_name('svg').get_attribute('width')
        applications_btn_icon_height = applications_btn.find_element_by_tag_name('svg').get_attribute('height')
        applications_count = applications_btn.find_element_by_id('applications-count').text
        applications_text = applications_btn.find_element_by_id('total-applicants').text

        if applications_btn_icon != APPLICATIONS_BTN_ICON_DATA:
            self.fail()
        if applications_btn_icon_width != APPLICATIONS_ICON_WIDTH:
            self.fail()
        if applications_btn_icon_height != APPLICATIONS_ICON_HEIGHT:
            self.fail()
        if applications_count != APPLICATIONS_COUNT_DATA:
            self.fail()
        if applications_text != APPLICATIONS_TEXT_DATA:
            self.fail()

        applications_btn.click()
        time.sleep(DELAY_SHORT)
        page_header = driver.find_element_by_css_selector('.container.mb-2')
        page_title = page_header.find_element_by_class_name('page-title').text
        bread_crumb_home = page_header.find_element_by_tag_name('a').text
        bread_crumb_home_url = page_header.find_element_by_tag_name('a').get_attribute('href')
        bread_crumb_title = page_header.find_element_by_tag_name('span').text

        if page_title != SIDE_MENU_MANAGE_CANDIDATES_NAME:
            self.fail()
        if bread_crumb_home != BREAD_CRUMB_HOME:
            self.fail()
        if bread_crumb_home_url != BREAD_CRUMB_HOME_URL:
            self.fail()
        if bread_crumb_title != SIDE_MENU_MANAGE_CANDIDATES_NAME:
            self.fail()

        applications_url = driver.current_url
        time.sleep(1)
        side_menu_applications = driver.find_element_by_css_selector(".managecandidate.active").text
        driver.execute_script("window.history.go(-1)")
        time.sleep(DELAY_SHORT)
        side_menu_dashboard = driver.find_element_by_css_selector(".dashboard.active").text
        if applications_url != MANAGE_CANDIDATES_URL:
            self.fail()
        if side_menu_applications != SIDE_MENU_MANAGE_CANDIDATES_NAME:
            self.fail()
        if side_menu_dashboard != SIDE_MENU_DASHBOARD_NAME:
            self.fail()



    def test__when_info_box__shortlisted_data__is_correct__pass(self):
        driver = self.driver
        driver.get(COMPANY_DASHBOARD_URL)
        try:
            dashboard_btn = driver.find_element_by_link_text('Dashboard')
            dashboard_btn.click()
        except:
            time.sleep(1)
        time.sleep(DELAY_SHORT)
        shortlisted_btn = driver.find_element_by_class_name('shortlisted-statistics')
        shortlisted_btn_icon = shortlisted_btn.find_element_by_tag_name('path').get_attribute('d')
        shortlisted_btn_icon_width = shortlisted_btn.find_element_by_tag_name('svg').get_attribute('width')
        shortlisted_btn_icon_height = shortlisted_btn.find_element_by_tag_name('svg').get_attribute('height')
        shortlisted_count = shortlisted_btn.find_element_by_id('shortlisted-count').text
        shortlisted_text = shortlisted_btn.find_element_by_id('total-shortlisted').text

        if shortlisted_btn_icon != SHORTLISTED_BTN_ICON_DATA:
            self.fail()
        if shortlisted_btn_icon_width != SHORTLISTED_ICON_WIDTH:
            self.fail()
        if shortlisted_btn_icon_height != SHORTLISTED_ICON_HEIGHT:
            self.fail()
        if shortlisted_count != SHORTLISTED_COUNT_DATA:
            self.fail()
        if shortlisted_text != SHORTLISTED_TEXT_DATA:
            self.fail()

        shortlisted_btn.click()
        time.sleep(DELAY_SHORT)

        page_header = driver.find_element_by_css_selector('.container.mb-2')
        page_title = page_header.find_element_by_class_name('page-title').text
        bread_crumb_home = page_header.find_element_by_tag_name('a').text
        bread_crumb_home_url = page_header.find_element_by_tag_name('a').get_attribute('href')
        bread_crumb_title = page_header.find_element_by_tag_name('span').text

        if page_title != SIDE_MENU_MANAGE_CANDIDATES_NAME:
            self.fail()
        if bread_crumb_home != BREAD_CRUMB_HOME:
            self.fail()
        if bread_crumb_home_url != BREAD_CRUMB_HOME_URL:
            self.fail()
        if bread_crumb_title != SIDE_MENU_MANAGE_CANDIDATES_NAME:
            self.fail()

        shortlisted_url = driver.current_url
        time.sleep(1)
        side_menu_shortlisted = driver.find_element_by_css_selector(".managecandidate.active").text
        driver.execute_script("window.history.go(-1)")
        time.sleep(DELAY_SHORT)
        side_menu_dashboard = driver.find_element_by_css_selector(".dashboard.active").text
        if shortlisted_url != MANAGE_CANDIDATES_IS_SHORTLISTED_URL:
            self.fail()
        if side_menu_shortlisted != SIDE_MENU_MANAGE_CANDIDATES_NAME:
            self.fail()
        if side_menu_dashboard != SIDE_MENU_DASHBOARD_NAME:
            self.fail()


    def test__when_company_name_image_email_data__are_correct__pass(self):
        driver = self.driver
        driver.get(COMPANY_DASHBOARD_URL)
        try:
            dashboard_btn = driver.find_element_by_link_text('Dashboard')
            dashboard_btn.click()
        except:
            time.sleep(1)
        time.sleep(DELAY_SHORT)
        company_info = driver.find_element_by_class_name('company-info')
        company_name = company_info.find_element_by_id('company_name_layout').text
        company_image = company_info.find_element_by_tag_name('img').get_attribute('src')
        progress_to = driver.find_element_by_class_name('progress-to').text

        company_bar = driver.find_element_by_css_selector('.nav-item.dropdown')
        company_image_in_nav = company_bar.find_element_by_tag_name('img').get_attribute('src')
        company_bar.click()
        time.sleep(1)
        company_account = company_bar.find_element_by_class_name('account-card')
        company_account_image = company_account.find_element_by_tag_name('img').get_attribute('src')
        company_account_name = company_account.find_element_by_tag_name('h5').text
        company_account_email = company_account.find_element_by_class_name('mail').text

        if company_name !=  COMPANY_NAME_DATA:
            self.fail()
        if company_account_name != COMPANY_NAME_DATA:
            self.fail()
        if company_image != COMPANY_IMAGE_DATA:
            self.fail()
        if company_image_in_nav != COMPANY_IMAGE_DATA:
            self.fail()
        if company_account_image != COMPANY_IMAGE_DATA:
            self.fail()
        if progress_to != PROGRESS_DATA:
            self.fail()
        if company_account_email != ACCOUNT_EMAIL:
            self.fail()

        nav_items = company_bar.find_elements_by_class_name('nav-item')
        nav_items_list = []
        nav_items_url_list = []
        for item in nav_items:
            nav_item = item.find_element_by_tag_name('a').text
            nav_item_url = item.find_element_by_tag_name('a').get_attribute('href')

            if nav_item != '':
                nav_items_list.append(nav_item)
            if nav_item_url != '':
                nav_items_url_list.append(nav_item_url)

        if nav_items_list != NAV_ITEM_NAME_LIST or nav_items_url_list != NAV_ITEMS_URL_LIST:
            self.fail()


    def test__when_company_edit_profile_page_is_correct__pass(self):
        driver = self.driver
        driver.get(COMPANY_DASHBOARD_URL)
        try:
            edit_profile_btn = driver.find_element_by_link_text('Edit Profile')
            edit_profile_btn.click()
        except:
            time.sleep(1)
        time.sleep(DELAY_SHORT)
        company_image = driver.find_element_by_class_name('update-photo')
        image = company_image.find_element_by_tag_name('img').get_attribute('src')
        if image != COMPANY_IMAGE_DATA:
            self.fail()

        page_header = driver.find_element_by_css_selector('.container.mb-2')
        page_title = page_header.find_element_by_class_name('page-title').text
        bread_crumb_home = page_header.find_element_by_tag_name('a').text
        bread_crumb_home_url = page_header.find_element_by_tag_name('a').get_attribute('href')
        bread_crumb_title = page_header.find_element_by_tag_name('span').text

        if page_title != SIDE_MENU_EDIT_PROFILE_NAME:
            self.fail()
        if bread_crumb_home != BREAD_CRUMB_HOME:
            self.fail()
        if bread_crumb_home_url != BREAD_CRUMB_HOME_URL:
            self.fail()
        if bread_crumb_title != SIDE_MENU_EDIT_PROFILE_NAME:
            self.fail()

        edit_profile_url = driver.current_url
        time.sleep(1)
        side_menu_edit_profile = driver.find_element_by_css_selector(".edit_pro.active").text
        driver.execute_script("window.history.go(-1)")
        time.sleep(DELAY_SHORT)
        side_menu_dashboard = driver.find_element_by_css_selector(".dashboard.active").text
        if edit_profile_url != EDIT_PROFILE_URL:
            self.fail()
        if side_menu_edit_profile != SIDE_MENU_EDIT_PROFILE_NAME:
            self.fail()
        if side_menu_dashboard != SIDE_MENU_DASHBOARD_NAME:
            self.fail()


    def test__when_company_post_job_page_is_correct__pass(self):
        driver = self.driver
        driver.get(COMPANY_DASHBOARD_URL)
        try:
            post_job_btn = driver.find_element_by_link_text('Post Job')
            post_job_btn.click()
        except:
            time.sleep(1)
        time.sleep(DELAY_SHORT)
        page_header = driver.find_element_by_css_selector('.container.mb-2')
        page_title = page_header.find_element_by_class_name('page-title').text
        bread_crumb_home = page_header.find_element_by_tag_name('a').text
        bread_crumb_home_url = page_header.find_element_by_tag_name('a').get_attribute('href')
        bread_crumb_title = page_header.find_element_by_tag_name('span').text

        if page_title != SIDE_MENU_POST_JOB_NAME:
            self.fail()
        if bread_crumb_home != BREAD_CRUMB_HOME:
            self.fail()
        if bread_crumb_home_url != BREAD_CRUMB_HOME_URL:
            self.fail()
        if bread_crumb_title != SIDE_MENU_POST_JOB_NAME:
            self.fail()

        post_job_url = driver.current_url
        time.sleep(1)
        side_menu_post_job = driver.find_element_by_css_selector(".post_job.active").text
        driver.execute_script("window.history.go(-1)")
        time.sleep(DELAY_SHORT)
        side_menu_dashboard = driver.find_element_by_css_selector(".dashboard.active").text
        if post_job_url != POST_JOB_URL:
            self.fail()
        if side_menu_post_job != SIDE_MENU_POST_JOB_NAME:
            self.fail()
        if side_menu_dashboard != SIDE_MENU_DASHBOARD_NAME:
            self.fail()


    def test__when_company_messages_page_is_correct__pass(self):
        driver = self.driver
        driver.get(COMPANY_DASHBOARD_URL)
        try:
            messages_btn = driver.find_element_by_link_text('Messages')
            messages_btn.click()
        except:
            time.sleep(1)
        time.sleep(DELAY_SHORT)
        page_header = driver.find_element_by_css_selector('.container.mb-2')
        page_title = page_header.find_element_by_class_name('page-title').text
        bread_crumb_home = page_header.find_element_by_tag_name('a').text
        bread_crumb_home_url = page_header.find_element_by_tag_name('a').get_attribute('href')
        bread_crumb_title = page_header.find_element_by_tag_name('span').text

        if page_title != SIDE_MENU_MESSAGES_NAME:
            self.fail()
        if bread_crumb_home != BREAD_CRUMB_HOME:
            self.fail()
        if bread_crumb_home_url != BREAD_CRUMB_HOME_URL:
            self.fail()
        if bread_crumb_title != SIDE_MENU_MESSAGES_NAME:
            self.fail()

        messages_url = driver.current_url
        time.sleep(1)
        side_menu_messages = driver.find_element_by_css_selector(".company_message.active").text
        driver.execute_script("window.history.go(-1)")
        time.sleep(DELAY_SHORT)
        side_menu_dashboard = driver.find_element_by_css_selector(".dashboard.active").text
        if messages_url != MESSAGES_URL:
            self.fail()
        if side_menu_messages != SIDE_MENU_MESSAGES_NAME:
            self.fail()
        if side_menu_dashboard != SIDE_MENU_DASHBOARD_NAME:
            self.fail()


    def test__when_company_recent_activity_is_correct__pass(self):
        driver = self.driver
        driver.get(COMPANY_DASHBOARD_URL)
        try:
            recent_activity_btn = driver.find_element_by_link_text('Recent Activity')
            recent_activity_btn.click()
        except:
            time.sleep(1)
        time.sleep(DELAY_SHORT)
        page_header = driver.find_element_by_css_selector('.container.mb-2')
        page_title = page_header.find_element_by_class_name('page-title').text
        bread_crumb_home = page_header.find_element_by_tag_name('a').text
        bread_crumb_home_url = page_header.find_element_by_tag_name('a').get_attribute('href')
        bread_crumb_title = page_header.find_element_by_tag_name('span').text

        if page_title != SIDE_MENU_RECENT_ACTIVITY_NAME:
            self.fail()
        if bread_crumb_home != BREAD_CRUMB_HOME:
            self.fail()
        if bread_crumb_home_url != BREAD_CRUMB_HOME_URL:
            self.fail()
        if bread_crumb_title != SIDE_MENU_RECENT_ACTIVITY_NAME:
            self.fail()

        recent_activity_url = driver.current_url
        time.sleep(1)
        side_menu_recent_activity = driver.find_element_by_css_selector(".com_recent_activity.active").text
        driver.execute_script("window.history.go(-1)")
        time.sleep(DELAY_SHORT)
        side_menu_dashboard = driver.find_element_by_css_selector(".dashboard.active").text
        if recent_activity_url != RECENT_ACTIVITY_URL:
            self.fail()
        if side_menu_recent_activity != SIDE_MENU_RECENT_ACTIVITY_NAME:
            self.fail()
        if side_menu_dashboard != SIDE_MENU_DASHBOARD_NAME:
            self.fail()



    def test__when_company_notifications_page_is_correct__pass(self):
        driver = self.driver
        driver.get(COMPANY_DASHBOARD_URL)
        try:
            notifications_btn = driver.find_element_by_link_text('Notifications')
            notifications_btn.click()
        except:
            time.sleep(1)
        time.sleep(DELAY_SHORT)
        page_header = driver.find_element_by_css_selector('.container.mb-2')
        page_title = page_header.find_element_by_class_name('page-title').text
        bread_crumb_home = page_header.find_element_by_tag_name('a').text
        bread_crumb_home_url = page_header.find_element_by_tag_name('a').get_attribute('href')
        bread_crumb_title = page_header.find_element_by_tag_name('span').text

        if page_title != SIDE_MENU_NOTIFICATIONS_NAME:
            self.fail()
        if bread_crumb_home != BREAD_CRUMB_HOME:
            self.fail()
        if bread_crumb_home_url != BREAD_CRUMB_HOME_URL:
            self.fail()
        if bread_crumb_title != SIDE_MENU_NOTIFICATIONS_NAME:
            self.fail()

        recent_activity_url = driver.current_url
        time.sleep(1)
        side_menu_recent_activity = driver.find_element_by_css_selector(".company_notification.active").text
        driver.execute_script("window.history.go(-1)")
        time.sleep(DELAY_SHORT)
        side_menu_dashboard = driver.find_element_by_css_selector(".dashboard.active").text
        if recent_activity_url != NOTIFICATIONS_URL:
            self.fail()
        if side_menu_recent_activity != SIDE_MENU_RECENT_ACTIVITY_NAME:
            self.fail()
        if side_menu_dashboard != SIDE_MENU_DASHBOARD_NAME:
            self.fail()



    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()