import time
import unittest

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from tests.config import VALID_PRO_VIEW_USERNAME, VALID_PRO_VIEW_PASSWORD
from tests.config_web import CHROME_DRIVER_LOCATION, DELAY_SHORT, MAIN_URL, MAIN_URL_HOME
from tests.test_ui.professional.test_signin import signin_helper

image_details = f'{MAIN_URL_HOME}/media/fd2ab2f8-1fda-4a0d-b40c-a88c30efec47-professional.jpeg'
facebook_details = ("http://facebook.com/example_view")
linkdin_details = ("http://linkedin.com/example_linkdin")
twitter_details = ("http://twitter.com/example_twitter")
basic_details = (
    "About Me:\n"
    "Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. \n"
    "Test about me. Test about me. \n"
    "Test about me. Test about me. \n"
    "Test about me. \n"
     "  Industry: Example Industry One\n"
    "Location: Current Location\n"
    "Years of Experience: Experience Example One years\n"
    "Qualification: Qualification Example One\n"
    "Mobile number: 01900000001\n"
    "Company: Company Example\n"
    "Designation: DevOps"
)
education_details = (
    "01/01/2020 - 18/07/2020\n"
    "Education Level Example One in Qualification Example One@Institution example one, CGPA: 4,00\n"
    "Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. \n"
    "Test about me. Test about me. \n"
    "Test about me. Test about me. \n"
    "Test about me. "
)
experiance_details = (
    "01/01/2020 - 18/07/2020\n"
    "DevOps@Company Example\n"
    "Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. \n"
    "Test about me. Test about me. \n"
    "Test about me. Test about me. \n"
    "Test about me. "
)
skill_details = (
    "HTML\n"
    "5/10\n"
    "Django\n"
    "4/10\n"
    "Python\n"
    "7/10\n"
    "CSS\n"
    "4/10"
)
certification_details = (
    "01/01/2020 - No Expiry Period\n"
    "Example certification@Example organization"
)
membership_details = (
    "01/01/2020 - 18/07/2020\n"
    "Member@Example organization\n"
    "Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. \n"
    "Test about me. Test about me. \n"
    "Test about me. Test about me. \n"
    "Test about me. "
)
portfolio_details = (
    "Example Portfolio\n"
    "Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. Test about me. \n"
    "Test about me. Test about me. \n"
    "Test about me. Test about me. \n"
    "Test about me. "
)
personal_details = (
"Full Name:Mr Prof Example view\n"
"Father's Name: Mr pro view father\n"
"Mother's Name: Mrs pro view mother\n"
"Date of Birth: 01/01/2020\n"
"Nationality: Bangladeshi\n"
"Gender: Male\n"
"Religion: Islam\n"
"Blood Group: A+\n"
"Address:\n"
"Niketon, Gulshan\n"
"Permanent Address:\n"
"Niketon, Gulshan, Dhaka, Bangladesh"
)

class TestProfessionalViewProfile(unittest.TestCase):


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

    def test_view_profile__when_show_all_valid_data__should_pss(self):
        driver = self.driver
        time.sleep(DELAY_SHORT)
        try:
            edit_profile_btn = driver.find_element_by_id('edit-profile-details')
            try:
                edit_profile_btn.click()
                time.sleep(1)
            except:
                time.sleep(1)
            time.sleep(1)
            user_info = driver.find_element_by_class_name('user-info')
            image = driver.find_element_by_id('image1').get_attribute('src')
            prof_image = user_info.find_element_by_tag_name('img').get_attribute('src')
            #print(prof_image)
            self.assertEqual(prof_image, image_details)

            # image link become so big for this
            # self.assertEqual(image, image_details)
            facebook = driver.find_element_by_class_name('facebook').get_attribute('href')
            linkedin = driver.find_element_by_class_name('linkedin').get_attribute('href')
            twitter = driver.find_element_by_class_name('twitter').get_attribute('href')
            basic_info = driver.find_element_by_xpath('//*[@id="about-details-div"]/div/ul').text
            education = driver.find_element_by_class_name('education-label').text
            experiance = driver.find_element_by_class_name('experience-section').text
            skill = driver.find_element_by_id('skill-label').text
            certification = driver.find_element_by_class_name('certification-label').text
            membership = driver.find_element_by_class_name('membership-label').text
            portfolio = driver.find_element_by_class_name('portfolio-section').text
            personal = driver.find_element_by_xpath('//*[@id="personal-information-div"]/div/ul').text

            self.assertEqual(facebook, facebook_details)
            self.assertEqual(linkedin, linkdin_details)
            self.assertEqual(twitter, twitter_details)
            self.assertEqual(basic_info, basic_details)
            self.assertEqual(education, education_details)
            self.assertEqual(experiance, experiance_details)
            self.assertEqual(skill, skill_details)
            self.assertEqual(certification, certification_details)
            self.assertEqual(membership, membership_details)
            self.assertEqual(portfolio, portfolio_details)
            self.assertEqual(personal, personal_details)

        except NoSuchElementException:
            self.fail('Not ok')


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit



def pro_viw_profile_helper(driver,row):
    try:

        sign_in = driver.find_element_by_id("sign-in")
        sign_in.click()
        time.sleep(DELAY_SHORT)
        name = driver.find_element_by_name("email")
        name.clear()
        name.send_keys(row['email'])
        password = driver.find_element_by_name("password")
        password.clear()
        password.send_keys(row['password'])
        submit_button = driver.find_element_by_id('edit-profile-details')
        submit_button.click()
        time.sleep(DELAY_SHORT)
        time.sleep(1)
        view_profile = driver.find_element_by_id('profile-details')
        view_profile.click()
        time.sleep(3)

    except NoSuchElementException:
        return 1


if __name__ == '__main__':
    unittest.main()