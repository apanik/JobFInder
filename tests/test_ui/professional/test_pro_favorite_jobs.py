import time
import unittest
#
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.chrome import webdriver
#
# from tests.config_web import CHROME_DRIVER_LOCATION, DELAY_SHORT, MAIN_URL

# total page job list result
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.color import Color

from tests.config import VALID_PRO_VIEW_USERNAME, VALID_PRO_VIEW_PASSWORD, ADMIN_URL
from tests.config_web import MAIN_URL, CHROME_DRIVER_LOCATION, DELAY_SHORT, MAIN_URL_HOME, DELAY_LONG
from tests.test_ui.professional.test_signin import signin_helper

APPLY_NOTE = 'Application Note will be here.'

FAVORITE_COUNT =  "12"
FAVORITE_COUNT_10 =  "10"
FAVORITE_COUNT_11 =  "11"
TOTAL_FAVORITE_JOBS_COUNT = f'Showing 1 - 10 of {FAVORITE_COUNT} Jobs'
TOTAL_FAVORITE_JOBS_COUNT_10 = f'Showing 1 - 10 of {FAVORITE_COUNT_10} Jobs'
TOTAL_FAVORITE_JOBS_COUNT_11 = f'Showing 1 - 10 of {FAVORITE_COUNT_11} Jobs'

FAVORITE_COUNT_MINUS_1 =  "11"
FAVORITE_COUNT_10_MINUS_1 =  "9"
FAVORITE_COUNT_11_MINUS_1 =  "10"
TOTAL_FAVORITE_JOBS_COUNT_MINUS_1 = f'Showing 1 - 10 of {FAVORITE_COUNT_MINUS_1} Jobs'
TOTAL_FAVORITE_JOBS_COUNT_10_MINUS_1 = f'Showing 1 - 9 of {FAVORITE_COUNT_10_MINUS_1} Jobs'
TOTAL_FAVORITE_JOBS_COUNT_11_MINUS_1 = f'Showing 1 - 10 of {FAVORITE_COUNT_11_MINUS_1} Jobs'


TOTAL_FAVORITE_JOBS_RESULT = [
 'Job Post Example Fourteen',
 'Job Post Example Fourteen Single',
 'Job Post Example Nineteen',
 'Job Post Example Five',
 'Job Post Example Twenty Four',
 'Job Post Example Twenty One',
 'Job Post Example Fourteen Double',
 'Job Post Example Fourteen',
 'Job Post Example Two',
 'Job Post Example Nine',
 'Job Post Example Fifteen',
 'Job Post Example One']

TOTAL_FAVORITE_JOBS_RESULT_10 = [
    'Job Post Example Fourteen Single',
    'Job Post Example Nineteen',
    'Job Post Example Five',
    'Job Post Example Twenty Four',
    'Job Post Example Twenty One',
    'Job Post Example Fourteen Double',
    'Job Post Example Fourteen',
    'Job Post Example Two',
    'Job Post Example Nine',
    'Job Post Example Fifteen']

TOTAL_FAVORITE_JOBS_RESULT_11 = [
    'Job Post Example Fourteen Single',
    'Job Post Example Nineteen',
    'Job Post Example Five',
    'Job Post Example Twenty Four',
    'Job Post Example Twenty One',
    'Job Post Example Fourteen Double',
    'Job Post Example Fourteen',
    'Job Post Example Two',
    'Job Post Example Nine',
    'Job Post Example Fifteen',
    'Job Post Example One']

LOVE_ICON_FILL = '#f5d91d'
qualification_three_result = ("Showing 1 - 1 of 1 Jobs")
qualification_three_search_result =[
 'Job Post Example Ten'
 ]
qualification_four_result = ("Showing 0 - 0 of 0 Jobs")
qualification_four_search_result = []
qualification_five_result = ("Showing 0 - 0 of 0 Jobs")
qualification_five_search_result = []

# apply button wise search result
apply_error_message = ("This field is required.")
captcha_error_message = ("You can't leave Captcha")
SUCCESS_FAVORITE_TEXT = "Job saved as a favorite."





class TestFavoriteJobsShow(unittest.TestCase):

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

    def test__all_favorited_jobs_in_list__when_signed_in__should_pass(self):
        driver = self.driver
        time.sleep(1)
        favorite_btn = driver.find_element_by_link_text('Favorite Jobs')
        favorite_btn.click()
        time.sleep(DELAY_SHORT)
        try:
            total_favorite_jobs_count_show = driver.find_element_by_class_name('bookmark-title').text
            if total_favorite_jobs_count_show != TOTAL_FAVORITE_JOBS_COUNT and total_favorite_jobs_count_show != TOTAL_FAVORITE_JOBS_COUNT_10 and total_favorite_jobs_count_show != TOTAL_FAVORITE_JOBS_COUNT_11:
                self.fail()

            titles = []
            i = 0;
            page_count = driver.find_elements_by_class_name('page-item ').__len__()
            for i in range(i, page_count - 2):
                if i <= page_count - 3:
                    page = driver.find_element_by_css_selector('.page-item.active').text

                    time.sleep(1)
                    self.assertEqual(page, str(i + 1))
                else:
                    time.sleep(1)
                job_list = driver.find_elements_by_class_name('job-list')

                for job in job_list:

                    # .  not all companies have review
                    try:
                        title = job.find_element_by_tag_name('h4').text
                    except:
                        title = ''
                    if title != '':
                        titles.append(title)
                if i != page_count - 3:
                    time.sleep(1)
                    page_next = driver.find_element_by_class_name('fa-arrow-right')
                    page_next.click()
                    time.sleep(DELAY_SHORT)
                time.sleep(1)

            if titles != TOTAL_FAVORITE_JOBS_RESULT and titles != TOTAL_FAVORITE_JOBS_RESULT_10 and  titles != TOTAL_FAVORITE_JOBS_RESULT_11:
                    self.fail()
        except NoSuchElementException:
            self.fail('Not ok')



    def test__all_favorited_jobs_in_list__when_unfavorited__should_pass(self):
        driver = self.driver
        time.sleep(1)
        favorite_btn = driver.find_element_by_link_text('Favorite Jobs')
        favorite_btn.click()
        time.sleep(DELAY_SHORT)
        total_favorite_jobs_count_show = driver.find_element_by_class_name('bookmark-title').text
        if total_favorite_jobs_count_show != TOTAL_FAVORITE_JOBS_COUNT and total_favorite_jobs_count_show != TOTAL_FAVORITE_JOBS_COUNT_10 and total_favorite_jobs_count_show != TOTAL_FAVORITE_JOBS_COUNT_11:
            self.fail()
        else:
            time.sleep(1)
            job_list = driver.find_element_by_class_name('job-list')
            time.sleep(1)
            job_title = job_list.find_element_by_class_name('job-title').text
            time.sleep(1)
            job_title_url = job_list.find_element_by_class_name('job-title').get_attribute('href')
            time.sleep(1)
            job_favorite_btn = job_list.find_element_by_css_selector('.feather.feather-heart')
            time.sleep(1)
            job_favorite_btn.click()
            time.sleep(DELAY_SHORT)
            job_list = driver.find_element_by_class_name('job-list')
            job_title_2 = job_list.find_element_by_class_name('job-title').text

            total_favorite_jobs_count_show = driver.find_element_by_class_name('bookmark-title').text

            try:
                if total_favorite_jobs_count_show != TOTAL_FAVORITE_JOBS_COUNT_MINUS_1 and total_favorite_jobs_count_show != TOTAL_FAVORITE_JOBS_COUNT_10_MINUS_1 and total_favorite_jobs_count_show != TOTAL_FAVORITE_JOBS_COUNT_11_MINUS_1:
                    try:
                        self.assertNotEqual(job_title, job_title_2)
                        time.sleep(1)
                        driver.get(job_title_url)
                        time.sleep(DELAY_SHORT)
                        job_detail_favorite_btn = driver.find_element_by_css_selector('.feather.feather-heart')
                        job_detail_favorite_btn.click()
                        time.sleep(1)
                        success_favorite = driver.find_element_by_class_name('//*[@id="swal2-content"]').text
                        time.sleep(1)
                        self.assertEqual(success_favorite,SUCCESS_FAVORITE_TEXT)
                        ok_btn = driver.find_element_by_class_name('swal2-confirm')
                        ok_btn.click()
                        time.sleep(1)
                    except:
                        self.fail()

                    self.fail()
                else:
                    time.sleep(1)
            except:
                self.fail()
            driver.refresh()
            time.sleep(DELAY_SHORT)
            try:
                if total_favorite_jobs_count_show != TOTAL_FAVORITE_JOBS_COUNT_MINUS_1 and total_favorite_jobs_count_show != TOTAL_FAVORITE_JOBS_COUNT_10_MINUS_1 and total_favorite_jobs_count_show != TOTAL_FAVORITE_JOBS_COUNT_11_MINUS_1:
                    try:
                        self.assertNotEqual(job_title, job_title_2)
                        time.sleep(1)
                        driver.get(job_title_url)
                        time.sleep(DELAY_SHORT)
                        job_detail_favorite_btn = driver.find_element_by_css_selector('.feather.feather-heart')
                        job_detail_favorite_btn.click()
                        time.sleep(1)
                        ok_btn = driver.find_element_by_class_name('swal2-confirm')
                        ok_btn.click()
                        time.sleep(1)
                    except:
                        self.fail()

                    self.fail()
                else:
                    time.sleep(1)
            except:
                self.fail()
            time.sleep(1)
            try:
                self.assertNotEqual(job_title, job_title_2)
                time.sleep(1)
                driver.get(job_title_url)
                time.sleep(DELAY_SHORT)
                job_detail_favorite_btn = driver.find_element_by_css_selector('.feather.feather-heart')
                job_detail_favorite_btn.click()
                time.sleep(1)
                ok_btn = driver.find_element_by_class_name('swal2-confirm')
                ok_btn.click()
                time.sleep(1)
            except:
                self.fail()
            driver.get(MAIN_URL_HOME+'/professional/favorite-jobs/')
            time.sleep(1)
            try:
                if total_favorite_jobs_count_show != TOTAL_FAVORITE_JOBS_COUNT and total_favorite_jobs_count_show != TOTAL_FAVORITE_JOBS_COUNT_10 and total_favorite_jobs_count_show != TOTAL_FAVORITE_JOBS_COUNT_11:
                    self.fail()
                else:
                    time.sleep(1)
            except:
                self.fail()


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


class TestFavoriteJobsIconFavorited(unittest.TestCase):

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


    def test__favorite_job_favorite_icon_is_filled__should_pass(self):
        driver = self.driver
        time.sleep(1)
        favorite_btn = driver.find_element_by_link_text('Favorite Jobs')
        favorite_btn.click()
        time.sleep(DELAY_SHORT)
        # --------------- KEEP THIS SECTION FOR PAGINATION START--------
        # i = 0;
        # page_count = driver.find_elements_by_class_name('page-item ').__len__()
        # for i in range(i, page_count-2):
        #     if i <= page_count-3:
        #         if page_count =
        #         page = driver.find_element_by_css_selector('.page-item.active').text

        #         time.sleep(1)
        #         self.assertEqual(page, str(i+1))
        #     else:
        #         time.sleep(1)
        # --------------- KEEP THIS SECTION FOR PAGINATION END--------

        time.sleep(1)
        job_list = driver.find_elements_by_class_name('job-list')
        for job in job_list:
            try:
                fill_color = job.find_element_by_class_name('feather-heart').value_of_css_property('fill')
                fill_color_hex = Color.from_string(fill_color).hex
                self.assertEqual(fill_color_hex, LOVE_ICON_FILL)
                time.sleep(1)
            except:
                self.fail()


            # --------------- KEEP THIS SECTION FOR PAGINATION START--------
            # if i != page_count-3:
            #     time.sleep(1)
            #     page_next = driver.find_element_by_link_text('Next')
            #     page_next.click()
            # time.sleep(DELAY_SHORT)
            # --------------- KEEP THIS SECTION FOR PAGINATION END--------

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


class TestFavoriteJobUnfavorite(unittest.TestCase):

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


    def test__favorite_job_favorite_icon_click_to_Unfavorite__should_pass(self):
        driver = self.driver
        time.sleep(1)
        favorite_btn = driver.find_element_by_link_text('Favorite Jobs')
        favorite_btn.click()
        time.sleep(DELAY_SHORT)

        time.sleep(1)
        job_list = driver.find_element_by_class_name('job-list')
        time.sleep(1)
        job_title = job_list.find_element_by_class_name('job-title').text
        time.sleep(1)
        job_title_url = job_list.find_element_by_class_name('job-title').get_attribute('href')
        time.sleep(1)
        job_favorite_btn = job_list.find_element_by_css_selector('.feather.feather-heart')
        time.sleep(1)
        job_favorite_btn.click()
        time.sleep(1)
        job_list = driver.find_element_by_class_name('job-list')
        job_title_2 = job_list.find_element_by_class_name('job-title').text

        try:
            self.assertNotEqual(job_title, job_title_2)
            time.sleep(1)
            driver.get(job_title_url)
            time.sleep(DELAY_SHORT)
            job_detail_favorite_btn = driver.find_element_by_css_selector('.feather.feather-heart')
            job_detail_favorite_btn.click()
            time.sleep(1)
            ok_btn = driver.find_element_by_class_name('swal2-confirm')
            ok_btn.click()
            time.sleep(1)
        except:
            self.fail()


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


class TestFavoriteJobApply(unittest.TestCase):

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


    def test__favorite_job_apply__should_pass(self):
        driver = self.driver
        data = {
            "user": "admin",
            "pass": "123",
            "value": "20"
        }
        time.sleep(DELAY_SHORT)
        admin_setting_completenss_helper(driver, data)
        time.sleep(DELAY_SHORT)
        try:
            driver.get('http://127.0.0.1:8000/professional/profile-dashboard/')
            time.sleep(DELAY_SHORT)
            favorite_btn = driver.find_element_by_link_text('Favorite Jobs')
            favorite_btn.click()
            time.sleep(DELAY_SHORT)
            job_button_list = driver.find_elements_by_class_name('buttons')

            time.sleep(DELAY_SHORT)
            for job in job_button_list:
                try:
                    apply = job.find_element_by_class_name('apply').text
                    if apply == 'Applied':
                       time.sleep(1)
                    elif apply == 'Apply':
                        try:
                            apply_btn = job.find_element_by_class_name('apply')
                            time.sleep(1)
                            apply_btn.click()
                            time.sleep(DELAY_SHORT)
                            driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
                            time.sleep(3)
                            apply_note = driver.find_element_by_id('tinymce')
                            apply_note.send_keys(APPLY_NOTE)
                            time.sleep(1)
                            driver.switch_to.default_content()
                            time.sleep(1)
                            apply_now_btn = driver.find_element_by_xpath('//*[@id="apply-form"]/button')
                            time.sleep(DELAY_SHORT)
                            apply_now_btn.click()
                            time.sleep(DELAY_LONG)
                            time.sleep(DELAY_LONG)
                            time.sleep(DELAY_LONG)
                            time.sleep(DELAY_LONG)
                            time.sleep(DELAY_LONG)
                            success_ok = driver.find_element_by_xpath('/html/body/div[7]/div/div[3]/button[1]')
                            success_ok.click()
                            driver.refresh()
                            pass
                            break
                        except:
                            self.fail()
                            break
                except:
                    self.fail()
        except:
            self.fail()


    def test__favorite_job_applied_button_has_no_hover__should_pass(self):
        driver = self.driver
        time.sleep(1)
        favorite_btn = driver.find_element_by_link_text('Favorite Jobs')
        favorite_btn.click()
        time.sleep(DELAY_SHORT)

        time.sleep(1)
        job_burron_list = driver.find_elements_by_class_name('buttons')
        for job in job_burron_list:
            try:
                apply = job.find_element_by_class_name('apply').text
                if apply == 'Apply':
                   time.sleep(1)
                elif apply == 'Applied':
                    try:
                        apply_btn = job.find_element_by_class_name('apply')
                        time.sleep(1)
                        apply_btn.click()
                        self.fail()
                        break
                    except:
                        pass
                        break
            except:
                self.fail()


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()



class TestCompleteProfileJobApply(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        data = {
            "user" : "admin",
            "pass" : "123",
            "value" : "99"
        }
        admin_setting_completenss_helper(cls.driver, data)

    def test__favorite_job_apply__when_profile_is_not_complete__should_pass(self):
        data = {
            "user": "admin",
            "pass": "123",
            "value": "20"
        }
        incomplete_ok_value = 'Please complete your profile with necessary and authentic information.'
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        time.sleep(DELAY_SHORT)
        data_signin = {
            "email": VALID_PRO_VIEW_USERNAME,
            "password": VALID_PRO_VIEW_PASSWORD,
        }
        signin_helper(driver, data_signin)
        time.sleep(DELAY_SHORT)

        favorite_btn = driver.find_element_by_link_text('Favorite Jobs')
        favorite_btn.click()
        time.sleep(DELAY_SHORT)

        time.sleep(1)
        job_button_list = driver.find_elements_by_class_name('buttons')
        for job in job_button_list:
            try:
                apply = job.find_element_by_class_name('apply').text
                if apply == 'Applied':
                   time.sleep(1)
                elif apply == 'Apply':
                    try:
                        apply_btn = job.find_element_by_class_name('apply')
                        time.sleep(1)
                        apply_btn.click()
                        time.sleep(DELAY_SHORT)
                        driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
                        time.sleep(3)
                        apply_note = driver.find_element_by_id('tinymce')
                        apply_note.send_keys(APPLY_NOTE)
                        time.sleep(1)
                        driver.switch_to.default_content()
                        time.sleep(1)
                        apply_now_btn = driver.find_element_by_xpath('//*[@id="apply-form"]/button')
                        time.sleep(DELAY_SHORT)
                        apply_now_btn.click()
                        time.sleep(DELAY_SHORT)
                        time.sleep(DELAY_SHORT)
                        time.sleep(DELAY_SHORT)
                        time.sleep(DELAY_SHORT)
                        time.sleep(DELAY_SHORT)
                        incomplete_ok = driver.find_element_by_id('swal2-content').text
                        if incomplete_ok != incomplete_ok_value:
                            self.fail()
                        break

                    except:
                        self.fail()
                        break
            except:
                self.fail()
        time.sleep(DELAY_SHORT)
        admin_setting_completenss_helper(driver, data)


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


def admin_setting_completenss_helper(driver, row):
    driver.get(ADMIN_URL)
    user_btn = driver.find_element_by_name('username')
    user_btn.send_keys(row['user'])
    time.sleep(1)
    pass_btn = driver.find_element_by_name('password')
    pass_btn.send_keys(row['pass'])
    time.sleep(1)
    submit = driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input')
    submit.click()
    time.sleep(DELAY_SHORT)
    setting_btn = driver.find_element_by_link_text('Settings')
    setting_btn.click()
    time.sleep(1)
    profile = driver.find_element_by_link_text('http://facebook.com/example')
    profile.click()
    time.sleep(1)
    completeness_value = driver.find_element_by_name('minimum_profile_completeness').text
    completeness_field = driver.find_element_by_name('minimum_profile_completeness')
    completeness_field.clear()
    completeness_field.send_keys(row['value'])
    time.sleep(1)
    save = driver.find_element_by_name('_save')
    save.click()
    try:
        log_out = driver.find_element_by_xpath('//*[@id="user-tools"]/a[3]')
        log_out.click()
        return 1
    except NoSuchElementException:
        return 0


if __name__ == '__main__':
    unittest.main()