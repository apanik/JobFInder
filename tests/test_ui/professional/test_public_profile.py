import time
import unittest

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.color import Color

# from tests.config import VALID_PRO_USERNAME
from tests.config_web import CHROME_DRIVER_LOCATION, DELAY_SHORT, MAIN_URL, PUBLIC_PROFILE

PROFESSIONAL_NAME = 'Mr Prof Example view'
PROFESSIONAL_FACEBOOK_ID = 'http://facebook.com/example_view'
PROFESSIONAL_TWITTER_ID = 'http://twitter.com/example_twitter'
PROFESSIONAL_LINKEDIN_ID = 'http://linkedin.com/example_linkdin'
FACEBOOK_CSS_COLOR = '#3b5998'
TWITTER_CSS_COLOR = '#00acee'
LINKEDIN_CSS_COLOR = '#0e76a8'
BREADCRUMB_TITLE = 'Public Profile'
PROFILE_PICTURE = f'{MAIN_URL}/media/fd2ab2f8-1fda-4a0d-b40c-a88c30efec47-professional.jpeg'
CERTIFICATION_IMAGE_SRC = f'{MAIN_URL}/static/images/certification-file.svg'
INDUSTRY = "Example Industry One"
CURRENT_COMPANY = "Company Example"
CURRENT_DESIGNATION = "DevOps"
EXPERIENCE = "Experience Example One years"
QUALIFICATION = "Qualification Example One"
LOCATION = "Niketon, Gulshan"


class TestPublicProfile(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = PUBLIC_PROFILE
        cls.driver = webdriver.WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        time.sleep(DELAY_SHORT)

    def test__when_breadcrumb_exists__should_pass(self):
        breadcrumb = self.driver.find_elements_by_class_name('breadcrumb-area')
        self.assertIsNotNone(breadcrumb)

    def test__when_breadcrumb_title_match__should_pass(self):
        breadcrumb_title = self.driver.find_element_by_class_name('page-title').text
        self.assertEqual(BREADCRUMB_TITLE, breadcrumb_title)

    def test__when_breadcrumb_home_link_clickable__should_pass(self):
        home_url = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/a')
        try:
            home_url.click()
        except WebDriverException:
            self.fail("Not Clickable")
        self.driver.back()

    def test__when_click_on_home_url__should_redirect_to_home_page(self):
        home_url = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/a')
        home_url.click()
        time.sleep(DELAY_SHORT)
        current_url = self.driver.current_url
        try:
            self.assertEqual(MAIN_URL + '/', current_url)
        except WebDriverException:
            self.fail("Error")
        self.driver.back()

    def test__when_username_match__should_pass(self):
        name = self.driver.find_element_by_id('name').text
        self.assertEqual(PROFESSIONAL_NAME, name)

    def test__when_facebook_id_match__should_pass(self):
        time.sleep(DELAY_SHORT)
        facebook_id = self.driver.find_element_by_id('facebook').get_attribute('href')
        self.assertEqual(PROFESSIONAL_FACEBOOK_ID, facebook_id)

    def test__when_facebook_id_clickable__should_pass(self):
        facebook_url = self.driver.find_element_by_id('facebook')
        try:
            facebook_url.click()
        except WebDriverException:
            self.fail("Not Clickable")
        self.driver.back()

    def test__when_facebook_css_color_match__should_pass(self):
        facebook = self.driver.find_element_by_xpath('//*[@id="facebook"]/i').value_of_css_property('color')
        facebook_css_color = Color.from_string(facebook).hex
        self.assertEqual(FACEBOOK_CSS_COLOR, facebook_css_color)

    def test__when_twitter_id_match__should_pass(self):
        twitter_id = self.driver.find_element_by_id('twitter').get_attribute('href')
        self.assertEqual(PROFESSIONAL_TWITTER_ID, twitter_id)

    def test__when_twitter_id_clickable__should_pass(self):
        twitter_url = self.driver.find_element_by_id('twitter')
        try:
            twitter_url.click()
        except WebDriverException:
            self.fail("Not Clickable")
        self.driver.back()

    def test__when_twitter_css_color_match__should_pass(self):
        twitter = self.driver.find_element_by_xpath('//*[@id="twitter"]/i').value_of_css_property('color')
        twitter_css_color = Color.from_string(twitter).hex
        self.assertEqual(TWITTER_CSS_COLOR, twitter_css_color)

    def test__when_linkedin_id_match__should_pass(self):
        time.sleep(DELAY_SHORT)
        linkedin_id = self.driver.find_element_by_id('linkedin').get_attribute('href')
        self.assertEqual(PROFESSIONAL_LINKEDIN_ID, linkedin_id)

    def test__when_linkedin_css_color_match__should_pass(self):
        linkedin = self.driver.find_element_by_xpath('//*[@id="linkedin"]/i').value_of_css_property('color')
        linkedin_css_color = Color.from_string(linkedin).hex
        self.assertEqual(LINKEDIN_CSS_COLOR, linkedin_css_color)

    def test__when_linkedin_id_clickable__should_pass(self):
        linkedin_url = self.driver.find_element_by_id('linkedin')
        try:
            linkedin_url.click()
        except WebDriverException:
            self.fail("Not Clickable")
        self.driver.back()

    def test__when__profile_picture_exist__should_pass(self):
        profile_picture = self.driver.find_element_by_xpath('//*[@id="img"]/img')
        self.assertIsNotNone(profile_picture)

    def test__when_profile_picture_match__should_pass(self):
        profile_picture = self.driver.find_element_by_xpath('//*[@id="img"]/img').get_attribute('src')
        self.assertEqual(PROFILE_PICTURE, profile_picture)

    def test__when_user_check_icon_exist_and_match__should_pass(self):
        user_check_icon = self.driver.find_elements_by_class_name('feather-user-check')
        self.assertIsNotNone(user_check_icon)

    def test__when_user_header_basic_info_list_of_content__exist__should_pass(self):
        basic_info_header = self.driver.find_element_by_xpath('//*[@id="about-details-div"]/div/ul').text
        self.assertIsNotNone(basic_info_header)

    def test__when_about_me_label_exist__should_pass(self):
        about_me_label = self.driver.find_element_by_xpath('//*[@id="about-details-div"]/div/ul/span[1]/h8').text
        self.assertIsNotNone(about_me_label)

    def test__when_about_me_paragraph_exist_and_match_should_pass(self):
        about_me_paragraph = self.driver.find_element_by_id('about_me').text
        self.assertIsNotNone(about_me_paragraph)

    def test__when_industry_label_exist__should_pass(self):
        industry_label = self.driver.find_element_by_xpath('//*[@id="ind_exp"]/span[1]/h8').text
        self.assertIsNotNone(industry_label)

    def test__when_industry_value_match__should_pass(self):
        industry = self.driver.find_element_by_id('industry_expertise').text
        self.assertEqual(INDUSTRY, industry)

    def test__when_experience_label_exist__should_pass(self):
        experience_label = self.driver.find_element_by_xpath('//*[@id="exp"]/span[1]/h8').text
        self.assertIsNotNone(experience_label)

    def test__when_experience_value_match__should_pass(self):
        experience = self.driver.find_element_by_id('experience').text
        self.assertEqual(EXPERIENCE, experience)

    def test__when_location_label_exist__should_pass(self):
        location_label = self.driver.find_element_by_xpath('//*[@id="loc"]/span[1]/h8').text
        self.assertIsNotNone(location_label)

    def test__when_location_value_match__should_pass(self):
        location = self.driver.find_element_by_id('address').text
        self.assertEqual(LOCATION, location)

    def test__when_qualification_label_exist__should_pass(self):
        qualification_label = self.driver.find_element_by_xpath('//*[@id="qua"]/span[1]/h8').text
        self.assertIsNotNone(qualification_label)

    def test__when_qualification_value_match__should_pass(self):
        qualification = self.driver.find_element_by_id('qualification').text
        self.assertEqual(QUALIFICATION, qualification)

    def test__when_status_label_exist__should_pass(self):
        status_label = self.driver.find_element_by_xpath('//*[@id="sts"]/span[1]/h8').text
        self.assertIsNotNone(status_label)

    def test__when_current_company_match__should_pass(self):
        current_company = self.driver.find_element_by_id('current_company').text
        self.assertEqual(CURRENT_COMPANY, current_company)

    def test__when_status_value_match__should_pass(self):
        current_designation = self.driver.find_element_by_id('current_designation').text
        self.assertEqual(CURRENT_DESIGNATION, current_designation)

    def test__when_feather_book_icon_exist__should_pass(self):
        feather_book = self.driver.find_elements_by_class_name('feather-book')
        self.assertIsNotNone(feather_book)

    def test__when_feather_book_icon_label_is_education__should_pass(self):
        feather_book_label = self.driver.find_element_by_xpath('//*[@id="edu"]/h4').text
        self.assertEqual("Education",feather_book_label)

    def test__when_eduction_value_exist__should_pass(self):
        education_val = self.driver.find_element_by_class_name('education-label').text
        self.assertIsNotNone(education_val)

    def test__when_feather_briefcase_exist__should_pass(self):
        feather_brief = self.driver.find_element_by_class_name('feather-briefcase')
        self.assertIsNotNone(feather_brief)

    def test__when_feather_brief_label_is_work_experience__should_pass(self):
        feather_brief_label = self.driver.find_element_by_xpath('//*[@id="work"]/h4').text
        self.assertEqual('Work Experience',feather_brief_label)

    def test__when_work_experience_value_exist__should_pass(self):
        work_experience_val = self.driver.find_element_by_id('work').text
        self.assertIsNotNone(work_experience_val)

    def test__when_pro_skills_exist__should_pass(self):
        pro_icon = self.driver.find_element_by_xpath('//*[@id="psks"]/h4/i')
        self.assertIsNotNone(pro_icon)

    def test__when_pro_skills_icon_label_is_professional_skill__should_pass(self):
        pro_icon_label = self.driver.find_element_by_xpath('//*[@id="psks"]/h4').text
        self.assertEqual('Professional Skill',pro_icon_label)

    def test__when_pro_skills_with_rating_exist__should_pass(self):
        pro_skills_val = self.driver.find_element_by_id('pro_skill').text
        self.assertIsNotNone(pro_skills_val)

    def test__when_certification_image_logo_exist__should_pass(self):
        certification_image_src = self.driver.find_element_by_id('certification-logo').get_attribute('src')
        self.assertEqual(CERTIFICATION_IMAGE_SRC,certification_image_src)

    def test__when_certification_label_is_match__should_pass(self):
        certification_label = self.driver.find_element_by_xpath('//*[@id="certificate"]/h4').text
        self.assertEqual("Certification",certification_label)

    def test__when_certification_val_exist__should_pass(self):
        certification_val = self.driver.find_element_by_id('certificate').text
        self.assertIsNotNone(certification_val)

    def test__when_membership_label_match__should_pass(self):
        membership_label = self.driver.find_element_by_xpath('//*[@id="mbrship"]/h4').text
        self.assertEqual('Membership',membership_label)

    def test__when_membership_value_exist__should_pass(self):
        membership_val = self.driver.find_element_by_id('mbrship').text
        self.assertIsNotNone(membership_val)

    def test__when_portfolio_icon_exist__should_pass(self):
        portfolio_icon = self.driver.find_element_by_class_name('feather-gift')
        self.assertIsNotNone(portfolio_icon)

    def test__when_portfolio_label_match__should_pass(self):
        portfolio_val = self.driver.find_element_by_id('pro_portfolio').text
        self.assertIsNotNone(portfolio_val)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
