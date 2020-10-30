import time
import unittest

from selenium.webdriver.chrome import webdriver

from tests.config_web import MAIN_URL_HOME, CHROME_DRIVER_LOCATION, DELAY_SHORT


RQUESTION_LIST_DATA = ['What is JobXprss?', 'Is it free?', 'Do you guarantee a job?', 'How to post a job on JobXprss?', 'Do you guarantee authenticity of the job details?', 'Do you provide training?', 'Do you have any mobile apps?']
ANSWER_LIST_DATA = ['JobXprss is an intelligent people-position matchmaking platform for the professionals and organizations. To know more, please visit About Us']


ICON_DATA = f'{MAIN_URL_HOME}/static/images/chat-icon.png'
TITLE_DATA = 'Didn’t get your answer?'
URL_LIST_DATA = [f'{MAIN_URL_HOME}/contact-us/', f'{MAIN_URL_HOME}/FAQ/#']
CALL_PARAGRAPH = 'Or maybe you’d like to call us: 01900000000'

class TestFaq(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = webdriver.WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        time.sleep(DELAY_SHORT)


    def test__when_faq_is_showing_data__should_pass(self):
        driver = self.driver
        faq_btn = driver.find_element_by_link_text('FAQ')
        faq_btn.click()
        time.sleep(DELAY_SHORT)
        header = driver.find_element_by_css_selector('.section-header.section-header-center')
        head_1 = header.find_element_by_tag_name('h6').text
        head_2 = header.find_element_by_tag_name('h2').text
        quick_contact = driver.find_element_by_class_name('quick-contact')
        icon = quick_contact.find_element_by_tag_name('img').get_attribute('src')
        title = quick_contact.find_element_by_tag_name('h4').text
        call_para = quick_contact.find_element_by_tag_name('p').text
        links = quick_contact.find_elements_by_tag_name('a')
        url_list = []
        for link in links:
            url = link.get_property('href')
            if url != '':
                url_list.append(url)
        if icon != ICON_DATA and title != TITLE_DATA and url_list != URL_LIST_DATA and call_para != CALL_PARAGRAPH:
            self.fail()
        faq_data = driver.find_element_by_id('accordionExample')
        questions_answers = faq_data.find_elements_by_class_name('card')
        questions_list = []
        answers_list = []
        for item in questions_answers:
            question = item.find_element_by_tag_name('h5').text
            answer = item.find_element_by_tag_name('p').text
            if question != '':
                questions_list.append(question)
            if answer != '':
                answers_list.append(answer)


        time.sleep(1)
        if questions_list != RQUESTION_LIST_DATA and answers_list != ANSWER_LIST_DATA:
            self.fail()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
