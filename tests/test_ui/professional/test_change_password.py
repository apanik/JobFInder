import time
import unittest

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome import webdriver

from tests.config import VALID_PRO_USERNAME, VALID_PRO_PASSWORD
from tests.config_web import CHROME_DRIVER_LOCATION,  DELAY_SHORT, MAIN_URL_HOME

INVALID_PRO_PASSWORD = "123456789"
spec_PRO_PASSWORD = "123456789"
BLANK_PASSWORD = ""
BLANK_SPACE_PASSWORD = "        "


class TestProfessionalChangePassword(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = webdriver.WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        time.sleep(DELAY_SHORT)
        cls.driver.maximize_window()



    def test_change_password__when_valid__should_pass(self):
        driver = self.driver
        data = {
            "email" : VALID_PRO_USERNAME,
            "password" : VALID_PRO_PASSWORD,
            "current_password" : VALID_PRO_PASSWORD,
            "new_password" : VALID_PRO_PASSWORD,
            "conf_password" : VALID_PRO_PASSWORD
        }
        change_pass_helper(driver,data)
        try:
            time.sleep(DELAY_SHORT)
            success = driver.find_element_by_class_name('green-color')
            time.sleep(1)
            ok_btn = driver.find_element_by_link_text('Okay')
            ok_btn.click()
            self.assertIsNotNone(success)
        except NoSuchElementException:
            self.fail('Not ok')


    def test_change_password__when_invalid_new_password__should_fail(self):
        driver= self.driver
        data = {
            "email" : VALID_PRO_USERNAME,
            "password" : VALID_PRO_PASSWORD,
            "current_password" : VALID_PRO_PASSWORD,
            "new_password" : INVALID_PRO_PASSWORD,
            "conf_password" : VALID_PRO_PASSWORD

        }
        change_pass_helper(driver,data)
        try:
            success = driver.find_element_by_class_name('green-color')
            time.sleep(1)
            ok_btn = driver.find_element_by_link_text('Okay')
            ok_btn.click()
            self.fail('Not ok')
        except NoSuchElementException:
            pass


    def test_change_password__when_blank_current_password__should_fail(self):
        driver= self.driver
        data = {
            "email" : VALID_PRO_USERNAME,
            "password" : VALID_PRO_PASSWORD,
            "current_password" : BLANK_PASSWORD,
            "new_password" : INVALID_PRO_PASSWORD,
            "conf_password" : VALID_PRO_PASSWORD

        }
        change_pass_helper(driver,data)
        try:
            success = driver.find_element_by_class_name('green-color')
            time.sleep(1)
            ok_btn = driver.find_element_by_link_text('Okay')
            ok_btn.click()
            self.fail('Not ok')
        except NoSuchElementException:
            pass



    def test_change_password__when_blank_new_password__should_fail(self):
        driver= self.driver
        data = {
            "email" : VALID_PRO_USERNAME,
            "password" : VALID_PRO_PASSWORD,
            "current_password" : VALID_PRO_PASSWORD,
            "new_password" : BLANK_PASSWORD,
            "conf_password" : VALID_PRO_PASSWORD

        }
        change_pass_helper(driver,data)
        try:
            success = driver.find_element_by_class_name('green-color')
            time.sleep(1)
            ok_btn = driver.find_element_by_link_text('Okay')
            ok_btn.click()
            self.fail('Not ok')
        except NoSuchElementException:
            pass



    def test_change_password__when_blank_conf_password__should_fail(self):
        driver= self.driver
        data = {
            "email" : VALID_PRO_USERNAME,
            "password" : VALID_PRO_PASSWORD,
            "current_password" : VALID_PRO_PASSWORD,
            "new_password" : VALID_PRO_PASSWORD,
            "conf_password" : BLANK_PASSWORD

        }
        change_pass_helper(driver,data)
        try:
            success = driver.find_element_by_class_name('green-color')
            time.sleep(1)
            ok_btn = driver.find_element_by_link_text('Okay')
            ok_btn.click()
            self.fail('Not ok')
        except NoSuchElementException:
            pass




    def test_change_password__when_blank_new_and_conf_password__should_fail(self):
        driver= self.driver
        data = {
            "email" : VALID_PRO_USERNAME,
            "password" : VALID_PRO_PASSWORD,
            "current_password" : VALID_PRO_PASSWORD,
            "new_password" : BLANK_PASSWORD,
            "conf_password" : BLANK_PASSWORD

        }
        change_pass_helper(driver,data)
        try:
            success = driver.find_element_by_class_name('green-color')
            time.sleep(1)
            ok_btn = driver.find_element_by_link_text('Okay')
            ok_btn.click()
            self.fail('Not ok')
        except NoSuchElementException:
            pass


    def test_change_password__when_blank_all_field_password__should_fail(self):
        driver= self.driver
        data = {
            "email" : VALID_PRO_USERNAME,
            "password" : VALID_PRO_PASSWORD,
            "current_password" : BLANK_PASSWORD,
            "new_password" : BLANK_PASSWORD,
            "conf_password" : BLANK_PASSWORD

        }
        change_pass_helper(driver,data)
        try:
            success = driver.find_element_by_class_name('green-color')
            time.sleep(1)
            ok_btn = driver.find_element_by_link_text('Okay')
            ok_btn.click()
            self.fail('Not ok')
        except NoSuchElementException:
            pass


    def test_change_password__when_blank_space_new_and_conf_password__should_fail(self):
        driver= self.driver
        data = {
            "email" : VALID_PRO_USERNAME,
            "password" : VALID_PRO_PASSWORD,
            "current_password" : VALID_PRO_PASSWORD,
            "new_password" : BLANK_SPACE_PASSWORD,
            "conf_password" : BLANK_SPACE_PASSWORD

        }
        change_pass_helper(driver,data)
        try:
            success = driver.find_element_by_class_name('green-color')
            time.sleep(1)
            ok_btn = driver.find_element_by_link_text('Okay')
            ok_btn.click()
            self.fail('Not ok')
        except NoSuchElementException:
            pass


    def test_change_password__when_invalid_con_password__should_fail(self):
        driver= self.driver
        data = {
            "email" : VALID_PRO_USERNAME,
            "password" : VALID_PRO_PASSWORD,
            "current_password" : VALID_PRO_PASSWORD,
            "new_password" : VALID_PRO_PASSWORD,
            "conf_password" : INVALID_PRO_PASSWORD

        }
        change_pass_helper(driver,data)
        try:
            success = driver.find_element_by_class_name('green-color')
            time.sleep(1)
            ok_btn = driver.find_element_by_link_text('Okay')
            ok_btn.click()
            self.fail('Not ok')
        except NoSuchElementException:
            pass



    def test_change_password__when_invalid__should_fail(self):
        driver= self.driver
        data = {
            "email" : VALID_PRO_USERNAME,
            "password" : VALID_PRO_PASSWORD,
            "current_password" : VALID_PRO_PASSWORD,
            "new_password" : INVALID_PRO_PASSWORD,
            "conf_password" : INVALID_PRO_PASSWORD

        }
        change_pass_helper(driver,data)
        try:
            success = driver.find_element_by_class_name('green-color')
            time.sleep(1)
            ok_btn = driver.find_element_by_link_text('Okay')
            ok_btn.click()
            self.fail('Not ok')
        except NoSuchElementException:
            pass


    def test_change_password__when_invalid_current_password__should_fail(self):
        driver= self.driver
        data = {
            "email" : VALID_PRO_USERNAME,
            "password" : VALID_PRO_PASSWORD,
            "current_password" : INVALID_PRO_PASSWORD,
            "new_password" : VALID_PRO_PASSWORD,
            "conf_password" : VALID_PRO_PASSWORD

        }
        change_pass_helper(driver,data)
        try:
            success = driver.find_element_by_class_name('green-color')
            time.sleep(1)
            ok_btn = driver.find_element_by_link_text('Okay')
            ok_btn.click()
            self.fail('Not ok')
        except NoSuchElementException:
            pass


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


def change_pass_helper(driver,row):
    try:
        try:
            sign_in = driver.find_element_by_id("sign-in")
            sign_in.click()
            time.sleep(4)
            name = driver.find_element_by_name("email")
            name.clear()
            time.sleep(1)
            name.send_keys(row['email'])
            time.sleep(1)
            password = driver.find_element_by_name("password")
            password.clear()
            time.sleep(1)
            password.send_keys(row['password'])
            time.sleep(1)
            submit_button = driver.find_element_by_id('signinButton')
            submit_button.click()
            time.sleep(DELAY_SHORT)
            action_button = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[6]/button')
            action_button.click()
            time.sleep(DELAY_SHORT)
            change_password = driver.find_element_by_link_text('Change Password')
            change_password.click()
            time.sleep(DELAY_SHORT)
        except:
            time.sleep(1)

        current_password = driver.find_element_by_name('old_password')
        current_password.clear()
        current_password.send_keys(row['current_password'])
        time.sleep(DELAY_SHORT)
        new_password = driver.find_element_by_name('new_password')
        new_password.clear()
        new_password.send_keys(row['new_password'])
        time.sleep(DELAY_SHORT)
        conf_new_password = driver.find_element_by_name('confirm_password')
        conf_new_password.clear()
        conf_new_password.send_keys(row['conf_password'])
        time.sleep(DELAY_SHORT)
        save_change_button = driver.find_element_by_id('changePasswordBtn')
        save_change_button.click()
        time.sleep(DELAY_SHORT)

    except NoSuchElementException:
        return 1


if __name__ == '__main__':
    unittest.main()