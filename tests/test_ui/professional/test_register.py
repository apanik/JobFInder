import unittest
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome import webdriver

from tests.config import VALID_PRO_USERNAME
from tests.config_web import CHROME_DRIVER_LOCATION, DELAY_SHORT, MAIN_URL, DELAY_LONG, MAIN_URL_HOME

VALID_PRO_FULL_NAME = 'Testing Name'
INVALID_NUM_ONLY_PRO_FULL_NAME = '11111'
INVALID_SPECIAL_CHAR_PRO_FULL_NAME = '@#!$$&$'
VALID_PRO_NEW_EMAIL = 'testing_example@ishraak.com'
VALID_PRO_MOBILE = '01900000001'
INVALID_SHORT_PRO_MOBILE = '019000'
INVALID_SPECIAL_CHAR_PRO_MOBILE = '#$@$@#$'
VALID_PRO_PASSWORD = '12345678a'
WRONG_PRO_PASSWORD = '12121212b'
EXIST_PRO_USERNAME = VALID_PRO_USERNAME
BLANK_FIELD = ''
INVALID_PRO_PREFIX_USERNAME = 'invalid_example'
INVALID_PRO_PREFIX_WITH_AT_USERNAME = 'invalid_example@'
INVALID_PRO_MID_FIX_USERNAME = 'invalid_example@ishraak'
INVALID_PRO_MID_FIX_WITH_DOT_USERNAME = 'invalid_example@ishraak'

INVALID_PRO_NUM_PASSWORD = '12121212'
INVALID_PRO_LETTER_PASSWORD = 'aaaaaaaa'
INVALID_PRO_NUM_SHORT_PASSWORD = '1212'
INVALID_PRO_LETTER_SHORT_PASSWORD = 'aaaa'
INVALID_PRO_NUM_AND_LETTER_SHORT_PASSWORD = '123a'
SELECT_TERMS_AND_CONDITION = 'on'


class TestProfessionalRegister(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = webdriver.WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        time.sleep(DELAY_SHORT)
        cls.driver.maximize_window()



    def test_register__when_valid__should_successful(self):
        driver = self.driver
        data = {
            'full_name': VALID_PRO_FULL_NAME,
            'email': VALID_PRO_NEW_EMAIL,
            'phone': VALID_PRO_MOBILE,
            'password': VALID_PRO_PASSWORD,
            'confirm_password': VALID_PRO_PASSWORD,
            'terms_and_condition_status': SELECT_TERMS_AND_CONDITION
        }
        register_helper(driver, data)
        time.sleep(DELAY_LONG)
        try:
            success = driver.find_element_by_class_name('green-color').text
            self.assertIsNotNone(success)
        except NoSuchElementException:
            self.fail('Not ok')


    def test_register__when_all_fields_are_empty__should__unsuccessful(self):
        driver = self.driver
        data = {
            'full_name': BLANK_FIELD,
            'email': BLANK_FIELD,
            'phone': BLANK_FIELD,
            'password': BLANK_FIELD,
            'confirm_password': BLANK_FIELD,
            'terms_and_condition_status': BLANK_FIELD
        }
        register_helper(driver, data)
        try:
            success = driver.find_element_by_class_name('green-color').text
            self.assertIsNone(success)
        except NoSuchElementException:
            pass


    def test_register__when_name_field_is_empty__should_unsuccessful(self):
        driver = self.driver
        data = {
            'full_name': BLANK_FIELD,
            'email': VALID_PRO_NEW_EMAIL,
            'phone': VALID_PRO_MOBILE,
            'password': VALID_PRO_PASSWORD,
            'confirm_password': VALID_PRO_PASSWORD,
            'terms_and_condition_status': SELECT_TERMS_AND_CONDITION
        }
        register_helper(driver, data)
        try:
            success = driver.find_element_by_class_name('green-color').text
            self.assertIsNone(success)
        except NoSuchElementException:
            pass


    def test_register__when_email_field_is_empty__should_unsuccessful(self):
        driver = self.driver
        data = {
            'full_name': VALID_PRO_FULL_NAME,
            'email': BLANK_FIELD,
            'phone': VALID_PRO_MOBILE,
            'password': VALID_PRO_PASSWORD,
            'confirm_password': VALID_PRO_PASSWORD,
            'terms_and_condition_status': SELECT_TERMS_AND_CONDITION
        }
        register_helper(driver, data)
        try:
            success = driver.find_element_by_class_name('green-color').text
            self.assertIsNone(success)
        except NoSuchElementException:
            pass


    def test_register__when_mobile_field_is_empty__should_unsuccessful(self):
        driver = self.driver
        data = {
            'full_name': VALID_PRO_FULL_NAME,
            'email': VALID_PRO_NEW_EMAIL,
            'phone': BLANK_FIELD,
            'password': VALID_PRO_PASSWORD,
            'confirm_password': VALID_PRO_PASSWORD,
            'terms_and_condition_status': SELECT_TERMS_AND_CONDITION
        }
        register_helper(driver, data)
        try:
            success = driver.find_element_by_class_name('green-color').text
            self.assertIsNone(success)
        except NoSuchElementException:
            pass


    def test_register__when_password_field_is_empty__should_unsuccessful(self):
        driver = self.driver
        data = {
            'full_name': VALID_PRO_FULL_NAME,
            'email': VALID_PRO_NEW_EMAIL,
            'phone': VALID_PRO_MOBILE,
            'password': BLANK_FIELD,
            'confirm_password': VALID_PRO_PASSWORD,
            'terms_and_condition_status': SELECT_TERMS_AND_CONDITION
        }
        register_helper(driver, data)
        try:
            success = driver.find_element_by_class_name('green-color').text
            self.assertIsNone(success)
        except NoSuchElementException:
            pass


    def test_register__when_confirm_password_is_empty__should_unsuccessful(self):
        driver = self.driver
        data = {
            'full_name': VALID_PRO_FULL_NAME,
            'email': VALID_PRO_NEW_EMAIL,
            'phone': VALID_PRO_MOBILE,
            'password': VALID_PRO_PASSWORD,
            'confirm_password': BLANK_FIELD,
            'terms_and_condition_status': SELECT_TERMS_AND_CONDITION
        }
        register_helper(driver, data)
        try:
            success = driver.find_element_by_class_name('green-color').text
            self.assertIsNone(success)
        except NoSuchElementException:
            pass


    def test_register__when_terms_and_condition_is_not_checked__should_unsuccessful(self):
        driver = self.driver
        data = {
            'full_name': VALID_PRO_FULL_NAME,
            'email': VALID_PRO_NEW_EMAIL,
            'phone': VALID_PRO_MOBILE,
            'password': VALID_PRO_PASSWORD,
            'confirm_password': VALID_PRO_PASSWORD,
            'terms_and_condition_status': BLANK_FIELD
        }
        register_helper(driver, data)
        try:
            success = driver.find_element_by_class_name('green-color').text
            self.assertIsNone(success)
        except NoSuchElementException:
            pass


    def test_register__when_only_name_field_has_value__should_unsuccessful(self):
        driver = self.driver
        data = {
            'full_name': VALID_PRO_FULL_NAME,
            'email': BLANK_FIELD,
            'phone': BLANK_FIELD,
            'password': BLANK_FIELD,
            'confirm_password': BLANK_FIELD,
            'terms_and_condition_status': BLANK_FIELD
        }
        register_helper(driver, data)
        try:
            success = driver.find_element_by_class_name('green-color').text
            self.assertIsNone(success)
        except NoSuchElementException:
            pass


    def test_register__when_only_email_field_has_value__should_unsuccessful(self):
        driver = self.driver
        data = {
            'full_name': BLANK_FIELD,
            'email': VALID_PRO_NEW_EMAIL,
            'phone': BLANK_FIELD,
            'password': BLANK_FIELD,
            'confirm_password': BLANK_FIELD,
            'terms_and_condition_status': BLANK_FIELD
        }
        register_helper(driver, data)
        try:
            success = driver.find_element_by_class_name('green-color').text
            self.assertIsNone(success)
        except NoSuchElementException:
            pass


    def test_register__when_only_phone_field_has_value__should_unsuccessful(self):
        driver = self.driver
        data = {
            'full_name': BLANK_FIELD,
            'email': BLANK_FIELD,
            'phone': VALID_PRO_MOBILE,
            'password': BLANK_FIELD,
            'confirm_password': BLANK_FIELD,
            'terms_and_condition_status': BLANK_FIELD
        }
        register_helper(driver, data)
        try:
            success = driver.find_element_by_class_name('green-color').text
            self.assertIsNone(success)
        except NoSuchElementException:
            pass


    def test_register__when_only_password_field_has_value__should_unsuccessful(self):
        driver = self.driver
        data = {
            'full_name': BLANK_FIELD,
            'email': BLANK_FIELD,
            'phone': BLANK_FIELD,
            'password': VALID_PRO_PASSWORD,
            'confirm_password': BLANK_FIELD,
            'terms_and_condition_status': BLANK_FIELD
        }
        register_helper(driver, data)
        try:
            success = driver.find_element_by_class_name('green-color').text
            self.assertIsNone(success)
        except NoSuchElementException:
            pass


    def test_register__when_only_confirm_password_field_has_value__should_unsuccessful(self):
        driver = self.driver
        data = {
            'full_name': BLANK_FIELD,
            'email': BLANK_FIELD,
            'phone': BLANK_FIELD,
            'password': BLANK_FIELD,
            'confirm_password': VALID_PRO_PASSWORD,
            'terms_and_condition_status': BLANK_FIELD
        }
        register_helper(driver, data)
        try:
            success = driver.find_element_by_class_name('green-color').text
            self.assertIsNone(success)
        except NoSuchElementException:
            pass


    def test_register__when_only_terms_and_condition_is_checked__should_unsuccessful(self):
        driver = self.driver
        data = {
            'full_name': BLANK_FIELD,
            'email': BLANK_FIELD,
            'phone': BLANK_FIELD,
            'password': BLANK_FIELD,
            'confirm_password': BLANK_FIELD,
            'terms_and_condition_status': SELECT_TERMS_AND_CONDITION
        }
        register_helper(driver, data)
        try:
            success = driver.find_element_by_class_name('green-color').text
            self.assertIsNone(success)
        except NoSuchElementException:
            pass


    def test_register__when_email_has_only_prefix__should_unsuccessful(self):
        driver = self.driver
        data = {
            'full_name': VALID_PRO_FULL_NAME,
            'email': INVALID_PRO_PREFIX_USERNAME,
            'phone': VALID_PRO_MOBILE,
            'password': VALID_PRO_PASSWORD,
            'confirm_password': VALID_PRO_PASSWORD,
            'terms_and_condition_status': SELECT_TERMS_AND_CONDITION
        }
        register_helper(driver, data)
        try:
            success = driver.find_element_by_class_name('green-color').text
            self.assertIsNone(success)
        except NoSuchElementException:
            pass


    def test_register__when_email_has_prefix_with_at__should_unsuccessful(self):
        driver = self.driver
        data = {
            'full_name': VALID_PRO_FULL_NAME,
            'email': INVALID_PRO_PREFIX_WITH_AT_USERNAME,
            'phone': VALID_PRO_MOBILE,
            'password': VALID_PRO_PASSWORD,
            'confirm_password': VALID_PRO_PASSWORD,
            'terms_and_condition_status': SELECT_TERMS_AND_CONDITION
        }
        register_helper(driver, data)
        try:
            success = driver.find_element_by_class_name('green-color').text
            self.assertIsNone(success)
        except NoSuchElementException:
            pass


    def test_register__when_email_has_midfix__should_unsuccessful(self):
        driver = self.driver
        data = {
            'full_name': VALID_PRO_FULL_NAME,
            'email': INVALID_PRO_MID_FIX_USERNAME,
            'phone': VALID_PRO_MOBILE,
            'password': VALID_PRO_PASSWORD,
            'confirm_password': VALID_PRO_PASSWORD,
            'terms_and_condition_status': SELECT_TERMS_AND_CONDITION
        }
        register_helper(driver, data)
        try:
            success = driver.find_element_by_class_name('green-color').text
            self.assertIsNone(success)
        except NoSuchElementException:
            pass


    def test_register__when_email_has_midfix_with_dot__should_unsuccessful(self):
        driver = self.driver
        data = {
            'full_name': VALID_PRO_FULL_NAME,
            'email': INVALID_PRO_MID_FIX_WITH_DOT_USERNAME,
            'phone': VALID_PRO_MOBILE,
            'password': VALID_PRO_PASSWORD,
            'confirm_password': VALID_PRO_PASSWORD,
            'terms_and_condition_status': SELECT_TERMS_AND_CONDITION
        }
        register_helper(driver, data)
        try:
            success = driver.find_element_by_class_name('green-color').text
            self.assertIsNone(success)
        except NoSuchElementException:
            pass


    def test_register__when_password_is_number_only__should_unsuccessful(self):
        driver = self.driver
        data = {
            'full_name': VALID_PRO_FULL_NAME,
            'email': VALID_PRO_NEW_EMAIL,
            'phone': VALID_PRO_MOBILE,
            'password': INVALID_PRO_NUM_PASSWORD,
            'confirm_password': INVALID_PRO_NUM_PASSWORD,
            'terms_and_condition_status': SELECT_TERMS_AND_CONDITION
        }
        register_helper(driver, data)
        try:
            success = driver.find_element_by_class_name('green-color').text
            self.assertIsNone(success)
        except NoSuchElementException:
            pass


    def test_register__when_password_is_letter_only__should_unsuccessful(self):
        driver = self.driver
        data = {
            'full_name': VALID_PRO_FULL_NAME,
            'email': VALID_PRO_NEW_EMAIL,
            'phone': VALID_PRO_MOBILE,
            'password': INVALID_PRO_LETTER_PASSWORD,
            'confirm_password': INVALID_PRO_LETTER_PASSWORD,
            'terms_and_condition_status': SELECT_TERMS_AND_CONDITION
        }
        register_helper(driver, data)
        try:
            success = driver.find_element_by_class_name('green-color').text
            self.assertIsNone(success)
        except NoSuchElementException:
            pass


    def test_register__when_password_is_short_number_only__should_unsuccessful(self):
        driver = self.driver
        data = {
            'full_name': VALID_PRO_FULL_NAME,
            'email': VALID_PRO_NEW_EMAIL,
            'phone': VALID_PRO_MOBILE,
            'password': INVALID_PRO_NUM_SHORT_PASSWORD,
            'confirm_password': INVALID_PRO_NUM_SHORT_PASSWORD,
            'terms_and_condition_status': SELECT_TERMS_AND_CONDITION
        }
        register_helper(driver, data)
        try:
            success = driver.find_element_by_class_name('green-color').text
            self.assertIsNone(success)
        except NoSuchElementException:
            pass


    def test_register__when_password_is_short_and_letters_only__should_unsuccessful(self):
        driver = self.driver
        data = {
            'full_name': VALID_PRO_FULL_NAME,
            'email': VALID_PRO_NEW_EMAIL,
            'phone': VALID_PRO_MOBILE,
            'password': INVALID_PRO_LETTER_SHORT_PASSWORD,
            'confirm_password': INVALID_PRO_LETTER_SHORT_PASSWORD,
            'terms_and_condition_status': SELECT_TERMS_AND_CONDITION
        }
        register_helper(driver, data)
        try:
            success = driver.find_element_by_class_name('green-color').text
            self.assertIsNone(success)
        except NoSuchElementException:
            pass


    def test_register__when_password_is_short_with_number_and_letter__should_unsuccessful(self):
        driver = self.driver
        data = {
            'full_name': VALID_PRO_FULL_NAME,
            'email': VALID_PRO_NEW_EMAIL,
            'phone': VALID_PRO_MOBILE,
            'password': INVALID_PRO_NUM_AND_LETTER_SHORT_PASSWORD,
            'confirm_password': INVALID_PRO_NUM_AND_LETTER_SHORT_PASSWORD,
            'terms_and_condition_status': SELECT_TERMS_AND_CONDITION
        }
        register_helper(driver, data)
        try:
            success = driver.find_element_by_class_name('green-color').text
            self.assertIsNone(success)
        except NoSuchElementException:
            pass


    def test_register__when_password_and_confirm_password_mismatched__should_unsuccessful(self):
        driver = self.driver
        data = {
            'full_name': BLANK_FIELD,
            'email': VALID_PRO_NEW_EMAIL,
            'phone': VALID_PRO_MOBILE,
            'password': VALID_PRO_PASSWORD,
            'confirm_password': WRONG_PRO_PASSWORD,
            'terms_and_condition_status': SELECT_TERMS_AND_CONDITION
        }
        register_helper(driver, data)
        try:
            success = driver.find_element_by_class_name('green-color').text
            self.assertIsNone(success)
        except NoSuchElementException:
            pass


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


def register_helper(driver, row):
    driver.refresh()
    time.sleep(DELAY_SHORT)
    try:
        try:
            register = driver.find_element_by_id('register')
            time.sleep(1)
            register.click()
            time.sleep(DELAY_SHORT)
        except:
            time.sleep(1)
        name = driver.find_element_by_name('full_name')
        name.clear()
        time.sleep(1)
        name.send_keys(row['full_name'])
        time.sleep(1)

        email = driver.find_element_by_name('email')
        email.clear()
        time.sleep(1)
        email.send_keys(row['email'])
        time.sleep(1)

        phone = driver.find_element_by_name('phone')
        phone.clear()
        time.sleep(1)
        phone.send_keys(row['phone'])
        time.sleep(1)

        password = driver.find_element_by_id('password')
        password.clear()
        time.sleep(1)
        password.send_keys(row['password'])
        time.sleep(1)

        con_password = driver.find_element_by_name('confirm_password')
        con_password.clear()
        time.sleep(1)
        con_password.send_keys(row['confirm_password'])
        time.sleep(1)

        accept = driver.find_element_by_class_name('dot')
        time.sleep(1)
        if row['terms_and_condition_status'] == SELECT_TERMS_AND_CONDITION:
            accept.click()

        time.sleep(1)
        save = driver.find_element_by_id('registerBtn')
        save.submit()
        time.sleep(DELAY_LONG)

    except NoSuchElementException:
        return 1


if __name__ == '__main__':
    unittest.main()