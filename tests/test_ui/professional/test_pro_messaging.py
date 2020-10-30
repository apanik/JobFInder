import time
import unittest

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.color import Color

from tests.config import VALID_PRO_VIEW_USERNAME, VALID_PRO_VIEW_PASSWORD, VALID_PRO_PASSWORD, VALID_PRO_USERNAME
from tests.config_web import MAIN_URL_HOME, CHROME_DRIVER_LOCATION, DELAY_SHORT
from tests.test_ui.professional.test_signin import signin_helper

COMPANY_EXAMPLE = "Company Example"
COMPANY_EXAMPLE_VIEW = "Company Example View"

MESSAGE_LIST_COM_EXAMPLE_VIEW_PRO_EXAMPLE_VIEW = [
    'Hi prof example View',
    'Hi Company Example View']

MESSAGE_LIST_COM_EXAMPLE_PRO_EXAMPLE_VIEW = [
    'Hi prof example View',
    'Hi Company Example View']

MESSAGE_LIST_COM_EXAMPLE_VIEW_PRO_EXAMPLE = [
    'Hi Prof Example',
    'Hi Company Example View'
    'How are you'
    'I am fine.'
]
MESSAGE_LIST_COM_EXAMPLE_PRO_EXAMPLE = [
    'Hi Prof Example',
    'Hi Company Example'
    'How are you'
    'I am fine.'
]


class TestProfessionalMessageViewExample(unittest.TestCase):

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


    def test__when_professional_message_box_showing_data__pass(self):
        driver = self.driver
        time.sleep(1)
        message_btn = driver.find_element_by_link_text('Messages')
        message_btn.click()
        time.sleep(DELAY_SHORT)
        messaging_company = driver.find_elements_by_class_name('message-single')

        time.sleep(DELAY_SHORT)
        for company in messaging_company:
            message_list = []
            try:
                company_name = company.find_element_by_class_name('username').text
                time.sleep(1)
                if company_name != COMPANY_EXAMPLE and company_name != COMPANY_EXAMPLE_VIEW:
                    self.fail()
                try:
                    messages = driver.find_elements_by_class_name('conversation')

                    time.sleep(DELAY_SHORT)
                    for message in messages:
                        try:
                            message_text = message.find_element_by_class_name('message').text
                        except:
                            message_text = ''
                        if message_list != '':
                            message_list.append(message_text)
                        time.sleep(1)

                    if company_name == COMPANY_EXAMPLE:
                        if message_list != MESSAGE_LIST_COM_EXAMPLE_PRO_EXAMPLE_VIEW:
                            self.fail()
                    elif company_name == COMPANY_EXAMPLE_VIEW:
                        if message_list != MESSAGE_LIST_COM_EXAMPLE_VIEW_PRO_EXAMPLE_VIEW:
                            self.fail()
                except:
                    self.fail()
            except:
                self.fail()


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


class TestProfessionalMessageViewExampleOne(unittest.TestCase):

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

    #
    # def test__when_professional_message_box_showing_all_companies_data_correctly__pass(self):
    #     driver = self.driver
    #     time.sleep(1)
    #     message_btn = driver.find_element_by_link_text('Messages')
    #     message_btn.click()
    #     time.sleep(DELAY_SHORT)
    #     messaging_company = driver.find_elements_by_class_name('message-single')
    #
    #     time.sleep(DELAY_SHORT)
    #     for company in messaging_company:
    #         message_list = []
    #         try:
    #             company_name = company.find_element_by_class_name('username').text
    #             company_name_btn = company.find_element_by_class_name('username')
    #             company_name_btn.click()
    #             time.sleep(DELAY_SHORT)
    #             if company_name != COMPANY_EXAMPLE and company_name != COMPANY_EXAMPLE_VIEW:
    #                 self.fail()
    #             try:
    #                 messages = driver.find_elements_by_class_name('conversation')
    #
    #                 time.sleep(DELAY_SHORT)
    #                 for message in messages:
    #                     try:
    #                         message_text = message.find_element_by_class_name('message').text
    #                     except:
    #                         message_text = ''
    #                     if message_list != '':
    #                         message_list.append(message_text)
    #                     time.sleep(1)
    #
    #                 if company_name == COMPANY_EXAMPLE:
    #                     if message_list != MESSAGE_LIST_COM_EXAMPLE_PRO_EXAMPLE:
    #                         self.fail()
    #                 elif company_name == COMPANY_EXAMPLE_VIEW:
    #                     if message_list != MESSAGE_LIST_COM_EXAMPLE_VIEW_PRO_EXAMPLE:
    #                         self.fail()
    #             except:
    #                 self.fail()
    #         except:
    #             self.fail()
    #
    #
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()