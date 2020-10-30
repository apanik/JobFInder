import time
import unittest

from selenium.webdriver.chrome import webdriver

from tests.config import VALID_PRO_USERNAME
from tests.config_web import CHROME_DRIVER_LOCATION, DELAY_SHORT, MAIN_URL, MAIN_URL_HOME


class TestResetPassword(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = webdriver.WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        cls.driver.find_element_by_id('sign-in').click()
        time.sleep(DELAY_SHORT)
        cls.driver.find_element_by_xpath('//*[@id="sign-in"]/div[3]/a').click()
        time.sleep(DELAY_SHORT)

    def test__when_email_invalid__should__fail(self):
        INVALID_PRO_USERNAME = "Invalid_Example@Ishraak.com"
        self.driver.find_element_by_id('email').send_keys(INVALID_PRO_USERNAME)
        self.driver.find_element_by_xpath('//*[@id="reset-password-button"]').click()
        time.sleep(DELAY_SHORT)
        error_message = self.driver.find_elements_by_class_name('pt')
        self.assertIsNotNone(error_message)

    def test__when_email_postfix_not_valid__should_fail(self):
        INVALID_PRO_USERNAME = "Invalid_Example"
        self.driver.refresh()
        self.driver.find_element_by_id('email').send_keys(INVALID_PRO_USERNAME)
        self.driver.find_element_by_xpath('//*[@id="reset-password-button"]').click()
        time.sleep(DELAY_SHORT)
        error_message = self.driver.find_elements_by_class_name('pt')
        self.assertIsNotNone(error_message)

    def test__when_email_field_empty__should_fail(self):
        INVALID_PRO_USERNAME = ""
        self.driver.refresh()
        self.driver.find_element_by_id('email').send_keys(INVALID_PRO_USERNAME)
        self.driver.find_element_by_xpath('//*[@id="reset-password-button"]').click()
        time.sleep(DELAY_SHORT)
        error_message = self.driver.find_elements_by_class_name('pt')
        self.assertIsNotNone(error_message)

    def test__when_valid__should_pass(self):
        self.driver.refresh()
        self.driver.find_element_by_id('email').send_keys(VALID_PRO_USERNAME)
        self.driver.find_element_by_xpath('//*[@id="reset-password-button"]').click()
        time.sleep(DELAY_SHORT)
        success_message = self.driver.find_elements_by_class_name('green-color')
        self.assertIsNotNone(success_message)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
