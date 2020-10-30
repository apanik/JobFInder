import time
import unittest

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome import webdriver

from tests.config import VALID_PRO_USERNAME, VALID_PRO_PASSWORD, VALID_COM_USERNAME, VALID_COM_PASSWORD
from tests.config_web import PRO_SIGNIN_URL, CHROME_DRIVER_LOCATION, DELAY_SHORT, MAIN_URL, MAIN_URL_HOME, DELAY_LONG

WRONG_COM_PASSWORD = '12121212b'
INVALID_COM_USERNAME = 'invalid_example@ishraak.com'
BLANK_USERNAME = ''
BLANK_PASSWORD = ''

class TestCompanylSignIn(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = webdriver.WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        time.sleep(DELAY_SHORT)
        cls.driver.maximize_window()

    def test_signin__when_valid__should_signin(self):    # menu = driver.find_element_by_class_name('navbar-toggler-icon').click()
        driver= self.driver
        data = {
            "email" : VALID_COM_USERNAME,
            "password" : VALID_COM_PASSWORD

        }
        signin_helper_company(driver,data)
        try:
            time.sleep(1)
            menu = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[6]/button')
            menu.click()
            time.sleep(1)
            signout = driver.find_element_by_xpath('//*[@id="userNavbarMain"]/ul/li[3]/a/span')
            signout.click()
            time.sleep(DELAY_SHORT)
            self.assertIsNotNone(menu)

        except NoSuchElementException:
            self.fail('Not ok')


    def test_signin__when_company_using_valid_pro_user_pass__should_fail(self):    # menu = driver.find_element_by_class_name('navbar-toggler-icon').click()
        driver= self.driver
        data = {
            "email" : VALID_PRO_USERNAME,
            "password" : VALID_PRO_PASSWORD
        }
        signin_helper_company(driver,data)
        try:
            menu = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[6]/button')
            self.fail()
        except NoSuchElementException:
            pass



    def test_signin__when_empty_username__should_fail(self):
        driver= self.driver
        data = {
            'email': BLANK_USERNAME,
            'password': VALID_COM_PASSWORD
        }
        signin_helper_company(driver,data)
        try:
            menu = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[6]/button')
            self.fail()
        except NoSuchElementException:
            pass


    def test_signin__when_empty_password__should_fail(self):    # menu = driver.find_element_by_class_name('navbar-toggler-icon').click()
        driver= self.driver
        data = {
            'email': VALID_COM_USERNAME,
            'password': BLANK_PASSWORD
        }
        signin_helper_company(driver,data)
        try:
            menu = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[6]/button')
            self.fail()
        except NoSuchElementException:
            pass


    def test_signin__when_invalid_username__should_fail(self):    # menu = driver.find_element_by_class_name('navbar-toggler-icon').click()
        driver= self.driver
        data = {
            'email': INVALID_COM_USERNAME,
            'password': VALID_COM_PASSWORD
        }
        signin_helper_company(driver,data)
        try:
            menu = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[6]/button')
            self.fail()
        except NoSuchElementException:
            pass


    def test_signin__when_wrong_password__should_fail(self):    # menu = driver.find_element_by_class_name('navbar-toggler-icon').click()
        driver= self.driver
        data = {
            'email': VALID_PRO_USERNAME,
            'password': WRONG_COM_PASSWORD
        }
        signin_helper_company(driver,data)
        try:
            menu = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[6]/button')
            self.fail()
        except NoSuchElementException:
            pass


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


def signin_helper_company(driver,row):
    driver.get(MAIN_URL_HOME)
    time.sleep(1)
    driver.refresh()
    time.sleep(DELAY_LONG)
    try:
        company_sign_In_btn = driver.find_element_by_link_text('Company Sign In')
        company_sign_In_btn.click()
        time.sleep(DELAY_SHORT)
        email = driver.find_element_by_name('email')
        time.sleep(DELAY_SHORT)
        email.clear()
        time.sleep(1)
        email.send_keys(row['email'])
        password = driver.find_element_by_name('password')
        time.sleep(DELAY_SHORT)
        password.clear()
        time.sleep(1)
        password.send_keys(row['password'])
        time.sleep(1)
        submit_btn = driver.find_element_by_xpath('//*[@id="signinButton"]')
        submit_btn.click()
        time.sleep(DELAY_SHORT)

    except NoSuchElementException:
        time.sleep(DELAY_SHORT)
        return 1

def signout_helper(driver):
    driver.get(MAIN_URL_HOME)
    time.sleep(DELAY_SHORT)
    profile_btn = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[6]/button')
    profile_btn.click()
    time.sleep(1)
    sign_out_btn = driver.find_element_by_xpath('//*[@id="userNavbarMain"]/ul/li[3]/a/span')
    sign_out_btn.click()
    time.sleep(1)



if __name__ == '__main__':
    unittest.main()