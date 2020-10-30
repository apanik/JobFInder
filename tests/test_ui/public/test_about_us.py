import time
import unittest

from selenium.webdriver.chrome import webdriver
from tests.config_web import MAIN_URL_HOME, CHROME_DRIVER_LOCATION, DELAY_SHORT


ROW_TITLE_DATA_LIST = ['Our Mission', 'Our Vision', 'Our Values', 'About JobXprss']
ROW_PARAGRAPH_DATA_LIST = [
    'To provide an intelligent people-position matchmaking platform for the professionals and organizations.',
    'To create the most compelling job platform by ensuring the best job for every professional and ideal talent pool for every organization.',
    'Innovation and Proactiveness: We actively pursue new and divergent ways to further our cause. Our tracks are built with utmost professionalism and creativity. We continuously adopt new cutting-edge technology concepts to best serve our professionals clients.',
    'Openness: We value transparency and believe in sharing information so that we can constantly learn, collaborate and arrive at the right decisions.',
    'People Orientation: We work together with integrity. We have respect and compassion for one another; fairness and group cohesion are strongly promoted.',
    'JobXprss is the most advanced job platform in Bangladesh.',
    'We use intelligent technology to match the right people with thousands of latest job postings obtained from numerous job sources. Compiled resumes are also awaiting to be sorted as per client requirements.',
    'Unlike other job sites, all these information are shared and presented in a way that best serves the purpose of the professionals and the organizations. In turn, job seekers on JobXprss are more informed about the jobs and the organizations they apply to and consider joining. JobXprss is available anywhere through its mobile apps.',
    'JobXprss is powered by Ishraak Solutions, a team of great technology experts.',
    'To get the best JobXprss experience, use the mobile app.',
    'Get email updates about our latest news.',
    'Powered By',
    'Copyright © 2020 JobXprss, All Right Reserved\nv1.0.127']


class TestAboutUs(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = webdriver.WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        time.sleep(DELAY_SHORT)


    def test__when_about_us_is_showing_data__should_pass(self):
        driver = self.driver
        about_us_btn = driver.find_element_by_link_text('About Us')
        about_us_btn.click()
        time.sleep(DELAY_SHORT)
        about_us_title_data = driver.find_elements_by_tag_name('h5')
        row_titles_list = []
        for row in about_us_title_data:
            title = row.text
            if title != '':
                row_titles_list.append(title)

        about_us_para_data = driver.find_elements_by_tag_name('p')
        row_para_list = []
        for row in about_us_para_data:
            para = row.text
            if para != '':
                row_para_list.append(para)

        time.sleep(1)
        if row_titles_list != ROW_TITLE_DATA_LIST and row_para_list != ROW_PARAGRAPH_DATA_LIST:
            self.fail()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
