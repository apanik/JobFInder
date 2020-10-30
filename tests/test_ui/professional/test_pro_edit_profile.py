import time
import unittest

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver

from tests.test_ui.professional.test_signin import signin_helper
from tests.config import VALID_PRO_USERNAME, VALID_PRO_PASSWORD
from tests.config_web import CHROME_DRIVER_LOCATION, DELAY_SHORT, MAIN_URL, TEST_IMAGE, MAIN_URL_HOME

FACEBOOK = 'http://facebook.com/'
TWITTER = 'https://twitter.com/'
LINKEDIN = 'https://www.linkedin.com/'

FACEBOOK_ID = 'example_fb'
TWITTER_ID = 'examaple_twitter'
LINKEDIN_ID = 'example_linkedin'

FACEBOOK_URL = 'http://facebook.com/example_fb'
TWITTER_URL = 'https://twitter.com/examaple_twitter'
LINKEDIN_URL = 'https://www.linkedin.com/example_linkedin'

BLANK = ''

# Basic Info Section
ABOUT_ME = 'About me example.'
INDUSTRY = 'Example Industry One'
CURRENT_LOCATION = 'Dhaka'
EXPERIENCE = 'Experience Example One years'
QUALIFICATION = 'Qualification Example One'

# Personal Info Section
FULL_NAME = 'Mr Prof Example'
FATHER_NAME = 'Mr Prof Father'
MOTHER_NAME = 'Mr Prof Mother'
DATE_OF_BIRTH = '01/01/2000'
NATIONALITY = 'Bangladeshi'
GENDER = 'Male'
RELIGION = 'Islam'
BLOOD_GROUP = 'A+'
ADDRESS = 'Dhaka, badda'
PERMANENT_ADDRESS = 'Niketon, Gulsan 1212'

# Education Section
INSTITUTION = 'Institution example one'
EDUCATION_LEVEL = 'Education Level Example One'
DEGREE_TEXT = 'Qualification Example One'

CGPA = '4.25'
MAJOR = 'Major Example Two'

# Work Experience
COMPANY = 'Company Example'
DESIGNATION = 'Designation Example'

# Skill Add
SKILL_NAME = 'Python'
SKILL_RATING = '5'

#Certification Add
CERTIFICATION_NAME = 'Certificate Example One'
ORGANIZATION = 'Organization Example One'
CREDENTIAL_ID = 'Credential Example One'
CREDENTIAL_URL = 'credential.ishraak.com'

#Membership
MEMBERSHIP_ORGANISATION = 'Membership Organisation Example One'
POSITION_HELD = 'Position Held Example One'

#Portfolio Name
PORTFOLIO_NAME = 'Portfolio Name Example'
PORTFOLIO_IMAGE = TEST_IMAGE

# MONTH = 'Jan'
# MONTH_VALUE = '0'
# START_YEAR = '2001'
# END_YEAR = '2005'

DESCRIPTION = 'Sample description is written here'
START_DATE = '01/01/2001'
END_DATE = '01/01/2005'
ON_GOING = 'Ongoing'
CURRENTLY_WORKING = 'Currently Working Here'
NO_EXPIRY_PERIOD = 'No Expiry Period'

PHONE = '01911111111'
CURRENT_COMPANY = 'Company Example One'
CURRENT_DESIGNATION = 'Designation Example One'

INSTITUTE_DEMO_IMAGE = '/static/images/candidate/Institute.png'
INSTITUTE_IMAGE = '/static/images/candidate/Institute.png'

class TestProfessionalEditProfileSocial(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        data_signin = {
            "email": VALID_PRO_USERNAME,
            "password": VALID_PRO_PASSWORD,
        }
        signin_helper(cls.driver,data_signin)
        time.sleep(DELAY_SHORT)


    def test__social_id_add__when_valid__should_pass(self):
        driver= self.driver
        data = {
            "facebook" : FACEBOOK_ID,
            "twitter" : TWITTER_ID,
            "linkedin" : LINKEDIN_ID,
        }
        prof_edit_profile_social_helper(driver,data)
        try:
            facebook_success = driver.find_element_by_class_name('facebook').get_attribute('href')
            time.sleep(1)
            twitter_success = driver.find_element_by_class_name('twitter').get_attribute('href')
            time.sleep(1)
            linkedin_success = driver.find_element_by_class_name('linkedin').get_attribute('href')
            self.assertEqual(facebook_success,FACEBOOK_URL )
            self.assertEqual(twitter_success,TWITTER_URL )
            self.assertEqual(linkedin_success,LINKEDIN_URL )

        except NoSuchElementException:
            self.fail('Not ok')


    def test__social_id__when_blank__should_pass(self):
            driver= self.driver
            data = {
                "facebook" : BLANK,
                "twitter" : BLANK,
                "linkedin" : BLANK,
            }
            prof_edit_profile_social_helper(driver,data)
            try:
                facebook_success = driver.find_element_by_class_name('facebook').get_attribute('href')
                time.sleep(1)
                twitter_success = driver.find_element_by_class_name('twitter').get_attribute('href')
                time.sleep(1)
                linkedin_success = driver.find_element_by_class_name('linkedin').get_attribute('href')
                self.assertEqual(facebook_success, FACEBOOK)
                self.assertEqual(twitter_success, TWITTER)
                self.assertEqual(linkedin_success, LINKEDIN)
                pass
            except NoSuchElementException:
                self.fail('Not ok')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


class TestProfessionalEditProfileBasicInfo(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        data_signin = {
            "email": VALID_PRO_USERNAME,
            "password": VALID_PRO_PASSWORD,
        }
        signin_helper(cls.driver, data_signin)
        time.sleep(DELAY_SHORT)


    def test__basic_info__when_valid__should_pass(self):
            driver= self.driver
            data = {
                "about_me" : ABOUT_ME,
                "industry_expertise" : INDUSTRY,
                "current_location" : CURRENT_LOCATION,
                "experience" : EXPERIENCE,
                "qualification" : QUALIFICATION,
                "phone" : PHONE,
                "current_company" : CURRENT_COMPANY,
                "current_designation" : CURRENT_DESIGNATION,
            }
            prof_edit_profile_basic_info_helper(driver, data)
            time.sleep(DELAY_SHORT)
            try:
                about_me_success = driver.find_element_by_id("about_me").text
                time.sleep(1)
                industry_success = driver.find_element_by_id("industry_expertise").text
                time.sleep(1)
                location_success = driver.find_element_by_id("current_location").text
                time.sleep(1)
                experience_success = driver.find_element_by_id("experience").text
                time.sleep(1)
                qualification_success = driver.find_element_by_id("qualification").text
                time.sleep(1)
                phone_success = driver.find_element_by_id("phone").text
                time.sleep(1)
                current_company_success = driver.find_element_by_id("current_company").text
                time.sleep(1)
                current_designation_success = driver.find_element_by_id("current_designation").text
                time.sleep(1)
                self.assertEqual(about_me_success, ABOUT_ME)
                self.assertEqual(industry_success, INDUSTRY)
                self.assertEqual(location_success, CURRENT_LOCATION)
                self.assertEqual(experience_success, EXPERIENCE)
                self.assertEqual(qualification_success, QUALIFICATION)
                self.assertEqual(phone_success, PHONE)
                self.assertEqual(current_company_success, CURRENT_COMPANY)
                self.assertEqual(current_designation_success, CURRENT_DESIGNATION)
            except NoSuchElementException:
                self.fail('Not ok')
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


class TestProfessionalEditProfilePersonalInfoAdd(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        data_signin = {
            "email": VALID_PRO_USERNAME,
            "password": VALID_PRO_PASSWORD,
        }
        signin_helper(cls.driver, data_signin)
        time.sleep(DELAY_SHORT)


    def test__personal_info_add__when_valid__should_pass(self):
            driver= self.driver
            data = {
                "full_name" : FULL_NAME,
                "father_name" : FATHER_NAME,
                "mother_name" : MOTHER_NAME,
                "date_of_birth" : DATE_OF_BIRTH,
                "nationality" : NATIONALITY,
                "gender" : GENDER,
                "religion" : RELIGION,
                "blood_group" : BLOOD_GROUP,
                "address" : ADDRESS,
                "permanent_address" : PERMANENT_ADDRESS,
            }
            prof_edit_profile_personal_info_helper(driver, data)
            time.sleep(1)
            try:
                error_msg = driver.find_element_by_class_name("my-error-class")
                self.fail('Not ok')
            except:
                pass


    def test__personal_info_add__when_empty_full_name__should_fail(self):
            driver= self.driver
            data = {
                "full_name" : '',
                "father_name" : FATHER_NAME,
                "mother_name" : MOTHER_NAME,
                "date_of_birth" : DATE_OF_BIRTH,
                "nationality" : NATIONALITY,
                "gender" : GENDER,
                "religion" : RELIGION,
                "blood_group" : BLOOD_GROUP,
                "address" : ADDRESS,
                "permanent_address" : PERMANENT_ADDRESS,
            }
            prof_edit_profile_personal_info_helper(driver, data)
            time.sleep(DELAY_SHORT)
            try:
                error_msg = driver.find_element_by_class_name("my-error-class")
                pass
            except:
                self.fail('Not ok')


    def test__personal_info__when_valid__should_view__should_pass(self):
            driver= self.driver
            data = {
                "full_name" : FULL_NAME,
                "father_name" : FATHER_NAME,
                "mother_name" : MOTHER_NAME,
                "date_of_birth" : DATE_OF_BIRTH,
                "nationality" : NATIONALITY,
                "gender" : GENDER,
                "religion" : RELIGION,
                "blood_group" : BLOOD_GROUP,
                "address" : ADDRESS,
                "permanent_address" : PERMANENT_ADDRESS,
            }
            prof_edit_profile_personal_info_helper(driver, data)
            time.sleep(1)
            try:
                full_name_success = driver.find_element_by_id("full_name").text
                time.sleep(1)
                father_name_success = driver.find_element_by_id("father_name").text
                time.sleep(1)
                mother_name_success = driver.find_element_by_id("mother_name").text
                time.sleep(1)
                do_birth_success = driver.find_element_by_id("do_birth").text
                time.sleep(1)
                nationality_success = driver.find_element_by_id("nationality").text
                time.sleep(1)
                gender_success = driver.find_element_by_id("gender").text
                time.sleep(1)
                religion_success = driver.find_element_by_id("religion").text
                time.sleep(1)
                blood_group_success = driver.find_element_by_id("blood_group").text
                time.sleep(1)
                address_success = driver.find_element_by_id("address").text
                time.sleep(1)
                permanent_address_success = driver.find_element_by_id("permanent_address").text
                time.sleep(1)
                self.assertEqual(full_name_success, FULL_NAME)
                self.assertEqual(father_name_success, FATHER_NAME)
                self.assertEqual(mother_name_success, MOTHER_NAME)
                self.assertEqual(do_birth_success, DATE_OF_BIRTH)
                self.assertEqual(nationality_success, NATIONALITY)
                self.assertEqual(gender_success, GENDER)
                self.assertEqual(religion_success, RELIGION)
                self.assertEqual(blood_group_success, BLOOD_GROUP)
                self.assertEqual(address_success, ADDRESS)
                self.assertEqual(permanent_address_success, PERMANENT_ADDRESS)

            except NoSuchElementException:
                self.fail('Not ok')


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


class TestProfessionalEditProfileEducationAdd(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        data_signin = {
            "email": VALID_PRO_USERNAME,
            "password": VALID_PRO_PASSWORD,
        }
        signin_helper(cls.driver, data_signin)
        time.sleep(DELAY_SHORT)


    def test__education_add__when_valid__should_pass(self):
            driver= self.driver
            data = {
                "institution_text" : INSTITUTION,
                "education_level" : EDUCATION_LEVEL,
                "degree_text" : DEGREE_TEXT,
                "cgpa" : CGPA,
                "major" : MAJOR,
                "description" : DESCRIPTION,
                "start_date" : START_DATE,
                "end_date" : END_DATE,
            }
            prof_edit_profile_education_helper(driver, data)
            try:
                error_msg = driver.find_element_by_class_name("my-error-class")
                self.fail('Not ok')
            except:
                pass


    def test__education_add__when_institute_name_is_empty__should_fail(self):
            driver= self.driver
            data = {
                "institution_text" : '',
                "education_level" : EDUCATION_LEVEL,
                "degree_text" : DEGREE_TEXT,
                "cgpa" : CGPA,
                "major" : MAJOR,
                "description" : DESCRIPTION,
                "start_date" : START_DATE,
                "end_date" : END_DATE,
            }
            prof_edit_profile_education_helper(driver, data)
            try:
                error_msg = driver.find_element_by_class_name("my-error-class")
                pass
            except:
                self.fail('Not ok')


    # def test__education_added_data_view__when_valid__should_pass(self):
    #         driver= self.driver
    #         data = {
    #             "institution_text" : INSTITUTION,
    #             "education_level" : EDUCATION_LEVEL,
    #             "degree_text" : DEGREE_TEXT,
    #             "cgpa" : CGPA,
    #             "major" : MAJOR,
    #             "description" : DESCRIPTION,
    #             "start_date" : START_DATE,
    #             "end_date" : END_DATE,
    #         }
    #         prof_edit_profile_education_helper(driver, data)
    #         try:
    #             education_list = driver.find_elements_by_class_name('edu-list')
    #             for edu in education_list:
    #                 institute_image_success = edu.find_element_by_class_name('img-fluid').get_attribute('src')
    #                 study_year_success = edu.find_element_by_class_name("study-year").text
    #                 qualification_institution_success = edu.find_element_by_tag_name("h5").text
    #                 description_success = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div[1]/div[4]/div[1]/div/div[2]/p[2]").text
    #             if data['end_date'] == ON_GOING:
    #                 self.assertEqual(study_year_success, START_DATE+' - '+ON_GOING)
    #             else:
    #                 self.assertEqual(study_year_success, START_DATE+' - '+END_DATE)
    #             self.assertEqual(qualification_institution_success, QUALIFICATION+' in '+DEGREE_TEXT+'@'+INSTITUTION+', CGPA: '+CGPA)
    #             self.assertEqual(description_success, DESCRIPTION)
    #             self.assertEqual(institute_image_success, MAIN_URL+ (INSTITUTE_IMAGE or INSTITUTE_DEMO_IMAGE))
    #             time.sleep(1)
    #         except NoSuchElementException:
    #             self.fail('Not ok')


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


class TestProfessionalEditProfileWorkExperienceAdd(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        data_signin = {
            "email": VALID_PRO_USERNAME,
            "password": VALID_PRO_PASSWORD,
        }
        signin_helper(cls.driver, data_signin)
        time.sleep(DELAY_SHORT)


    def test__work_experience_add__when_valid__should_pass(self):
            driver= self.driver
            data = {
                #  description start_date end_date
                "company" : COMPANY,
                "designation" : DESIGNATION,
                "description" : DESCRIPTION,
                "start_date" : START_DATE,
                "end_date" : CURRENTLY_WORKING,
            }
            prof_edit_profile_work_experience_helper(driver, data)
            try:
                error_msg = driver.find_element_by_class_name("my-error-class")
                self.fail('Not ok')
            except:
                pass


    def test__work_experience_add__when_company_is_empty__should_fail(self):
            driver= self.driver
            data = {
                #  description start_date end_date
                "company" : '',
                "designation" : DESIGNATION,
                "description" : DESCRIPTION,
                "start_date" : START_DATE,
                "end_date" : CURRENTLY_WORKING,
            }
            prof_edit_profile_work_experience_helper(driver, data)
            try:
                error_msg = driver.find_element_by_class_name("my-error-class")
                pass
            except:
                self.fail('Not ok')


    #
    # def test__work_experience__when_valid__should_pass(self):
    #         driver= self.driver
    #         data = {
    #             #  description start_date end_date
    #             "company" : COMPANY,
    #             "designation" : DESIGNATION,
    #             "description" : DESCRIPTION,
    #             "start_date" : START_DATE,
    #             "end_date" : CURRENTLY_WORKING,
    #         }
    #         prof_edit_profile_work_experience_helper(driver, data)
    #         try:
    #             time.sleep(1)
    #             service_year_success = driver.find_element_by_class_name("service-year").text
    #             time.sleep(1)
    #             designation_success = driver.find_element_by_xpath('//*[@id="experience-div"]/div/h5').text
    #             time.sleep(1)
    #             description_success = driver.find_element_by_xpath('//*[@id="experience-div"]/div[1]/p[2]').text
    #             if data['end_date'] == CURRENTLY_WORKING:
    #                 self.assertEqual(service_year_success, START_DATE+' - '+CURRENTLY_WORKING)
    #             else:
    #                 self.assertEqual(service_year_success, START_DATE+' - '+END_DATE)
    #             self.assertEqual(designation_success, DESIGNATION+'@'+COMPANY)
    #             self.assertEqual(description_success, DESCRIPTION)
    #
    #         except NoSuchElementException:
    #             self.fail('Not ok')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


class TestProfessionalEditProfileSkillAdd(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        data_signin = {
            "email": VALID_PRO_USERNAME,
            "password": VALID_PRO_PASSWORD,
        }
        signin_helper(cls.driver, data_signin)
        time.sleep(DELAY_SHORT)

    def test__professional_skill_add__when_valid__should_pass(self):
            driver= self.driver
            data = {
                "skill_name" : SKILL_NAME,
                "skill_rating" : SKILL_RATING,
            }
            prof_edit_profile_skill_helper(driver, data)
            try:
                error_msg = driver.find_element_by_class_name("my-error-class")
                self.fail('Not ok')
            except:
                pass


    def test__professional_skill_add__when_skill_name_is_empty__should_fail(self):
            driver= self.driver
            data = {
                "skill_name" : '',
                "skill_rating" : SKILL_RATING,
            }
            prof_edit_profile_skill_helper(driver, data)
            try:
                error_msg = driver.find_element_by_class_name("my-error-class")
                pass
            except:
                self.fail('Not ok')


    # def test__professional_skill__when_valid__should_pass(self):
    #         driver= self.driver
    #         data = {
    #             "skill_name" : SKILL_NAME,
    #             "skill_rating" : SKILL_RATING,
    #         }
    #         prof_edit_profile_skill_helper(driver, data)
    #         try:
    #             time.sleep(5)
    #             skill_name_success = driver.find_element_by_xpath('//*[@id="skill-label"]/div/div[1]/p').text
    #             time.sleep(1)
    #             skill_rating_success = driver.find_element_by_xpath('//*[@id="skill-label"]/div/div[2]/p').text
    #             time.sleep(1)
    #             skill_progress_bar_success = driver.find_element_by_class_name('progress-bar').get_attribute('aria-valuenow')
    #             time.sleep(1)
    #             self.assertEqual(skill_name_success, SKILL_NAME)
    #             self.assertEqual(skill_rating_success, SKILL_RATING+'/10')
    #             self.assertEqual(skill_progress_bar_success, SKILL_RATING+'0')
    #
    #         except NoSuchElementException:
    #             self.fail('Not ok')


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


class TestProfessionalEditProfileCertificationAdd(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        data_signin = {
            "email": VALID_PRO_USERNAME,
            "password": VALID_PRO_PASSWORD,
        }
        signin_helper(cls.driver, data_signin)
        time.sleep(DELAY_SHORT)


    def test__certification_add__when_valid__should_pass(self):
            driver= self.driver
            data = {
                #  certificate_name organization credential_id organization month year
                "certificate_name" : CERTIFICATION_NAME,
                "organization" : ORGANIZATION,
                "credential_id" : CREDENTIAL_ID,
                "credential_url" : CREDENTIAL_URL,
                "start_date" : START_DATE,
                "end_date" : NO_EXPIRY_PERIOD,
            }
            prof_edit_profile_Certification_helper(driver, data)
            try:
                error_msg = driver.find_element_by_class_name("my-error-class")
                self.fail('Not ok')
            except:
                pass

    def test__certification_add__when_cirtificate_name_is_empty__should_fail(self):
            driver= self.driver
            data = {
                #  certificate_name organization credential_id organization month year
                "certificate_name" : '',
                "organization" : ORGANIZATION,
                "credential_id" : CREDENTIAL_ID,
                "credential_url" : CREDENTIAL_URL,
                "start_date" : START_DATE,
                "end_date" : NO_EXPIRY_PERIOD,
            }
            prof_edit_profile_Certification_helper(driver, data)
            try:
                error_msg = driver.find_element_by_class_name("my-error-class")
                pass
            except:
                self.fail('Not ok')

    # def test__certification__when_valid__should_pass(self):
    #         driver= self.driver
    #         data = {
    #             #  certificate_name organization credential_id organization month year
    #             "certificate_name" : CERTIFICATION_NAME,
    #             "organization" : ORGANIZATION,
    #             "credential_id" : CREDENTIAL_ID,
    #             "credential_url" : CREDENTIAL_URL,
    #             "start_date" : START_DATE,
    #             "end_date" : NO_EXPIRY_PERIOD,
    #         }
    #         prof_edit_profile_Certification_helper(driver, data)
    #         try:
    #             time.sleep(1)
    #             service_year_success = driver.find_element_by_xpath('//*[@id="certification-div"]/div/span').text
    #             time.sleep(1)
    #             certification_success = driver.find_element_by_xpath('//*[@id="certification-div"]/div/h5').text
    #             time.sleep(1)
    #             if data['end_date'] == NO_EXPIRY_PERIOD:
    #                 self.assertEqual(service_year_success, START_DATE+' - '+NO_EXPIRY_PERIOD)
    #             else:
    #                 self.assertEqual(service_year_success, START_DATE+' - '+END_DATE)
    #             self.assertEqual(certification_success, CERTIFICATION_NAME+'@'+ORGANIZATION)
    #
    #
    #         except NoSuchElementException:
    #             self.fail('Not ok')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()




class TestProfessionalEditProfileMembershipAdd(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        data_signin = {
            "email": VALID_PRO_USERNAME,
            "password": VALID_PRO_PASSWORD,
        }
        signin_helper(cls.driver, data_signin)
        time.sleep(DELAY_SHORT)


    def test__Membership_add__when_valid__should_pass(self):
            driver= self.driver
            data = {
                "organization" : MEMBERSHIP_ORGANISATION,
                "position_held" : POSITION_HELD,
                "description" : DESCRIPTION,
                "start_date" : START_DATE,
                "end_date" : END_DATE
            }
            prof_edit_profile_Membership_helper(driver, data)
            try:
                error_msg = driver.find_element_by_class_name("my-error-class")
                self.fail('Not ok')
            except:
                pass


    def test__Membership_add__when_organization_name_is_empty__should_fail(self):
            driver= self.driver
            data = {
                "organization" : MEMBERSHIP_ORGANISATION,
                "position_held" : POSITION_HELD,
                "description" : DESCRIPTION,
                "start_date" : START_DATE,
                "end_date" : END_DATE
            }
            prof_edit_profile_Membership_helper(driver, data)
            try:
                error_msg = driver.find_element_by_class_name("my-error-class")
                pass
            except:
                self.fail('Not ok')


    #
    # def test__Membership__when_valid_with_view__should_pass(self):
    #         driver= self.driver
    #         data = {
    #             "organization" : MEMBERSHIP_ORGANISATION,
    #             "position_held" : POSITION_HELD,
    #             "description" : DESCRIPTION,
    #             "start_date" : START_DATE,
    #             "end_date" : END_DATE
    #         }
    #         prof_edit_profile_Membership_helper(driver, data)
    #         try:
    #             time.sleep(1)
    #             service_year_success = driver.find_element_by_class_name("study-year").text
    #             time.sleep(1)
    #             membership_success = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[1]/div[8]/div[1]/div/h5').text
    #             time.sleep(1)
    #             description_success = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[1]/div[8]/div[1]/div/p[2]').text
    #             if data['end_date'] == ON_GOING:
    #                 self.assertEqual(service_year_success, START_DATE+' - '+ON_GOING)
    #             else:
    #                 self.assertEqual(service_year_success, START_DATE+' - '+END_DATE)
    #             self.assertEqual(membership_success, MEMBERSHIP_ORGANISATION+'@'+POSITION_HELD)
    #             self.assertEqual(description_success, DESCRIPTION)
    #
    #         except NoSuchElementException:
    #             self.fail('Not ok')


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()



class TestProfessionalEditProfilePortfolioAdd(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        data_signin = {
            "email": VALID_PRO_USERNAME,
            "password": VALID_PRO_PASSWORD,
        }
        time.sleep(DELAY_SHORT)
        cls.driver.maximize_window()
        signin_helper(cls.driver, data_signin)


    def test__professional_portfolio_add__when_valid__should_pass(self):
            driver= self.driver
            data = {
                "name" : PORTFOLIO_NAME,
                # "portfolio_image" : PORTFOLIO_IMAGE,
                "description" : DESCRIPTION,
            }
            prof_edit_profile_portfolio_helper(driver, data)
            try:
                error_msg = driver.find_element_by_class_name("my-error-class")
                self.fail('Not ok')
            except:
                pass


    def test__professional_portfolio_add__when_portfolio_name_is_empty__should_fail(self):
            driver= self.driver
            data = {
                "name" : '',
                # "portfolio_image" : PORTFOLIO_IMAGE,
                "description" : DESCRIPTION,
            }
            prof_edit_profile_portfolio_helper(driver, data)
            try:
                error_msg = driver.find_element_by_class_name("my-error-class")
                pass
            except:
                self.fail('Not ok')


class TestProfessionalEditProfileReferenceAdd(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        data_signin = {
            "email": VALID_PRO_USERNAME,
            "password": VALID_PRO_PASSWORD,
        }
        time.sleep(DELAY_SHORT)
        cls.driver.maximize_window()
        signin_helper(cls.driver, data_signin)


    def test__professional_reference_add__when_valid__should_pass(self):
            driver= self.driver
            data = {
                "description" : DESCRIPTION,
            }
            prof_edit_profile_reference_helper(driver, data)
            try:
                error_msg = driver.find_element_by_class_name("my-error-class")
                self.fail('Not ok')
            except:
                pass


    def test__professional__reference_add__when_description_is_empty__should_fail(self):
            driver= self.driver
            time.sleep(DELAY_SHORT)
            data = {
                "description" : '',
            }
            prof_edit_profile_reference_helper(driver, data)
            try:
                error_msg = driver.find_element_by_class_name("my-error-class")
                pass
            except:
                self.fail('Not ok')


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()




def prof_edit_profile_social_helper(driver:WebDriver, row):
    driver.refresh()
    time.sleep(DELAY_SHORT)
    try:
        edit_profile_btn = driver.find_element_by_id('edit-profile-details')
        try:
            edit_profile_btn.click()
            time.sleep(1)
        except:
            time.sleep(1)
        time.sleep(1)
        social = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div[1]/div[1]/div/button")
        social.click()
        facebook = driver.find_element_by_id("facebook_id")
        time.sleep(1)
        facebook.clear()
        time.sleep(1)
        facebook.send_keys(row['facebook'])
        time.sleep(1)
        twitter = driver.find_element_by_id("twitter_id")
        time.sleep(1)
        twitter.clear()
        time.sleep(1)
        twitter.send_keys(row['twitter'])
        time.sleep(1)
        linkedin = driver.find_element_by_id("linkedin_id")
        time.sleep(1)
        linkedin.clear()
        time.sleep(1)
        linkedin.send_keys(row['linkedin'])
        time.sleep(1)
        save_button = driver.find_element_by_xpath('//*[@id="social-update-form"]/div[4]/div/div/button[1]')
        save_button.click()
        time.sleep(1)

    except NoSuchElementException:
        return 1


def prof_edit_profile_basic_info_helper(driver:WebDriver, row):
    driver.refresh()
    time.sleep(DELAY_SHORT)
    try:
        edit_profile_btn = driver.find_element_by_id('edit-profile-details')
        try:
            edit_profile_btn.click()
            time.sleep(1)
        except:
            time.sleep(1)
        time.sleep(1)
        edit_info_btn = driver.find_element_by_xpath('//*[@id="about-details-div"]/button')
        edit_info_btn.click()
        time.sleep(1)
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        about_me = driver.find_element_by_id("tinymce")
        about_me.clear()
        about_me.send_keys(row['about_me'])
        driver.switch_to.default_content()
        time.sleep(1)
        industry_expertise = driver.find_element_by_name("industry_expertise")
        time.sleep(1)
        industry_expertise.send_keys('Select Category')
        time.sleep(1)
        industry_expertise.send_keys(row['industry_expertise'])
        time.sleep(1)
        location = driver.find_element_by_name("current_location")
        time.sleep(1)
        location.clear()
        time.sleep(1)
        location.send_keys(row['current_location'])
        time.sleep(1)
        experience = driver.find_element_by_name("experience")
        time.sleep(1)
        experience.send_keys('Experience')
        time.sleep(1)
        experience.send_keys(row['experience'])
        time.sleep(1)
        qualification = driver.find_element_by_name("qualification")
        time.sleep(1)
        qualification.send_keys('Qualification')
        time.sleep(1)
        qualification.send_keys(row['qualification'])
        time.sleep(1)
        phone = driver.find_element_by_name("phone")
        time.sleep(1)
        phone.clear()
        time.sleep(1)
        phone.send_keys(row['phone'])
        time.sleep(1)
        current_company = driver.find_element_by_name("current_company")
        time.sleep(1)
        current_company.clear()
        time.sleep(1)
        current_company.send_keys(row['current_company'])
        time.sleep(1)
        current_designation = driver.find_element_by_name("current_designation")
        time.sleep(1)
        current_designation.clear()
        time.sleep(1)
        current_designation.send_keys(row['current_designation'])
        time.sleep(DELAY_SHORT)

        save_button = driver.find_element_by_xpath('//*[@id="info-update-form"]/div[9]/div/div/button[1]')
        save_button.click()
        time.sleep(1)

    except NoSuchElementException:
        return 1


def prof_edit_profile_personal_info_helper(driver:WebDriver, row):
    driver.refresh()
    time.sleep(DELAY_SHORT)
    try:
        edit_profile_btn = driver.find_element_by_id('edit-profile-details')
        try:
            edit_profile_btn.click()
            time.sleep(1)
        except:
            time.sleep(1)
        time.sleep(1)
        edit_info_btn = driver.find_element_by_xpath('//*[@id="personal-information-div"]/button')
        time.sleep(1)
        edit_info_btn.click()
        time.sleep(DELAY_SHORT)
        # driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        full_name = driver.find_element_by_name("full_name")
        time.sleep(1)
        full_name.clear()
        time.sleep(1)
        full_name.send_keys(row['full_name'])
        # driver.switch_to.default_content()
        time.sleep(1)
        father_name = driver.find_element_by_name("father_name")
        time.sleep(1)
        father_name.clear()
        time.sleep(1)
        father_name.send_keys(row['father_name'])
        time.sleep(1)
        mother_name = driver.find_element_by_name("mother_name")
        time.sleep(1)
        mother_name.clear()
        time.sleep(1)
        mother_name.send_keys(row['mother_name'])
        time.sleep(1)
        date_of_birth_delete = driver.find_element_by_xpath('//*[@id="remove-dob"]')
        time.sleep(1)
        date_of_birth_delete.click()
        time.sleep(1)
        date_of_birth_delete_confirm = driver.find_element_by_class_name('swal2-confirm')
        time.sleep(1)
        date_of_birth_delete_confirm.click()
        time.sleep(1)
        if row['date_of_birth'] == DATE_OF_BIRTH:
            driver.execute_script("$('#date_of_birth').datepicker('setDate',new Date('01-Jan-2000'))")
        else:
            time.sleep(1)
        time.sleep(1)
        nationality = driver.find_element_by_name("nationality")
        time.sleep(1)
        nationality.send_keys('Nationality')
        time.sleep(1)
        nationality.send_keys(row['nationality'])
        time.sleep(1)
        gender = driver.find_element_by_name("gender")
        time.sleep(1)
        gender.send_keys('Gender')
        time.sleep(1)
        gender.send_keys(row['gender'])
        time.sleep(1)
        religion = driver.find_element_by_name("religion")
        time.sleep(1)
        religion.send_keys('Religion')
        time.sleep(1)
        religion.send_keys(row['religion'])
        time.sleep(1)
        blood_group = driver.find_element_by_name("blood_group")
        time.sleep(1)
        blood_group.clear()
        time.sleep(1)
        blood_group.send_keys(row['blood_group'])
        time.sleep(1)
        driver.switch_to.frame(driver.find_element_by_id('address_ifr'))
        time.sleep(1)
        address = driver.find_element_by_id("tinymce")
        time.sleep(1)
        address.clear()
        time.sleep(1)
        address.send_keys(row['address'])
        time.sleep(1)
        driver.switch_to.default_content()
        time.sleep(1)
        driver.switch_to.frame(driver.find_element_by_id('permanent_address_ifr'))
        time.sleep(1)
        permanent_address = driver.find_element_by_id("tinymce")
        time.sleep(1)
        permanent_address.clear()
        time.sleep(1)
        permanent_address.send_keys(row['permanent_address'])
        time.sleep(1)
        driver.switch_to.default_content()
        time.sleep(1)

        save_button = driver.find_element_by_xpath('//*[@id="details-update-button"]')
        save_button.click()
        time.sleep(1)

    except NoSuchElementException:
        return 1


def prof_edit_profile_education_helper(driver:WebDriver, row):
    driver.refresh()
    time.sleep(DELAY_SHORT)
    try:
        edit_profile_btn = driver.find_element_by_id('edit-profile-details')
        time.sleep(1)
        try:
            edit_profile_btn.click()
            time.sleep(1)
        except:
            time.sleep(1)
        time.sleep(1)
        add_education = driver.find_element_by_id('add-education')
        time.sleep(1)
        add_education.click()
        time.sleep(DELAY_SHORT)
        institution_text = driver.find_element_by_name("institution_text")
        time.sleep(1)
        institution_text.clear()
        time.sleep(1)
        institution_text.send_keys(row['institution_text'])
        time.sleep(1)
        education_level = driver.find_element_by_name("education_level_id")
        time.sleep(1)
        education_level.send_keys('Select Level of education')
        time.sleep(1)
        education_level.send_keys(row['education_level'])
        time.sleep(1)
        degree_text = driver.find_element_by_name("degree_text")
        time.sleep(1)
        degree_text.send_keys(row['degree_text'])
        time.sleep(1)
        cgpa = driver.find_element_by_name("cgpa")
        time.sleep(1)
        cgpa.clear()
        time.sleep(1)
        cgpa.send_keys(row['cgpa'])
        time.sleep(1)
        major_btn = driver.find_element_by_name("major_text")
        time.sleep(1)
        major_btn.send_keys(row['major'])
        time.sleep(1)
        driver.switch_to.frame(driver.find_element_by_id("edu-description_ifr"))
        description = driver.find_element_by_id("tinymce")
        description.clear()
        time.sleep(1)
        description.send_keys(row['description'])
        time.sleep(1)
        driver.switch_to.default_content()
        time.sleep(DELAY_SHORT)
        if row['start_date'] == START_DATE:
            enrolled_btn = driver.find_element_by_name('enrolled_date')
            time.sleep(1)
            enrolled_btn.click()
            time.sleep(1)
            enrolled_month = driver.find_element_by_class_name('ui-datepicker-month')
            time.sleep(1)
            enrolled_month.click()
            time.sleep(1)
            enrolled_year = driver.find_element_by_class_name('ui-datepicker-year')
            enrolled_year.click()
            time.sleep(1)
            enrolled_year_next_btn = driver.find_element_by_class_name('ui-icon-circle-triangle-e')
            enrolled_year_next_btn.click()
            time.sleep(1)
            driver.execute_script("$('#enrolled_date').datepicker('setDate',new Date('01-Jan-2001'))")
        else:
            time.sleep(1)
        time.sleep(DELAY_SHORT)
        if row['end_date'] == ON_GOING:
            ongoing_click = driver.find_element_by_name('is_ongoing')
            ongoing_click.click()
            time.sleep(1)
            try:
                graduation_btn = driver.find_element_by_name('graduation_date')
                graduation_btn.click()
                time.sleep(1)
            except:
                return 0
        elif row['end_date'] == END_DATE:
            graduation_btn = driver.find_element_by_name('graduation_date')
            graduation_btn.click()
            time.sleep(1)
            graduation_month = driver.find_element_by_class_name('ui-datepicker-month')
            graduation_month.click()
            time.sleep(1)
            graduation_year = driver.find_element_by_class_name('ui-datepicker-year')
            graduation_year.click()
            time.sleep(1)
            graduation_year_next_btn = driver.find_element_by_class_name('ui-icon-circle-triangle-e')
            graduation_year_next_btn.click()
            time.sleep(1)
            driver.execute_script("$('#graduation_date').datepicker('setDate',new Date('01-Jan-2005'))")
            time.sleep(1)
        else:
            time.sleep(1)

        save_button = driver.find_element_by_class_name('edu-submit')
        save_button.click()
        time.sleep(1)

    except NoSuchElementException:
        return 1


def prof_edit_profile_work_experience_helper(driver:WebDriver, row):
    driver.refresh()
    time.sleep(DELAY_SHORT)
    try:
        edit_profile_btn = driver.find_element_by_id('edit-profile-details')
        time.sleep(1)
        try:
            edit_profile_btn.click()
            time.sleep(1)
        except:
            time.sleep(1)
        add_experience = driver.find_element_by_id('add-experience')
        time.sleep(1)
        add_experience.click()
        time.sleep(DELAY_SHORT)
        company_text = driver.find_element_by_name("company_text")
        time.sleep(DELAY_SHORT)
        company_text.clear()
        time.sleep(1)
        company_text.send_keys(row['company'])
        time.sleep(1)
        designation = driver.find_element_by_name("designation")
        time.sleep(1)
        designation.clear()
        time.sleep(1)
        designation.send_keys(row['designation'])
        time.sleep(1)
        driver.switch_to.frame(driver.find_element_by_id("wexp-description_ifr"))
        description = driver.find_element_by_id("tinymce")
        description.clear()
        description.send_keys(row['description'])
        driver.switch_to.default_content()
        time.sleep(1)
        time.sleep(DELAY_SHORT)
        if row['start_date'] == START_DATE:
            start_date_btn = driver.find_element_by_name('start_date')
            start_date_btn.click()
            time.sleep(1)
            start_date_month = driver.find_element_by_class_name('ui-datepicker-month')
            start_date_month.click()
            time.sleep(1)
            start_date_year = driver.find_element_by_class_name('ui-datepicker-year')
            start_date_year.click()
            time.sleep(1)
            start_date_year_next_btn = driver.find_element_by_class_name('ui-icon-circle-triangle-e')
            start_date_year_next_btn.click()
            time.sleep(1)
            driver.execute_script("$('#start_date').datepicker('setDate',new Date('01-Jan-2001'))")
        else:
            time.sleep(1)
        time.sleep(DELAY_SHORT)
        if row['end_date'] == CURRENTLY_WORKING:
            is_currently_working = driver.find_element_by_xpath('//*[@id="experience-form"]/div[1]/div[6]/div/div/label/span')
            is_currently_working.click()
            time.sleep(1)
            try:
                end_date_btn = driver.find_element_by_name('end_date')
                end_date_btn.click()
            except:
                return 0
        elif row['end_date'] == END_DATE:
            end_date_btn = driver.find_element_by_name('end_date')
            end_date_btn.click()
            time.sleep(1)
            end_date_month = driver.find_element_by_class_name('ui-datepicker-month')
            end_date_month.click()
            time.sleep(1)
            end_date_year = driver.find_element_by_class_name('ui-datepicker-year')
            end_date_year.click()
            time.sleep(1)
            end_date_year_next_btn = driver.find_element_by_class_name('ui-icon-circle-triangle-e')
            end_date_year_next_btn.click()
            time.sleep(1)
            driver.execute_script("$('#end_date').datepicker('setDate',new Date('01-Jan-2005'))")
            time.sleep(1)
        else:
            time.sleep(1)

        save_button = driver.find_element_by_xpath('//*[@id="experience-form"]/div[2]/div/div/button[1]')
        save_button.click()
        time.sleep(1)

    except NoSuchElementException:
        return 1


def prof_edit_profile_Certification_helper(driver: WebDriver, row):
    driver.refresh()
    time.sleep(DELAY_SHORT)
    try:
        edit_profile_btn = driver.find_element_by_id('edit-profile-details')
        time.sleep(1)
        try:
            edit_profile_btn.click()
            time.sleep(1)
        except:
            time.sleep(1)
        time.sleep(1)
        add_certification = driver.find_element_by_id('add-certification')
        add_certification.click()
        time.sleep(DELAY_SHORT)
        certificate_name = driver.find_element_by_name("certificate_name")
        time.sleep(DELAY_SHORT)
        certificate_name.clear()
        time.sleep(1)
        certificate_name.send_keys(row['certificate_name'])
        time.sleep(1)
        organization = driver.find_element_by_name("organization")
        time.sleep(1)
        organization.clear()
        time.sleep(1)
        organization.send_keys(row['organization'])
        time.sleep(1)
        credential_id = driver.find_element_by_name("credential_id")
        time.sleep(1)
        credential_id.clear()
        time.sleep(1)
        credential_id.send_keys(row['credential_id'])
        time.sleep(1)
        credential_url = driver.find_element_by_name("credential_url")
        time.sleep(1)
        credential_url.clear()
        time.sleep(1)
        credential_url.send_keys(row['credential_url'])
        time.sleep(DELAY_SHORT)
        if row['start_date'] == START_DATE:
            issue_date_btn = driver.find_element_by_name('issue_date')
            issue_date_btn.click()
            time.sleep(1)
            issue_date_month = driver.find_element_by_class_name('ui-datepicker-month')
            issue_date_month.click()
            time.sleep(1)
            issue_date_year = driver.find_element_by_class_name('ui-datepicker-year')
            issue_date_year.click()
            time.sleep(1)
            issue_date_year_next_btn = driver.find_element_by_class_name('ui-icon-circle-triangle-e')
            issue_date_year_next_btn.click()
            time.sleep(1)
            driver.execute_script("$('#issue_date').datepicker('setDate',new Date('01-Jan-2001'))")
        else:
            time.sleep(1)
        time.sleep(DELAY_SHORT)
        if row['end_date'] == END_DATE:
            has_expiry_period = driver.find_element_by_name('has_expiry_period')
            has_expiry_period.click()
            time.sleep(1)
            expiry_date_btn = driver.find_element_by_name('expiry_date')
            expiry_date_btn.click()
            time.sleep(1)
            expiry_date_month = driver.find_element_by_class_name('ui-datepicker-month')
            expiry_date_month.click()
            time.sleep(1)
            expiry_date_year = driver.find_element_by_class_name('ui-datepicker-year')
            expiry_date_year.click()
            time.sleep(1)
            expiry_date_year_next_btn = driver.find_element_by_class_name('ui-icon-circle-triangle-e')
            expiry_date_year_next_btn.click()
            time.sleep(1)
            driver.execute_script("$('#end_date').datepicker('setDate',new Date('01-Jan-2005'))")
            time.sleep(1)

        elif row['end_date'] == NO_EXPIRY_PERIOD:
            try:
                end_date_btn = driver.find_element_by_name('end_date')
                try:
                    end_date_btn.click()
                    return 0
                except:
                    time.sleep(1)
            except:
                return 0
        else:
            time.sleep(1)

        save_button = driver.find_element_by_xpath('//*[@id="certification-form"]/div[2]/div/div/button[1]')
        save_button.click()
        time.sleep(1)
        return 1

    except NoSuchElementException:
        return 0


def prof_edit_profile_Membership_helper(driver: WebDriver, row):
    driver.refresh()
    time.sleep(DELAY_SHORT)
    try:
        edit_profile_btn = driver.find_element_by_id('edit-profile-details')
        time.sleep(1)
        try:
            edit_profile_btn.click()
            time.sleep(1)
        except:
            time.sleep(1)
        time.sleep(1)
        add_membership = driver.find_element_by_id('add-membership')
        add_membership.click()
        time.sleep(DELAY_SHORT)
        membership_organization = driver.find_element_by_id('membership_organization')
        time.sleep(DELAY_SHORT)
        membership_organization.clear()
        time.sleep(1)
        membership_organization.send_keys(row['organization'])
        time.sleep(1)
        position_held = driver.find_element_by_name("position_held")
        time.sleep(1)
        position_held.clear()
        time.sleep(1)
        position_held.send_keys(row['position_held'])
        time.sleep(1)
        driver.switch_to.frame(driver.find_element_by_id("mbr-description_ifr"))
        description = driver.find_element_by_id("tinymce")
        description.clear()
        description.send_keys(row['description'])
        driver.switch_to.default_content()

        time.sleep(DELAY_SHORT)
        if row['start_date'] == START_DATE:
            start_date_mbr_btn = driver.find_element_by_name('start_date_mbr')
            start_date_mbr_btn.click()
            time.sleep(1)
            start_date_mbr_month = driver.find_element_by_class_name('ui-datepicker-month')
            start_date_mbr_month.click()
            time.sleep(1)
            start_date_mbr_year = driver.find_element_by_class_name('ui-datepicker-year')
            start_date_mbr_year.click()
            time.sleep(1)
            start_date_mbr_year_next_btn = driver.find_element_by_class_name('ui-icon-circle-triangle-e')
            start_date_mbr_year_next_btn.click()
            time.sleep(1)
            driver.execute_script("$('#start_date_mbr').datepicker('setDate',new Date('01-Jan-2001'))")
        else:
            time.sleep(1)
        time.sleep(DELAY_SHORT)
        if row['end_date'] == END_DATE:
            end_date_mbr_btn = driver.find_element_by_name('end_date_mbr')
            end_date_mbr_btn.click()
            time.sleep(1)
            end_date_mbr_month = driver.find_element_by_class_name('ui-datepicker-month')
            end_date_mbr_month.click()
            time.sleep(1)
            end_date_mbr_year = driver.find_element_by_class_name('ui-datepicker-year')
            end_date_mbr_year.click()
            time.sleep(1)
            end_date_mbr_year_next_btn = driver.find_element_by_class_name('ui-icon-circle-triangle-e')
            end_date_mbr_year_next_btn.click()
            time.sleep(1)
            driver.execute_script("$('#end_date').datepicker('setDate',new Date('01-Jan-2005'))")
            time.sleep(1)

        elif row['end_date'] == ON_GOING:
            membership_ongoing = driver.find_element_by_name('membership_ongoing')
            membership_ongoing.click()
            time.sleep(1)
            try:
                end_date_mbr_btn = driver.find_element_by_name('end_date_mbr')
                end_date_mbr_btn.click()
            except:
                return 0
        else:
            time.sleep(1)

        save_button = driver.find_element_by_xpath('//*[@id="membership-form"]/div[2]/div/div/button[1]')
        save_button.click()
        time.sleep(1)

    except NoSuchElementException:
        return 1


def prof_edit_profile_skill_helper(driver: WebDriver, row):
    driver.refresh()
    time.sleep(DELAY_SHORT)
    try:
        edit_profile_btn = driver.find_element_by_id('edit-profile-details')
        time.sleep(1)
        try:
            edit_profile_btn.click()
            time.sleep(1)
        except:
            time.sleep(1)
        time.sleep(1)
        add_skill = driver.find_element_by_id('add-skill')
        add_skill.click()
        time.sleep(DELAY_SHORT)
        skill_name = driver.find_element_by_name("skill_name")
        time.sleep(DELAY_SHORT)
        skill_name.send_keys(' ')
        time.sleep(1)
        skill_name.send_keys(row['skill_name'])
        time.sleep(1)
        skill_rating = driver.find_element_by_name("rating")
        time.sleep(1)
        skill_rating.clear()
        time.sleep(1)
        skill_rating.send_keys(row['skill_rating'])
        time.sleep(1)

        save_button = driver.find_element_by_xpath('//*[@id="pro-skill-form"]/div[2]/div/div/button[1]')
        save_button.click()
        time.sleep(1)

    except NoSuchElementException:
        return 1



def prof_edit_profile_portfolio_helper(driver: WebDriver, row):
    driver.refresh()
    time.sleep(DELAY_SHORT)
    try:
        edit_profile_btn = driver.find_element_by_id('edit-profile-details')
        time.sleep(1)
        try:
            edit_profile_btn.click()
            time.sleep(1)
        except:
            time.sleep(1)
        time.sleep(1)
        add_portfolio = driver.find_element_by_id('add-portfolio')
        add_portfolio.click()
        time.sleep(DELAY_SHORT)
        portfolio_name = driver.find_element_by_name("name")
        time.sleep(1)
        portfolio_name.clear()
        time.sleep(1)
        portfolio_name.send_keys(row['name'])
        time.sleep(1)
        # portfolio_image = driver.find_element_by_name("portfolio-image")
        # time.sleep(DELAY_SHORT)
        # portfolio_image.clear()
        # time.sleep(1)
        # portfolio_image.send_keys(row['portfolio_image'])
        # time.sleep(1)
        driver.switch_to.frame(driver.find_element_by_id("port-description_ifr"))
        description = driver.find_element_by_id("tinymce")
        description.clear()
        description.send_keys(row['description'])
        driver.switch_to.default_content()
        time.sleep(1)

        save_button = driver.find_element_by_xpath('//*[@id="portfolio-form"]/div[2]/div/div/button[1]')
        save_button.click()
        time.sleep(1)

    except NoSuchElementException:
        return 1

def prof_edit_profile_reference_helper(driver: WebDriver, row):
    driver.refresh()
    time.sleep(DELAY_SHORT)
    try:
        edit_profile_btn = driver.find_element_by_id('edit-profile-details')
        time.sleep(1)
        try:
            edit_profile_btn.click()
            time.sleep(1)
        except:
            time.sleep(1)
        time.sleep(1)
        add_reference = driver.find_element_by_id('add-reference')
        time.sleep(1)
        add_reference.click()
        time.sleep(DELAY_SHORT)
        driver.switch_to.frame(driver.find_element_by_id("port-description_ifr"))
        time.sleep(1)
        description = driver.find_element_by_id("tinymce")
        time.sleep(1)
        description.clear()
        time.sleep(1)
        description.send_keys(row['description'])
        time.sleep(1)
        driver.switch_to.default_content()
        time.sleep(1)

        save_button = driver.find_element_by_xpath('//*[@id="reference-form"]/div[2]/div/div/button[1]')
        save_button.click()
        time.sleep(1)

    except NoSuchElementException:
        return 1


if __name__ == '__main__':
    unittest.main()