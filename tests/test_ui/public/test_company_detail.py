import time
import unittest

from selenium.webdriver.chrome import webdriver

from tests.config import VALID_COM_VIEW_USERNAME, VALID_COM_VIEW_PASSWORD, VALID_PRO_VIEW_USERNAME, \
    VALID_PRO_VIEW_PASSWORD
from tests.config_web import MAIN_URL_HOME, CHROME_DRIVER_LOCATION, DELAY_SHORT
from tests.test_ui.company.test_signin import signin_helper_company, signout_helper
from tests.test_ui.professional.test_signin import signin_helper

COMPANY_IMAGE_URL = f'{MAIN_URL_HOME}/media/images/portfolio.png'
COMPANY_EXAMPLE_VIEW = 'Company Example View'
COMPANY_CITY = 'Bangladesh,Dhaka'
COMPANY_LOCATION_ICON_DATA = 'M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z'
COMPANY_JOBS_COUNT = '11 Job(s)'
COMPANY_ABOUT_US = 'Company Example Profile'
COMPANY_EXAMPLE_VIEW_RECENT_JOBS_WITH_SIGNIN = ['Job Post Example Twenty', 'Job Post Example Nineteen', 'Job Post Example Seventeen', 'Job Post Example Fourteen', 'Job Post Example Fourteen Single', 'Job Post Example Fifteen', 'Job Post Example Company Four', 'Job Post Example Company Six', 'Job Post Example Company Three', 'Job Post Example Company Five', 'Job Post Example Company Ten']
COMPANY_EXAMPLE_VIEW_RECENT_JOBS_WITHOUT_SIGNIN = ['Job Post Example Twenty', 'Job Post Example Nineteen', 'Job Post Example Seventeen', 'Job Post Example Fourteen', 'Job Post Example Fourteen Single', 'Job Post Example Fifteen', 'Job Post Example Company Four', 'Job Post Example Company Six', 'Job Post Example Company Three', 'Job Post Example Company Five']
SECTIONS_LABEL_LIST_DATA = ['Basic Information', 'Contact Number', 'Address', 'Other Information', 'Our Location']
INFORMATION_LABEL_LIST_DATA = ['Name:', 'Year of Establishment:', 'Legal Structure:', 'No of Human Resources:', 'No of IT Resources:', 'Mobile No:', 'Email:', 'Web Address:', 'Address:', 'Dhaka, Gulsan', 'Area:', 'City:', 'BASIS Membership No:', 'Name in Google:', 'Name in Bdjobs:', 'Name in Facebook:', 'Map data ©2020']
INFORMATION_VALUE_LIST_DATA = ['Company Example View', '2020', 'CompanyLegality', '25', '21', '01911111111', '01911111112', '01911111113', 'com_example_view@ishraak.com', 'Niketon', 'Bangladesh,Dhaka', '4', 'bdgoogle', 'bdjobs.com/company', 'fb/company']

COMPANY_DETAIL_PAGE_TITLE = 'Company Details'
BREAD_CRUMB_HOME = 'Home'
BREAD_CRUMB_HOME_URL = f'{MAIN_URL_HOME}/'


LABEL_COMPANY_ABOUT_US = 'About Us'
LABEL_COMPANY_RECENT_JOB = 'Recent Job(s)'

COMPANY_CURRENT_URL = f'{MAIN_URL_HOME}/company-details/Company%20Example%20View/'
COMPANY_URL = url = f'{MAIN_URL_HOME}/company-details/Company%20Example%20View/'

class TestCompanyDetail(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = webdriver.WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        time.sleep(DELAY_SHORT)


    def test__when_company_detail_is_showing_data__should_pass(self):
        driver = self.driver
        data = company_detail_helper(driver, COMPANY_URL)
        time.sleep(1)
        if data['page_title'] != COMPANY_DETAIL_PAGE_TITLE:
            self.fail()
        if data['bread_crumb_home'] != BREAD_CRUMB_HOME:
            self.fail()
        if data['bread_crumb_home_url'] != BREAD_CRUMB_HOME_URL:
            self.fail()
        if data['bread_crumb_title'] != COMPANY_DETAIL_PAGE_TITLE:
            self.fail()
        if data['company_image'] != COMPANY_IMAGE_URL:
            self.fail()
        if data['company_name'] != COMPANY_EXAMPLE_VIEW:
            self.fail()
        if data['location_icon'] != COMPANY_LOCATION_ICON_DATA:
            self.fail()
        if data['location_city'] != COMPANY_CITY:
            self.fail()
        if data['jobs_count'] != COMPANY_JOBS_COUNT:
            self.fail()
        if data['about_us_label'] != LABEL_COMPANY_ABOUT_US:
            self.fail()
        if data['company_profile'] != COMPANY_ABOUT_US:
            self.fail()
        if data['sections_label_list'] != SECTIONS_LABEL_LIST_DATA:
            self.fail()
        if data['information_label_list'] != INFORMATION_LABEL_LIST_DATA:
            self.fail()
        if data['information_value_list'] != INFORMATION_VALUE_LIST_DATA:
            self.fail()
        if data['company_current_url'] != COMPANY_CURRENT_URL:
            self.fail()
        time.sleep(1)



    def test_job_detail__when__company_signed_in__view_recent_jobs__should_pss(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        data = {
            "email": VALID_COM_VIEW_USERNAME,
            "password": VALID_COM_VIEW_PASSWORD,
        }
        signin_helper_company(driver, data)
        time.sleep(DELAY_SHORT)
        job_list = job_list_with_signin_helper(driver, COMPANY_URL)
        signout_helper(driver)
        if job_list != COMPANY_EXAMPLE_VIEW_RECENT_JOBS_WITH_SIGNIN:
            self.fail()
        time.sleep(1)


    def test_job_detail__when__professional_signed_in__view_recent_jobs__should_pss(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        data = {
            "email": VALID_PRO_VIEW_USERNAME,
            "password": VALID_PRO_VIEW_PASSWORD,
        }
        signin_helper(driver, data)
        time.sleep(DELAY_SHORT)
        job_list = job_list_with_signin_helper(driver, COMPANY_URL)
        signout_helper(driver)
        if job_list != COMPANY_EXAMPLE_VIEW_RECENT_JOBS_WITH_SIGNIN:
            self.fail()
        time.sleep(1)


    def test_job_detail__without_signed_in__view_recent_jobs__should_pss(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        job_list = job_list_without_signin_helper(driver, COMPANY_URL)
        if job_list != COMPANY_EXAMPLE_VIEW_RECENT_JOBS_WITHOUT_SIGNIN:
            self.fail()
        time.sleep(1)


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


def company_detail_helper(driver, url):
    driver.get(url)
    time.sleep(DELAY_SHORT)
    sections_label_list = []
    information_label_list = []
    information_value_list = []
    time.sleep(1)
    page_header = driver.find_element_by_css_selector('.alice-bg.shadow.mb-3')
    page_title = page_header.find_element_by_css_selector('.col-md.page-title').text
    bread_crumb_home = page_header.find_element_by_tag_name('a').text
    bread_crumb_home_url = page_header.find_element_by_tag_name('a').get_attribute('href')
    bread_crumb_title = page_header.find_element_by_tag_name('span').text
    title_and_info = driver.find_element_by_class_name('title-and-info')
    company_image = title_and_info.find_element_by_tag_name('img').get_attribute('src')
    company_name = title_and_info.find_element_by_id('name').text
    try:
        location_icon = title_and_info.find_element_by_tag_name('path').get_attribute('d')
    except:
        location_icon = ''
    try:
        location_city = title_and_info.find_element_by_tag_name('p').text
    except:
        location_city = ''
    jobs_count = title_and_info.find_element_by_id('jobCount').text
    about_us_section = driver.find_element_by_id('about_us_section')
    about_us_label = about_us_section.find_element_by_tag_name('h4').text
    company_profile = about_us_section.find_element_by_id('company_profile').text
    company_detail = driver.find_element_by_class_name('details-information')
    information = company_detail.find_element_by_css_selector('.col-xl-4.col-lg-4')
    information_sections_label = information.find_elements_by_tag_name('h4')
    information_label = information.find_elements_by_tag_name('span')
    information_value = information.find_elements_by_tag_name('p')
    for item in information_sections_label:
        sections_label_text = item.text
        if sections_label_text != '':
            sections_label_list.append(sections_label_text)
    for item in information_label:
        information_label_name = item.text
        if information_label_name != '':
            information_label_list.append(information_label_name)
    for item in information_value:
        information_value_text = item.text
        if information_value_text != '':
            information_value_list.append(information_value_text)
    company_current_url = driver.current_url
    time.sleep(1)

    data = {
        'page_title' : page_title,
        'bread_crumb_home' : bread_crumb_home,
        'bread_crumb_home_url' : bread_crumb_home_url,
        'bread_crumb_title' : bread_crumb_title,
        'company_image' : company_image,
        'company_name': company_name,
        'location_icon': location_icon,
        'location_city': location_city,
        'jobs_count': jobs_count,
        'about_us_label': about_us_label,
        'company_profile': company_profile,
        'sections_label_list': sections_label_list,
        'information_label_list': information_label_list,
        'information_value_list': information_value_list,
        'company_current_url': company_current_url
    }

    return data

def job_list_with_signin_helper(driver, url):
    driver.get(url)
    time.sleep(DELAY_SHORT)
    try:
        titles = []
        i = 0;
        page_count = driver.find_elements_by_class_name('page-item ').__len__()
        time.sleep(1)
        for i in range(i, page_count - 2):
            if i <= page_count - 3:
                time.sleep(1)
                page = driver.find_element_by_css_selector('.page-item.active').text
                time.sleep(1)
            else:
                time.sleep(1)
            job_list = driver.find_elements_by_class_name('job-list')

            for job in job_list:

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
        return titles

    except:
        return 0


def job_list_without_signin_helper(driver, url):
    driver.get(url)
    time.sleep(DELAY_SHORT)
    try:
        titles = []
        i = 0;
        page_count = driver.find_elements_by_class_name('page-item ').__len__()
        time.sleep(1)
        for i in range(i, page_count - 2):
            if i <= page_count - 3:
                time.sleep(1)
                page = driver.find_element_by_css_selector('.page-item.active').text
                time.sleep(1)
            else:
                time.sleep(1)
            job_list = driver.find_elements_by_class_name('job-list')

            for job in job_list:

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
                try:
                    signin_button = driver.find_element_by_id('signinButton')
                    break
                except:
                    return 0

            time.sleep(1)

        return titles

    except:
        return 0

if __name__ == '__main__':
    unittest.main()
