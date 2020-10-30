import time
import unittest

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.color import Color

from p7.settings_dev import APP_VERSION_NUMBER
from tests.config import VALID_PRO_USERNAME, VALID_PRO_PASSWORD, VALID_COM_USERNAME, VALID_COM_PASSWORD
from tests.test_ui.company.test_signin import signin_helper_company
from tests.test_ui.professional.test_signin import signin_helper
from tests.config_web import CHROME_DRIVER_LOCATION, DELAY_SHORT, MAIN_URL, PRO_SIGNIN_URL, DELAY_LONG, PROF_REGISTER_URL, \
    MAIN_URL_HOME

USERNAME = "Mr Prof Example"
COM_USERNAME = "Mr Com Example"
ADMIN_EMAIL = "example@ishraak.com"
ADMIN_PHONE = "01900000000"
FACEBOOK_URL = "http://facebook.com/example"
LINKEDIN_URL = "http://bd.linkedin.com/example"
TWITTER_URL = "http://twitter.com/example"
PRO_PIC = MAIN_URL + "/static/images/alternate.jpg"
PRO_PIC_COMPANY = MAIN_URL + "/static/images/company/company-logo-1.png"
PRO_PIC_PROFESSIONAL = MAIN_URL + "/media/5f7528f7-21a3-48de-83ab-ad511578df20-professional.jpeg"
CAREER_ADVICE_ONE_IMAGE_SRC = MAIN_URL + '/media/images/career_advice_thumb_GODFqWj.jpeg'
HOME = "Home"
JOBS = "Jobs"
JOB_SEARCH_PAGE = MAIN_URL + '/jobs/?page_size=10'
JOB_SEARCH_PAGE_ONLY = MAIN_URL + '/jobs/'
JOBS_URL = MAIN_URL + '/jobs/'
CAREER_ADVICE = "Career Advice"
CAREER_ADVICE_URL = MAIN_URL + '/career-advice/'
ABOUT_US = "About Us"
ABOUT_US_URL = MAIN_URL + '/about-us/'
CONTACT_US = "Contact Us"
CONTACT_US_URL = MAIN_URL + "/contact-us/"
SIGN_IN = "Sign In"
SIGN_UP = "Sign Up"
REGISTER = "Register"
DASHBOARD = " Dashboard"
DASHBOARD_URL = MAIN_URL + '/professional/profile-dashboard/'
COM_DASHBOARD = MAIN_URL + '/company/dashboard/'
CHANGE_PASSWORD = " Change Password"
CHANGE_PASSWORD_URL = MAIN_URL + '/change-password/'
SIGN_OUT = " Sign out"
SIGN_OUT_URL = MAIN_URL + '/sign-out'
LOGO_SRC_BLACK = MAIN_URL + '/static/images/logo_black.png'
LOGO_SRC_NORMAL = MAIN_URL + '/static/images/logo.png'
HOMEPAGE_TITLE = "All the Great Jobs in One Place!"
SHORT_PARAGRAPH = "Find Jobs, Employment & Career Opportunities"
PLACEHOLDER = "Enter Keywords"
BTN_NAME = "SEARCH"
YELLOW_COLOR_HEX = "#f5d91d"
HEADING_COLOR = "#f5d91d"
HOMEPAGE_TITLE_COLOR = "#ffffff"
HEADING_COLOR_BLACK = "#ffffff"
BLACK_HEADING_COLOR = "#212529"
TOP_SECTION_COLOR = "#101725"
TOP_SECTION_ICON_COLOR = "#343a40"
BANNER_SEARCH_BACKGROUND_COLOR = "rgba(0, 0, 0, 0.4)"
# BANNER_SEARCH_BACKGROUND_COLOR = "rgba(255, 255, 255, 0.2)"
BORDER_TOP_COLOR = "rgba(245, 217, 29, 1)"
BLACK_HEX = "#000000"
TRENDING_KEYWORDS = "Trending Keywords:"
SEARCH_KEYWORD = "Example"
SEARCH_KEYWORD_1 = "Twenty"
JOB_SEARCH_PAGE_URL = MAIN_URL + '/jobs/?page=1&q=Example&job_city=&category=&top-skill=&skill=&salaryMin=0&salaryMax=100000&experienceMin=0&experienceMax=10&datePosted=&gender=&job_type=&qualification=&unspecified_salary=1&sort=descending'
TITLE_UNDER_BANNER = "Explore The Right Job"
PARAGRAPH_UNDER_TITLE = "Go for the top ones"
TOP_CATEGORIES_TITLE = "TOP CATEGORIES"
TOP_CATEGORIES_SEARCH_VALUE = "Showing 1 - 10 of 13 Jobs"
TOP_CATEGORIES_SEARCH_VALUE_1 = "Showing 1 - 10 of 19 Jobs"
TOP_SKILLS_TITLE = "TOP SKILLS"
TOP_SKILLS_SARCH_VALUE = "Showing 1 - 10 of 22 Jobs"
TOP_SKILLS_SARCH_VALUE_1 = "Showing 1 - 10 of 31 Jobs"
TOP_COMPANIES_TITLE = "TOP COMPANIES"
RECENT_JOBS_TITLE = "Recent Jobs"
BROWSE_ALL_JOBS_LINK_TITLE = "Browse All Jobs"
OPEN_JOBS_TEXT = "Jobs"
VACANCY_TEXT = "Vacancies"
SKILLS_TEXT = "Skills"
COMPANIES_TEXT = "Companies"
FEATURED_COMPANIES_TITLE = "Featured Companies"
FEATURED_COMPANY_ONE = "Featured Company Nine"
MIN_FEATURED_COMPANY = 9
FEATURED_COMPANY_LOCATION = "Dhaka, Bangladesh"

CAREER_ADVICE_TEXT = "Career Advice"
CAREER_ADVICE_TITLE_ONE = "Career Advice Example One"
CAREER_ADVICE_ONE_AUTHOR_NAME = "Author Example One"
DATE_AND_DAY = "23/08/2020"
CAREER_ADVICE_DESCRIPTION_ONE = "Career Advice Short Description is here. Career Advice Short Description is here. Career Advice Short Description is here. Career Advice Short Description is here. Career Advice Short Description is here. Career Advice Short Description is here. Career Advice Short Description is here. Career Advice Short Description is here. Career Advice Short Description is here. Career Advice Short Description is here. Career Advice Short Description is here. Career Advice Short Description is here. Career Advice Short Description is here. Career Advice Short Description is here. Career Advice Short Description is here. Career Advice Short Description is here. Career Advice Short Description is here. Career Advice Short Description is here."

APP_BANNER_TEXT = "Get JobXprss App"
APP_BANNER_PARAGRAPH = "To get the best JobXprss experience, use the mobile app."
# COUNT VALUES FOR CHECKING IN TEST CASE
TOP_CATEGORIES_COUNT = '3'
TOP_SKILLS_COUNT = '7'
TOP_COMPANIES_COUNT = '2'
JOB_CATEGORY_EXAMPLE_TWO_JOBS = '13'
JOB_CATEGORY_EXAMPLE_ONE_JOBS = '12'
JOB_CATEGORY_EXAMPLE_THREE_JOBS = '3'
CSS_JOBS_COUNT = '22'
AWS_JOBS_COUNT = '15'
HTML_JOBS_COUNT = '14'
PYTHON_JOBS_COUNT = '13'
DJANGO_JOBS_COUNT = '12'
PHP_JOBS_COUNT = '10'
JAVA_JOBS_COUNT = '3'
COMPANY_EXAMPLE_JOBS_COUNT = '17'
COMPANY_EXAMPLE_TWO_JOBS_COUNT = '11'
RECENT_JOBS_COUNT = '6'
OPEN_JOBS_COUNT = '27'
OPEN_JOBS_COUNT_1 = '37'
OPEN_JOBS_COUNT_2 = '36'
VACANCY_COUNT = '37'
VACANCY_COUNT_1 = '36'
SKILLS_COUNT = '7'
SKILLS_COUNT_1 = '8'
COMPANIES_COUNT = '12'
COMPANIES_COUNT_1 = '14'
# TOP CATEGORIES LISTS
FIRST_CATEGORIES = "Job Category Example Two({})".format(JOB_CATEGORY_EXAMPLE_TWO_JOBS)
SECOND_CATEGORIES = "Job Category Example One({})".format(JOB_CATEGORY_EXAMPLE_ONE_JOBS)
THIRD_CATEGORIES = "Job Category Example Three({})".format(JOB_CATEGORY_EXAMPLE_THREE_JOBS)
JOB_CATEGORIES_LIST = [FIRST_CATEGORIES, SECOND_CATEGORIES, THIRD_CATEGORIES]
FIRST_SKILL = "CSS({})".format(CSS_JOBS_COUNT)
SECOND_SKILL = "AWS({})".format(AWS_JOBS_COUNT)
THIRD_SKILL = "HTML({})".format(HTML_JOBS_COUNT)
FOURTH_SKILL = "Python({})".format(PYTHON_JOBS_COUNT)
FIFTH_SKILL = "Django({})".format(DJANGO_JOBS_COUNT)
SIXTH_SKILL = "PHP({})".format(PHP_JOBS_COUNT)
SEVENTH_SKILL = "Java({})".format(JAVA_JOBS_COUNT)
SKILLS_LIST = [FIRST_SKILL, SECOND_SKILL, THIRD_SKILL, FOURTH_SKILL, FIFTH_SKILL, SIXTH_SKILL, SEVENTH_SKILL]
RECENT_JOBS_LIST = [
    "Job Post Example Four",
    "Job Post Example Fourteen",
    "Job Post Example Eleven",
    "Job Post Example Fourteen",
    "Job Post Example Twenty One",
    "Job Post Example Twenty Four"]

RECENT_JOBS_LIST_1 = [
    'Job Post Example Four',
    'Job Post Example Fourteen',
    'Job Post Example Eleven',
    'Job Post Example Fourteen Double',
    'Job Post Example Twenty One',
    'Job Post Example Twenty Four']

RECENT_JOBS_LIST_2 = [
    'Job Post Example Fourteen',
    'Job Post Example Eleven',
    'Job Post Example Fourteen Double',
    'Job Post Example Twenty One',
    'Job Post Example Twenty Four',
    'Job Post Example Five']


FIRST_FOOTER_SECTION_TITLE = "Information"
SECOND_FOOTER_SECTION_TITLE = "Company"
THIRD_FOOTER_SECTION_TITLE = "Job Seekers"
FOURTH_FOOTER_SECTION_TITLE = "Address"
FIFTH_FOOTER_SECTION_TITLE = "Job Alert"
JOB_ALERT = "Get email updates about our latest news."
JOB_ALERT_BTN_NAME = "Subscribe Now..."
JOB_ALERT_BTN_NAME_2 = "Subscribe"
JOB_ALERT_BTN_NULL_FOR_PRO_LOGIN = ""
JOB_ALERT_SUCCSS_MSG = "You have subscribed job alert."
ADDRESS = "House 76 (Level 4)\nRoad 4, Block B\nNiketan, Gulshan 1\nDhaka 1212, Bangladesh"
IHSRAAK_WEBSITE = "http://www.ishraak.com/"
COPYRIGHT_TEXT = 'Copyright © 2020 JobXprss, All Right Reserved\n'+APP_VERSION_NUMBER
SUBSCRIBE_NOW_TEXT = "Subscribe Now..."

FEATURED_CITY = 'Dhaka, Bangladesh'
FEATURED_COMPANY_JOB_COUNT_LIST = ['3 Job(s)', '0 Job(s)', '1 Job(s)', '0 Job(s)', '0 Job(s)', '0 Job(s)', '0 Job(s)', '0 Job(s)', '0 Job(s)']
FEATURED_COMPANY_LOCATION_LIST = [FEATURED_CITY, FEATURED_CITY, FEATURED_CITY, FEATURED_CITY, FEATURED_CITY, FEATURED_CITY, FEATURED_CITY, FEATURED_CITY,FEATURED_CITY]
FEATURED_COMPANY_TITLE_LIST = ['Featured Company Eight', 'Featured Company Five', 'Featured Company Four', 'Featured Company Nine', 'Featured Company One', 'Featured Company Seven', 'Featured Company Six', 'Featured Company Ten', 'Featured Company Three']




class TestNavSection(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = webdriver.WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        time.sleep(DELAY_SHORT)

    def test__when_bg_yellow_exist_in_top__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        bg_yellow_class = driver.find_element_by_class_name('bg-yellow')
        bg_yellow = bg_yellow_class.value_of_css_property('background-color')
        bg_yellow_hex = Color.from_string(bg_yellow).hex
        self.assertIsNotNone(bg_yellow_class)
        self.assertEqual(YELLOW_COLOR_HEX, bg_yellow_hex)

    def test__when_admin_email_and_phone_exist__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        admin_email_class = driver.find_element_by_class_name('admin-email')
        admin_phone_class = driver.find_element_by_class_name('phone-number')
        envelope_icon = driver.find_element_by_xpath('/html/body/header/div[1]/div/div/div[1]/a[1]/span')
        phone_icon = driver.find_element_by_xpath('/html/body/header/div[1]/div/div/div[1]/a[2]/span')
        admin_email = admin_email_class.text
        admin_phone = admin_phone_class.text
        self.assertIsNotNone(envelope_icon)
        self.assertIsNotNone(phone_icon)
        self.assertIsNotNone(admin_email_class)
        self.assertEqual(ADMIN_EMAIL, admin_email)
        self.assertIsNotNone(admin_phone_class)
        self.assertEqual(ADMIN_PHONE, admin_phone)

    def test__when_social_icons_exist__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        facebook_icon = driver.find_element_by_class_name('fa-facebook-square')
        linkedin_icon = driver.find_element_by_class_name('fa-linkedin')
        twitter_icon = driver.find_element_by_class_name('fa-twitter-square')
        self.assertIsNotNone(facebook_icon)
        self.assertIsNotNone(linkedin_icon)
        self.assertIsNotNone(twitter_icon)

    def test__when_social_urls_match__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        facebook_url = driver.find_element_by_class_name('facebook-url').get_attribute('href')
        linkedin_url = driver.find_element_by_class_name('linkedin-url').get_attribute('href')
        twitter_url = driver.find_element_by_class_name('twitter-url').get_attribute('href')
        self.assertEqual(FACEBOOK_URL, facebook_url)
        self.assertEqual(TWITTER_URL, twitter_url)
        self.assertEqual(LINKEDIN_URL, linkedin_url)

    def test__when_social_icon_clickable__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        facebook_url = driver.find_element_by_class_name('facebook-url')
        try:
            facebook_url.click()
        except WebDriverException:
            self.fail("Facebook Icon not click kable ")
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        linkedin_url = driver.find_element_by_class_name('linkedin-url')
        try:
            linkedin_url.click()
        except WebDriverException:
            self.fail("Linkedin Icon not click able")
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        twitter_url = driver.find_element_by_class_name('twitter-url')
        try:
            twitter_url.click()
        except WebDriverException:
            self.fail("Twitter Icon not click able")
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)

    def test__when_logo_exist_and_match__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        image_fluid = driver.find_element_by_class_name('img-fluid')
        image_fluid_src = image_fluid.get_attribute('src')
        self.assertIsNotNone(image_fluid)
        self.assertEqual(LOGO_SRC_BLACK, image_fluid_src)

    def test__when_logo_click_able__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        image_fluid_logo = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[1]/a')
        try:
            image_fluid_logo.click()
            driver.back()
            time.sleep(DELAY_LONG)
        except WebDriverException:
            self.fail("Not click able")
        self.driver.get(self.url)
        driver.maximize_window()
        time.sleep(DELAY_SHORT)
    #
    # def test__while_user_not_logged_in_and_all_nav_valid__should_pass(self):
    #     driver = self.driver
    #     driver.delete_all_cookies()
    #     driver.refresh()
    #     driver.get(MAIN_URL_HOME)
    #     time.sleep(DELAY_SHORT)
    #     fluid_logo = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[1]/a/img')
    #     self.assertIsNotNone(fluid_logo)
    #     fluid_logo_src = fluid_logo.get_attribute("src")
    #     self.assertEqual(LOGO_SRC_NORMAL, fluid_logo_src)
    #     home = driver.find_element_by_link_text('Home')
    #     home_text = home.text
    #     home_link_color = home.value_of_css_property('color')
    #     home_link_color_hex = Color.from_string(home_link_color).hex
    #     self.assertIsNotNone(home)
    #     self.assertEqual(HOME, home_text)
    #     self.assertEqual(HEADING_COLOR_BLACK, home_link_color_hex)
    #     try:
    #         time.sleep(DELAY_SHORT)
    #         self.assertEqual(MAIN_URL + '/', self.driver.current_url)
    #     except WebDriverException:
    #         self.fail("Home Fail")
    #     driver.back()
    #     ##WILL BE SEPERATED
    #     # time.sleep(DELAY_SHORT)
    #     # jobs = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[2]/a')
    #     # jobs_text = jobs.text
    #     # self.assertEqual(JOBS, jobs_text)
    #     # try:
    #     #     time.sleep()
    #     #     jobs.click()
    #     #     time.sleep(DELAY_SHORT)
    #     #     if JOB_SEARCH_PAGE_ONLY != self.driver.current_url and JOB_SEARCH_PAGE != self.driver.current_url:
    #     #         self.fail()
    #     # except WebDriverException:
    #     #     self.fail()
    #     driver.get(MAIN_URL_HOME)
    #     time.sleep(DELAY_SHORT)
    #     career_advice = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[3]/a')
    #     career_advice_text = career_advice.text
    #     self.assertEqual(CAREER_ADVICE, career_advice_text)
    #     try:
    #         career_advice.click()
    #         time.sleep(DELAY_SHORT)
    #         self.assertEqual(CAREER_ADVICE_URL, self.driver.current_url)
    #     except WebDriverException:
    #         self.fail("CAREER ADVICE Fail")
    #     driver.back()
    #     time.sleep(DELAY_SHORT)
    #     about_us = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[4]/a')
    #     about_us_text = about_us.text
    #     self.assertEqual(ABOUT_US, about_us_text)
    #     try:
    #         about_us.click()
    #         time.sleep(DELAY_SHORT)
    #         self.assertEqual(ABOUT_US_URL, self.driver.current_url)
    #     except WebDriverException:
    #         self.fail("ABOUT US Fail")
    #     driver.back()
    #     time.sleep(DELAY_SHORT)
    #     contact_us = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[5]/a')
    #     contact_us_text = contact_us.text
    #     self.assertEqual(CONTACT_US, contact_us_text)
    #     try:
    #         contact_us.click()
    #         time.sleep(DELAY_SHORT)
    #         self.assertEqual(CONTACT_US_URL, self.driver.current_url)
    #     except WebDriverException:
    #         self.fail("CONTACT US Fail")
    #     driver.back()
    #     time.sleep(DELAY_SHORT)
    #     sign_in = driver.find_element_by_xpath('//*[@id="sign-in"]/a')
    #     sign_in_text = sign_in.text
    #     self.assertEqual(SIGN_IN, sign_in_text)
    #     try:
    #         sign_in.click()
    #         time.sleep(DELAY_SHORT)
    #         self.assertEqual(PRO_SIGNIN_URL + '/', self.driver.current_url)
    #     except WebDriverException:
    #         self.fail("SIGN IN Fail")
    #     driver.back()
    #     time.sleep(DELAY_SHORT)
    #     register = driver.find_element_by_xpath('//*[@id="register"]/a')
    #     register_text = register.text
    #     self.assertEqual(SIGN_UP, register_text)
    #     try:
    #         register.click()
    #         time.sleep(DELAY_SHORT)
    #         self.assertEqual(PROF_REGISTER_URL + '/', self.driver.current_url)
    #     except WebDriverException:
    #         self.fail("REGISTER Fail")
    #     driver.back()
    #     time.sleep(DELAY_SHORT)
    #     driver.execute_script("window.scrollTo(0, 700)")
    #     time.sleep(DELAY_LONG)
    #     fluid_logo = driver.find_element_by_xpath('/html/body/header/nav/div[1]/a/img')
    #     self.assertIsNotNone(fluid_logo)
    #     fluid_logo_src = fluid_logo.get_attribute("src")
    #     self.assertEqual(LOGO_SRC_BLACK, fluid_logo_src)
    #     sign_in_round = driver.find_element_by_xpath('/html/body/header/nav/div[2]/a[1]')
    #     sign_in_round_text = sign_in_round.text
    #     sign_in_round_url = sign_in_round.get_attribute('href')
    #     self.assertEqual(PRO_SIGNIN_URL + '/', sign_in_round_url)
    #     sign_in_round_text_color = sign_in_round.value_of_css_property('color')
    #     sign_in_round_text_bg_color = sign_in_round.value_of_css_property('background-color')
    #     sign_in_round_text_color_hex = Color.from_string(sign_in_round_text_color).hex
    #     sign_in_round_text_bg_color_hex = Color.from_string(sign_in_round_text_bg_color).hex
    #     self.assertEqual(BLACK_HEX, sign_in_round_text_color_hex)
    #     self.assertEqual(YELLOW_COLOR_HEX, sign_in_round_text_bg_color_hex)
    #     self.assertEqual(sign_in_round_text, SIGN_IN)
    #     try:
    #         sign_in_round.click()
    #         time.sleep(DELAY_SHORT)
    #         self.assertEqual(PRO_SIGNIN_URL + '/', self.driver.current_url)
    #     except WebDriverException:
    #         self.fail("SIGN IN round Fail")
    #     driver.back()
    #     time.sleep(DELAY_SHORT)
    #     driver.execute_script("window.scrollTo(0, 700)")
    #     time.sleep(DELAY_SHORT)
    #     sign_up_round = driver.find_element_by_xpath('/html/body/header/nav/div[2]/a[2]')
    #     sign_up_round_text = sign_up_round.text
    #     self.assertEqual(SIGN_UP, sign_up_round_text)
    #     try:
    #         sign_up_round.click()
    #         time.sleep(DELAY_SHORT)
    #         self.assertEqual(PROF_REGISTER_URL + '/', self.driver.current_url)
    #     except WebDriverException:
    #         self.fail("SIGN IN round Fail")
    #     driver.back()
    #     time.sleep(DELAY_LONG)
    #     ##Will BE SEPERATED CSE
    #     # driver.execute_script("window.scrollTo(0, 700)")
    #     # toogle_icon = driver.find_element_by_xpath('/html/body/header/nav/div[3]/button')
    #     # toogle_icon_bg_image = toogle_icon.value_of_css_property('background-image')
    #     # self.assertIsNotNone(toogle_icon_bg_image)
    #     # try:
    #     #     toogle_icon.click()
    #     #     time.sleep(DELAY_SHORT)
    #     #     jobs = driver.find_element_by_xpath('//*[@id="collapsibleNavbar"]/ul/li[1]/a')
    #     #     jobs_text = jobs.text
    #     #     self.assertEqual(JOBS, jobs_text)
    #     #     jobs_url = jobs.get_attribute('href')
    #     #     self.assertEqual(JOBS_URL, jobs_url)
    #     #     career_advice = driver.find_element_by_xpath('//*[@id="collapsibleNavbar"]/ul/li[2]/a')
    #     #     career_advice_text = career_advice.text
    #     #     self.assertEqual(CAREER_ADVICE_TEXT, career_advice_text)
    #     #     career_advice_url = career_advice.get_attribute('href')
    #     #     self.assertEqual(CAREER_ADVICE_URL, career_advice_url)
    #     #     about_us = driver.find_element_by_xpath('//*[@id="collapsibleNavbar"]/ul/li[3]/a')
    #     #     about_us_text = about_us.text
    #     #     self.assertEqual(ABOUT_US, about_us_text)
    #     #     about_us_url = about_us.get_attribute('href')
    #     #     self.assertEqual(ABOUT_US_URL, about_us_url)
    #     #     contact_us = driver.find_element_by_xpath('//*[@id="collapsibleNavbar"]/ul/li[4]/a')
    #     #     contact_us_text = contact_us.text
    #     #     self.assertEqual(CONTACT_US, contact_us_text)
    #     #     contact_us_url = contact_us.get_attribute('href')
    #     #     self.assertEqual(CONTACT_US_URL, contact_us_url)
    #     # except WebDriverException:
    #     #     self.fail("FAIL")
    #     # toogle_icon = driver.find_element_by_xpath('/html/body/header/nav/div[3]/button/span')
    #     # toogle_icon.click()

    def test__when_user_type_pro_nav_valid__should_pass(self):
        driver = self.driver
        driver.delete_all_cookies()
        time.sleep(DELAY_SHORT)
        driver.refresh()
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        data = {
            "email": VALID_PRO_USERNAME,
            "password": VALID_PRO_PASSWORD

        }
        signin_helper(driver, data)
        time.sleep(1)
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        home = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[1]/a')
        home.click()
        time.sleep(DELAY_LONG)
        fluid_logo = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[1]/a/img')
        self.assertIsNotNone(fluid_logo)
        fluid_logo_src = fluid_logo.get_attribute("src")
        self.assertEqual(LOGO_SRC_NORMAL, fluid_logo_src)
        home = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[1]/a')
        home_text = home.text
        time.sleep(1)
        home_link_color = home.value_of_css_property('color')
        home_link_color_hex = Color.from_string(home_link_color).hex
        self.assertIsNotNone(home)
        self.assertEqual(HOME, home_text)
        self.assertEqual(HEADING_COLOR, home_link_color_hex)
        try:
            home.click()
            time.sleep(DELAY_SHORT)
            self.assertEqual(MAIN_URL + '/#', self.driver.current_url)
        except WebDriverException:
            self.fail("Home Fail")
        driver.back()
        time.sleep(DELAY_SHORT)
        jobs = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[2]/a')
        jobs_text = jobs.text
        self.assertEqual(JOBS, jobs_text)
        try:
            jobs.click()
            time.sleep(DELAY_SHORT)
            if JOB_SEARCH_PAGE_ONLY != self.driver.current_url and JOB_SEARCH_PAGE != self.driver.current_url:
                self.fail()
        except WebDriverException:
            self.fail()
        driver.back()
        time.sleep(DELAY_SHORT)
        career_advice = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[3]/a')
        career_advice_text = career_advice.text
        self.assertEqual(CAREER_ADVICE, career_advice_text)
        try:
            time.sleep(1)
            career_advice.click()
            time.sleep(DELAY_SHORT)
            self.assertEqual(CAREER_ADVICE_URL, self.driver.current_url)
        except WebDriverException:
            self.fail("CAREER ADVICE Fail")
        driver.back()
        time.sleep(DELAY_SHORT)
        about_us = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[4]/a')
        about_us_text = about_us.text
        self.assertEqual(ABOUT_US, about_us_text)
        try:
            time.sleep(1)
            about_us.click()
            time.sleep(DELAY_SHORT)
            self.assertEqual(ABOUT_US_URL, self.driver.current_url)
        except:
            self.fail("ABOUT US Fail")
        driver.back()
        time.sleep(DELAY_SHORT)
        contact_us = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[5]/a')
        contact_us_text = contact_us.text
        self.assertEqual(CONTACT_US, contact_us_text)
        try:
            time.sleep(1)
            contact_us.click()
            time.sleep(DELAY_SHORT)
            self.assertEqual(CONTACT_US_URL, self.driver.current_url)
        except:
            self.fail("CONTACT US Fail")
        driver.back()
        time.sleep(DELAY_SHORT)
        # # WILL BE SEPERATED CASE
        # image_fluid = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[6]/button/img')
        # image_fluid_src = image_fluid.get_attribute('src')
        # if PRO_PIC_PROFESSIONAL != image_fluid_src and PRO_PIC_COMPANY != image_fluid_src:
        #     self.fail()
        # try:
        #     image_fluid.click()
        #     time.sleep(DELAY_SHORT)
        #     pro_name = driver.find_element_by_xpath('//*[@id="userNavbarMain"]/div[1]/div/h5/a').text
        #     self.assertEqual(USERNAME, pro_name)
        #     pro_email = driver.find_element_by_xpath('//*[@id="userNavbarMain"]/div[1]/div/span').text
        #     self.assertEqual(VALID_PRO_USERNAME, pro_email)
        #     pro_image = driver.find_element_by_xpath('//*[@id="userNavbarMain"]/div[1]/a/img').get_attribute('src')
        #     self.assertEqual(PRO_PIC, pro_image)
        #     ti_home = driver.find_element_by_class_name('ti-public')
        #     self.assertIsNotNone(ti_home)
        #     ti_home_color = ti_home.value_of_css_property('color')
        #     ti_home_color_hex = Color.from_string(ti_home_color).hex
        #     self.assertEqual(BLACK_HEX, ti_home_color_hex)
        #     dashboard = driver.find_element_by_xpath('//*[@id="userNavbarMain"]/ul/li[1]/a')
        #     dashboard_text = dashboard.text
        #     dashboard_url = dashboard.get_attribute('href')
        #     self.assertEqual(DASHBOARD, dashboard_text)
        #     self.assertEqual(DASHBOARD_URL, dashboard_url)
        #     ti_key = driver.find_element_by_class_name('ti-key')
        #     self.assertIsNotNone(ti_key)
        #     change_password = driver.find_element_by_xpath('//*[@id="userNavbarMain"]/ul/li[2]/a')
        #     change_password_text = change_password.text
        #     change_password_url = change_password.get_attribute('href')
        #     self.assertEqual(CHANGE_PASSWORD, change_password_text)
        #     self.assertEqual(CHANGE_PASSWORD_URL, change_password_url)
        #     ti_power_off = driver.find_element_by_class_name('ti-power-off')
        #     self.assertIsNotNone(ti_power_off)
        #     sign_out = driver.find_element_by_xpath('//*[@id="userNavbarMain"]/ul/li[3]/a')
        #     sign_out_text = sign_out.text
        #     sign_out_url = sign_out.get_attribute('href')
        #     self.assertEqual(SIGN_OUT, sign_out_text)
        #     self.assertEqual(SIGN_OUT_URL, sign_out_url)
        # except WebDriverException:
        #     self.fail("FAIL")
        # toogle = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[6]/button')
        # toogle.click()
        self.driver.delete_all_cookies()
        self.driver.refresh()
        time.sleep(DELAY_LONG)

    # def test__when_user_type_pro_slight_down_nav_valid__should_pass(self):
    #     driver = self.driver
    #     driver.get(MAIN_URL_HOME)
    #     time.sleep(DELAY_SHORT)
    #     data = {
    #         "email": VALID_PRO_USERNAME,
    #         "password": VALID_PRO_PASSWORD
    #
    #     }
    #     signin_helper(driver, data)
    #     time.sleep(1)
    #     driver.get(MAIN_URL_HOME)
    #     time.sleep(DELAY_LONG)
    #     ##WILL BE SEPERATE CASE
    #     # driver.execute_script("window.scrollTo(0, 700)")
    #     # time.sleep(DELAY_LONG)
    #     # fluid_logo = driver.find_element_by_css_selector('.img-fluid.logo')
    #     # self.assertIsNotNone(fluid_logo)
    #     # fluid_logo_src = fluid_logo.get_attribute("src")
    #     # self.assertEqual(LOGO_SRC_BLACK, fluid_logo_src)
    #     # toogle_icon = driver.find_element_by_xpath('//*[@id="navBtnGroup"]/div[2]/button')
    #     #
    #     # try:
    #     #     toogle_icon.click()
    #     #     time.sleep(DELAY_LONG)
    #     #     jobs = driver.find_element_by_xpath('//*[@id="collapsibleNavbar"]/ul/li[1]/a')
    #     #     jobs_text = jobs.text
    #     #     self.assertEqual(JOBS, jobs_text)
    #     #     jobs_url = jobs.get_attribute('href')
    #     #     self.assertEqual(JOBS_URL, jobs_url)
    #     #     career_advice = driver.find_element_by_xpath('//*[@id="collapsibleNavbar"]/ul/li[2]/a')
    #     #     career_advice_text = career_advice.text
    #     #     self.assertEqual(CAREER_ADVICE_TEXT, career_advice_text)
    #     #     career_advice_url = career_advice.get_attribute('href')
    #     #     self.assertEqual(CAREER_ADVICE_URL, career_advice_url)
    #     #     about_us = driver.find_element_by_xpath('//*[@id="collapsibleNavbar"]/ul/li[3]/a')
    #     #     about_us_text = about_us.text
    #     #     self.assertEqual(ABOUT_US, about_us_text)
    #     #     about_us_url = about_us.get_attribute('href')
    #     #     self.assertEqual(ABOUT_US_URL, about_us_url)
    #     #     contact_us = driver.find_element_by_xpath('//*[@id="collapsibleNavbar"]/ul/li[4]/a')
    #     #     contact_us_text = contact_us.text
    #     #     self.assertEqual(CONTACT_US, contact_us_text)
    #     #     contact_us_url = contact_us.get_attribute('href')
    #     #     self.assertEqual(CONTACT_US_URL, contact_us_url)
    #     # except WebDriverException:
    #     #     self.fail("FAIL")
    #     # toogle_icon = driver.find_element_by_xpath('//*[@id="navBtnGroup"]/div[2]/button')
    #     # toogle_icon.click()
    #     # time.sleep(DELAY_SHORT)
    #     # image_fluid = driver.find_element_by_xpath('//*[@id="navBtnGroup"]/div[3]/button')
    #     # image_fluid_src = driver.find_element_by_xpath('//*[@id="navBtnGroup"]/div[3]/button/img').get_attribute(
    #     #     'src')
    #     # self.assertEqual(PRO_PIC, image_fluid_src)
    #     # try:
    #     #     image_fluid.click()
    #     #     time.sleep(DELAY_SHORT)
    #         # pro_name = driver.find_element_by_xpath('//*[@id="userNavbar"]/div[1]/div/h5/a').text
    #         # self.assertEqual(USERNAME, pro_name)
    #     #     pro_email = driver.find_element_by_xpath('//*[@id="userNavbar"]/div[1]/div/span').text
    #     #     self.assertEqual(VALID_PRO_USERNAME, pro_email)
    #     #     pro_image = driver.find_element_by_xpath('//*[@id="userNavbar"]/div[1]/a/img').get_attribute('src')
    #     #     self.assertEqual(PRO_PIC, pro_image)
    #     #     ti_home = driver.find_element_by_class_name('ti-public')
    #     #     self.assertIsNotNone(ti_home)
    #     #     ti_home_color = ti_home.value_of_css_property('color')
    #     #     ti_home_color_hex = Color.from_string(ti_home_color).hex
    #     #     self.assertEqual(BLACK_HEX, ti_home_color_hex)
    #     #     dashboard = driver.find_element_by_xpath('//*[@id="userNavbar"]/ul/li[1]/a')
    #     #     dashboard_text = dashboard.text
    #     #     dashboard_url = dashboard.get_attribute('href')
    #     #     self.assertEqual(DASHBOARD, dashboard_text)
    #     #     self.assertEqual(DASHBOARD_URL, dashboard_url)
    #     #     ti_key = driver.find_element_by_class_name('ti-key')
    #     #     self.assertIsNotNone(ti_key)
    #     #     change_password = driver.find_element_by_xpath('//*[@id="userNavbar"]/ul/li[2]/a')
    #     #     change_password_text = change_password.text
    #     #     change_password_url = change_password.get_attribute('href')
    #     #     self.assertEqual(CHANGE_PASSWORD, change_password_text)
    #     #     self.assertEqual(CHANGE_PASSWORD_URL, change_password_url)
    #     #     ti_power_off = driver.find_element_by_class_name('ti-power-off')
    #     #     self.assertIsNotNone(ti_power_off)
    #     #     sign_out = driver.find_element_by_xpath('//*[@id="userNavbar"]/ul/li[3]/a')
    #     #     sign_out_text = sign_out.text
    #     #     sign_out_url = sign_out.get_attribute('href')
    #     #     self.assertEqual(SIGN_OUT, sign_out_text)
    #     #     self.assertEqual(SIGN_OUT_URL, sign_out_url)
    #     # except WebDriverException:
    #     #     self.fail("FAIL")
    #     # self.driver.delete_all_cookies()
    #     # self.driver.refresh()
    #     time.sleep(DELAY_LONG)

    def test__when_user_type_com_nav_valid__should_pass(self):
        driver = self.driver
        driver.delete_all_cookies()
        driver.refresh()
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        driver.execute_script("window.scrollTo(0, 3000)")
        time.sleep(DELAY_SHORT)
        data = {
            "email": VALID_COM_USERNAME,
            "password": VALID_COM_PASSWORD

        }
        signin_helper_company(driver, data)
        time.sleep(1)
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        home = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[1]/a')
        home.click()
        time.sleep(DELAY_LONG)
        fluid_logo = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[1]/a/img')
        self.assertIsNotNone(fluid_logo)
        fluid_logo_src = fluid_logo.get_attribute("src")
        self.assertEqual(LOGO_SRC_NORMAL, fluid_logo_src)
        home = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[1]/a')
        home_text = home.text
        home_link_color = home.value_of_css_property('color')
        home_link_color_hex = Color.from_string(home_link_color).hex
        self.assertIsNotNone(home)
        self.assertEqual(HOME, home_text)
        self.assertEqual(HEADING_COLOR, home_link_color_hex)
        try:
            home.click()
            time.sleep(DELAY_SHORT)
            self.assertEqual(MAIN_URL + '/#', self.driver.current_url)
        except WebDriverException:
            self.fail("Home Fail")
        driver.back()
        time.sleep(DELAY_SHORT)
        jobs = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[2]/a')
        jobs_text = jobs.text
        self.assertEqual(JOBS, jobs_text)
        try:
            jobs.click()
            time.sleep(DELAY_SHORT)
            if JOB_SEARCH_PAGE != self.driver.current_url and JOB_SEARCH_PAGE_ONLY != self.driver.current_url:
                self.fail()
        except WebDriverException:
            self.fail()
        driver.back()
        time.sleep(DELAY_SHORT)
        career_advice = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[3]/a')
        career_advice_text = career_advice.text
        self.assertEqual(CAREER_ADVICE, career_advice_text)
        try:
            career_advice.click()
            time.sleep(DELAY_SHORT)
            self.assertEqual(CAREER_ADVICE_URL, self.driver.current_url)
        except WebDriverException:
            self.fail("CAREER ADVICE Fail")
        driver.back()
        time.sleep(DELAY_SHORT)
        about_us = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[4]/a')
        about_us_text = about_us.text
        self.assertEqual(ABOUT_US, about_us_text)
        try:
            about_us.click()
            time.sleep(DELAY_SHORT)
            self.assertEqual(ABOUT_US_URL, self.driver.current_url)
        except WebDriverException:
            self.fail("ABOUT US Fail")
        driver.back()
        time.sleep(DELAY_SHORT)
        contact_us = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[5]/a')
        contact_us_text = contact_us.text
        self.assertEqual(CONTACT_US, contact_us_text)
        try:
            contact_us.click()
            time.sleep(DELAY_SHORT)
            self.assertEqual(CONTACT_US_URL, self.driver.current_url)
        except WebDriverException:
            self.fail("CONTACT US Fail")
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        # # WILL BE SEPERATED CASE
        # image_fluid = driver.find_element_by_xpath('//*[@id="navBtnGroup"]/div[2]/button')
        # image_fluid_src = image_fluid.find_element_by_tag_name('img').get_attribute('src')
        # self.assertEqual(PRO_PIC_COMPANY, image_fluid_src)
        # try:
        #     image_fluid.click()
        #     time.sleep(DELAY_SHORT)
        #     com_name = driver.find_element_by_xpath('//*[@id="userNavbarMain"]/div[1]/div/h5/a').text
        #     self.assertEqual(COM_USERNAME, com_name)
        #     com_email = driver.find_element_by_xpath('//*[@id="userNavbarMain"]/div[1]/div/span').text
        #     self.assertEqual(VALID_COM_USERNAME, com_email)
        #     pro_image = driver.find_element_by_xpath('//*[@id="userNavbarMain"]/div[1]/a/img').get_attribute('src')
        #     self.assertEqual(PRO_PIC_COMPANY, pro_image)
        #     ### COULDNOT OUND TI_PUBLIC IN PAGE SOURCE OF HOME
        #     # ti_home = driver.find_element_by_class_name('ti-public')
        #     # self.assertIsNotNone(ti_home)
        #     # ti_home_color = ti_home.value_of_css_property('color')
        #     # ti_home_color_hex = Color.from_string(ti_home_color).hex
        #     # self.assertEqual(BLACK_HEX, ti_home_color_hex)
        #     dashboard = driver.find_element_by_xpath('//*[@id="userNavbarMain"]/ul/li[1]/a')
        #     dashboard_text = dashboard.text
        #     com_dashboard_url = dashboard.get_attribute('href')
        #     self.assertEqual(DASHBOARD, dashboard_text)
        #     self.assertEqual(COM_DASHBOARD, com_dashboard_url)
        #     ti_key = driver.find_element_by_class_name('ti-key')
        #     self.assertIsNotNone(ti_key)
        #     change_password = driver.find_element_by_xpath('//*[@id="userNavbarMain"]/ul/li[2]/a')
        #     change_password_text = change_password.text
        #     change_password_url = change_password.get_attribute('href')
        #     self.assertEqual(CHANGE_PASSWORD, change_password_text)
        #     self.assertEqual(CHANGE_PASSWORD_URL, change_password_url)
        #     ti_power_off = driver.find_element_by_class_name('ti-power-off')
        #     self.assertIsNotNone(ti_power_off)
        #     sign_out = driver.find_element_by_xpath('//*[@id="userNavbarMain"]/ul/li[3]/a')
        #     sign_out_text = sign_out.text
        #     sign_out_url = sign_out.get_attribute('href')
        #     self.assertEqual(SIGN_OUT, sign_out_text)
        #     self.assertEqual(SIGN_OUT_URL, sign_out_url)
        # except WebDriverException:
        #     self.fail("FAIL")
        # toogle = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[6]/button')
        # toogle.click()
        self.driver.delete_all_cookies()
        self.driver.refresh()
        time.sleep(DELAY_LONG)

    def test__when_user_type_com_slight_down_nav_valid__should_pass(self):
        driver = self.driver
        driver.delete_all_cookies()
        driver.refresh()
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        driver.execute_script("window.scrollTo(0, 3000)")
        time.sleep(DELAY_SHORT)
        data = {
            "email": VALID_COM_USERNAME,
            "password": VALID_COM_PASSWORD

        }
        signin_helper_company(driver, data)
        time.sleep(1)
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        home = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[1]/a')
        home.click()
        time.sleep(DELAY_LONG)
        # ##WILL BE SEPERATED CASE
        # driver.execute_script("window.scrollTo(0, 700)")
        # time.sleep(DELAY_LONG)
        # fluid_logo = driver.find_element_by_xpath('//*[@id="navBtnGroup"]/div[1]/a/img')
        # self.assertIsNotNone(fluid_logo)
        # fluid_logo_src = fluid_logo.get_attribute("src")
        # self.assertEqual(LOGO_SRC_BLACK, fluid_logo_src)

        # toogle_icon = driver.find_element_by_xpath('//*[@id="navBtnGroup"]/div[3]/button/span')
        #
        # toogle_icon_bg_image = driver.find_element_by_class_name('navbar-toggler-icon').value_of_css_property('background-image')
        # self.assertIsNotNone(toogle_icon_bg_image)
        # try:
        #     toogle_icon.click()
        #     time.sleep(1)
        #     jobs = driver.find_element_by_xpath('//*[@id="collapsibleNavbar"]/ul/li[1]/a')
        #     jobs_text = jobs.text
        #     self.assertEqual(JOBS, jobs_text)
        #     jobs_url = jobs.get_attribute('href')
        #     self.assertEqual(JOBS_URL, jobs_url)
        #     career_advice = driver.find_element_by_xpath('//*[@id="collapsibleNavbar"]/ul/li[2]/a')
        #     career_advice_text = career_advice.text
        #     self.assertEqual(CAREER_ADVICE_TEXT, career_advice_text)
        #     career_advice_url = career_advice.get_attribute('href')
        #     self.assertEqual(CAREER_ADVICE_URL, career_advice_url)
        #     about_us = driver.find_element_by_xpath('//*[@id="collapsibleNavbar"]/ul/li[3]/a')
        #     about_us_text = about_us.text
        #     self.assertEqual(ABOUT_US, about_us_text)
        #     about_us_url = about_us.get_attribute('href')
        #     self.assertEqual(ABOUT_US_URL, about_us_url)
        #     contact_us = driver.find_element_by_xpath('//*[@id="collapsibleNavbar"]/ul/li[4]/a')
        #     contact_us_text = contact_us.text
        #     self.assertEqual(CONTACT_US, contact_us_text)
        #     contact_us_url = contact_us.get_attribute('href')
        #     self.assertEqual(CONTACT_US_URL, contact_us_url)
        # except WebDriverException:
        #     self.fail("FAIL")
        # # toogle_icon = driver.find_element_by_css_selector('.fa.fa-bars')
        # # toogle_icon.click()
        # time.sleep(DELAY_SHORT)
        # image_fluid = driver.find_element_by_xpath('//*[@id="navBtnGroup"]/div[2]/button')
        # time.sleep(1)
        # try:
        #     image_fluid.click()
        #     time.sleep(DELAY_SHORT)
        #     com_name = driver.find_element_by_xpath('//*[@id="userNavbar"]/div[1]/div/h5/a').text
        #     self.assertEqual(COM_USERNAME, com_name)
        #     com_email = driver.find_element_by_xpath('//*[@id="userNavbar"]/div[1]/div/span').text
        #     self.assertEqual(VALID_COM_USERNAME, com_email)
        #     pro_image = driver.find_element_by_xpath('//*[@id="userNavbar"]/div[1]/a/img').get_attribute('src')
        #     self.assertEqual(PRO_PIC_COMPANY, pro_image)
        #     ## TI-PUBLIC IS NOT FOUND IN VIEWSOURCE
        #     # ti_home = driver.find_element_by_class_name('ti-public')
        #     # self.assertIsNotNone(ti_home)
        #     # ti_home_color = ti_home.value_of_css_property('color')
        #     # ti_home_color_hex = Color.from_string(ti_home_color).hex
        #     # self.assertEqual(BLACK_HEX, ti_home_color_hex)
        #     dashboard = driver.find_element_by_xpath('//*[@id="userNavbar"]/ul/li[1]/a')
        #     dashboard_text = dashboard.text
        #     com_dashboard_url = dashboard.get_attribute('href')
        #     self.assertEqual(DASHBOARD, dashboard_text)
        #     self.assertEqual(COM_DASHBOARD, com_dashboard_url)
        #     ti_key = driver.find_element_by_class_name('ti-key')
        #     self.assertIsNotNone(ti_key)
        #     change_password = driver.find_element_by_xpath('//*[@id="userNavbar"]/ul/li[2]/a')
        #     change_password_text = change_password.text
        #     change_password_url = change_password.get_attribute('href')
        #     self.assertEqual(CHANGE_PASSWORD, change_password_text)
        #     self.assertEqual(CHANGE_PASSWORD_URL, change_password_url)
        #     ti_power_off = driver.find_element_by_class_name('ti-power-off')
        #     self.assertIsNotNone(ti_power_off)
        #     sign_out = driver.find_element_by_xpath('//*[@id="userNavbar"]/ul/li[3]/a')
        #     sign_out_text = sign_out.text
        #     sign_out_url = sign_out.get_attribute('href')
        #     self.assertEqual(SIGN_OUT, sign_out_text)
        #     self.assertEqual(SIGN_OUT_URL, sign_out_url)
        # except WebDriverException:
        #     self.fail("FAIL")
        self.driver.delete_all_cookies()
        self.driver.refresh()
        time.sleep(DELAY_LONG)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


class TestBannerSection(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = webdriver.WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        time.sleep(DELAY_SHORT)

    def test__when__homepage_title_match__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        homepage_title = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/h1')
        homepage_title_text = homepage_title.text
        homepage_title_color = homepage_title.value_of_css_property('color')
        homepage_title_color_hex = Color.from_string(homepage_title_color).hex
        self.assertEqual(HOMEPAGE_TITLE_COLOR, homepage_title_color_hex)
        self.assertEqual(HOMEPAGE_TITLE, homepage_title_text)

    def test__when_short_paragraph_match__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        short_paragraph = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/p')
        short_paragraph_text = short_paragraph.text
        short_paragraph_color = short_paragraph.value_of_css_property('color')
        short_paragraph_color_hex = Color.from_string(short_paragraph_color).hex
        self.assertEqual(HOMEPAGE_TITLE_COLOR, short_paragraph_color_hex)
        self.assertEqual(SHORT_PARAGRAPH, short_paragraph_text)

    def test__when_banner_search_background_image_match__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        background_image_url = driver.find_element_by_class_name('banner-4-bg').value_of_css_property('background-image')
        self.assertIsNotNone(background_image_url)

    def test__when_banner_search_exist__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        banner_search = driver.find_element_by_class_name('banner-search')
        self.assertIsNotNone(banner_search)

    def test__when_banner_search_background_color_match__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        banner_search_background_color = driver.find_element_by_class_name('banner-search').value_of_css_property('background-color')
        self.assertEqual(BANNER_SEARCH_BACKGROUND_COLOR, banner_search_background_color)

    def test__when_enter_keywords_input_field_exist__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        input_field = driver.find_element_by_id('keyword')
        self.assertIsNotNone(input_field)

    def test__when_placeholder_match__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        placeholder = driver.find_element_by_id('keyword').get_attribute('placeholder')
        self.assertEqual(PLACEHOLDER, placeholder)

    def test__when_search_button_exist__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        btn = driver.find_element_by_xpath('//*[@id="search-form"]/button')
        self.assertIsNotNone(btn)

    def test__when_button_name_match__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        btn_name = driver.find_element_by_xpath('//*[@id="search-form"]/button').text
        self.assertEqual(BTN_NAME, btn_name)

    def test__when_button_icon_fa_search_exist__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        btn_icon = driver.find_element_by_class_name('fa-search')
        self.assertIsNotNone(btn_icon)

    def test__when_search_btn_color_match__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        search_btn_color_rgba = driver.find_element_by_xpath('//*[@id="search-form"]/button').value_of_css_property('background-color')
        search_btn_color_hex = Color.from_string(search_btn_color_rgba).hex
        self.assertEqual(YELLOW_COLOR_HEX, search_btn_color_hex)

    def test__when_button_icon_color_valid__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        btn_icon_black = driver.find_element_by_class_name('text-dark').value_of_css_property('color')
        btn_icon_black_hex = Color.from_string(btn_icon_black).hex
        self.assertEqual(TOP_SECTION_ICON_COLOR, btn_icon_black_hex)

    def test__when_trending_keywords_color_match__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        trending_keywords = driver.find_element_by_xpath('//*[@id="trend-keywords"]')
        trending_keywords_color = trending_keywords.value_of_css_property('color')
        trending_keywords_color_hex = Color.from_string(trending_keywords_color).hex
        self.assertEqual(HOMEPAGE_TITLE_COLOR, trending_keywords_color_hex)

    def test__when_search_by_keywords_all_valid__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        driver.find_element_by_id('keyword').send_keys(SEARCH_KEYWORD)
        driver.find_element_by_xpath('//*[@id="search-form"]/button').click()
        time.sleep(DELAY_LONG)
        search_field_val = driver.find_element_by_id('search-keyword').get_attribute('value')
        self.assertEqual(SEARCH_KEYWORD, search_field_val)
        home = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[1]/a')
        home.click()
        time.sleep(DELAY_LONG)
        search_keyword = driver.find_element_by_xpath('//*[@id="trend-keywords"]/a/span').text
        if SEARCH_KEYWORD != search_field_val and SEARCH_KEYWORD_1 != search_field_val:
            self.fail()
        search_example_link = driver.find_element_by_xpath('//*[@id="trend-keywords"]/a')
        try:
            search_example_link.click()
            time.sleep(DELAY_LONG)
            search_field_val = driver.find_element_by_id('search-keyword').get_attribute('value')
            if SEARCH_KEYWORD != search_field_val and SEARCH_KEYWORD_1 != search_field_val:
                self.fail()
        except WebDriverException:
            self.fail("Fail")
        home = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[1]/a')
        home.click()
        time.sleep(DELAY_SHORT)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


class TestYellowTopSection(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = webdriver.WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        time.sleep(DELAY_SHORT)

    def test__when_yellow_bg_color_valid__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        bg_yellow = driver.find_element_by_class_name('bg-yellow')
        bg_yellow_color = bg_yellow.value_of_css_property('background-color')
        bg_yellow_color_hex = Color.from_string(bg_yellow_color).hex
        self.assertEqual(YELLOW_COLOR_HEX, bg_yellow_color_hex)

    def test__when_title_match__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        title_under_banner = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/h2')
        title_under_banner_text = title_under_banner.text
        title_under_banner_color = title_under_banner.value_of_css_property('color')
        title_under_banner_color_hex = Color.from_string(title_under_banner_color).hex
        self.assertEqual(BLACK_HEADING_COLOR, title_under_banner_color_hex)
        self.assertEqual(TITLE_UNDER_BANNER, title_under_banner_text)

    def test__when_short_paragraph_under_title_match__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        paragraph_under_title = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/p').text
        self.assertEqual(PARAGRAPH_UNDER_TITLE, paragraph_under_title)

    def test__when_top_categories_title_and_icon_match__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        top_categories = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div/div[1]/h5')
        top_categories_title = top_categories.text
        top_categories_color = top_categories.value_of_css_property('color')
        top_categories_color_hex = Color.from_string(top_categories_color).hex
        top_categories_icon = driver.find_element_by_class_name('fa-city')
        top_categories_icon_color = top_categories_icon.value_of_css_property('color')
        top_categories_icon_color_hex = Color.from_string(top_categories_icon_color).hex
        underline = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div/hr')
        underline_color = underline.value_of_css_property('border-top-color')
        self.assertIsNotNone(underline)
        self.assertEqual(BORDER_TOP_COLOR, underline_color)
        self.assertEqual(TOP_CATEGORIES_TITLE, top_categories_title)
        self.assertIsNotNone(top_categories_icon)
        self.assertEqual(TOP_SECTION_COLOR, top_categories_color_hex)
        self.assertEqual(TOP_SECTION_ICON_COLOR, top_categories_icon_color_hex)

    def test__when_total_top_categories_count_match__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        driver.maximize_window()
        time.sleep(DELAY_SHORT)
        top_categories_count = len(driver.find_elements_by_xpath('//*[@id="category-list"]/li'))
        self.assertEqual(TOP_CATEGORIES_COUNT, str(top_categories_count))
        ### CATEGORY JOB LIST NEED TO BE CHANGED AS JOBb PAGE AFTER MODIFICATION
        # categories_list = []
        # for category in range(1, top_categories_count + 1):
        #     categories = driver.find_element_by_xpath(
        #         '//*[@id="category-list"]/li[' + category + ']/a').text
        #     categories_list.append(categories)
        # self.assertEqual(JOB_CATEGORIES_LIST, categories_list)
        # self.assertEqual(top_categories_count, len(categories_list))

    def test__when_click_on_top_categories_if_valid__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        top_categories_one = driver.find_element_by_xpath('//*[@id="category-list"]/li[1]/a')
        try:
            top_categories_one.click()
            time.sleep(DELAY_SHORT)
            total_jobs_text = driver.find_element_by_xpath('//*[@id="jobs"]/div[1]/div[2]/span').text
            if TOP_CATEGORIES_SEARCH_VALUE != total_jobs_text and TOP_CATEGORIES_SEARCH_VALUE_1 != total_jobs_text:
                self.fail()
        except WebDriverException:
            self.fail("Fail")
        home = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[1]/a')
        home.click()
        time.sleep(DELAY_SHORT)

    def test__when_top_companies_title_and_icon_match__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        top_skills = driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[2]/div/div[1]/h5')
        top_skills_title = top_skills.text
        top_skills_title_color = top_skills.value_of_css_property('color')
        top_skills_title_color_hex = Color.from_string(top_skills_title_color).hex
        top_skills_icon = driver.find_element_by_class_name('fa-tools')
        top_skills_icon_color = top_skills_icon.value_of_css_property('color')
        top_skills_icon_color_hex = Color.from_string(top_skills_icon_color).hex
        underline = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/hr')
        underline_color = underline.value_of_css_property('border-top-color')
        self.assertIsNotNone(underline)
        self.assertEqual(underline_color, BORDER_TOP_COLOR)
        self.assertEqual(TOP_SKILLS_TITLE, top_skills_title)
        self.assertEqual(TOP_SECTION_COLOR, top_skills_title_color_hex)
        self.assertIsNotNone(top_skills_icon)
        self.assertEqual(TOP_SECTION_ICON_COLOR, top_skills_icon_color_hex)

    def test__when_total_top_skills_count_match__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        driver.maximize_window()
        time.sleep(DELAY_SHORT)
        top_skills_count = len(driver.find_elements_by_xpath(
            '//*[@id="skill-list"]/li'))
        self.assertEqual(TOP_SKILLS_COUNT, str(top_skills_count))
        # skill_list = []
        # for skill in range(1, top_skills_count + 1):
        #     skills = driver.find_element_by_xpath(
        #         '//*[@id="skill-list"]/li[' + skill + ']/a').text
        #     skill_list.append(skills)
        # self.assertEqual(SKILLS_LIST, skill_list)
        # self.assertEqual(top_skills_count, len(skill_list))

    def test__when_click_on_top_skills_if_valid__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        top_skills_one = driver.find_element_by_xpath('//*[@id="skill-list"]/li[1]/a')
        try:
            top_skills_one.click()
            time.sleep(DELAY_SHORT)
            total_jobs_text = driver.find_element_by_xpath('//*[@id="jobs"]/div[1]/div[2]/span').text
            if TOP_SKILLS_SARCH_VALUE != total_jobs_text and TOP_SKILLS_SARCH_VALUE_1 != total_jobs_text:
                self.fail()
        except WebDriverException:
            self.fail("Fail")
        home = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[1]/a')
        home.click()
        time.sleep(DELAY_SHORT)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


class TestRecentJobsSection(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = webdriver.WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        time.sleep(DELAY_SHORT)

    def test__when_recent_jobs_title_and_underline_exist__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        recent_job = driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/h2')
        recent_job_title = recent_job.text
        recent_job_title_color = recent_job.value_of_css_property('color')
        recent_job_title_color_hex = Color.from_string(recent_job_title_color).hex
        recent_job_underline = driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/span')
        recent_job_underline_color = recent_job_underline.value_of_css_property('border-top-color')
        self.assertIsNotNone(recent_job)
        self.assertEqual(RECENT_JOBS_TITLE, recent_job_title)
        self.assertIsNotNone(recent_job_underline)
        self.assertEqual(BORDER_TOP_COLOR, recent_job_underline_color)
        self.assertEqual(BLACK_HEADING_COLOR, recent_job_title_color_hex)

    def test__when_recent_jobs_count_match__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        recent_jobs_count = len(driver.find_elements_by_class_name('job-title'))
        job_list = len(driver.find_elements_by_class_name('job-title'))
        recent_jobs_list = []
        for i in range(2, job_list + 2):
            recent_job_title = driver.find_element_by_xpath('//*[@id="job-list"]/div[' + str(i) + ']/div[2]/div[1]/h4/a')
            recent_job_title_text = recent_job_title.text
            recent_jobs_list.append(recent_job_title_text)
            recent_job_image = driver.find_element_by_xpath('//*[@id="job-list"]/div[' + str(i) + ']/div[1]/a/img')
            recent_job_location = driver.find_element_by_xpath('//*[@id="job-list"]/div[' + str(i) + ']/div[2]/div[1]/div/span[1]/a')
            recent_job_type = driver.find_element_by_xpath('//*[@id="job-list"]/div[' + str(i) + ']/div[2]/div[1]/div/span[3]/a/span')
            recent_job_deadline = driver.find_element_by_xpath('//*[@id="job-list"]/div[' + str(i) + ']/div[2]/div[2]/p')
            self.assertIsNotNone(recent_job_title)
            self.assertIsNotNone(recent_job_image)
            self.assertIsNotNone(recent_job_location)
            self.assertIsNotNone(recent_job_type)
            self.assertIsNotNone(recent_job_deadline)
        if RECENT_JOBS_LIST != recent_jobs_list and RECENT_JOBS_LIST_1 != recent_jobs_list and RECENT_JOBS_LIST_2 != recent_jobs_list:
            self.fail()
        if RECENT_JOBS_COUNT != str(recent_jobs_count):
            self.fail()

    # def test__when_fav_valid__should_pass(self):
    #     time.sleep(DELAY_LONG)
    #     fav_btn = driver.find_element_by_xpath('//*[@id="job-list"]/div[2]/div[2]/div[2]/div/a[2]')
    #     try:
    #         fav_btn.click()
    #         time.sleep(DELAY_SHORT)
    #         sign_in = driver.find_element_by_xpath('/html/body/div[10]/div/div[3]/button[1]')
    #         sign_in.click()
    #         time.sleep(DELAY_SHORT)
    #         email = driver.find_element_by_id('email')
    #         email.clear()
    #         email.send_keys(VALID_PRO_USERNAME)
    #         password = driver.find_element_by_name('password')
    #         password.clear()
    #         password.send_keys(VALID_PRO_PASSWORD)
    #         submit_btn = driver.find_element_by_id('signinButton')
    #         submit_btn.click()
    #         time.sleep(DELAY_LONG)
    #         fav_jobs = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div[3]/ul/li[4]/a')
    #         fav_jobs.click()
    #         time.sleep(DELAY_LONG)
    #         total_jobs = driver.find_element_by_xpath('//*[@id="jobs"]/h4').text
    #         public = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[1]/a')
    #         public.click()
    #         self.assertNotEqual(total_jobs, '0 Job(s)')
    #     except WebDriverException:
    #         self.fail()
    #     public = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[1]/a')
    #     public.click()
    #     time.sleep(DELAY_SHORT)

    def test__when_browse_all_is_valid__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        browse_all_btn = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/a')
        browse_all_btn_color = browse_all_btn.value_of_css_property('background-color')
        browse_all_btn_color_hex = Color.from_string(browse_all_btn_color).hex
        self.assertIsNotNone(browse_all_btn)
        self.assertEqual(YELLOW_COLOR_HEX, browse_all_btn_color_hex)
        try:
            browse_all_btn.click()
            time.sleep(DELAY_SHORT)
        except WebDriverException:
            self.fail("Not Click able")
        driver.back()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


class TestFeaturedCompaniesSection(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = webdriver.WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        time.sleep(DELAY_SHORT)

    def test__when_featured_company_valid__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        featured_companies_title = driver.find_element_by_xpath('//*[@id="featured-companies"]/div[1]/div/div/h2')
        featured_companies_title_text = featured_companies_title.text
        featured_companies_title_text_color = featured_companies_title.value_of_css_property('color')
        featured_companies_title_color_hex = Color.from_string(featured_companies_title_text_color).hex
        underline = driver.find_element_by_xpath('//*[@id="featured-companies"]/div[1]/div/div/span')
        underline_color = underline.value_of_css_property('border-top-color')
        underline_color_hex = Color.from_string(underline_color).hex
        featured_company_count = len(driver.find_elements_by_class_name('featured-company-list'))
        featured_company_one_image = driver.find_element_by_xpath(
            '//*[@id="featured-companies"]/div[3]/div[2]/div/div[1]/a/img')
        feather_map_pin = driver.find_element_by_class_name('feather-map-pin')
        featured_company_location = driver.find_element_by_xpath(
            '//*[@id="featured-companies"]/div[3]/div[2]/div/div[2]/div/div/span/a').text
        self.assertIsNotNone(featured_companies_title)
        self.assertEqual(FEATURED_COMPANIES_TITLE, featured_companies_title_text)
        self.assertEqual(BLACK_HEADING_COLOR, featured_companies_title_color_hex)
        self.assertIsNotNone(underline)
        self.assertEqual(YELLOW_COLOR_HEX, underline_color_hex)
        self.assertEqual(MIN_FEATURED_COMPANY, featured_company_count)
        self.assertIsNotNone(featured_company_one_image)
        self.assertIsNotNone(feather_map_pin)
        self.assertEqual(FEATURED_COMPANY_LOCATION, featured_company_location)

    def test__when_click_on_featured_company_if_valid__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        titles = []
        locations = []
        job_count_list = []
        featured_company_list = driver.find_elements_by_css_selector('.job-list.featured-company-list')
        for featured_company in featured_company_list:
            title = featured_company.find_element_by_tag_name('h4').text
            location = featured_company.find_element_by_class_name('info').text
            job_count = featured_company.find_element_by_css_selector('.button.btn-yellow').text
            time.sleep(1)
            titles.append(title)
            locations.append(location)
            job_count_list.append(job_count)
            time.sleep(1)
            title_link = featured_company.find_element_by_tag_name('h4')
            title_link.click()
            time.sleep(DELAY_LONG)
            title_single_job = driver.find_element_by_xpath('//*[@id="name"]').text
            time.sleep(1)
            if title != title_single_job:
                self.fail()
            else:
                break


    def test__featured_company_if_valid__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        titles = []
        locations = []
        job_count_list = []
        featured_company_list = driver.find_elements_by_css_selector('.job-list.featured-company-list')
        for featured_company in featured_company_list:
            title = featured_company.find_element_by_tag_name('h4').text
            location = featured_company.find_element_by_class_name('info').text
            job_count = featured_company.find_element_by_css_selector('.button.btn-yellow').text
            time.sleep(1)
            titles.append(title)
            locations.append(location)
            job_count_list.append(job_count)
        time.sleep(1)
        if titles != FEATURED_COMPANY_TITLE_LIST and locations != FEATURED_COMPANY_LOCATION_LIST and job_count_list != FEATURED_COMPANY_JOB_COUNT_LIST:
            self.fail()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


class TestVitalStatsSection(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = webdriver.WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        time.sleep(DELAY_SHORT)

    def test__when_vital_stats_valid__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        vital_stat_section = driver.find_element_by_class_name('bg-vital-stats')
        vital_stat_section_bg_color = vital_stat_section.value_of_css_property('background-color')
        vital_stat_section_bg_color_hex = Color.from_string(vital_stat_section_bg_color).hex
        vital_stat_section_bg_image = driver.find_element_by_class_name('vital-stats').value_of_css_property(
            'background-image')
        fa_briefcase = driver.find_element_by_class_name('fa-briefcase')
        fa_briefcase_color = fa_briefcase.value_of_css_property('color')
        fa_briefcase_color_hex = Color.from_string(fa_briefcase_color).hex
        # fa_briefcase_font_family = fa_briefcase.value_of_css_property('font-family')
        # fa_briefcase_font_weight = fa_briefcase.value_of_css_property('font-weight')
        # fa_briefcase_font_size = fa_briefcase.value_of_css_property('font-size')
        job_count = driver.find_element_by_id('job_counts')
        job_count_num = job_count.text
        job_count_color = job_count.value_of_css_property('color')
        job_count_color_hex = Color.from_string(job_count_color).hex
        open_jobs_text = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[1]/div/p[2]').text
        fa_users_cog = driver.find_element_by_class_name('fa-users-cog')
        vacancy_count = driver.find_element_by_id('vacancy_count')
        vacancy_count_num = vacancy_count.text
        pro_text = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/p[2]').text
        fa_tools = driver.find_element_by_class_name('fa-tools')
        skill_count = driver.find_element_by_id('skill_count')
        skill_count_num = skill_count.text
        skill_text = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/div/p[2]').text
        fa_building = driver.find_element_by_class_name('fa-building')
        companies_count = driver.find_element_by_id('companies_count')
        companies_count_num = companies_count.text
        companies_text = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[4]/div/p[2]').text
        self.assertIsNotNone(vital_stat_section)
        self.assertEqual(BLACK_HEX, vital_stat_section_bg_color_hex)
        self.assertIsNotNone(fa_briefcase)
        self.assertEqual(YELLOW_COLOR_HEX, fa_briefcase_color_hex)
        self.assertEqual(OPEN_JOBS_TEXT, open_jobs_text)
        if OPEN_JOBS_COUNT != job_count_num and OPEN_JOBS_COUNT_1 != job_count_num and OPEN_JOBS_COUNT_2 != job_count_num:
            self.fail()
        self.assertEqual(HOMEPAGE_TITLE_COLOR, job_count_color_hex)
        self.assertIsNotNone(fa_users_cog)
        if VACANCY_COUNT != vacancy_count_num and VACANCY_COUNT_1 != vacancy_count_num:
            self.fail()
        self.assertEqual(VACANCY_TEXT, pro_text)
        self.assertIsNotNone(fa_tools)
        if SKILLS_COUNT != skill_count_num and SKILLS_COUNT_1 != skill_count_num:
            self.fail()
        self.assertEqual(SKILLS_TEXT, skill_text)
        self.assertIsNotNone(fa_building)
        if COMPANIES_COUNT != companies_count_num and COMPANIES_COUNT_1 != companies_count_num:
            self.fail()
        self.assertEqual(COMPANIES_TEXT, companies_text)
        self.assertIsNotNone(vital_stat_section_bg_image)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


class TestCareerAdviceSection(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = webdriver.WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        time.sleep(DELAY_SHORT)

    def test__when_career_advice_valid__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        career_advice = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div/div/h2')
        career_advice_text = career_advice.text
        career_advice_color = career_advice.value_of_css_property('color')
        career_advice_color_hex = Color.from_string(career_advice_color).hex
        underline = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div/div/span')
        underline_color = underline.value_of_css_property('border-top-color')
        underline_color_hex = Color.from_string(underline_color).hex
        career_advice_title = driver.find_element_by_xpath('//*[@id="career-advice"]/div[1]/article/div[2]/h3')
        career_advice_image = driver.find_element_by_xpath('//*[@id="career-advice"]/div[1]/article/div[1]/img')
        career_advice_image_src = career_advice_image.get_attribute('src')
        self.assertEqual(career_advice_image_src, CAREER_ADVICE_ONE_IMAGE_SRC)
        career_advice_title_text = career_advice_title.text
        author_name = driver.find_element_by_xpath('//*[@id="ad-author"]').text
        user_icon = driver.find_element_by_class_name('feather-user')
        date_and_day = driver.find_element_by_xpath('//*[@id="career-advice"]/div[1]/article/div[2]/span[2]').text
        career_advice_paragraph = driver.find_element_by_xpath('//*[@id="ad-description"]').text
        self.assertIsNotNone(career_advice)
        self.assertEqual(CAREER_ADVICE_TEXT, career_advice_text)
        self.assertEqual(BLACK_HEADING_COLOR, career_advice_color_hex)
        self.assertIsNotNone(underline)
        self.assertEqual(YELLOW_COLOR_HEX, underline_color_hex)
        self.assertIsNotNone(career_advice_image)
        self.assertEqual(CAREER_ADVICE_TITLE_ONE, career_advice_title_text)
        self.assertEqual(CAREER_ADVICE_ONE_AUTHOR_NAME, author_name)
        self.assertIsNotNone(user_icon)
        self.assertEqual(DATE_AND_DAY, date_and_day)
        self.assertEqual(CAREER_ADVICE_DESCRIPTION_ONE, career_advice_paragraph)

    def test__when_click_on_career_advice_valid__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        career_advice_one = driver.find_element_by_xpath('//*[@id="career-advice"]/div[1]/article/div[1]/div/a')
        try:
            career_advice_one.click()
            time.sleep(DELAY_SHORT)
            title = driver.find_element_by_tag_name('h3').text
            self.assertEqual(title, CAREER_ADVICE_TITLE_ONE)
        except WebDriverException:
            self.fail("Fail")
        home = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[1]/a')
        home.click()
        time.sleep(DELAY_SHORT)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


class TestAppSection(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = webdriver.WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        time.sleep(DELAY_SHORT)

    def test__when_app_section_valid__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        app_banner_h2 = driver.find_element_by_xpath('/html/body/div[7]/div/div/div[1]/div/h2')
        app_banner_text = app_banner_h2.text
        app_banner_paragraph = driver.find_element_by_xpath('/html/body/div[7]/div/div/div[1]/div/p').text
        app_banner_h2_color = app_banner_h2.value_of_css_property('color')
        app_banner_h2_color_hex = Color.from_string(app_banner_h2_color).hex
        app_image = driver.find_element_by_class_name('app_image')
        android_app_image = driver.find_element_by_class_name('android-app')
        apple_app_image = driver.find_element_by_class_name('apple-app')
        banner_bg_image = driver.find_element_by_class_name('jobxprss-app').value_of_css_property(
            'background-image')
        self.assertEqual(APP_BANNER_TEXT, app_banner_text)
        self.assertEqual(APP_BANNER_PARAGRAPH, app_banner_paragraph)
        self.assertEqual(BLACK_HEX, app_banner_h2_color_hex)
        self.assertIsNotNone(app_image)
        self.assertIsNotNone(android_app_image)
        self.assertIsNotNone(apple_app_image)
        self.assertIsNotNone(banner_bg_image)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


class TestFooterSection(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = webdriver.WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        time.sleep(DELAY_SHORT)

        # Footer for Anonymous User

    def test__when_footer_valid_for_anonymous__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        driver.delete_all_cookies()
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        driver.execute_script("window.scrollTo(0, 3000)")
        footer_social = driver.find_element_by_class_name('footer-social')
        self.assertIsNotNone(footer_social)
        fluid_logo = driver.find_element_by_xpath('/html/body/footer/div[1]/div/div/div[1]/div/a')
        border_yellow = driver.find_element_by_class_name('border-yellow')
        border_yellow_color = border_yellow.value_of_css_property('border-top-color')
        border_yellow_col_hex = Color.from_string(border_yellow_color).hex
        self.assertIsNotNone(border_yellow)
        self.assertEqual(YELLOW_COLOR_HEX, border_yellow_col_hex)
        first_footer_section = driver.find_element_by_xpath('/html/body/footer/div[2]/div/div/div[1]/div/h4')
        first_footer_section_title = first_footer_section.text
        first_footer_section_title_color = first_footer_section.value_of_css_property('color')
        first_footer_section_title_color_hex = Color.from_string(first_footer_section_title_color).hex
        self.assertEqual(FIRST_FOOTER_SECTION_TITLE, first_footer_section_title)
        self.assertEqual(YELLOW_COLOR_HEX, first_footer_section_title_color_hex)
        second_footer_section_title = driver.find_element_by_xpath('/html/body/footer/div[2]/div/div/div[2]/div/h4').text
        self.assertEqual(SECOND_FOOTER_SECTION_TITLE, second_footer_section_title)
        third_footer_section_title = driver.find_element_by_xpath('/html/body/footer/div[2]/div/div/div[3]/div/h4').text
        self.assertEqual(THIRD_FOOTER_SECTION_TITLE, third_footer_section_title)
        fourth_footer_section_title = driver.find_element_by_xpath('/html/body/footer/div[2]/div/div/div[4]/div/div/h4').text
        self.assertEqual(FOURTH_FOOTER_SECTION_TITLE, fourth_footer_section_title)
        fifth_footer_section_title = driver.find_element_by_xpath('/html/body/footer/div[2]/div/div/div[5]/div/h4[1]').text
        self.assertEqual(FIFTH_FOOTER_SECTION_TITLE, fifth_footer_section_title)
        address = driver.find_element_by_xpath('/html/body/footer/div[2]/div/div/div[4]/div/div/address').text
        self.assertEqual(ADDRESS, address)
        try:
            fluid_logo.click()
        except WebDriverException:
            self.fail("Logo not Click able")
        driver.back()
        self.driver.get(self.url)
        driver.maximize_window()
        facebook = driver.find_element_by_xpath('/html/body/footer/div[1]/div/div/div[2]/div/a[1]')
        facebook_url = facebook.get_attribute('href')
        facebook_color = driver.find_element_by_xpath('/html/body/footer/div[1]/div/div/div[2]/div/a[1]/i').value_of_css_property('color')
        facebook_color_hex = Color.from_string(facebook_color).hex
        self.assertEqual(FACEBOOK_URL, facebook_url)
        self.assertEqual(YELLOW_COLOR_HEX, facebook_color_hex)
        try:
            facebook.click()
        except WebDriverException:
            self.fail("Facebook Not click able")
        self.driver.get(self.url)
        time.sleep(DELAY_SHORT)
        twitter = driver.find_element_by_xpath('/html/body/footer/div[1]/div/div/div[2]/div/a[3]')
        twitter_url = twitter.get_attribute('href')
        self.assertEqual(TWITTER_URL, twitter_url)
        try:
            twitter.click()
        except WebDriverException:
            self.fail("Twitter Not click able")
        self.driver.get(self.url)
        time.sleep(DELAY_SHORT)
        linkedin = driver.find_element_by_xpath('/html/body/footer/div[1]/div/div/div[2]/div/a[2]')
        linkedin_url = linkedin.get_attribute('href')
        self.assertEqual(LINKEDIN_URL, linkedin_url)
        try:
            linkedin.click()
        except WebDriverException:
            self.fail("Linkedin Not click able")
        self.driver.get(self.url)
        time.sleep(DELAY_SHORT)
        about_us = driver.find_element_by_xpath('/html/body/footer/div[2]/div/div/div[1]/div/div/ul/li[1]/a')
        self.assertIsNotNone(about_us)
        try:
            about_us.click()
        except WebDriverException:
            self.fail("about us not click able")
        driver.back()
        contact_us = driver.find_element_by_xpath('/html/body/footer/div[2]/div/div/div[1]/div/div/ul/li[2]/a')
        self.assertIsNotNone(contact_us)
        try:
            contact_us.click()
        except WebDriverException:
            self.fail("contact us not click able")
        driver.back()
        time.sleep(DELAY_SHORT)
        privacy_policy = driver.find_element_by_xpath(
            '/html/body/footer/div[2]/div/div/div[1]/div/div/ul/li[3]/a')
        self.assertIsNotNone(privacy_policy)
        try:
            privacy_policy.click()
        except WebDriverException:
            self.fail("privacy policy not click able")
        driver.back()
        time.sleep(DELAY_SHORT)
        terms_and_condition = driver.find_element_by_xpath(
            '/html/body/footer/div[2]/div/div/div[1]/div/div/ul/li[4]/a')
        self.assertIsNotNone(terms_and_condition)
        try:
            terms_and_condition.click()
        except WebDriverException:
            self.fail("terms and condition not click able")
        driver.back()
        time.sleep(DELAY_SHORT)
        create_account = driver.find_element_by_link_text('Create Account')
        self.assertIsNotNone(create_account)
        try:
            create_account.click()
            time.sleep(DELAY_SHORT)
            current_url = self.driver.current_url
            self.assertEqual(PROF_REGISTER_URL + '/', current_url)
        except WebDriverException:
            self.fail("Create Account is not click able")
        driver.back()
        time.sleep(DELAY_SHORT)
        career_advice = driver.find_element_by_xpath(
            '/html/body/footer/div[2]/div/div/div[2]/div/div/ul/li[2]/a')
        self.assertIsNotNone(career_advice)
        try:
            career_advice.click()
        except WebDriverException:
            self.fail("Career advice is not click able")
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        faq = driver.find_element_by_link_text('FAQ')
        self.assertIsNotNone(faq)
        try:
            faq.click()
        except WebDriverException:
            self.fail("faq is not click able")
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        company_signin = driver.find_element_by_id('company_sign')
        self.assertIsNotNone(company_signin)
        try:
            company_signin.click()
        except WebDriverException:
            self.fail('company sign in not click able')
        driver.back()
        self.driver.get(self.url)
        driver.maximize_window()
        time.sleep(DELAY_SHORT)
        request_for_access = driver.find_element_by_id('request_for_access')
        self.assertIsNotNone(request_for_access)
        try:
            request_for_access.click()
        except WebDriverException:
            self.fail("Not Click able")
        time.sleep(DELAY_SHORT)
        sub_input_field = driver.find_element_by_id('email')
        sub_input_field.send_keys(VALID_PRO_USERNAME)
        time.sleep(1)
        paper_plane_btn = driver.find_element_by_xpath('//*[@id="job-alert"]/div/div')
        try:
            paper_plane_btn.click()
        except WebDriverException:
            self.fail("subscribe btn not click able")
        driver.back()
        time.sleep(DELAY_LONG)
        paper_plane_icon = driver.find_element_by_xpath('//*[@id="job-alert"]/div/div/button/i')
        self.assertIsNotNone(paper_plane_icon)
        powered_by = driver.find_element_by_xpath(
            '/html/body/footer/div[3]/div/div/div/div/div/div[1]/p/span').text
        self.assertEqual("Powered By", powered_by)
        ishraak_logo = driver.find_element_by_xpath(
            '/html/body/footer/div[3]/div/div/div/div/div/div[1]/p/a/img')
        self.assertIsNotNone(ishraak_logo)
        ishraak = driver.find_element_by_xpath('/html/body/footer/div[3]/div/div/div/div/div/div[1]/p/a')
        ishraak_url = ishraak.get_attribute('href')
        self.assertEqual(IHSRAAK_WEBSITE, ishraak_url)
        copyright_text = driver.find_element_by_class_name('copyright-text').text
        self.assertEqual(COPYRIGHT_TEXT, copyright_text)
        back_to_top = driver.find_element_by_xpath('/html/body/footer/div[3]/div/div/div/div/div/div[2]/div/a')
        self.assertIsNotNone(back_to_top)
        try:
            back_to_top.click()
        except WebDriverException:
            self.fail("Not Click able")
        driver.back()
        self.driver.get(self.url)
        driver.maximize_window()
        time.sleep(DELAY_SHORT)

        # Footer for Pro User

    #
    # def test__when_footer_valid_for_pro__should_pass(self):
    #     driver = self.driver
    #     driver.get(MAIN_URL_HOME)
    #     driver.delete_all_cookies()
    #     driver.get(MAIN_URL_HOME)
    #     time.sleep(DELAY_SHORT)
    #     data = {
    #         "email": VALID_PRO_USERNAME,
    #         "password": VALID_PRO_PASSWORD
    #
    #     }
    #     signin_helper(driver, data)
    #
    #     driver.get(MAIN_URL_HOME)
    #     time.sleep(DELAY_LONG)
    #     driver.execute_script("window.scrollTo(0, 3000)")
    #     footer_social = driver.find_element_by_class_name('footer-social')
    #     self.assertIsNotNone(footer_social)
    #     fluid_logo = driver.find_element_by_xpath('/html/body/footer/div[1]/div/div/div[1]/div/a/img')
    #     border_yellow = driver.find_element_by_class_name('border-yellow')
    #     border_yellow_color = border_yellow.value_of_css_property('border-top-color')
    #     border_yellow_col_hex = Color.from_string(border_yellow_color).hex
    #     self.assertIsNotNone(border_yellow)
    #     self.assertEqual(YELLOW_COLOR_HEX, border_yellow_col_hex)
    #     first_footer_section = driver.find_element_by_xpath('/html/body/footer/div[2]/div/div/div[1]/div/h4')
    #     first_footer_section_title = first_footer_section.text
    #     first_footer_section_title_color = first_footer_section.value_of_css_property('color')
    #     first_footer_section_title_color_hex = Color.from_string(first_footer_section_title_color).hex
    #     self.assertEqual(FIRST_FOOTER_SECTION_TITLE, first_footer_section_title)
    #     self.assertEqual(YELLOW_COLOR_HEX, first_footer_section_title_color_hex)
    #     second_footer_section_title = driver.find_element_by_xpath('/html/body/footer/div[2]/div/div/div[2]/div/h4').text
    #     if SECOND_FOOTER_SECTION_TITLE != second_footer_section_title and THIRD_FOOTER_SECTION_TITLE != second_footer_section_title:
    #         self.fail()
    #     third_footer_section_title = driver.find_element_by_xpath('/html/body/footer/div[2]/div/div/div[3]/div/div/h4').text
    #     if THIRD_FOOTER_SECTION_TITLE != third_footer_section_title and FOURTH_FOOTER_SECTION_TITLE != third_footer_section_title:
    #         self.fail()
    #     fourth_footer_section_title = driver.find_element_by_xpath('/html/body/footer/div[2]/div/div/div[4]/div/h4').text
    #     if FOURTH_FOOTER_SECTION_TITLE != fourth_footer_section_title and FIFTH_FOOTER_SECTION_TITLE != fourth_footer_section_title:
    #         self.fail()
    #     address = driver.find_element_by_xpath('/html/body/footer/div[2]/div/div/div[3]/div/div/address').text
    #     self.assertEqual(ADDRESS, address)
    #     try:
    #         fluid_logo.click()
    #     except WebDriverException:
    #         self.fail("Logo not Click able")
    #     driver.get(MAIN_URL_HOME)
    #     driver.maximize_window()
    #     time.sleep(DELAY_SHORT)
    #     facebook = driver.find_element_by_xpath('/html/body/footer/div[1]/div/div/div[2]/div/a[1]')
    #     facebook_url = facebook.get_attribute('href')
    #     facebook_color = driver.find_element_by_xpath(
    #         '/html/body/footer/div[1]/div/div/div[2]/div/a[1]/i').value_of_css_property('color')
    #     facebook_color_hex = Color.from_string(facebook_color).hex
    #     self.assertEqual(FACEBOOK_URL, facebook_url)
    #     self.assertEqual(YELLOW_COLOR_HEX, facebook_color_hex)
    #     try:
    #         facebook.click()
    #     except WebDriverException:
    #         self.fail("Facebook Not click able")
    #     driver.get(MAIN_URL_HOME)
    #     time.sleep(DELAY_SHORT)
    #     twitter = driver.find_element_by_xpath('/html/body/footer/div[1]/div/div/div[2]/div/a[3]')
    #     twitter_url = twitter.get_attribute('href')
    #     self.assertEqual(TWITTER_URL, twitter_url)
    #     try:
    #         twitter.click()
    #     except WebDriverException:
    #         self.fail("Twitter Not click able")
    #     driver.get(MAIN_URL_HOME)
    #     time.sleep(DELAY_SHORT)
    #     linkedin = driver.find_element_by_xpath('/html/body/footer/div[1]/div/div/div[2]/div/a[2]')
    #     linkedin_url = linkedin.get_attribute('href')
    #     self.assertEqual(LINKEDIN_URL, linkedin_url)
    #     try:
    #         linkedin.click()
    #     except WebDriverException:
    #         self.fail("Linkedin Not click able")
    #     driver.get(MAIN_URL_HOME)
    #     time.sleep(DELAY_SHORT)
    #     about_us = driver.find_element_by_xpath('/html/body/footer/div[2]/div/div/div[1]/div/div/ul/li[1]/a')
    #     self.assertIsNotNone(about_us)
    #     try:
    #         about_us.click()
    #     except WebDriverException:
    #         self.fail("about us not click able")
    #     driver.back()
    #     contact_us = driver.find_element_by_xpath('/html/body/footer/div[2]/div/div/div[1]/div/div/ul/li[2]/a')
    #     self.assertIsNotNone(contact_us)
    #     try:
    #         contact_us.click()
    #     except WebDriverException:
    #         self.fail("contact us not click able")
    #     driver.back()
    #     time.sleep(DELAY_SHORT)
    #     privacy_policy = driver.find_element_by_xpath(
    #         '/html/body/footer/div[2]/div/div/div[1]/div/div/ul/li[3]/a')
    #     self.assertIsNotNone(privacy_policy)
    #     try:
    #         privacy_policy.click()
    #     except WebDriverException:
    #         self.fail("privacy policy not click able")
    #     driver.back()
    #     time.sleep(DELAY_SHORT)
    #     terms_and_condition = driver.find_element_by_xpath(
    #         '/html/body/footer/div[2]/div/div/div[1]/div/div/ul/li[4]/a')
    #     self.assertIsNotNone(terms_and_condition)
    #     try:
    #         terms_and_condition.click()
    #     except WebDriverException:
    #         self.fail("terms and condition not click able")
    #     driver.back()
    #     time.sleep(DELAY_SHORT)
    #     create_account = driver.find_element_by_xpath('/html/body/footer/div[2]/div/div/div[2]/div/div/ul/li[1]/a')
    #     self.assertIsNotNone(create_account)
    #     try:
    #         create_account.click()
    #         time.sleep(DELAY_SHORT)
    #         current_url = self.driver.current_url
    #         self.assertEqual(PROF_REGISTER_URL + '/', current_url)
    #     except WebDriverException:
    #         self.fail("Create Account is not click able")
    #     driver.back()
    #     time.sleep(DELAY_SHORT)
    #     career_advice = driver.find_element_by_xpath('/html/body/footer/div[2]/div/div/div[2]/div/div/ul/li[2]/a')
    #     self.assertIsNotNone(career_advice)
    #     try:
    #         career_advice.click()
    #     except WebDriverException:
    #         self.fail("Career advice is not click able")
    #     driver.get(MAIN_URL_HOME)
    #     time.sleep(DELAY_SHORT)
    #     faq = driver.find_element_by_link_text('FAQ')
    #     self.assertIsNotNone(faq)
    #     try:
    #         faq.click()
    #     except WebDriverException:
    #         self.fail("faq is not click able")
    #     driver.get(MAIN_URL_HOME)
    #     time.sleep(DELAY_SHORT)
    #     self.driver.get(self.url)
    #     driver.maximize_window()
    #     time.sleep(DELAY_SHORT)
    #     try:
    #         subscribe_alert = driver.find_element_by_id('alert-msg').text
    #         time.sleep(1)
    #     except:
    #         subscribe_btn = driver.find_element_by_xpath('//*[@id="job-alert"]/button')
    #         subscribe_btn_text = subscribe_btn.text
    #         subscribe_btn_bg_color = subscribe_btn.value_of_css_property('background-color')
    #         subscribe_btn_bg_color_hex = Color.from_string(subscribe_btn_bg_color).hex
    #         subscribe_btn_border_color = subscribe_btn.value_of_css_property('border-top-color')
    #         subscribe_btn_border_color_hex = Color.from_string(subscribe_btn_border_color).hex
    #         if JOB_ALERT_BTN_NAME != subscribe_btn_text and JOB_ALERT_BTN_NAME_2 != subscribe_btn_text and JOB_ALERT_BTN_NULL_FOR_PRO_LOGIN != subscribe_btn_text:
    #             self.fail()
    #         self.assertEqual(YELLOW_COLOR_HEX, subscribe_btn_bg_color_hex)
    #         self.assertEqual(YELLOW_COLOR_HEX, subscribe_btn_border_color_hex)
    #         try:
    #             subscribe_btn.click()
    #             time.sleep(DELAY_SHORT)
    #             alert_msg = driver.find_element_by_id('alert-msg').text
    #             self.assertEqual(JOB_ALERT_SUCCSS_MSG, alert_msg)
    #             if subscribe_btn.is_displayed():
    #                 self.fail()
    #         except WebDriverException:
    #             self.fail("Not ok")
    #
    #     powered_by = driver.find_element_by_xpath('/html/body/footer/div[3]/div/div/div/div/div/div[1]/p/span').text
    #     self.assertEqual("Powered By", powered_by)
    #     ishraak_logo = driver.find_element_by_xpath('/html/body/footer/div[3]/div/div/div/div/div/div[1]/p/a/img')
    #     self.assertIsNotNone(ishraak_logo)
    #     ishraak = driver.find_element_by_xpath('/html/body/footer/div[3]/div/div/div/div/div/div[1]/p/a')
    #     ishraak_url = ishraak.get_attribute('href')
    #     self.assertEqual(IHSRAAK_WEBSITE, ishraak_url)
    #     copyright_text = driver.find_element_by_class_name('copyright-text').text
    #     self.assertEqual(COPYRIGHT_TEXT, copyright_text)
    #     back_to_top = driver.find_element_by_xpath('/html/body/footer/div[3]/div/div/div/div/div/div[2]/div/a')
    #     self.assertIsNotNone(back_to_top)
    #     try:
    #         back_to_top.click()
    #     except WebDriverException:
    #         self.fail("Not Click able")
    #     driver.back()
    #     self.driver.get(self.url)
    #     driver.maximize_window()
    #     time.sleep(DELAY_SHORT)
    #     toogle = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[6]/button')
    #     toogle.click()
    #     sign_out = driver.find_element_by_xpath('//*[@id="userNavbarMain"]/ul/li[3]/a')
    #     ActionChains(self.driver).move_to_element_with_offset(sign_out, 5, 15).click().perform()
    #     time.sleep(DELAY_SHORT)
    #     driver.delete_all_cookies()
    #     driver.get(self.url)
    #     driver.maximize_window()
    #     time.sleep(DELAY_LONG)
    # #
    # # def test__when_footer_valid_for_company__should_pass(self):
    # #     driver = self.driver
    # #     driver.get(MAIN_URL_HOME)
    # #     driver.delete_all_cookies()
    # #     driver.get(MAIN_URL_HOME)
    # #     time.sleep(DELAY_SHORT)
    # #     driver = self.driver
    # #     data = {
    # #         "email": VALID_COM_USERNAME,
    # #         "password": VALID_COM_PASSWORD
    # #
    # #     }
    # #     signin_helper_company(driver, data)
    # #     driver.get(MAIN_URL)
    # #     time.sleep(DELAY_LONG)
    # #     time.sleep(DELAY_SHORT)
    # #     driver.execute_script("window.scrollTo(0, 3000)")
    # #     footer_social = driver.find_element_by_class_name('footer-social')
    # #     self.assertIsNotNone(footer_social)
    # #     fluid_logo = driver.find_element_by_xpath('/html/body/footer/div[1]/div/div/div[1]/div/a/img')
    # #     first_footer_section = driver.find_element_by_xpath('/html/body/footer/div[2]/div/div/div[1]/div/h4')
    # #     first_footer_section_title = first_footer_section.text
    # #     first_footer_section_title_color = first_footer_section.value_of_css_property('color')
    # #     first_footer_section_title_color_hex = Color.from_string(first_footer_section_title_color).hex
    # #     self.assertEqual(FIRST_FOOTER_SECTION_TITLE, first_footer_section_title)
    # #     self.assertEqual(YELLOW_COLOR_HEX, first_footer_section_title_color_hex)
    # #     third_footer_section_title = driver.find_element_by_xpath('/html/body/footer/div[2]/div/div/div[2]/div/div/h4').text
    # #     self.assertEqual(FOURTH_FOOTER_SECTION_TITLE, third_footer_section_title)
    # #     address = driver.find_element_by_xpath('/html/body/footer/div[2]/div/div/div[2]/div/div/address').text
    # #     self.assertEqual(ADDRESS, address)
    # #     try:
    # #         fluid_logo.click()
    # #     except WebDriverException:
    # #         self.fail("Logo not Click able")
    # #     driver.get(MAIN_URL_HOME)
    # #     driver.maximize_window()
    # #     time.sleep(1)
    # #     facebook = driver.find_element_by_xpath('/html/body/footer/div[1]/div/div/div[2]/div/a[1]')
    # #     facebook_url = facebook.get_attribute('href')
    # #     facebook_color = driver.find_element_by_xpath(
    # #         '/html/body/footer/div[1]/div/div/div[2]/div/a[1]/i').value_of_css_property('color')
    # #     facebook_color_hex = Color.from_string(facebook_color).hex
    # #     self.assertEqual(FACEBOOK_URL, facebook_url)
    # #     self.assertEqual(YELLOW_COLOR_HEX, facebook_color_hex)
    # #     try:
    # #         facebook.click()
    # #     except WebDriverException:
    # #         self.fail("Facebook Not click able")
    # #     driver.get(MAIN_URL_HOME)
    # #     time.sleep(DELAY_SHORT)
    # #     twitter = driver.find_element_by_xpath('/html/body/footer/div[1]/div/div/div[2]/div/a[3]')
    # #     twitter_url = twitter.get_attribute('href')
    # #     self.assertEqual(TWITTER_URL, twitter_url)
    # #     try:
    # #         twitter.click()
    # #     except WebDriverException:
    # #         self.fail("Twitter Not click able")
    # #     driver.get(MAIN_URL_HOME)
    # #     time.sleep(DELAY_SHORT)
    # #     linkedin = driver.find_element_by_xpath('/html/body/footer/div[1]/div/div/div[2]/div/a[2]')
    # #     linkedin_url = linkedin.get_attribute('href')
    # #     self.assertEqual(LINKEDIN_URL, linkedin_url)
    # #     try:
    # #         linkedin.click()
    # #     except WebDriverException:
    # #         self.fail("Linkedin Not click able")
    # #     driver.get(MAIN_URL_HOME)
    # #     time.sleep(DELAY_SHORT)
    # #     about_us = driver.find_element_by_xpath('/html/body/footer/div[2]/div/div/div[1]/div/div/ul/li[1]/a')
    # #     self.assertIsNotNone(about_us)
    # #     try:
    # #         about_us.click()
    # #     except WebDriverException:
    # #         self.fail("about us not click able")
    # #     driver.back()
    # #     contact_us = driver.find_element_by_xpath('/html/body/footer/div[2]/div/div/div[1]/div/div/ul/li[2]/a')
    # #     self.assertIsNotNone(contact_us)
    # #     try:
    # #         contact_us.click()
    # #     except WebDriverException:
    # #         self.fail("contact us not click able")
    # #     driver.back()
    # #     time.sleep(DELAY_SHORT)
    # #     privacy_policy = driver.find_element_by_xpath(
    # #         '/html/body/footer/div[2]/div/div/div[1]/div/div/ul/li[3]/a')
    # #     self.assertIsNotNone(privacy_policy)
    # #     try:
    # #         privacy_policy.click()
    # #     except WebDriverException:
    # #         self.fail("privacy policy not click able")
    # #     driver.back()
    # #     time.sleep(DELAY_SHORT)
    # #     terms_and_condition = driver.find_element_by_xpath(
    # #         '/html/body/footer/div[2]/div/div/div[1]/div/div/ul/li[4]/a')
    # #     self.assertIsNotNone(terms_and_condition)
    # #     try:
    # #         terms_and_condition.click()
    # #     except WebDriverException:
    # #         self.fail("terms and condition not click able")
    # #     driver.back()
    # #     time.sleep(DELAY_SHORT)
    # #     powered_by = driver.find_element_by_xpath(
    # #         '/html/body/footer/div[3]/div/div/div/div/div/div[1]/p/span').text
    # #     self.assertEqual("Powered By", powered_by)
    # #     ishraak_logo = driver.find_element_by_xpath(
    # #         '/html/body/footer/div[3]/div/div/div/div/div/div[1]/p/a/img')
    # #     self.assertIsNotNone(ishraak_logo)
    # #     ishraak = driver.find_element_by_xpath('/html/body/footer/div[3]/div/div/div/div/div/div[1]/p/a')
    # #     ishraak_url = ishraak.get_attribute('href')
    # #     self.assertEqual(IHSRAAK_WEBSITE, ishraak_url)
    # #     copyright_text = driver.find_element_by_class_name('copyright-text').text
    # #     self.assertEqual(COPYRIGHT_TEXT, copyright_text)
    # #     back_to_top = driver.find_element_by_xpath('/html/body/footer/div[3]/div/div/div/div/div/div[2]/div/a')
    # #     self.assertIsNotNone(back_to_top)
    # #     try:
    # #         back_to_top.click()
    # #     except WebDriverException:
    # #         self.fail("Not Click able")
    # #     time.sleep(DELAY_SHORT)
    # #     toogle = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[6]/button')
    # #     toogle.click()
    # #     sign_out = driver.find_element_by_xpath('//*[@id="userNavbarMain"]/ul/li[3]/a')
    # #     ActionChains(self.driver).move_to_element_with_offset(sign_out, 5, 15).click().perform()
    # #     time.sleep(DELAY_SHORT)
    # #     driver.delete_all_cookies()
    # #     driver.get(self.url)
    # #     driver.maximize_window()
    # #     time.sleep(DELAY_LONG)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
