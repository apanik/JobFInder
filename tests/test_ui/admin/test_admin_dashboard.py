import time
import unittest
#
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.chrome import webdriver
#
# from tests.config_web import CHROME_DRIVER_LOCATION, DELAY_SHORT, MAIN_URL

# total page job list result
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.color import Color

from tests.config import VALID_PRO_VIEW_USERNAME, VALID_PRO_VIEW_PASSWORD, ADMIN_URL, VALID_STAFF_PASSWORD, \
    VALID_STAFF_USERNAME
from tests.config_web import MAIN_URL, CHROME_DRIVER_LOCATION, DELAY_SHORT, MAIN_URL_HOME
from tests.test_ui.professional.test_signin import signin_helper


ADD_GROUP = "Add group"
ADD_TOKEN = "Add Token"
ADD_USER = "Add user"
ADD_CAREER_ADVICE = "Add Career Advice"
ADD_PASSWORD_RESET_TOKEN = "Add Password Reset Token"
ADD_APPLICATION_STATUSES = "Add Application Status"
ADD_CITY = "Add City"
ADD_COMPANY = "Add Company"
ADD_CURRENCY = "Add Currency"
ADD_EXPERIENCE = "Add Experience"
ADD_GENDER_PREFERENCE_JOB = "Add Gender Preference(Job)"
ADD_GENDER = "Add Gender (Pro)"
ADD_INDUSTRY = "Add Industry"
ADD_JOB_APPLICATION = "Add Job Application"
ADD_JOB_CATEGORY = "Add Job Category"
ADD_JOB_SOURCE = "Add Job Source"
ADD_JOB = "Add Job"
ADD_QUALIFICATION = "Add Qualification"
ADD_SKILL = "Add Skill"
ADD_TRENDING_KEYWORD = "Add TrendingKeyword"
ADD_EMPLOYER_MESSAGE = "Add Employer Message"
ADD_NOTIFICATION = "Add Notification"
ADD_CERTIFICATE_NAME = "Add certificate name"
ADD_CERTIFICATE = "Add certification"
ADD_CERTIFYING_ORGANIZATION = "Add certifying organization"
ADD_EDUCATION_LEVEL = "Add education level"
ADD_INSTITUTE = "Add institute"
ADD_MAJOR = "Add major"
ADD_MEMBERSHIP_ORGANIZATION = "Add membership organization"
ADD_MEMBERSHIP = "Add membership"
ADD_NATIONALITY = "Add nationality"
ADD_ORGANIZATION = "Add organization"
ADD_PORTFOLIO = "Add portfolio"
ADD_PROFESSIONAL_EDUCATION = "Add professional education"
ADD_PROFESSIONAL_SKILL = "Add professional skill"
ADD_PROFESSIONAL = "Add Professional"
ADD_REFERENCE = "Add reference"
ADD_RELIGION = "Add religion"
ADD_WORK_EXPERIENCE = "Add work experience"
ADD_TESTIMONIAL = "Add Testimonial"
SETTING_TITLE = "Select Setting to change"
POST_A_JOB = "Post Your Job"

ADMIN_USER = 'admin'
ADMIN_PASS = '123'

class TestStaffPageUrlAndAddData(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = ADMIN_URL
        cls.driver = WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        data_staff_login = {
            "user": VALID_STAFF_USERNAME,
            "pass": VALID_STAFF_PASSWORD,
        }
        staff_login_helper(cls.driver, data_staff_login)
        time.sleep(DELAY_SHORT)

    #
    # def test__admin_page_token_and_add_token_link_are_not_broken__should_pass(self):
    #     driver = self.driver
    #     driver.get(ADMIN_URL)
    #     time.sleep(1)
    #     try:
    #         tokens_btn = driver.find_element_by_link_text('Tokens')
    #         tokens_btn.click()
    #         time.sleep(DELAY_SHORT)
    #         add_token = driver.find_element_by_class_name('addlink')
    #         add_token.click()
    #         time.sleep(1)
    #         title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
    #         time.sleep(1)
    #     except:
    #         self.fail()
    #
    #     if title_name != ADD_TOKEN:
    #         self.fail()


    def test__admin_page_groups_and_add_group_link_are_not_broken__should_pass(self):
        driver = self.driver
        driver.get(ADMIN_URL)
        time.sleep(1)
        try:
            groups_btn = driver.find_element_by_link_text('Groups')
            groups_btn.click()
            time.sleep(DELAY_SHORT)
            add_link = driver.find_element_by_class_name('addlink')
            add_link.click()
            time.sleep(1)
            title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
            time.sleep(1)
        except:
            self.fail()

        if title_name != ADD_GROUP:
            self.fail()


    def test__admin_page_users_and_add_user_link_are_not_broken__should_pass(self):
        driver = self.driver
        driver.get(ADMIN_URL)
        time.sleep(1)
        try:
            users_btn = driver.find_element_by_link_text('Users')
            users_btn.click()
            time.sleep(DELAY_SHORT)
            add_link = driver.find_element_by_class_name('addlink')
            add_link.click()
            time.sleep(1)
            title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
            time.sleep(1)
        except:
            self.fail()

        if title_name != ADD_USER:
            self.fail()


    def test__admin_page_career_advices_and_add_career_advices_link_are_not_broken__should_pass(self):
        driver = self.driver
        driver.get(ADMIN_URL)
        time.sleep(1)
        try:
            career_advices_btn = driver.find_element_by_link_text('Career Advices')
            career_advices_btn.click()
            time.sleep(DELAY_SHORT)
            add_link = driver.find_element_by_class_name('addlink')
            add_link.click()
            time.sleep(1)
            title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
            time.sleep(1)
        except:
            self.fail()

        if title_name != ADD_CAREER_ADVICE:
            self.fail()

    #
    # def test__admin_page_password_reset_tokens_and_add_link_are_not_broken__should_pass(self):
    #     driver = self.driver
    #     driver.get(ADMIN_URL)
    #     time.sleep(1)
    #     try:
    #         password_reset_tokens_btn = driver.find_element_by_link_text('Password Reset Tokens')
    #         password_reset_tokens_btn.click()
    #         time.sleep(DELAY_SHORT)
    #         add_link = driver.find_element_by_class_name('addlink')
    #         add_link.click()
    #         time.sleep(1)
    #         title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
    #         time.sleep(1)
    #     except:
    #         self.fail()
    #
    #     if title_name != ADD_PASSWORD_RESET_TOKEN:
    #         self.fail()


    def test__admin_page_application_statuses_and_add_link_are_not_broken__should_pass(self):
        driver = self.driver
        driver.get(ADMIN_URL)
        time.sleep(1)
        try:
            application_statuses_btn = driver.find_element_by_link_text('Application Statuses')
            application_statuses_btn.click()
            time.sleep(DELAY_SHORT)
            add_link = driver.find_element_by_class_name('addlink')
            add_link.click()
            time.sleep(1)
            title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
            time.sleep(1)
        except:
            self.fail()

        if title_name != ADD_APPLICATION_STATUSES:
            self.fail()


    def test__admin_page_cities_and_add_link_are_not_broken__should_pass(self):
        driver = self.driver
        driver.get(ADMIN_URL)
        time.sleep(1)
        try:
            cities_btn = driver.find_element_by_link_text('Cities')
            cities_btn.click()
            time.sleep(DELAY_SHORT)
            add_link = driver.find_element_by_class_name('addlink')
            add_link.click()
            time.sleep(1)
            title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
            time.sleep(1)
        except:
            self.fail()

        if title_name != ADD_CITY:
            self.fail()


    def test__admin_page_companies_and_add_link_are_not_broken__should_pass(self):
        driver = self.driver
        driver.get(ADMIN_URL)
        time.sleep(1)
        try:
            companies_btn = driver.find_element_by_link_text('Companies')
            companies_btn.click()
            time.sleep(DELAY_SHORT)
            add_link = driver.find_element_by_class_name('addlink')
            add_link.click()
            time.sleep(1)
            title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
            time.sleep(1)
        except:
            self.fail()

        if title_name != ADD_COMPANY:
            self.fail()


    def test__admin_page_currencies_and_add_link_are_not_broken__should_pass(self):
        driver = self.driver
        driver.get(ADMIN_URL)
        time.sleep(1)
        try:
            currencies_btn = driver.find_element_by_link_text('Currencies')
            currencies_btn.click()
            time.sleep(DELAY_SHORT)
            add_link = driver.find_element_by_class_name('addlink')
            add_link.click()
            time.sleep(1)
            title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
            time.sleep(1)
        except:
            self.fail()

        if title_name != ADD_CURRENCY:
            self.fail()


    def test__admin_page_experiences_and_add_link_are_not_broken__should_pass(self):
        driver = self.driver
        driver.get(ADMIN_URL)
        time.sleep(1)
        try:
            experiences_btn = driver.find_element_by_link_text('Experiences')
            experiences_btn.click()
            time.sleep(DELAY_SHORT)
            add_link = driver.find_element_by_class_name('addlink')
            add_link.click()
            time.sleep(1)
            title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
            time.sleep(1)
        except:
            self.fail()

        if title_name != ADD_EXPERIENCE:
            self.fail()


    def test__admin_page_gender_preferences_job_and_add_link_are_not_broken__should_pass(self):
        driver = self.driver
        driver.get(ADMIN_URL)
        time.sleep(1)
        try:
            gender_preferences_job_btn = driver.find_element_by_link_text('Gender Preferences(Job)')
            gender_preferences_job_btn.click()
            time.sleep(DELAY_SHORT)
            add_link = driver.find_element_by_class_name('addlink')
            add_link.click()
            time.sleep(1)
            title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
            time.sleep(1)
        except:
            self.fail()

        if title_name != ADD_GENDER_PREFERENCE_JOB:
            self.fail()


    def test__admin_page_genders_and_add_link_are_not_broken__should_pass(self):
        driver = self.driver
        driver.get(ADMIN_URL)
        time.sleep(1)
        try:
            genders_btn = driver.find_element_by_link_text('Genders (Pro)')
            genders_btn.click()
            time.sleep(DELAY_SHORT)
            add_link = driver.find_element_by_class_name('addlink')
            add_link.click()
            time.sleep(1)
            title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
            time.sleep(1)
        except:
            self.fail()

        if title_name != ADD_GENDER:
            self.fail()


    def test__admin_page_industries_and_add_link_are_not_broken__should_pass(self):
        driver = self.driver
        driver.get(ADMIN_URL)
        time.sleep(1)
        try:
            industries_btn = driver.find_element_by_link_text('Industries')
            industries_btn.click()
            time.sleep(DELAY_SHORT)
            add_link = driver.find_element_by_class_name('addlink')
            add_link.click()
            time.sleep(1)
            title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
            time.sleep(1)
        except:
            self.fail()

        if title_name != ADD_INDUSTRY:
            self.fail()


    def test__admin_page_job_applications_and_add_link_are_not_broken__should_pass(self):
        driver = self.driver
        driver.get(ADMIN_URL)
        time.sleep(1)
        try:
            job_applications_btn = driver.find_element_by_link_text('Job Applications')
            job_applications_btn.click()
            time.sleep(DELAY_SHORT)
            add_link = driver.find_element_by_class_name('addlink')
            add_link.click()
            time.sleep(1)
            title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
            time.sleep(1)
        except:
            self.fail()

        if title_name != ADD_JOB_APPLICATION:
            self.fail()


    def test__admin_page_job_categories_and_add_link_are_not_broken__should_pass(self):
        driver = self.driver
        driver.get(ADMIN_URL)
        time.sleep(1)
        try:
            job_categories_btn = driver.find_element_by_link_text('Job Categories')
            job_categories_btn.click()
            time.sleep(DELAY_SHORT)
            add_link = driver.find_element_by_class_name('addlink')
            add_link.click()
            time.sleep(1)
            title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
            time.sleep(1)
        except:
            self.fail()

        if title_name != ADD_JOB_CATEGORY:
            self.fail()


    def test__admin_page_job_sources_and_add_link_are_not_broken__should_pass(self):
        driver = self.driver
        driver.get(ADMIN_URL)
        time.sleep(1)
        try:
            job_sources_btn = driver.find_element_by_link_text('Job Sources')
            job_sources_btn.click()
            time.sleep(DELAY_SHORT)
            add_link = driver.find_element_by_class_name('addlink')
            add_link.click()
            time.sleep(1)
            title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
            time.sleep(1)
        except:
            self.fail()

        if title_name != ADD_JOB_SOURCE:
            self.fail()


    def test__admin_page_jobs_and_add_link_are_not_broken__should_pass(self):
        driver = self.driver
        driver.get(ADMIN_URL)
        time.sleep(1)
        try:
            jobs_btn = driver.find_element_by_link_text('Jobs')
            jobs_btn.click()
            time.sleep(DELAY_SHORT)
            add_link = driver.find_element_by_class_name('addlink')
            add_link.click()
            time.sleep(1)
            title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
            time.sleep(1)
        except:
            self.fail()

        if title_name != ADD_JOB:
            self.fail()


    def test__admin_page_qualifications_and_add_link_are_not_broken__should_pass(self):
        driver = self.driver
        driver.get(ADMIN_URL)
        time.sleep(1)
        try:
            qualifications_btn = driver.find_element_by_link_text('Qualifications')
            qualifications_btn.click()
            time.sleep(DELAY_SHORT)
            add_link = driver.find_element_by_class_name('addlink')
            add_link.click()
            time.sleep(1)
            title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
            time.sleep(1)
        except:
            self.fail()

        if title_name != ADD_QUALIFICATION:
            self.fail()


    def test__admin_page_skills_and_add_link_are_not_broken__should_pass(self):
        driver = self.driver
        driver.get(ADMIN_URL)
        time.sleep(1)
        try:
            skills_btn = driver.find_element_by_link_text('Skills')
            skills_btn.click()
            time.sleep(DELAY_SHORT)
            add_link = driver.find_element_by_class_name('addlink')
            add_link.click()
            time.sleep(1)
            title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
            time.sleep(1)
        except:
            self.fail()

        if title_name != ADD_SKILL:
            self.fail()

    #
    # def test__admin_page_trending_keywords_and_add_link_are_not_broken__should_pass(self):
    #     driver = self.driver
    #     driver.get(ADMIN_URL)
    #     time.sleep(1)
    #     try:
    #         trending_keywords_btn = driver.find_element_by_link_text('TrendingKeywords')
    #         trending_keywords_btn.click()
    #         time.sleep(DELAY_SHORT)
    #         add_link = driver.find_element_by_class_name('addlink')
    #         add_link.click()
    #         time.sleep(1)
    #         title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
    #         time.sleep(1)
    #     except:
    #         self.fail()
    #
    #     if title_name != ADD_TRENDING_KEYWORD:
    #         self.fail()


    def test__admin_page_employer_messages_and_add_link_are_not_broken__should_pass(self):
        driver = self.driver
        driver.get(ADMIN_URL)
        time.sleep(1)
        try:
            employer_messages_btn = driver.find_element_by_link_text('Employer Messages')
            employer_messages_btn.click()
            time.sleep(DELAY_SHORT)
            add_link = driver.find_element_by_class_name('addlink')
            add_link.click()
            time.sleep(1)
            title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
            time.sleep(1)
        except:
            self.fail()

        if title_name != ADD_EMPLOYER_MESSAGE:
            self.fail()


    def test__admin_page_notifications_and_add_link_are_not_broken__should_pass(self):
        driver = self.driver
        driver.get(ADMIN_URL)
        time.sleep(1)
        try:
            notifications_btn = driver.find_element_by_link_text('Notifications')
            notifications_btn.click()
            time.sleep(DELAY_SHORT)
            add_link = driver.find_element_by_class_name('addlink')
            add_link.click()
            time.sleep(1)
            title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
            time.sleep(1)
        except:
            self.fail()

        if title_name != ADD_NOTIFICATION:
            self.fail()


    def test__admin_page_certificate_names_and_add_link_are_not_broken__should_pass(self):
        driver = self.driver
        driver.get(ADMIN_URL)
        time.sleep(1)
        try:
            certificate_names_btn = driver.find_element_by_link_text('Certificate names')
            certificate_names_btn.click()
            time.sleep(DELAY_SHORT)
            add_link = driver.find_element_by_class_name('addlink')
            add_link.click()
            time.sleep(1)
            title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
            time.sleep(1)
        except:
            self.fail()

        if title_name != ADD_CERTIFICATE_NAME:
            self.fail()


    def test__admin_page_certifications_and_add_link_are_not_broken__should_pass(self):
        driver = self.driver
        driver.get(ADMIN_URL)
        time.sleep(1)
        try:
            certifications_btn = driver.find_element_by_link_text('Certifications')
            certifications_btn.click()
            time.sleep(DELAY_SHORT)
            add_link = driver.find_element_by_class_name('addlink')
            add_link.click()
            time.sleep(1)
            title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
            time.sleep(1)
        except:
            self.fail()

        if title_name != ADD_CERTIFICATE:
            self.fail()


    def test__admin_page_certifying_organizations_and_add_link_are_not_broken__should_pass(self):
        driver = self.driver
        driver.get(ADMIN_URL)
        time.sleep(1)
        try:
            certifying_organizations_btn = driver.find_element_by_link_text('Certifying organizations')
            certifying_organizations_btn.click()
            time.sleep(DELAY_SHORT)
            add_link = driver.find_element_by_class_name('addlink')
            add_link.click()
            time.sleep(1)
            title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
            time.sleep(1)
        except:
            self.fail()

        if title_name != ADD_CERTIFYING_ORGANIZATION:
            self.fail()


    def test__admin_page_education_levels_and_add_link_are_not_broken__should_pass(self):
        driver = self.driver
        driver.get(ADMIN_URL)
        time.sleep(1)
        try:
            education_levels_btn = driver.find_element_by_link_text('Education levels')
            education_levels_btn.click()
            time.sleep(DELAY_SHORT)
            add_link = driver.find_element_by_class_name('addlink')
            add_link.click()
            time.sleep(1)
            title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
            time.sleep(1)
        except:
            self.fail()

        if title_name != ADD_EDUCATION_LEVEL:
            self.fail()


    def test__admin_page_institutes_and_add_link_are_not_broken__should_pass(self):
        driver = self.driver
        driver.get(ADMIN_URL)
        time.sleep(1)
        try:
            institutes_btn = driver.find_element_by_link_text('Institutes')
            institutes_btn.click()
            time.sleep(DELAY_SHORT)
            add_link = driver.find_element_by_class_name('addlink')
            add_link.click()
            time.sleep(1)
            title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
            time.sleep(1)
        except:
            self.fail()

        if title_name != ADD_INSTITUTE:
            self.fail()


    def test__admin_page_majors_and_add_link_are_not_broken__should_pass(self):
        driver = self.driver
        driver.get(ADMIN_URL)
        time.sleep(1)
        try:
            majors_btn = driver.find_element_by_link_text('Majors')
            majors_btn.click()
            time.sleep(DELAY_SHORT)
            add_link = driver.find_element_by_class_name('addlink')
            add_link.click()
            time.sleep(1)
            title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
            time.sleep(1)
        except:
            self.fail()

        if title_name != ADD_MAJOR:
            self.fail()


    def test__admin_page_membership_organizations_and_add_link_are_not_broken__should_pass(self):
        driver = self.driver
        driver.get(ADMIN_URL)
        time.sleep(1)
        try:
            membership_organizations_btn = driver.find_element_by_link_text('Membership organizations')
            membership_organizations_btn.click()
            time.sleep(DELAY_SHORT)
            add_link = driver.find_element_by_class_name('addlink')
            add_link.click()
            time.sleep(1)
            title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
            time.sleep(1)
        except:
            self.fail()

        if title_name != ADD_MEMBERSHIP_ORGANIZATION:
            self.fail()


    def test__admin_page_memberships_and_add_link_are_not_broken__should_pass(self):
        driver = self.driver
        driver.get(ADMIN_URL)
        time.sleep(1)
        try:
            memberships_btn = driver.find_element_by_link_text('Memberships')
            memberships_btn.click()
            time.sleep(DELAY_SHORT)
            add_link = driver.find_element_by_class_name('addlink')
            add_link.click()
            time.sleep(1)
            title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
            time.sleep(1)
        except:
            self.fail()

        if title_name != ADD_MEMBERSHIP:
            self.fail()


    def test__admin_page_nationalitys_and_add_link_are_not_broken__should_pass(self):
        driver = self.driver
        driver.get(ADMIN_URL)
        time.sleep(1)
        try:
            nationalitys_btn = driver.find_element_by_link_text('Nationalitys')
            nationalitys_btn.click()
            time.sleep(DELAY_SHORT)
            add_link = driver.find_element_by_class_name('addlink')
            add_link.click()
            time.sleep(1)
            title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
            time.sleep(1)
        except:
            self.fail()

        if title_name != ADD_NATIONALITY:
            self.fail()


    def test__admin_page_organizations_and_add_link_are_not_broken__should_pass(self):
        driver = self.driver
        driver.get(ADMIN_URL)
        time.sleep(1)
        try:
            organizations_btn = driver.find_element_by_link_text('Organizations')
            organizations_btn.click()
            time.sleep(DELAY_SHORT)
            add_link = driver.find_element_by_class_name('addlink')
            add_link.click()
            time.sleep(1)
            title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
            time.sleep(1)
        except:
            self.fail()

        if title_name != ADD_ORGANIZATION:
            self.fail()


    def test__admin_page_portfolios_and_add_link_are_not_broken__should_pass(self):
        driver = self.driver
        driver.get(ADMIN_URL)
        time.sleep(1)
        try:
            portfolios_btn = driver.find_element_by_link_text('Portfolios')
            portfolios_btn.click()
            time.sleep(DELAY_SHORT)
            add_link = driver.find_element_by_class_name('addlink')
            add_link.click()
            time.sleep(1)
            title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
            time.sleep(1)
        except:
            self.fail()

        if title_name != ADD_PORTFOLIO:
            self.fail()


    def test__admin_page_professional_educations_and_add_link_are_not_broken__should_pass(self):
        driver = self.driver
        driver.get(ADMIN_URL)
        time.sleep(1)
        try:
            professional_educations_btn = driver.find_element_by_link_text('Professional educations')
            professional_educations_btn.click()
            time.sleep(DELAY_SHORT)
            add_link = driver.find_element_by_class_name('addlink')
            add_link.click()
            time.sleep(1)
            title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
            time.sleep(1)
        except:
            self.fail()

        if title_name != ADD_PROFESSIONAL_EDUCATION:
            self.fail()


    def test__admin_page_professional_skills_and_add_link_are_not_broken__should_pass(self):
        driver = self.driver
        driver.get(ADMIN_URL)
        time.sleep(1)
        try:
            professional_skills_btn = driver.find_element_by_link_text('Professional skills')
            professional_skills_btn.click()
            time.sleep(DELAY_SHORT)
            add_link = driver.find_element_by_class_name('addlink')
            add_link.click()
            time.sleep(1)
            title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
            time.sleep(1)
        except:
            self.fail()

        if title_name != ADD_PROFESSIONAL_SKILL:
            self.fail()


    def test__admin_page_professionals_and_add_link_are_not_broken__should_pass(self):
        driver = self.driver
        driver.get(ADMIN_URL)
        time.sleep(1)
        try:
            professionals_btn = driver.find_element_by_link_text('Professionals')
            professionals_btn.click()
            time.sleep(DELAY_SHORT)
            add_link = driver.find_element_by_class_name('addlink')
            add_link.click()
            time.sleep(1)
            title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
            time.sleep(1)
        except:
            self.fail()

        if title_name != ADD_PROFESSIONAL:
            self.fail()


    def test__admin_page_references_and_add_link_are_not_broken__should_pass(self):
        driver = self.driver
        driver.get(ADMIN_URL)
        time.sleep(1)
        try:
            references_btn = driver.find_element_by_link_text('References')
            references_btn.click()
            time.sleep(DELAY_SHORT)
            add_link = driver.find_element_by_class_name('addlink')
            add_link.click()
            time.sleep(1)
            title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
            time.sleep(1)
        except:
            self.fail()

        if title_name != ADD_REFERENCE:
            self.fail()


    def test__admin_page_religions_and_add_link_are_not_broken__should_pass(self):
        driver = self.driver
        driver.get(ADMIN_URL)
        time.sleep(1)
        try:
            religions_btn = driver.find_element_by_link_text('Religions')
            religions_btn.click()
            time.sleep(DELAY_SHORT)
            add_link = driver.find_element_by_class_name('addlink')
            add_link.click()
            time.sleep(1)
            title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
            time.sleep(1)
        except:
            self.fail()

        if title_name != ADD_RELIGION:
            self.fail()


    def test__admin_page_work_experiences_and_add_link_are_not_broken__should_pass(self):
        driver = self.driver
        driver.get(ADMIN_URL)
        time.sleep(1)
        try:
            work_experiences_btn = driver.find_element_by_link_text('Work experiences')
            work_experiences_btn.click()
            time.sleep(DELAY_SHORT)
            add_link = driver.find_element_by_class_name('addlink')
            add_link.click()
            time.sleep(1)
            title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
            time.sleep(1)
        except:
            self.fail()

        if title_name != ADD_WORK_EXPERIENCE:
            self.fail()


    def test__admin_page_testimonials_and_add_link_are_not_broken__should_pass(self):
        driver = self.driver
        driver.get(ADMIN_URL)
        time.sleep(1)
        try:
            testimonials_btn = driver.find_element_by_link_text('Testimonials')
            testimonials_btn.click()
            time.sleep(DELAY_SHORT)
            add_link = driver.find_element_by_class_name('addlink')
            add_link.click()
            time.sleep(1)
            title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
            time.sleep(1)
        except:
            self.fail()

        if title_name != ADD_TESTIMONIAL:
            self.fail()


    def test__admin_page_settings_is_not_broken__should_pass(self):
        driver = self.driver
        driver.get(ADMIN_URL)
        time.sleep(1)
        try:
            settings_btn = driver.find_element_by_link_text('Settings')
            settings_btn.click()
            time.sleep(DELAY_SHORT)
            title_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text
            time.sleep(1)
        except:
            self.fail()

        if title_name != SETTING_TITLE:
            self.fail()


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()




def staff_login_helper(driver, row):
    driver.refresh()
    user_btn = driver.find_element_by_name('username')
    user_btn.send_keys(row['user'])
    time.sleep(1)
    pass_btn = driver.find_element_by_name('password')
    pass_btn.send_keys(row['pass'])
    time.sleep(1)
    submit = driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input')
    submit.click()
    time.sleep(DELAY_SHORT)

    try:
        log_out = driver.find_element_by_xpath('//*[@id="user-tools"]/a[3]')
        return 1
    except NoSuchElementException:
        return 0



if __name__ == '__main__':
    unittest.main()