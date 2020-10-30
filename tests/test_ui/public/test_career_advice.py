import time
import unittest

from selenium.webdriver.chrome import webdriver

from tests.config import MAIN_URL
from tests.config_web import MAIN_URL_HOME, CHROME_DRIVER_LOCATION, DELAY_SHORT

AUTHOR_INFO_LIST_VALUE = [
    'Author Example One, 23/08/2020',
    'Author Example Two, 23/08/2020',
    'Author Example Three, 23/08/2020',
    'Author Example Four, 23/08/2020',
    'Author Example Five, 23/08/2020',
    'Author Example Six, 23/08/2020',
    'Author Example Seven, 23/08/2020',
    'Author Example Eight, 23/08/2020',
    'Author Example Nine, 23/08/2020',
    'Author Example Ten, 23/08/2020']

CAREER_THUMB_LIST_VALUE = [
    f'{MAIN_URL}/media/images/career_advice_thumb_GODFqWj.jpeg',
    f'{MAIN_URL}/media/images/career_advice_thumb_ifiEBgM.jpeg',
    f'{MAIN_URL}/media/images/career_advice_thumb_pybYJGF.jpeg',
    f'{MAIN_URL}/media/images/career_advice_thumb_rmVyNbO.jpeg',
    f'{MAIN_URL}/media/images/career_advice_thumb_nvXnTsz.jpeg',
    f'{MAIN_URL}/media/images/career_advice_thumb_7D8MbKK.jpeg',
    f'{MAIN_URL}/media/images/career_advice_thumb_1WDQrXY.jpeg',
    f'{MAIN_URL}/media/images/career_advice_thumb_1sxyzP5.jpeg',
    f'{MAIN_URL}/media/images/career_advice_thumb_sgauh9x.jpeg',
    f'{MAIN_URL}/media/images/career_advice_thumb_R2XkTDN.jpeg']

CAREER_ADVICE_DESCRIPTION_SAMPLE = 'Career Advice Short Description is here. Career Advice Short Description is here. Career Advice Short Description is here. Career Advice Short Description is here. Career Advice Short Description is here. Career Advice Short Description is here. Career Advice Short Description is here. Career Advice Short Description is here. Career Advice Short Description is here. Career Advice Short Description is here. Career Advice Short Description is here. Career Advice Short Description is here. Career Advice Short Description is here. Career Advice Short Description is here. Career Advice Short Description is here. Career Advice Short Description is here. Career Advice Short Description is here. Career Advice Short Description is here.more..'
CAREER_DESCRIPTION_LIST_VALUE = [
    CAREER_ADVICE_DESCRIPTION_SAMPLE,
    CAREER_ADVICE_DESCRIPTION_SAMPLE,
    CAREER_ADVICE_DESCRIPTION_SAMPLE,
    CAREER_ADVICE_DESCRIPTION_SAMPLE,
    CAREER_ADVICE_DESCRIPTION_SAMPLE,
    CAREER_ADVICE_DESCRIPTION_SAMPLE,
    CAREER_ADVICE_DESCRIPTION_SAMPLE,
    CAREER_ADVICE_DESCRIPTION_SAMPLE,
    CAREER_ADVICE_DESCRIPTION_SAMPLE,
    CAREER_ADVICE_DESCRIPTION_SAMPLE]

MORE_LINK_LIST_VALUE = [
    f'{MAIN_URL}/career-advice/details/1',
    f'{MAIN_URL}/career-advice/details/2',
    f'{MAIN_URL}/career-advice/details/3',
    f'{MAIN_URL}/career-advice/details/4',
    f'{MAIN_URL}/career-advice/details/5',
    f'{MAIN_URL}/career-advice/details/6',
    f'{MAIN_URL}/career-advice/details/7',
    f'{MAIN_URL}/career-advice/details/8',
    f'{MAIN_URL}/career-advice/details/9',
    f'{MAIN_URL}/career-advice/details/10']

TITLE_DETAIL_TEXT = 'Career Advice Example One'
FEATURED_IMAG_URL = f'{MAIN_URL}/media/images/career_advice_thumb_GODFqWj.jpeg'

class TestCareerAdvice(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = webdriver.WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        time.sleep(DELAY_SHORT)


    def test__when_career_advice_list_is_showing_data__should_pass(self):
        driver = self.driver
        career_advice_btn = driver.find_element_by_link_text('Career Advice')
        career_advice_btn.click()
        time.sleep(DELAY_SHORT)
        career_advice_list = driver.find_elements_by_class_name('blog-list')
        career_thumb_list = []
        author_info_list = []
        career_description_list = []
        more_link_list = []
        for career in career_advice_list:
            try:
                career_thumb = career.find_element_by_css_selector('.img-fluid.ca-thumb').get_property('src')
                career_thumb_list.append(career_thumb)
                time.sleep(1)
                author_info = career.find_element_by_class_name('author-info').text
                author_info_list.append(author_info)
                time.sleep(1)
                career_description = career.find_element_by_tag_name('p').text
                career_description_list.append(career_description)
                time.sleep(1)
                more_link = career.find_element_by_link_text('more..')
                more_link_url = more_link.get_property('href')
                more_link_list.append(more_link_url)

            except:
                self.fail('Not Ok')

        time.sleep(1)
        try:
            self.assertEquals(career_thumb_list,CAREER_THUMB_LIST_VALUE)
            self.assertEquals(author_info_list, AUTHOR_INFO_LIST_VALUE)
            self.assertEquals(career_description_list, CAREER_DESCRIPTION_LIST_VALUE)
            self.assertEquals(more_link_list, MORE_LINK_LIST_VALUE)
        except:
            self.fail('Not Ok')


    def test__when_career_advice_detail_is_showing_data__should_pass(self):
        driver = self.driver
        career_advice_btn = driver.find_element_by_link_text('Career Advice')
        career_advice_btn.click()
        time.sleep(DELAY_SHORT)
        career_advice_list = driver.find_elements_by_class_name('blog-list')
        for career in career_advice_list:
            try:
                career_advice_title = career.find_element_by_xpath('//*[@id="career-result"]/article[1]/div[2]/h3/a').get_property('href')
                time.sleep(1)
                more_link = career.find_element_by_link_text('more..').get_property('href')
                detail_url = career.find_element_by_link_text('more..')
                if career_advice_title == more_link:
                    detail_url.click()
                    time.sleep(1)

                title_detail = driver.find_element_by_tag_name('h3').text
                time.sleep(1)
                featured_image = driver.find_element_by_css_selector('.img-fluid.ca-thumb').get_property('src')
                time.sleep(1)
                break
            except:
                self.fail('Not Ok')
                break

        time.sleep(1)
        try:
            self.assertEquals(title_detail, TITLE_DETAIL_TEXT)
            self.assertEquals(featured_image, FEATURED_IMAG_URL)
        except:
            self.fail('Not Ok')



    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
