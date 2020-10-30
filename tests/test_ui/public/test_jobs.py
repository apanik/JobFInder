import time
import unittest

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome import webdriver

from tests.config import VALID_PRO_USERNAME, VALID_PRO_PASSWORD
from tests.config_web import CHROME_DRIVER_LOCATION, DELAY_SHORT, MAIN_URL_HOME

# total page job list result
from tests.test_ui.professional.test_signin import signin_helper

APPLY_NOTE = 'Application Note will be here.'

total_result_show = ("Showing 1 - 10 of 37 Jobs")
total_result_show_pro = ("Showing 1 - 10 of 36 Jobs")
total_result_show_pro_2 = ("Showing 1 - 10 of 31 Jobs")
total_result_show_pro_3 = ("Showing 1 - 10 of 32 Jobs")
total_job_result_show = [
    'Job Post Example Four',
    'Job Post Example Fourteen',
    'Job Post Example Eleven',
    'Job Post Example Fourteen Double',
    'Job Post Example Twenty One',
    'Job Post Example Twenty Four',
    'Job Post Example Five',
    'Job Post Example Three',
    'Job Post Example Seven',
    'Job Post Example Twenty',
    'Job Post Example Nineteen',
    'Job Post Example Seventeen',
    'Job Post Example Fourteen',
    'Job Post Example Fourteen Single',
    'Job Post Example Fifteen',
    'Job Post Example One',
    'Job Post Example Nine',
    'Job Post Example Two',
    'Job Post Example Twenty Three',
    'Job Post Example Six',
    'Job Post Example Eighteen',
    'Job Post Example Twelve',
    'Job Post Example Thirteen',
    'Job Post Example Twenty Two',
    'Job Post Example Twenty Five',
    'Job Post Example Eight',
    'Job Post Example Ten',
    'Job Post Example Sixteen',
    'Job Post Example Company Four',
    'Job Post Example Company Six',
    'Job Post Example Company Three',
    'Job Post Example Company Five',
    'Job Post Example Company Ten',
    'Job Post Example Nineteen Seven',
    'Job Post Example Company Eight',
    'Job Post Example Company Nine',
    'Job Post Example Company Two'
]

total_job_result_show_api = [
    'Title Example',
    'Job Post Example Fourteen',
    'Job Post Example Eleven',
    'Job Post Example Fourteen Double',
    'Job Post Example Twenty One',
    'Job Post Example Twenty Four',
    'Job Post Example Five',
    'Job Post Example Three',
    'Job Post Example Seven',
    'Job Post Example Twenty',
    'Job Post Example Nineteen',
    'Job Post Example Seventeen',
    'Job Post Example Fourteen',
    'Job Post Example Fourteen Single',
    'Job Post Example Fifteen',
    'Job Post Example One',
    'Job Post Example Nine',
    'Job Post Example Two',
    'Job Post Example Twenty Three',
    'Job Post Example Six',
    'Job Post Example Eighteen',
    'Job Post Example Twelve',
    'Job Post Example Thirteen',
    'Job Post Example Twenty Two',
    'Job Post Example Twenty Five',
    'Job Post Example Eight',
    'Job Post Example Ten',
    'Job Post Example Sixteen',
    'Job Post Example Company Four',
    'Job Post Example Company Six',
    'Job Post Example Company Three',
    'Job Post Example Company Five',
    'Job Post Example Company Ten',
    'Job Post Example Nineteen Seven',
    'Job Post Example Company Eight',
    'Job Post Example Company Nine',
    'Job Post Example Company Two']

total_job_result_show_api_pro = [
    'Job Post Example Fourteen',
    'Job Post Example Eleven',
    'Job Post Example Fourteen Double',
    'Job Post Example Twenty One',
    'Job Post Example Twenty Four',
    'Job Post Example Five',
    'Job Post Example Three',
    'Job Post Example Seven',
    'Job Post Example Twenty',
    'Job Post Example Nineteen',
    'Job Post Example Seventeen',
    'Job Post Example Fourteen',
    'Job Post Example Fourteen Single',
    'Job Post Example Fifteen',
    'Job Post Example One',
    'Job Post Example Nine',
    'Job Post Example Two',
    'Job Post Example Twenty Three',
    'Job Post Example Six',
    'Job Post Example Eighteen',
    'Job Post Example Twelve',
    'Job Post Example Thirteen',
    'Job Post Example Twenty Two',
    'Job Post Example Twenty Five',
    'Job Post Example Eight',
    'Job Post Example Ten',
    'Job Post Example Sixteen',
    'Job Post Example Company Four',
    'Job Post Example Company Six',
    'Job Post Example Company Three',
    'Job Post Example Company Five',
    'Job Post Example Company Ten',
    'Job Post Example Nineteen Seven',
    'Job Post Example Company Eight',
    'Job Post Example Company Nine',
    'Job Post Example Company Two']

total_job_result_show_api_pro_2 = [
    'Job Post Example Fourteen',
    'Job Post Example Eleven',
    'Job Post Example Fourteen Double',
    'Job Post Example Five',
    'Job Post Example Three',
    'Job Post Example Seven',
    'Job Post Example Twenty',
    'Job Post Example Nineteen',
    'Job Post Example Seventeen',
    'Job Post Example Fourteen',
    'Job Post Example Fourteen Single',
    'Job Post Example Fifteen',
    'Job Post Example One',
    'Job Post Example Nine',
    'Job Post Example Two',
    'Job Post Example Six',
    'Job Post Example Eighteen',
    'Job Post Example Twelve',
    'Job Post Example Thirteen',
    'Job Post Example Eight',
    'Job Post Example Ten',
    'Job Post Example Sixteen',
    'Job Post Example Company Four',
    'Job Post Example Company Six',
    'Job Post Example Company Three',
    'Job Post Example Company Five',
    'Job Post Example Company Ten',
    'Job Post Example Nineteen Seven',
    'Job Post Example Company Eight',
    'Job Post Example Company Nine',
    'Job Post Example Company Two']

total_job_result_show_api_pro_3 = [
     'Job Post Example Four',
     'Job Post Example Fourteen',
     'Job Post Example Eleven',
     'Job Post Example Fourteen Double',
     'Job Post Example Five',
     'Job Post Example Three',
     'Job Post Example Seven',
     'Job Post Example Twenty',
     'Job Post Example Nineteen',
     'Job Post Example Seventeen',
     'Job Post Example Fourteen',
     'Job Post Example Fourteen Single',
     'Job Post Example Fifteen',
     'Job Post Example One',
     'Job Post Example Nine',
     'Job Post Example Two',
     'Job Post Example Six',
     'Job Post Example Eighteen',
     'Job Post Example Twelve',
     'Job Post Example Thirteen',
     'Job Post Example Eight',
     'Job Post Example Ten',
     'Job Post Example Sixteen',
     'Job Post Example Company Four',
     'Job Post Example Company Six',
     'Job Post Example Company Three',
     'Job Post Example Company Five',
     'Job Post Example Company Ten',
     'Job Post Example Nineteen Seven',
     'Job Post Example Company Eight',
     'Job Post Example Company Nine',
     'Job Post Example Company Two']

# total_job_result_show_api = [
#  'Title Example',
#  'Job Post Example Fourteen',
#  'Job Post Example Eleven',
#  'Job Post Example Fourteen Double',
#  'Job Post Example Twenty One',
#  'Job Post Example Twenty Four',
#  'Job Post Example Five',
#  'Job Post Example Three',
#  'Job Post Example Seven',
#  'Job Post Example Twenty',
#  'Job Post Example Nineteen',
#  'Job Post Example Seventeen',
#  'Job Post Example Fourteen',
#  'Job Post Example Fourteen Single',
#  'Job Post Example Fifteen',
#  'Job Post Example One',
#  'Job Post Example Nine',
#  'Job Post Example Two',
#  'Job Post Example Twenty Three',
#  'Job Post Example Six',
#  'Job Post Example Eighteen',
#  'Job Post Example Twelve',
#  'Job Post Example Thirteen',
#  'Job Post Example Twenty Two',
#  'Job Post Example Twenty Five',
#  'Job Post Example Eight',
#  'Job Post Example Ten',
#  'Job Post Example Sixteen',
#  'Job Post Example Company Four',
#  'Job Post Example Company Six',
#  'Job Post Example Company Three',
#  'Job Post Example Company Five',
#  'Job Post Example Company Ten',
#  'Job Post Example Nineteen Seven',
#  'Job Post Example Company Eight',
#  'Job Post Example Company Nine',
#  'Job Post Example Company Two']

total_job_result_show_10_count = '10'
total_job_result_show_10 = [
    'Job Post Example Four',
    'Job Post Example Fourteen',
    'Job Post Example Eleven',
    'Job Post Example Fourteen Double',
    'Job Post Example Twenty One',
    'Job Post Example Twenty Four',
    'Job Post Example Five',
    'Job Post Example Three',
    'Job Post Example Seven',
    'Job Post Example Twenty'
]

total_job_result_show_10_api = [
    'Title Example',
    'Job Post Example Fourteen',
    'Job Post Example Eleven',
    'Job Post Example Fourteen Double',
    'Job Post Example Twenty One',
    'Job Post Example Twenty Four',
    'Job Post Example Five',
    'Job Post Example Three',
    'Job Post Example Seven',
    'Job Post Example Twenty']

total_job_result_unspecified_show_10_api_pro = [
    'Job Post Example Fourteen',
    'Job Post Example Eleven',
    'Job Post Example Fourteen Double',
    'Job Post Example Twenty One',
    'Job Post Example Twenty Four',
    'Job Post Example Five',
    'Job Post Example Three',
    'Job Post Example Seven',
    'Job Post Example Twenty',
    'Job Post Example Nineteen']

total_job_result_show_10_api_pro = [
    'Job Post Example Fourteen',
    'Job Post Example Eleven',
    'Job Post Example Fourteen Double',
    'Job Post Example Twenty One',
    'Job Post Example Twenty Four',
    'Job Post Example Five',
    'Job Post Example Three',
    'Job Post Example Seven',
    'Job Post Example Twenty',
    'Job Post Example Nineteen']

# keyword search result
job_search_result_one = ("Showing 1 - 2 of 2 Jobs")
job_post_search_result_one = [
    'Job Post Example Twenty One',
    'Job Post Example One'
]

# filer search result

top_rated_job_result_show = [
    'Job Post Example Fourteen',
    'Job Post Example Fourteen Double',
    'Job Post Example Twenty One',
    'Job Post Example Twenty Four',
    'Job Post Example Five',
    'Job Post Example One',
    'Job Post Example Twenty',
    'Job Post Example Nineteen',
    'Job Post Example Two',
    'Job Post Example Fourteen',
    'Job Post Example Fourteen Single',
    'Job Post Example Nine',
    'Job Post Example Fifteen',
    'Job Post Example Four',
    'Job Post Example Eleven',
    'Job Post Example Three',
    'Job Post Example Company Four',
    'Job Post Example Seven',
    'Job Post Example Company Six',
    'Job Post Example Company Three',
    'Job Post Example Seventeen',
    'Job Post Example Eight',
    'Job Post Example Company Five',
    'Job Post Example Company Ten',
    'Job Post Example Sixteen',
    'Job Post Example Twenty Five',
    'Job Post Example Ten',
    'Job Post Example Twenty Two',
    'Job Post Example Nineteen Seven',
    'Job Post Example Company Eight',
    'Job Post Example Thirteen',
    'Job Post Example Company Nine',
    'Job Post Example Company Two',
    'Job Post Example Twelve',
    'Job Post Example Twenty Three',
    'Job Post Example Eighteen',
    'Job Post Example Six'
]

top_rated_job_result_show_api = [
    'Job Post Example Fourteen',
    'Job Post Example Fourteen Double',
    'Job Post Example Twenty One',
    'Job Post Example Twenty Four',
    'Job Post Example Five',
    'Job Post Example One',
    'Job Post Example Twenty',
    'Job Post Example Nineteen',
    'Job Post Example Two',
    'Job Post Example Fourteen',
    'Job Post Example Fourteen Single',
    'Job Post Example Nine',
    'Job Post Example Fifteen',
    'Title Example',
    'Job Post Example Eleven',
    'Job Post Example Three',
    'Job Post Example Company Four',
    'Job Post Example Seven',
    'Job Post Example Company Six',
    'Job Post Example Company Three',
    'Job Post Example Seventeen',
    'Job Post Example Eight',
    'Job Post Example Company Five',
    'Job Post Example Company Ten',
    'Job Post Example Sixteen',
    'Job Post Example Twenty Five',
    'Job Post Example Ten',
    'Job Post Example Twenty Two',
    'Job Post Example Nineteen Seven',
    'Job Post Example Company Eight',
    'Job Post Example Thirteen',
    'Job Post Example Company Nine',
    'Job Post Example Company Two',
    'Job Post Example Twelve',
    'Job Post Example Twenty Three',
    'Job Post Example Eighteen',
    'Job Post Example Six']

top_rated_job_result_show_api_pro = [
    'Job Post Example Fourteen',
    'Job Post Example Fourteen Double',
    'Job Post Example Twenty One',
    'Job Post Example Twenty Four',
    'Job Post Example Five',
    'Job Post Example One',
    'Job Post Example Twenty',
    'Job Post Example Nineteen',
    'Job Post Example Two',
    'Job Post Example Fourteen',
    'Job Post Example Fourteen Single',
    'Job Post Example Nine',
    'Job Post Example Fifteen',
    'Job Post Example Eleven',
    'Job Post Example Three',
    'Job Post Example Company Four',
    'Job Post Example Seven',
    'Job Post Example Company Six',
    'Job Post Example Company Three',
    'Job Post Example Seventeen',
    'Job Post Example Eight',
    'Job Post Example Company Five',
    'Job Post Example Company Ten',
    'Job Post Example Sixteen',
    'Job Post Example Twenty Five',
    'Job Post Example Ten',
    'Job Post Example Twenty Two',
    'Job Post Example Nineteen Seven',
    'Job Post Example Company Eight',
    'Job Post Example Thirteen',
    'Job Post Example Company Nine',
    'Job Post Example Company Two',
    'Job Post Example Twelve',
    'Job Post Example Twenty Three',
    'Job Post Example Eighteen',
    'Job Post Example Six']

top_rated_job_result_show_10 = [
    'Job Post Example Fourteen',
    'Job Post Example Fourteen Double',
    'Job Post Example Twenty One',
    'Job Post Example Twenty Four',
    'Job Post Example Five',
    'Job Post Example One',
    'Job Post Example Twenty',
    'Job Post Example Nineteen',
    'Job Post Example Two',
    'Job Post Example Fourteen']

most_applied_job_result_show_a = [
    'Job Post Example Eleven',
    'Job Post Example Five',
    'Job Post Example Three',
    'Job Post Example Twenty',
    'Job Post Example Four',
    'Job Post Example Fourteen',
    'Job Post Example Fourteen Double',
    'Job Post Example Seventeen',
    'Job Post Example Company Two',
    'Job Post Example Fourteen',
    'Job Post Example Fourteen Single',
    'Job Post Example Nine',
    'Job Post Example Twenty One',
    'Job Post Example Twenty Four',
    'Job Post Example Company Four',
    'Job Post Example Seven',
    'Job Post Example One',
    'Job Post Example Company Six',
    'Job Post Example Company Three',
    'Job Post Example Nineteen',
    'Job Post Example Eight',
    'Job Post Example Company Five',
    'Job Post Example Company Ten',
    'Job Post Example Sixteen',
    'Job Post Example Twenty Five',
    'Job Post Example Ten',
    'Job Post Example Twenty Two',
    'Job Post Example Nineteen Seven',
    'Job Post Example Company Eight',
    'Job Post Example Thirteen',
    'Job Post Example Company Nine',
    'Job Post Example Two',
    'Job Post Example Twelve',
    'Job Post Example Twenty Three',
    'Job Post Example Eighteen',
    'Job Post Example Six',
    'Job Post Example Fifteen']

most_applied_job_result_show_a_pro = [
    'Job Post Example Five',
    'Job Post Example Three',
    'Job Post Example Twenty',
    'Job Post Example Eleven',
    'Job Post Example Fourteen Double',
    'Job Post Example Nineteen',
    'Job Post Example Seventeen',
    'Job Post Example Company Two',
    'Job Post Example Fourteen',
    'Job Post Example Fourteen Single',
    'Job Post Example Nine',
    'Job Post Example Fourteen',
    'Job Post Example Twenty One',
    'Job Post Example Twenty Four',
    'Job Post Example Company Four',
    'Job Post Example Seven',
    'Job Post Example One',
    'Job Post Example Company Six',
    'Job Post Example Company Three',
    'Job Post Example Eight',
    'Job Post Example Company Five',
    'Job Post Example Company Ten',
    'Job Post Example Sixteen',
    'Job Post Example Twenty Five',
    'Job Post Example Ten',
    'Job Post Example Twenty Two',
    'Job Post Example Nineteen Seven',
    'Job Post Example Company Eight',
    'Job Post Example Thirteen',
    'Job Post Example Company Nine',
    'Job Post Example Two',
    'Job Post Example Twelve',
    'Job Post Example Twenty Three',
    'Job Post Example Eighteen',
    'Job Post Example Six',
    'Job Post Example Fifteen']

most_applied_job_result_show_a_pro_2 = [
    'Job Post Example Five',
    'Job Post Example Three',
    'Job Post Example Twenty',
    'Job Post Example Eleven',
    'Job Post Example Fourteen Double',
    'Job Post Example Seventeen',
    'Job Post Example Company Two',
    'Job Post Example Fourteen',
    'Job Post Example Fourteen Single',
    'Job Post Example Nine',
    'Job Post Example Fourteen',
    'Job Post Example Twenty One',
    'Job Post Example Twenty Four',
    'Job Post Example Company Four',
    'Job Post Example Seven',
    'Job Post Example One',
    'Job Post Example Company Six',
    'Job Post Example Company Three',
    'Job Post Example Nineteen',
    'Job Post Example Eight',
    'Job Post Example Company Five',
    'Job Post Example Company Ten',
    'Job Post Example Sixteen',
    'Job Post Example Twenty Five',
    'Job Post Example Ten',
    'Job Post Example Twenty Two',
    'Job Post Example Nineteen Seven',
    'Job Post Example Company Eight',
    'Job Post Example Thirteen',
    'Job Post Example Company Nine',
    'Job Post Example Two',
    'Job Post Example Twelve',
    'Job Post Example Twenty Three',
    'Job Post Example Eighteen',
    'Job Post Example Six',
    'Job Post Example Fifteen']


most_applied_job_result_show_a_pro_3 = [
    'Job Post Example Five',
    'Job Post Example Three',
    'Job Post Example Twenty',
    'Job Post Example Fourteen',
    'Job Post Example Eleven',
    'Job Post Example Fourteen Double',
    'Job Post Example Twenty One',
    'Job Post Example Seventeen',
    'Job Post Example Company Two',
    'Job Post Example Fourteen',
    'Job Post Example Fourteen Single',
    'Job Post Example Nine',
    'Job Post Example Twenty Four',
    'Job Post Example Company Four',
    'Job Post Example Seven',
    'Job Post Example One',
    'Job Post Example Company Six',
    'Job Post Example Company Three',
    'Job Post Example Nineteen',
    'Job Post Example Eight',
    'Job Post Example Company Five',
    'Job Post Example Company Ten',
    'Job Post Example Sixteen',
    'Job Post Example Twenty Five',
    'Job Post Example Ten',
    'Job Post Example Twenty Two',
    'Job Post Example Nineteen Seven',
    'Job Post Example Company Eight',
    'Job Post Example Thirteen',
    'Job Post Example Company Nine',
    'Job Post Example Two',
    'Job Post Example Twelve',
    'Job Post Example Twenty Three',
    'Job Post Example Eighteen',
    'Job Post Example Six',
    'Job Post Example Fifteen']



most_applied_job_result_show_a_pro_4 = [
    'Job Post Example Five',
    'Job Post Example Three',
    'Job Post Example Twenty',
    'Job Post Example Fourteen',
    'Job Post Example Eleven',
    'Job Post Example Fourteen Double',
    'Job Post Example Twenty One',
    'Job Post Example Twenty Four',
    'Job Post Example Nineteen',
    'Job Post Example Seventeen',
    'Job Post Example Company Two',
    'Job Post Example Fourteen',
    'Job Post Example Fourteen Single',
    'Job Post Example Nine',
    'Job Post Example Company Four',
    'Job Post Example Seven',
    'Job Post Example One',
    'Job Post Example Company Six',
    'Job Post Example Company Three',
    'Job Post Example Eight',
    'Job Post Example Company Five',
    'Job Post Example Company Ten',
    'Job Post Example Sixteen',
    'Job Post Example Twenty Five',
    'Job Post Example Ten',
    'Job Post Example Twenty Two',
    'Job Post Example Nineteen Seven',
    'Job Post Example Company Eight',
    'Job Post Example Thirteen',
    'Job Post Example Company Nine',
    'Job Post Example Two',
    'Job Post Example Twelve',
    'Job Post Example Twenty Three',
    'Job Post Example Eighteen',
    'Job Post Example Six',
    'Job Post Example Fifteen']

most_applied_job_result_show = [
    'Job Post Example Five',
    'Job Post Example Three',
    'Job Post Example Twenty',
    'Job Post Example Eleven',
    'Job Post Example Fourteen Double',
    'Job Post Example Seventeen',
    'Job Post Example Company Two',
    'Job Post Example Fourteen',
    'Job Post Example Fourteen Single',
    'Job Post Example Nine',
    'Job Post Example Four',
    'Job Post Example Fourteen',
    'Job Post Example Twenty One',
    'Job Post Example Twenty Four',
    'Job Post Example Company Four',
    'Job Post Example Seven',
    'Job Post Example One',
    'Job Post Example Company Six',
    'Job Post Example Company Three',
    'Job Post Example Nineteen',
    'Job Post Example Eight',
    'Job Post Example Company Five',
    'Job Post Example Company Ten',
    'Job Post Example Sixteen',
    'Job Post Example Twenty Five',
    'Job Post Example Ten',
    'Job Post Example Twenty Two',
    'Job Post Example Nineteen Seven',
    'Job Post Example Company Eight',
    'Job Post Example Thirteen',
    'Job Post Example Company Nine',
    'Job Post Example Two',
    'Job Post Example Twelve',
    'Job Post Example Twenty Three',
    'Job Post Example Eighteen',
    'Job Post Example Six',
    'Job Post Example Fifteen'
]

most_applied_job_result_show_10 = [
    'Job Post Example Five',
    'Job Post Example Three',
    'Job Post Example Twenty',
    'Job Post Example Eleven',
    'Job Post Example Fourteen Double',
    'Job Post Example Seventeen',
    'Job Post Example Company Two',
    'Job Post Example Fourteen',
    'Job Post Example Fourteen Single',
    'Job Post Example Nine']

most_applied_job_result_show_10_a = [
    'Job Post Example Five',
    'Job Post Example Three',
    'Job Post Example Twenty',
    'Job Post Example Four',
    'Job Post Example Eleven',
    'Job Post Example Fourteen Double',
    'Job Post Example Seventeen',
    'Job Post Example Company Two',
    'Job Post Example Fourteen',
    'Job Post Example Fourteen Single']

most_applied_job_result_show_10_a_pro = [
    'Job Post Example Five',
    'Job Post Example Three',
    'Job Post Example Twenty',
    'Job Post Example Eleven',
    'Job Post Example Fourteen Double',
    'Job Post Example Nineteen',
    'Job Post Example Seventeen',
    'Job Post Example Company Two',
    'Job Post Example Fourteen',
    'Job Post Example Fourteen Single']

most_applied_job_result_show_10_a_pro_b = [
    'Job Post Example Five',
    'Job Post Example Three',
    'Job Post Example Twenty',
    'Job Post Example Fourteen',
    'Job Post Example Eleven',
    'Job Post Example Fourteen Double',
    'Job Post Example Twenty One',
    'Job Post Example Twenty Four',
    'Job Post Example Nineteen',
    'Job Post Example Seventeen']

most_applied_job_result_show_10_a_pro_c = ['Job Post Example Five', 'Job Post Example Three', 'Job Post Example Twenty', 'Job Post Example Fourteen', 'Job Post Example Eleven', 'Job Post Example Fourteen Double', 'Job Post Example Twenty One', 'Job Post Example Seventeen', 'Job Post Example Company Two', 'Job Post Example Fourteen']
# job category wise search result
job_category_1_result = ("Showing 1 - 10 of 15 Jobs")
job_category_1_result_api = ("Showing 1 - 10 of 14 Jobs")
job_search_category_1_result = [
    'Job Post Example Four',
    'Job Post Example Fourteen Double',
    'Job Post Example Five',
    'Job Post Example Three',
    'Job Post Example Seven',
    'Job Post Example Fourteen',
    'Job Post Example Fourteen Single',
    'Job Post Example Fifteen',
    'Job Post Example One',
    'Job Post Example Six',
    'Job Post Example Eight',
    'Job Post Example Sixteen',
    'Job Post Example Company Six',
    'Job Post Example Company Five',
    'Job Post Example Company Two']

job_search_category_1_result_api = [
    'Job Post Example Fourteen Double',
    'Job Post Example Five',
    'Job Post Example Three',
    'Job Post Example Seven',
    'Job Post Example Fourteen',
    'Job Post Example Fourteen Single',
    'Job Post Example Fifteen',
    'Job Post Example One',
    'Job Post Example Six',
    'Job Post Example Eight',
    'Job Post Example Sixteen',
    'Job Post Example Company Six',
    'Job Post Example Company Five',
    'Job Post Example Company Two']

job_search_category_1_result_10 = [
    'Job Post Example Four',
    'Job Post Example Fourteen Double',
    'Job Post Example Five',
    'Job Post Example Three',
    'Job Post Example Seven',
    'Job Post Example Fourteen',
    'Job Post Example Fourteen Single',
    'Job Post Example Fifteen',
    'Job Post Example One',
    'Job Post Example Six']

job_search_category_1_result_10_api = [
    'Job Post Example Fourteen Double',
    'Job Post Example Five',
    'Job Post Example Three',
    'Job Post Example Seven',
    'Job Post Example Fourteen',
    'Job Post Example Fourteen Single',
    'Job Post Example Fifteen',
    'Job Post Example One',
    'Job Post Example Six',
    'Job Post Example Eight']

job_category_2_result = ("Showing 1 - 10 of 19 Jobs")
job_category_2_result_api = ("Showing 1 - 10 of 20 Jobs")
job_search_category_2_result = [
    'Job Post Example Eleven',
    'Job Post Example Twenty One',
    'Job Post Example Twenty Four',
    'Job Post Example Twenty',
    'Job Post Example Nineteen',
    'Job Post Example Seventeen',
    'Job Post Example Nine',
    'Job Post Example Two',
    'Job Post Example Twenty Three',
    'Job Post Example Eighteen',
    'Job Post Example Twenty Two',
    'Job Post Example Twenty Five',
    'Job Post Example Ten',
    'Job Post Example Company Four',
    'Job Post Example Company Three',
    'Job Post Example Company Ten',
    'Job Post Example Nineteen Seven',
    'Job Post Example Company Eight',
    'Job Post Example Company Nine']

job_search_category_2_result_api = [
    'Title Example',
    'Job Post Example Eleven',
    'Job Post Example Twenty One',
    'Job Post Example Twenty Four',
    'Job Post Example Twenty',
    'Job Post Example Nineteen',
    'Job Post Example Seventeen',
    'Job Post Example Nine',
    'Job Post Example Two',
    'Job Post Example Twenty Three',
    'Job Post Example Eighteen',
    'Job Post Example Twenty Two',
    'Job Post Example Twenty Five',
    'Job Post Example Ten',
    'Job Post Example Company Four',
    'Job Post Example Company Three',
    'Job Post Example Company Ten',
    'Job Post Example Nineteen Seven',
    'Job Post Example Company Eight',
    'Job Post Example Company Nine']

job_search_category_2_result_10 = [
    'Job Post Example Eleven',
    'Job Post Example Twenty One',
    'Job Post Example Twenty Four',
    'Job Post Example Twenty',
    'Job Post Example Nineteen',
    'Job Post Example Seventeen',
    'Job Post Example Nine',
    'Job Post Example Two',
    'Job Post Example Twenty Three',
    'Job Post Example Eighteen']

job_search_category_2_result_10_api = [
    'Title Example',
    'Job Post Example Eleven',
    'Job Post Example Twenty One',
    'Job Post Example Twenty Four',
    'Job Post Example Twenty',
    'Job Post Example Nineteen',
    'Job Post Example Seventeen',
    'Job Post Example Nine',
    'Job Post Example Two',
    'Job Post Example Twenty Three']

job_category_3_result = ("Showing 1 - 3 of 3 Jobs")
job_search_category_3_result = [
    'Job Post Example Fourteen',
    'Job Post Example Twelve',
    'Job Post Example Thirteen'
]

# skill wise search result
job_skill_python_result = ("Showing 1 - 10 of 18 Jobs")
job_search_skill_python_result = [
    'Job Post Example Twenty One',
    'Job Post Example Twenty Four',
    'Job Post Example Twenty',
    'Job Post Example Nineteen',
    'Job Post Example One',
    'Job Post Example Nine',
    'Job Post Example Two',
    'Job Post Example Twenty Three',
    'Job Post Example Six',
    'Job Post Example Eighteen',
    'Job Post Example Twenty Two',
    'Job Post Example Twenty Five',
    'Job Post Example Eight',
    'Job Post Example Company Three',
    'Job Post Example Company Ten',
    'Job Post Example Nineteen Seven',
    'Job Post Example Company Eight',
    'Job Post Example Company Nine']

job_search_skill_python_result_10 = [
    'Job Post Example Twenty One',
    'Job Post Example Twenty Four',
    'Job Post Example Twenty',
    'Job Post Example Nineteen',
    'Job Post Example One',
    'Job Post Example Nine',
    'Job Post Example Two',
    'Job Post Example Twenty Three',
    'Job Post Example Six',
    'Job Post Example Eighteen']

# job type search result
contractual_job_result = ("Showing 1 - 10 of 12 Jobs")
contractual_job_search_result = [
    'Job Post Example Four',
    'Job Post Example Twenty One',
    'Job Post Example Twenty Four',
    'Job Post Example Five',
    'Job Post Example Twenty',
    'Job Post Example Nineteen',
    'Job Post Example Fourteen',
    'Job Post Example Fifteen',
    'Job Post Example Twenty Three',
    'Job Post Example Six',
    'Job Post Example Twenty Two',
    'Job Post Example Twenty Five'
]

contractual_job_search_result_10 = [
    'Job Post Example Four',
    'Job Post Example Twenty One',
    'Job Post Example Twenty Four',
    'Job Post Example Five',
    'Job Post Example Twenty',
    'Job Post Example Nineteen',
    'Job Post Example Fourteen',
    'Job Post Example Fifteen',
    'Job Post Example Twenty Three',
    'Job Post Example Six']

internship_job_result = ("Showing 0 - 0 of 0 Jobs")
internship_job_search_result = []
permanent_ft_job_result = ("Showing 0 - 0 of 0 Jobs")
permanent_ft_job_search_result = []
permanent_pt_job_result = ("Showing 0 - 0 of 0 Jobs")
permanent_pt_job_search_result = []

# unspecified Salary search result
deselect_unspecified_job_result = ("Showing 1 - 10 of 32 Jobs")
deselect_unspecified_job_result_api = ("Showing 1 - 10 of 31 Jobs")
deselect_unspecified_job_result_api_pro = ("Showing 1 - 10 of 30 Jobs")
deselect_unspecified_job_search_result = [
    'Job Post Example Four',
    'Job Post Example Fourteen',
    'Job Post Example Eleven',
    'Job Post Example Fourteen Double',
    'Job Post Example Five',
    'Job Post Example Three',
    'Job Post Example Seven',
    'Job Post Example Twenty',
    'Job Post Example Nineteen',
    'Job Post Example Seventeen',
    'Job Post Example Fourteen',
    'Job Post Example Fourteen Single',
    'Job Post Example Fifteen',
    'Job Post Example One',
    'Job Post Example Nine',
    'Job Post Example Two',
    'Job Post Example Six',
    'Job Post Example Eighteen',
    'Job Post Example Twelve',
    'Job Post Example Thirteen',
    'Job Post Example Eight',
    'Job Post Example Ten',
    'Job Post Example Sixteen',
    'Job Post Example Company Four',
    'Job Post Example Company Six',
    'Job Post Example Company Three',
    'Job Post Example Company Five',
    'Job Post Example Company Ten',
    'Job Post Example Nineteen Seven',
    'Job Post Example Company Eight',
    'Job Post Example Company Nine',
    'Job Post Example Company Two']

deselect_unspecified_job_search_result_api = [
    'Title Example',
    'Job Post Example Fourteen',
    'Job Post Example Eleven',
    'Job Post Example Fourteen Double',
    'Job Post Example Five',
    'Job Post Example Three',
    'Job Post Example Seven',
    'Job Post Example Twenty',
    'Job Post Example Nineteen',
    'Job Post Example Seventeen',
    'Job Post Example Fourteen',
    'Job Post Example Fourteen Single',
    'Job Post Example Fifteen',
    'Job Post Example One',
    'Job Post Example Nine',
    'Job Post Example Two',
    'Job Post Example Six',
    'Job Post Example Eighteen',
    'Job Post Example Twelve',
    'Job Post Example Thirteen',
    'Job Post Example Eight',
    'Job Post Example Ten',
    'Job Post Example Sixteen',
    'Job Post Example Company Four',
    'Job Post Example Company Six',
    'Job Post Example Company Three',
    'Job Post Example Company Five',
    'Job Post Example Company Ten',
    'Job Post Example Nineteen Seven',
    'Job Post Example Company Eight',
    'Job Post Example Company Nine',
    'Job Post Example Company Two']

deselect_unspecified_job_search_result_api_pro = [
    'Job Post Example Fourteen',
    'Job Post Example Eleven',
    'Job Post Example Fourteen Double',
    'Job Post Example Five',
    'Job Post Example Three',
    'Job Post Example Seven',
    'Job Post Example Twenty',
    'Job Post Example Nineteen',
    'Job Post Example Seventeen',
    'Job Post Example Fourteen',
    'Job Post Example Fourteen Single',
    'Job Post Example Fifteen',
    'Job Post Example One',
    'Job Post Example Nine',
    'Job Post Example Two',
    'Job Post Example Six',
    'Job Post Example Eighteen',
    'Job Post Example Twelve',
    'Job Post Example Thirteen',
    'Job Post Example Eight',
    'Job Post Example Ten',
    'Job Post Example Sixteen',
    'Job Post Example Company Four',
    'Job Post Example Company Six',
    'Job Post Example Company Three',
    'Job Post Example Company Five',
    'Job Post Example Company Ten',
    'Job Post Example Nineteen Seven',
    'Job Post Example Company Eight',
    'Job Post Example Company Nine',
    'Job Post Example Company Two']

deselect_unspecified_job_search_result_10 = [
    'Job Post Example Four',
    'Job Post Example Fourteen',
    'Job Post Example Eleven',
    'Job Post Example Fourteen Double',
    'Job Post Example Five',
    'Job Post Example Three',
    'Job Post Example Seven',
    'Job Post Example Twenty',
    'Job Post Example Nineteen',
    'Job Post Example Seventeen']

deselect_unspecified_job_search_result_10_api = [
    'Title Example',
    'Job Post Example Fourteen',
    'Job Post Example Eleven',
    'Job Post Example Fourteen Double',
    'Job Post Example Five',
    'Job Post Example Three',
    'Job Post Example Seven',
    'Job Post Example Twenty',
    'Job Post Example Nineteen',
    'Job Post Example Seventeen']

deselect_unspecified_job_search_result_10_api_pro = [
    'Job Post Example Fourteen',
    'Job Post Example Eleven',
    'Job Post Example Fourteen Double',
    'Job Post Example Five',
    'Job Post Example Three',
    'Job Post Example Seven',
    'Job Post Example Twenty',
    'Job Post Example Nineteen',
    'Job Post Example Seventeen',
    'Job Post Example Fourteen']

select_unspecified_job_result = ("Showing 1 - 10 of 28 Jobs")
select_unspecified_job_search_result = [
    'Job Post Example Four',
    'Job Post Example Fourteen',
    'Job Post Example Eleven',
    'Job Post Example Fourteen',
    'Job Post Example Twenty One',
    'Job Post Example Twenty Four',
    'Job Post Example Five',
    'Job Post Example Three',
    'Job Post Example Seven',
    'Job Post Example Twenty',
    'Job Post Example Nineteen',
    'Job Post Example Seventeen',
    'Job Post Example Fourteen',
    'Job Post Example Fourteen',
    'Job Post Example Fifteen',
    'Job Post Example One',
    'Job Post Example Nine',
    'Job Post Example Two',
    'Job Post Example Twenty Three',
    'Job Post Example Six',
    'Job Post Example Eighteen',
    'Job Post Example Twelve',
    'Job Post Example Thirteen',
    'Job Post Example Twenty Two',
    'Job Post Example Twenty Five',
    'Job Post Example Eight',
    'Job Post Example Ten',
    'Job Post Example Sixteen'
]

select_unspecified_job_search_result_10 = [
    'Job Post Example Four',
    'Job Post Example Fourteen',
    'Job Post Example Eleven',
    'Job Post Example Fourteen',
    'Job Post Example Twenty One',
    'Job Post Example Twenty Four',
    'Job Post Example Five',
    'Job Post Example Three',
    'Job Post Example Seven',
    'Job Post Example Twenty']

# date wise posted search result
last_hour_result = ("Showing 0 - 0 of 0 Jobs")
last_hour_search_result = []
last_24_hour_result = ("Showing 0 - 0 of 0 Jobs")
last_24_hour_search_result = []
last_7_days_result = ("Showing 0 - 0 of 0 Jobs")
last_7_days_search_result = []
last_14_days_result = ("Showing 0 - 0 of 0 Jobs")
last_14_days_search_result = []
last_30_days_result = ("Showing 0 - 0 of 0 Jobs")
last_30_days_search_result = []

# gender wise search result
any_gender_result = ("Showing 1 - 10 of 28 Jobs")
any_gender_search_result = [
    'Job Post Example Four',
    'Job Post Example Fourteen',
    'Job Post Example Eleven',
    'Job Post Example Fourteen',
    'Job Post Example Twenty One',
    'Job Post Example Twenty Four',
    'Job Post Example Five',
    'Job Post Example Three',
    'Job Post Example Seven',
    'Job Post Example Twenty',
    'Job Post Example Nineteen',
    'Job Post Example Seventeen',
    'Job Post Example Fourteen',
    'Job Post Example Fourteen',
    'Job Post Example Fifteen',
    'Job Post Example One',
    'Job Post Example Nine',
    'Job Post Example Two',
    'Job Post Example Twenty Three',
    'Job Post Example Six',
    'Job Post Example Eighteen',
    'Job Post Example Twelve',
    'Job Post Example Thirteen',
    'Job Post Example Twenty Two',
    'Job Post Example Twenty Five',
    'Job Post Example Eight',
    'Job Post Example Ten',
    'Job Post Example Sixteen'
]

any_gender_search_result_10 = [
    'Job Post Example Four',
    'Job Post Example Fourteen',
    'Job Post Example Eleven',
    'Job Post Example Fourteen',
    'Job Post Example Twenty One',
    'Job Post Example Twenty Four',
    'Job Post Example Five',
    'Job Post Example Three',
    'Job Post Example Seven',
    'Job Post Example Twenty']

female_gender_result = ("Showing 1 - 6 of 6 Jobs")
female_gender_search_result = [
    'Job Post Example Fourteen',
    'Job Post Example Fourteen',
    'Job Post Example Two',
    'Job Post Example Twelve',
    'Job Post Example Thirteen',
    'Job Post Example Sixteen'
]
male_gender_result = ("Showing 1 - 10 of 13 Jobs")
male_gender_search_result = [
    'Job Post Example Eleven',
    'Job Post Example Twenty One',
    'Job Post Example Twenty Four',
    'Job Post Example Twenty',
    'Job Post Example Nineteen',
    'Job Post Example Seventeen',
    'Job Post Example One',
    'Job Post Example Nine',
    'Job Post Example Twenty Three',
    'Job Post Example Eighteen',
    'Job Post Example Twenty Two',
    'Job Post Example Twenty Five',
    'Job Post Example Ten'
]

male_gender_search_result_10 = [
    'Job Post Example Eleven',
    'Job Post Example Twenty One',
    'Job Post Example Twenty Four',
    'Job Post Example Twenty',
    'Job Post Example Nineteen',
    'Job Post Example Seventeen',
    'Job Post Example One',
    'Job Post Example Nine',
    'Job Post Example Twenty Three',
    'Job Post Example Eighteen']

# qualification wise search result
qualification_one_result = ("Showing 1 - 10 of 14 Jobs")
qualification_one_result_api = ("Showing 1 - 10 of 13 Jobs")
qualification_one_search_result = [
    'Job Post Example Four',
    'Job Post Example Eleven',
    'Job Post Example Twenty One',
    'Job Post Example Twenty Four',
    'Job Post Example Five',
    'Job Post Example Three',
    'Job Post Example Seven',
    'Job Post Example One',
    'Job Post Example Nine',
    'Job Post Example Twenty Three',
    'Job Post Example Six',
    'Job Post Example Twenty Two',
    'Job Post Example Twenty Five',
    'Job Post Example Eight'
]
qualification_one_search_result_api = [
    'Job Post Example Eleven',
    'Job Post Example Twenty One',
    'Job Post Example Twenty Four',
    'Job Post Example Five',
    'Job Post Example Three',
    'Job Post Example Seven',
    'Job Post Example One',
    'Job Post Example Nine',
    'Job Post Example Twenty Three',
    'Job Post Example Six',
    'Job Post Example Twenty Two',
    'Job Post Example Twenty Five',
    'Job Post Example Eight']

qualification_one_search_result_10 = [
    'Job Post Example Four',
    'Job Post Example Eleven',
    'Job Post Example Twenty One',
    'Job Post Example Twenty Four',
    'Job Post Example Five',
    'Job Post Example Three',
    'Job Post Example Seven',
    'Job Post Example One',
    'Job Post Example Nine',
    'Job Post Example Twenty Three']

qualification_one_search_result_10_api = [
    'Job Post Example Eleven',
    'Job Post Example Twenty One',
    'Job Post Example Twenty Four',
    'Job Post Example Five',
    'Job Post Example Three',
    'Job Post Example Seven',
    'Job Post Example One',
    'Job Post Example Nine',
    'Job Post Example Twenty Three',
    'Job Post Example Six']

qualification_two_result = ("Showing 1 - 10 of 22 Jobs")
qualification_two_search_result = [
    'Job Post Example Fourteen',
    'Job Post Example Fourteen Double',
    'Job Post Example Twenty',
    'Job Post Example Nineteen',
    'Job Post Example Seventeen',
    'Job Post Example Fourteen',
    'Job Post Example Fourteen Single',
    'Job Post Example Fifteen',
    'Job Post Example Two',
    'Job Post Example Eighteen',
    'Job Post Example Twelve',
    'Job Post Example Thirteen',
    'Job Post Example Sixteen',
    'Job Post Example Company Four',
    'Job Post Example Company Six',
    'Job Post Example Company Three',
    'Job Post Example Company Five',
    'Job Post Example Company Ten',
    'Job Post Example Nineteen Seven',
    'Job Post Example Company Eight',
    'Job Post Example Company Nine',
    'Job Post Example Company Two']

qualification_two_search_result_10 = [
    'Job Post Example Fourteen',
    'Job Post Example Fourteen Double',
    'Job Post Example Twenty',
    'Job Post Example Nineteen',
    'Job Post Example Seventeen',
    'Job Post Example Fourteen',
    'Job Post Example Fourteen Single',
    'Job Post Example Fifteen',
    'Job Post Example Two',
    'Job Post Example Eighteen']

qualification_three_result = ("Showing 1 - 1 of 1 Jobs")
qualification_three_search_result = [
    'Job Post Example Ten'
]
qualification_four_result = ("Showing 0 - 0 of 0 Jobs")
qualification_four_result_api = ("Showing 1 - 1 of 1 Jobs")
qualification_four_search_result = []
qualification_four_search_result_api = ['Title Example']
qualification_five_result = ("Showing 0 - 0 of 0 Jobs")
qualification_five_search_result = []

# apply button wise search result
apply_error_message = ("This field is required.")
captcha_error_message = ("You can't leave Captcha")


class TestJobSearchTotalResultCount(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = webdriver.WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        time.sleep(DELAY_SHORT)

    def test_job_search__when_signed_in__view_total_jobs__should_pss(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        data = {
            "email": VALID_PRO_USERNAME,
            "password": VALID_PRO_PASSWORD,
        }
        signin_helper(driver, data)
        job_search_helper(driver, data)
        try:
            total_result = driver.find_element_by_class_name('showing-number').text
            if total_result != total_result_show and total_result != total_result_show_pro:
                self.fail()

            titles = []
            i = 0;
            page_count = driver.find_elements_by_class_name('page-item ').__len__()
            time.sleep(1)
            for i in range(i, page_count - 2):
                if i <= page_count - 3:
                    time.sleep(1)
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
            if titles != total_job_result_show and titles != total_job_result_show_api and titles != total_job_result_show_api_pro:
                self.fail()

            profile_btn = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[6]/button')
            profile_btn.click()
            time.sleep(1)
            sign_out_btn = driver.find_element_by_xpath('//*[@id="userNavbarMain"]/ul/li[3]/a/span')
            sign_out_btn.click()


        except NoSuchElementException:
            self.fail('Not ok')

    def test_job_search__when_not_signed_in__view_total_jobs__should_pss(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        data = {

        }
        job_search_helper(driver, data)
        try:
            total_result = driver.find_element_by_class_name('showing-number').text
            if total_result != total_result_show and total_result != total_result_show_pro:
                self.fail()

            titles = []
            i = 0;
            page_count = driver.find_elements_by_class_name('page-item ').__len__()
            for i in range(i, page_count - 2):
                if i <= page_count - 3:
                    time.sleep(1)
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
                    try:
                        signin_button = driver.find_element_by_id('signinButton')
                        pass
                    except:
                        self.fail()
                break

                time.sleep(DELAY_SHORT)
            if titles != total_job_result_show_10 and titles != total_job_result_show_10_api and titles != total_job_result_show_10_api_pro:
                self.fail()

        except NoSuchElementException:
            self.fail('Not ok')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


class TestKeywordSearchResultCount(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = webdriver.WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        time.sleep(DELAY_SHORT)

    def test_job_search__when_job_serch_valid_job__should_pss(self):
        driver = self.driver
        data = {
            "job_search": 'one'
        }
        job_search_helper(driver, data)
        try:
            search_button = driver.find_element_by_id("search-keyword")
            search_button.click()
            search_button.send_keys(data['job_search'])
            click_button = driver.find_element_by_class_name("search-job-button")
            click_button.click()
            time.sleep(2)
            job_result = driver.find_element_by_class_name('showing-number').text
            self.assertEqual(job_result, job_search_result_one)
            titles = []
            i = 0;
            page_count = driver.find_elements_by_class_name('page-item ').__len__()
            for i in range(i, page_count - 2):
                if i <= page_count - 3:
                    time.sleep(1)
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

            self.assertEqual(titles, job_post_search_result_one)
        except NoSuchElementException:
            self.fail('Not ok')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


class TestFilterSearchResultCount(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = webdriver.WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        time.sleep(DELAY_SHORT)

    def test_filter_search__when_signed_in_job_search_most_recent_job__should_pss(self):
        driver = self.driver
        data = {
            "email": VALID_PRO_USERNAME,
            "password": VALID_PRO_PASSWORD,
        }
        signin_helper(driver, data)
        job_search_helper(driver, data)
        try:
            most_recent = driver.find_element_by_xpath('//*[@id="jobs"]/div[1]/div[1]/div/div/button/div/div/div')
            most_recent.click()
            time.sleep(1)
            select_most_recent = driver.find_element_by_id('bs-select-1-0')
            select_most_recent.click()
            time.sleep(2)
            total_result = driver.find_element_by_class_name('showing-number').text
            if total_result != total_result_show and total_result != total_result_show_pro:
                self.fail()

            titles = []
            i = 0;
            page_count = driver.find_elements_by_class_name('page-item ').__len__()
            for i in range(i, page_count - 2):
                if i <= page_count - 3:
                    time.sleep(1)
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

            if titles != total_job_result_show and titles != total_job_result_show_api and titles != total_job_result_show_api_pro:
                self.fail()

            profile_btn = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[6]/button')
            profile_btn.click()
            time.sleep(1)
            sign_out_btn = driver.find_element_by_xpath('//*[@id="userNavbarMain"]/ul/li[3]/a/span')
            sign_out_btn.click()

        except NoSuchElementException:
            self.fail('Not ok')

    def test_filter_search__when_not_signed_in__job_search_most_recent_job__should_pss(self):
        driver = self.driver
        data = {

        }
        job_search_helper(driver, data)
        try:
            time.sleep(DELAY_SHORT)
            most_recent = driver.find_element_by_xpath('//*[@id="jobs"]/div[1]/div[1]/div/div/button/div/div/div')
            time.sleep(1)
            most_recent.click()
            time.sleep(1)
            select_most_recent = driver.find_element_by_id('bs-select-1-0')
            select_most_recent.click()
            time.sleep(2)
            total_result = driver.find_element_by_class_name('showing-number').text
            if total_result != total_result_show and total_result != total_result_show_pro:
                self.fail()

            titles = []
            i = 0;
            page_count = driver.find_elements_by_class_name('page-item ').__len__()
            for i in range(i, page_count - 2):
                if i <= page_count - 3:
                    time.sleep(1)
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
                    try:
                        signin_button = driver.find_element_by_id('signinButton')
                        pass
                    except:
                        self.fail()
                break
                time.sleep(1)

            if titles != total_job_result_show_10 and titles != total_job_result_show_10_api and titles != total_job_result_show_10_api_pro:
                self.fail()

        except NoSuchElementException:
            self.fail('Not ok')

    def test_filter_search__when_signed_in__job_search_top_rated_job__should_pss(self):
        driver = self.driver
        data = {
            "email": VALID_PRO_USERNAME,
            "password": VALID_PRO_PASSWORD,
        }
        signin_helper(driver, data)
        job_search_helper(driver, data)
        try:
            time.sleep(DELAY_SHORT)
            most_recent = driver.find_element_by_xpath('//*[@id="jobs"]/div[1]/div[1]/div/div/button/div/div/div')
            time.sleep(1)
            most_recent.click()
            time.sleep(1)
            select_top_rated = driver.find_element_by_id('bs-select-1-1')
            select_top_rated.click()
            time.sleep(2)
            total_result = driver.find_element_by_class_name('showing-number').text
            if total_result != total_result_show and total_result != total_result_show_pro:
                self.fail()

            titles = []
            i = 0;
            page_count = driver.find_elements_by_class_name('page-item ').__len__()
            for i in range(i, page_count - 2):
                if i <= page_count - 3:
                    time.sleep(1)
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

            if titles != top_rated_job_result_show and titles != top_rated_job_result_show_api and titles != top_rated_job_result_show_api_pro:
                self.fail()


            profile_btn = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[6]/button')
            profile_btn.click()
            time.sleep(1)
            sign_out_btn = driver.find_element_by_xpath('//*[@id="userNavbarMain"]/ul/li[3]/a/span')
            sign_out_btn.click()

        except NoSuchElementException:
            self.fail('Not ok')

    def test_filter_search__when_not_signed_in__job_search_top_rated_job__should_pss(self):
        driver = self.driver
        data = {

        }
        job_search_helper(driver, data)
        try:
            time.sleep(DELAY_SHORT)
            most_recent = driver.find_element_by_xpath('//*[@id="jobs"]/div[1]/div[1]/div/div/button/div/div/div')
            most_recent.click()
            time.sleep(1)
            select_top_rated = driver.find_element_by_id('bs-select-1-1')
            select_top_rated.click()
            time.sleep(2)
            total_result = driver.find_element_by_class_name('showing-number').text
            if total_result != total_result_show and total_result != total_result_show_pro:
                self.fail()
            titles = []
            i = 0;
            page_count = driver.find_elements_by_class_name('page-item ').__len__()
            for i in range(i, page_count - 2):
                if i <= page_count - 3:
                    time.sleep(1)
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
                    try:
                        signin_button = driver.find_element_by_id('signinButton')
                        pass
                    except:
                        self.fail()
                break
                time.sleep(1)

            if titles != top_rated_job_result_show_10:
                self.fail()
        except NoSuchElementException:
            self.fail('Not ok')

    def test_filter_search__when_signed_in__job_search_most_applied_job__should_pss(self):
        driver = self.driver
        data = {
            "email": VALID_PRO_USERNAME,
            "password": VALID_PRO_PASSWORD,
        }
        signin_helper(driver, data)
        job_search_helper(driver, data)
        try:
            most_recent = driver.find_element_by_xpath('//*[@id="jobs"]/div[1]/div[1]/div/div/button/div/div/div')
            most_recent.click()
            time.sleep(1)
            select_most_applied = driver.find_element_by_id('bs-select-1-2')
            select_most_applied.click()
            time.sleep(2)
            total_result = driver.find_element_by_class_name('showing-number').text

            if total_result != total_result_show and total_result != total_result_show_pro:
                self.fail()

            titles = []
            i = 0;
            page_count = driver.find_elements_by_class_name('page-item ').__len__()
            for i in range(i, page_count - 2):
                time.sleep(1)
                if i <= page_count - 3:
                    time.sleep(1)
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

            if titles != most_applied_job_result_show and titles != most_applied_job_result_show_a and titles != most_applied_job_result_show_a_pro and titles != most_applied_job_result_show_a_pro_2 and titles != most_applied_job_result_show_a_pro_3 and titles != most_applied_job_result_show_a_pro_4:
                self.fail()

            profile_btn = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[6]/button')
            profile_btn.click()
            time.sleep(1)
            sign_out_btn = driver.find_element_by_xpath('//*[@id="userNavbarMain"]/ul/li[3]/a/span')
            sign_out_btn.click()

        except NoSuchElementException:
            self.fail('Not ok')

    def test_filter_search__when_not_signed_in__job_search_most_applied_job__should_pss(self):
        driver = self.driver
        data = {

        }
        job_search_helper(driver, data)
        try:
            most_recent = driver.find_element_by_xpath('//*[@id="jobs"]/div[1]/div[1]/div/div/button/div/div/div')
            most_recent.click()
            time.sleep(1)
            select_most_applied = driver.find_element_by_id('bs-select-1-2')
            select_most_applied.click()
            time.sleep(2)
            total_result = driver.find_element_by_class_name('showing-number').text
            if total_result != total_result_show and total_result != total_result_show_pro:
                self.fail()
            titles = []
            i = 0;
            page_count = driver.find_elements_by_class_name('page-item ').__len__()
            for i in range(i, page_count - 2):
                if i <= page_count - 3:
                    time.sleep(1)
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
                    try:
                        signin_button = driver.find_element_by_id('signinButton')
                        pass
                    except:
                        self.fail()
                break
                time.sleep(1)

            if titles != most_applied_job_result_show_10 and titles != most_applied_job_result_show_10_a and titles != most_applied_job_result_show_10_a_pro and titles != most_applied_job_result_show_10_a_pro_b and titles != most_applied_job_result_show_10_a_pro_c:
                self.fail()
        except NoSuchElementException:
            self.fail('Not ok')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


class TestJobCategorySearchResultCount(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = webdriver.WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        time.sleep(DELAY_SHORT)

    def test_job_filter__when_signed_in__click_job_category_1__should_pass(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        data = {
            "email": VALID_PRO_USERNAME,
            "password": VALID_PRO_PASSWORD,
        }
        signin_helper(driver, data)
        job_search_helper(driver, data)
        try:
            job_category = driver.find_element_by_xpath(
                '/html/body/div[3]/div/div/div/div/div[2]/div[3]/div/button/div/div/div')
            job_category.click()
            job_select_1 = driver.find_element_by_id('bs-select-2-1')
            job_select_1.click()
            time.sleep(2)
            job_category_1 = driver.find_element_by_class_name("showing-number").text
            if job_category_1 == job_category_1_result and job_category_1 == job_category_1_result_api:
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

            if titles != job_search_category_1_result and titles != job_search_category_1_result_api:
                self.fail()

            profile_btn = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[6]/button')
            profile_btn.click()
            time.sleep(1)
            sign_out_btn = driver.find_element_by_xpath('//*[@id="userNavbarMain"]/ul/li[3]/a/span')
            sign_out_btn.click()

        except NoSuchElementException:
            self.fail('Not ok')

    def test_job_filter__when_not_signed_in__click_job_category_1__should_pass(self):
        driver = self.driver
        data = {

        }
        job_search_helper(driver, data)
        try:
            job_category = driver.find_element_by_xpath(
                '/html/body/div[3]/div/div/div/div/div[2]/div[3]/div/button/div/div/div')
            job_category.click()
            job_select_1 = driver.find_element_by_id('bs-select-2-1')
            job_select_1.click()
            time.sleep(2)
            job_category_1 = driver.find_element_by_class_name("showing-number").text

            if job_category_1 != job_category_1_result and job_category_1 != job_category_1_result_api:
                self.fail()

            titles = []
            i = 0;
            page_count = driver.find_elements_by_class_name('page-item ').__len__()
            for i in range(i, page_count - 2):
                if i <= page_count - 3:
                    time.sleep(1)
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
                    try:
                        signin_button = driver.find_element_by_id('signinButton')
                        pass
                    except:
                        self.fail()
                break
                time.sleep(1)

            if titles != job_search_category_1_result_10 and titles != job_search_category_1_result_10_api:
                self.fail()

        except NoSuchElementException:
            self.fail('Not ok')

    def test_job_filter__when_signed_in__click_job_category_2__should_pass(self):
        driver = self.driver
        data = {
            "email": VALID_PRO_USERNAME,
            "password": VALID_PRO_PASSWORD,
        }
        signin_helper(driver, data)
        job_search_helper(driver, data)
        try:
            job_category = driver.find_element_by_xpath(
                '/html/body/div[3]/div/div/div/div/div[2]/div[3]/div/button/div/div/div')
            job_category.click()
            job_select_2 = driver.find_element_by_id('bs-select-2-0')
            job_select_2.click()
            time.sleep(2)
            job_category_2 = driver.find_element_by_class_name("showing-number").text

            if job_category_2 != job_category_2_result and job_category_2 != job_category_2_result_api:
                self.fail()

            titles = []
            i = 0;
            page_count = driver.find_elements_by_class_name('page-item ').__len__()
            for i in range(i, page_count - 2):
                if i <= page_count - 3:
                    time.sleep(1)
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

            if titles != job_search_category_2_result and titles != job_search_category_2_result_api:
                self.fail()

            profile_btn = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[6]/button')
            profile_btn.click()
            time.sleep(1)
            sign_out_btn = driver.find_element_by_xpath('//*[@id="userNavbarMain"]/ul/li[3]/a/span')
            sign_out_btn.click()

        except NoSuchElementException:
            self.fail('Not ok')

    def test_job_filter__when_not_signed_in__click_job_category_2__should_pass(self):
        driver = self.driver
        data = {

        }
        job_search_helper(driver, data)
        try:
            job_category = driver.find_element_by_xpath(
                '/html/body/div[3]/div/div/div/div/div[2]/div[3]/div/button/div/div/div')
            job_category.click()
            job_select_2 = driver.find_element_by_id('bs-select-2-0')
            job_select_2.click()
            time.sleep(2)
            job_category_2 = driver.find_element_by_class_name("showing-number").text

            if job_category_2 != job_category_2_result and job_category_2 != job_category_2_result_api:
                self.fail()

            titles = []
            i = 0;
            page_count = driver.find_elements_by_class_name('page-item ').__len__()
            for i in range(i, page_count - 2):
                if i <= page_count - 3:
                    time.sleep(1)
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
                    try:
                        signin_button = driver.find_element_by_id('signinButton')
                        pass
                    except:
                        self.fail()
                break
                time.sleep(1)

            if titles != job_search_category_2_result_10 and titles != job_search_category_2_result_10_api:
                self.fail()


        except NoSuchElementException:
            self.fail('Not ok')

    def test_job_filter__when_click_job_category_3__should_pass(self):
        driver = self.driver
        data = {

        }
        job_search_helper(driver, data)
        try:
            job_category = driver.find_element_by_xpath(
                '/html/body/div[3]/div/div/div/div/div[2]/div[3]/div/button/div/div/div')
            job_category.click()
            job_select_3 = driver.find_element_by_id('bs-select-2-2')
            job_select_3.click()
            time.sleep(2)
            job_category_3 = driver.find_element_by_class_name("showing-number").text

            self.assertEqual(job_category_3, job_category_3_result)
            titles = []
            i = 0;
            page_count = driver.find_elements_by_class_name('page-item ').__len__()
            for i in range(i, page_count - 2):
                if i <= page_count - 3:
                    time.sleep(1)
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

            self.assertEqual(titles, job_search_category_3_result)

        except NoSuchElementException:
            self.fail('Not ok')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


class TestSkillSearchResultCount(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = webdriver.WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        time.sleep(DELAY_SHORT)

    def test_job_skill__when_signed_in__click_job_skill_python__should_pass(self):
        driver = self.driver
        data = {
            "email": VALID_PRO_USERNAME,
            "password": VALID_PRO_PASSWORD,
        }
        signin_helper(driver, data)
        job_search_helper(driver, data)
        try:
            search_skill_dropdown = driver.find_element_by_xpath(
                '/html/body/div[3]/div/div/div/div/div[2]/div[4]/div/button/div/div/div')
            search_skill_dropdown.click()
            job_skill_1 = driver.find_element_by_id('bs-select-3-0')
            job_skill_1.click()
            time.sleep(5)
            job_skill_python = driver.find_element_by_class_name("showing-number").text
            self.assertEqual(job_skill_python, job_skill_python_result)
            titles = []
            i = 0;
            page_count = driver.find_elements_by_class_name('page-item ').__len__()
            for i in range(i, page_count - 2):
                if i <= page_count - 3:
                    time.sleep(1)
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

            self.assertEqual(titles, job_search_skill_python_result)
            profile_btn = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[6]/button')
            profile_btn.click()
            time.sleep(1)
            sign_out_btn = driver.find_element_by_xpath('//*[@id="userNavbarMain"]/ul/li[3]/a/span')
            sign_out_btn.click()

        except NoSuchElementException:
            self.fail('Not ok')

    def test_job_skill__when_not_signed_in__click_job_skill_python__should_pass(self):
        driver = self.driver
        data = {

        }
        job_search_helper(driver, data)
        try:
            search_skill_dropdown = driver.find_element_by_xpath(
                '/html/body/div[3]/div/div/div/div/div[2]/div[4]/div/button/div/div/div')
            search_skill_dropdown.click()
            job_skill_1 = driver.find_element_by_id('bs-select-3-0')
            job_skill_1.click()
            time.sleep(5)
            job_skill_python = driver.find_element_by_class_name("showing-number").text
            self.assertEqual(job_skill_python, job_skill_python_result)
            titles = []
            i = 0;
            page_count = driver.find_elements_by_class_name('page-item ').__len__()
            for i in range(i, page_count - 2):
                if i <= page_count - 3:
                    time.sleep(1)
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
                    try:
                        signin_button = driver.find_element_by_id('signinButton')
                        pass
                    except:
                        self.fail()
                break
                time.sleep(1)

            self.assertEqual(titles, job_search_skill_python_result_10)
        except NoSuchElementException:
            self.fail('Not ok')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


# class TestJobTypeSearchResultCount(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls) -> None:
#             cls.url = MAIN_URL_HOME
#             cls.driver = webdriver.WebDriver(CHROME_DRIVER_LOCATION)
#             cls.driver.get(cls.url)
#             cls.driver.maximize_window()
#             time.sleep(DELAY_SHORT)
#
#     def test_job_type__when_click_contractual__should_pass(self):
#         driver= self.driver
#         data = {
#
#         }
#         job_search_helper(driver,data)
#         try:
#             contractual = driver.find_element_by_link_text("Contractual")
#             contractual.click()
#             time.sleep(3)
#             contractual_job = driver.find_element_by_class_name("showing-number").text
#             self.assertEqual(contractual_job, contractual_job_result)
#             titles = []
#             i = 0;
#             page_count = driver.find_elements_by_class_name('page-item ').__len__()
#             for i in range(i, page_count-2):
#                 if i <= page_count-3:
#                     page = driver.find_element_by_css_selector('.page-item.active').text
#
#                     time.sleep(1)
#                     self.assertEqual(page, str(i+1))
#                 else:
#                     time.sleep(1)
#                 job_list = driver.find_elements_by_class_name('job-list')
#
#                 for job in job_list:
#
#                     # .  not all companies have review
#                     try:
#                         title = job.find_element_by_tag_name('h4').text
#                     except:
#                         title = ''
#                     if title != '':
#                         titles.append(title)
#                 if i != page_count-3:
#                     time.sleep(1)
#                     page_next = driver.find_element_by_class_name('fa-arrow-right')
#                     page_next.click()
#                 time.sleep(DELAY_SHORT)
#
#             self.assertEqual(titles, contractual_job_search_result)
#         except NoSuchElementException:
#             self.fail('Not ok')
#
#
#     def test_job_type__when_click_internship__should_pass(self):
#         driver= self.driver
#         data = {
#
#
#
#         }
#         job_search_helper(driver,data)
#         try:
#             internship = driver.find_element_by_link_text("Internship")
#             internship.click()
#             time.sleep(3)
#             internship_job = driver.find_element_by_class_name("showing-number").text
#
#             self.assertEqual(internship_job, internship_job_result)
#             titles = []
#             i = 0;
#             page_count = driver.find_elements_by_class_name('page-item ').__len__()
#             for i in range(i, page_count-2):
#                 if i <= page_count-3:
#                     page = driver.find_element_by_css_selector('.page-item.active').text
#
#                     time.sleep(1)
#                     self.assertEqual(page, str(i+1))
#                 else:
#                     time.sleep(1)
#                 job_list = driver.find_elements_by_class_name('job-list')
#
#                 for job in job_list:
#
#                     # .  not all companies have review
#                     try:
#                         title = job.find_element_by_tag_name('h4').text
#                     except:
#                         title = ''
#                     if title != '':
#                         titles.append(title)
#                 if i != page_count-3:
#                     time.sleep(1)
#                     page_next = driver.find_element_by_class_name('fa-arrow-right')
#                     page_next.click()
#                 time.sleep(DELAY_SHORT)
#
#             self.assertEqual(titles, internship_job_search_result)
#         except NoSuchElementException:
#             self.fail('Not ok')
#
#
#     def test_job_type__when_click_permanent_ft__should_pass(self):
#         driver= self.driver
#         data = {
#
#
#
#         }
#         job_search_helper(driver,data)
#         try:
#             Permanent_ft = driver.find_element_by_link_text("Permanent (Full-time)")
#             Permanent_ft.click()
#             time.sleep(3)
#             Permanent_ft_job = driver.find_element_by_class_name("showing-number").text
#
#             self.assertEqual(Permanent_ft_job, permanent_ft_job_result)
#             titles = []
#             i = 0;
#             page_count = driver.find_elements_by_class_name('page-item ').__len__()
#             for i in range(i, page_count-2):
#                 if i <= page_count-3:
#                     page = driver.find_element_by_css_selector('.page-item.active').text
#
#                     time.sleep(1)
#                     self.assertEqual(page, str(i+1))
#                 else:
#                     time.sleep(1)
#                 job_list = driver.find_elements_by_class_name('job-list')
#
#                 for job in job_list:
#
#                     # .  not all companies have review
#                     try:
#                         title = job.find_element_by_tag_name('h4').text
#                     except:
#                         title = ''
#                     if title != '':
#                         titles.append(title)
#                 if i != page_count-3:
#                     time.sleep(1)
#                     page_next = driver.find_element_by_class_name('fa-arrow-right')
#                     page_next.click()
#                 time.sleep(DELAY_SHORT)
#
#             self.assertEqual(titles, permanent_ft_job_search_result)
#         except NoSuchElementException:
#             self.fail('Not ok')
#
#
#     def test_job_type__when_click_permanent_pt__should_pass(self):
#         driver= self.driver
#         data = {
#
#
#
#         }
#         job_search_helper(driver,data)
#         try:
#             permanent_pt = driver.find_element_by_link_text("Permanent (Part-time)")
#             permanent_pt.click()
#             time.sleep(3)
#             permanent_pt_job = driver.find_element_by_class_name("showing-number").text
#
#             self.assertEqual(permanent_pt_job, permanent_pt_job_result)
#             titles = []
#             i = 0
#             page_count = driver.find_elements_by_class_name('page-item ').__len__()
#             for i in range(i, page_count-2):
#                 if i <= page_count-3:
#                     page = driver.find_element_by_css_selector('.page-item.active').text
#
#                     time.sleep(1)
#                     self.assertEqual(page, str(i+1))
#                 else:
#                     time.sleep(1)
#                 job_list = driver.find_elements_by_class_name('job-list')
#
#                 for job in job_list:
#
#                     # .  not all companies have review
#                     try:
#                         title = job.find_element_by_tag_name('h4').text
#                     except:
#                         title = ''
#                     if title != '':
#                         titles.append(title)
#                 if i != page_count-3:
#                     time.sleep(1)
#                     page_next = driver.find_element_by_class_name('fa-arrow-right')
#                     page_next.click()
#                 time.sleep(DELAY_SHORT)
#
#             self.assertEqual(titles, permanent_pt_job_search_result)
#         except NoSuchElementException:
#             self.fail('Not ok')
#
#
#     @classmethod
#     def tearDownClass(cls) -> None:
#             cls.driver.close()
#             cls.driver.quit()


class TestSalarySearchResultCount(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = webdriver.WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        time.sleep(DELAY_SHORT)

    def test_job_search__when_deselect_unspecified_salary__should_pss(self):
        driver = self.driver
        data = {

        }
        job_search_helper(driver, data)
        try:
            unspecified_salary = driver.find_element_by_xpath(
                "/html/body/div[3]/div/div/div/div/div[2]/div[7]/div/label/span")
            unspecified_salary.click()
            time.sleep(2)
            unspecified_salary = driver.find_element_by_class_name('showing-number').text
            if unspecified_salary != deselect_unspecified_job_result and unspecified_salary != deselect_unspecified_job_result_api and unspecified_salary != deselect_unspecified_job_result_api_pro:
                self.fail()

        except NoSuchElementException:
            self.fail('Not ok')

    def test_job_search__when_signed_in__deselect_unspecified_and_salary_0_to_0__should_pss(self):
        driver = self.driver
        data = {
            "email": VALID_PRO_USERNAME,
            "password": VALID_PRO_PASSWORD,
        }
        signin_helper(driver, data)
        job_search_helper(driver, data)
        try:
            time.sleep(1)
            unspecified_salary = driver.find_element_by_xpath(
                "/html/body/div[3]/div/div/div/div/div[2]/div[7]/div/label/span")
            unspecified_salary.click()
            time.sleep(2)
            unspecified_salary = driver.find_element_by_class_name('showing-number').text
            if unspecified_salary != deselect_unspecified_job_result and unspecified_salary != deselect_unspecified_job_result_api and unspecified_salary != deselect_unspecified_job_result_api_pro:
                self.fail()

            titles = []
            i = 0
            page_count = driver.find_elements_by_class_name('page-item ').__len__()
            for i in range(i, page_count - 2):
                time.sleep(1)
                if i <= page_count - 3:
                    time.sleep(1)
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

            if titles != deselect_unspecified_job_search_result and titles != deselect_unspecified_job_search_result_api and titles != deselect_unspecified_job_search_result_api_pro:
                self.fail()
            profile_btn = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[6]/button')
            profile_btn.click()
            time.sleep(1)
            sign_out_btn = driver.find_element_by_xpath('//*[@id="userNavbarMain"]/ul/li[3]/a/span')
            sign_out_btn.click()


        except NoSuchElementException:
            self.fail('Not ok')

    def test_job_search__when_not_signed_in__deselect_unspecified_and_salary_0_to_0__should_pss(self):
        driver = self.driver
        data = {

        }
        job_search_helper(driver, data)
        try:
            unspecified_salary = driver.find_element_by_xpath(
                "/html/body/div[3]/div/div/div/div/div[2]/div[7]/div/label/span")
            unspecified_salary.click()
            time.sleep(2)
            unspecified_salary = driver.find_element_by_class_name('showing-number').text
            if unspecified_salary != deselect_unspecified_job_result and unspecified_salary != deselect_unspecified_job_result_api and unspecified_salary != deselect_unspecified_job_result_api_pro:
                self.fail()

            titles = []
            i = 0
            page_count = driver.find_elements_by_class_name('page-item ').__len__()
            for i in range(i, page_count - 2):
                if i <= page_count - 3:
                    time.sleep(1)
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
                    try:
                        signin_button = driver.find_element_by_id('signinButton')
                        pass
                    except:
                        self.fail()
                break
                time.sleep(1)

            if titles != deselect_unspecified_job_search_result_10 and titles != deselect_unspecified_job_search_result_10_api and titles != deselect_unspecified_job_search_result_10_api_pro:
                self.fail()

        except NoSuchElementException:
            self.fail('Not ok')

    def test_job_search__when_signed_in__select_unspecified_salary__should_pss(self):
        driver = self.driver
        data = {
            "email": VALID_PRO_USERNAME,
            "password": VALID_PRO_PASSWORD,
        }
        signin_helper(driver, data)
        job_search_helper(driver, data)
        try:
            time.sleep(1)
            unspecified_salary = driver.find_element_by_xpath(
                "/html/body/div[3]/div/div/div/div/div[2]/div[7]/div/label/span")
            unspecified_salary.click()
            time.sleep(2)
            unspecified_salary = driver.find_element_by_class_name('showing-number').text

            if unspecified_salary != total_result_show and unspecified_salary != total_result_show_pro and unspecified_salary != total_result_show_pro_2 and unspecified_salary != total_result_show_pro_3:
                self.fail()

            titles = []
            i = 0
            page_count = driver.find_elements_by_class_name('page-item ').__len__()
            for i in range(i, page_count - 2):
                time.sleep(1)
                if i <= page_count - 3:
                    time.sleep(1)
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
                    page_next = driver.find_element_by_class_name('fa-arrow-right')
                    try:
                        page_next.click()
                        time.sleep(DELAY_SHORT)
                    except:
                        time.sleep(1)

            if titles != total_job_result_show and titles != total_job_result_show_api and titles != total_job_result_show_api_pro and titles != total_job_result_show_api_pro_2 and titles != total_job_result_show_api_pro_3:
                self.fail()

            profile_btn = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[6]/button')
            profile_btn.click()
            time.sleep(1)
            sign_out_btn = driver.find_element_by_xpath('//*[@id="userNavbarMain"]/ul/li[3]/a/span')
            sign_out_btn.click()


        except NoSuchElementException:
            self.fail('Not ok')

    def test_job_search__when_not_signed_in__select_unspecified_salary__should_pss(self):
        driver = self.driver
        data = {

        }
        job_search_helper(driver, data)
        try:
            driver.find_element_by_id("unspecified_salary")
            time.sleep(2)
            unspecified_salary = driver.find_element_by_class_name('showing-number').text
            if unspecified_salary != total_result_show and unspecified_salary != total_result_show_pro:
                self.fail()

            titles = []
            i = 0
            page_count = driver.find_elements_by_class_name('page-item ').__len__()
            for i in range(i, page_count - 2):
                if i <= page_count - 3:
                    time.sleep(1)
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
                    try:
                        signin_button = driver.find_element_by_id('signinButton')
                        pass
                    except:
                        self.fail()
                break
                time.sleep(1)

            if titles != total_job_result_show_10 and titles != total_job_result_show_10_api and titles != total_job_result_show_10_api_pro and titles != total_job_result_unspecified_show_10_api_pro:
                self.fail()

        except NoSuchElementException:
            self.fail('Not ok')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


class TestDatePostedSearchResultCount(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = webdriver.WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        time.sleep(DELAY_SHORT)

    def test_job_search__when_search_last_hour__should_pss(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        data = {

        }
        job_search_helper(driver, data)
        try:
            last_hour = driver.find_element_by_link_text("Last hour")
            last_hour.click()
            time.sleep(DELAY_SHORT)
            last_hour = driver.find_element_by_class_name('showing-number').text
            self.assertEqual(last_hour, last_hour_result)
            titles = []
            i = 0
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

            self.assertEqual(titles, last_hour_search_result)

        except NoSuchElementException:
            self.fail('Not ok')

    def test_job_search__when_search_last_24_hour__should_pss(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        data = {

        }
        job_search_helper(driver, data)
        try:
            last_24_hour = driver.find_element_by_link_text("Last 24 hour")
            last_24_hour.click()
            time.sleep(2)
            last_24_hour = driver.find_element_by_class_name('showing-number').text

            self.assertEqual(last_24_hour, last_24_hour_result)
            titles = []
            i = 0
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

            self.assertEqual(titles, last_24_hour_search_result)

        except NoSuchElementException:
            self.fail('Not ok')

    def test_job_search__when_search_last_7_days__should_pss(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        data = {

        }
        job_search_helper(driver, data)
        try:
            last_7_days = driver.find_element_by_link_text("Last 7 days")
            last_7_days.click()
            time.sleep(2)
            last_7_days = driver.find_element_by_class_name('showing-number').text
            self.assertEqual(last_7_days, last_7_days_result)
            titles = []
            i = 0
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

            self.assertEqual(titles, last_7_days_search_result)

        except NoSuchElementException:
            self.fail('Not ok')

    def test_job_search__when_search_last_14_days__should_pss(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        data = {

        }
        job_search_helper(driver, data)
        try:
            last_14_days = driver.find_element_by_link_text("Last 14 days")
            last_14_days.click()
            time.sleep(2)
            last_14_days = driver.find_element_by_class_name('showing-number').text

            self.assertEqual(last_14_days, last_14_days_result)
            self.driver.execute_script("scroll(0, 0);")
            titles = []
            i = 0
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

            self.assertEqual(titles, last_14_days_search_result)

        except NoSuchElementException:
            self.fail('Not ok')

    def test_job_search__when_search_last_30_days__should_pss(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        data = {

        }
        job_search_helper(driver, data)
        try:
            last_30_days = driver.find_element_by_link_text("Last 30 days")
            last_30_days.click()
            time.sleep(2)
            last_30_days = driver.find_element_by_class_name('showing-number').text

            self.assertEqual(last_30_days, last_30_days_result)
            self.driver.execute_script("scroll(0, 0);")
            titles = []
            i = 0
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

            self.assertEqual(titles, last_30_days_search_result)

        except NoSuchElementException:
            self.fail('Not ok')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


#
# class TestGenderSearchResultCount(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls) -> None:
#         cls.url = MAIN_URL_HOME
#         cls.driver = webdriver.WebDriver(CHROME_DRIVER_LOCATION)
#         cls.driver.get(cls.url)
#         cls.driver.maximize_window()
#         time.sleep(DELAY_SHORT)
#
#     def test_job_search__when_select_any_gender__should_pss(self):
#         driver = self.driver
#         data = {
#
#         }
#         job_search_helper(driver, data)
#         try:
#             any_gender = driver.find_element_by_link_text("Any")
#             any_gender.click()
#             time.sleep(2)
#             any_gender = driver.find_element_by_class_name('showing-number').text
#             self.assertEqual(any_gender, any_gender_result)
#             self.driver.execute_script("scroll(0, 0);")
#             titles = []
#             i = 0
#             page_count = driver.find_elements_by_class_name('page-item ').__len__()
#             for i in range(i, page_count - 2):
#                 if i <= page_count - 3:
#                     page = driver.find_element_by_css_selector('.page-item.active').text
#
#                     time.sleep(1)
#                     self.assertEqual(page, str(i + 1))
#                 else:
#                     time.sleep(1)
#                 job_list = driver.find_elements_by_class_name('job-list')
#
#                 for job in job_list:
#
#                     # .  not all companies have review
#                     try:
#                         title = job.find_element_by_tag_name('h4').text
#                     except:
#                         title = ''
#                     if title != '':
#                         titles.append(title)
#                 if i != page_count - 3:
#                     time.sleep(1)
#                     page_next = driver.find_element_by_class_name('fa-arrow-right')
#                     page_next.click()
#                 time.sleep(DELAY_SHORT)
#
#             self.assertEqual(titles, any_gender_search_result)
#
#         except NoSuchElementException:
#             self.fail('Not ok')
#
#
#     def test_job_search__when_select_female_gender__should_pss(self):
#         driver = self.driver
#         data = {
#
#         }
#         job_search_helper(driver, data)
#         try:
#             female_gender = driver.find_element_by_link_text("Female")
#             female_gender.click()
#             time.sleep(2)
#             female_gender = driver.find_element_by_class_name('showing-number').text
#             self.assertEqual(female_gender, female_gender_result)
#             self.driver.execute_script("scroll(0, 0);")
#             titles = []
#             i = 0
#             page_count = driver.find_elements_by_class_name('page-item ').__len__()
#             for i in range(i, page_count - 2):
#                 if i <= page_count - 3:
#                     page = driver.find_element_by_css_selector('.page-item.active').text
#
#                     time.sleep(1)
#                     self.assertEqual(page, str(i + 1))
#                 else:
#                     time.sleep(1)
#                 job_list = driver.find_elements_by_class_name('job-list')
#
#                 for job in job_list:
#
#                     # .  not all companies have review
#                     try:
#                         title = job.find_element_by_tag_name('h4').text
#                     except:
#                         title = ''
#                     if title != '':
#                         titles.append(title)
#                 if i != page_count - 3:
#                     time.sleep(1)
#                     page_next = driver.find_element_by_class_name('fa-arrow-right')
#                     page_next.click()
#                 time.sleep(DELAY_SHORT)
#
#             self.assertEqual(titles, female_gender_search_result)
#
#         except NoSuchElementException:
#             self.fail('Not ok')
#
#
#     def test_job_search__when_select_male_gender__should_pss(self):
#         driver = self.driver
#         data = {
#
#         }
#         job_search_helper(driver, data)
#         try:
#             male_gender = driver.find_element_by_link_text("Male")
#             male_gender.click()
#             time.sleep(2)
#             male_gender = driver.find_element_by_class_name('showing-number').text
#             self.assertEqual(male_gender, male_gender_result)
#             self.driver.execute_script("scroll(0, 0);")
#             titles = []
#             i = 0
#             page_count = driver.find_elements_by_class_name('page-item ').__len__()
#             for i in range(i, page_count - 2):
#                 if i <= page_count - 3:
#                     page = driver.find_element_by_css_selector('.page-item.active').text
#
#                     time.sleep(1)
#                     self.assertEqual(page, str(i + 1))
#                 else:
#                     time.sleep(1)
#                 job_list = driver.find_elements_by_class_name('job-list')
#
#                 for job in job_list:
#
#                     # .  not all companies have review
#                     try:
#                         title = job.find_element_by_tag_name('h4').text
#                     except:
#                         title = ''
#                     if title != '':
#                         titles.append(title)
#                 if i != page_count - 3:
#                     time.sleep(1)
#                     page_next = driver.find_element_by_class_name('fa-arrow-right')
#                     page_next.click()
#                 time.sleep(DELAY_SHORT)
#
#             self.assertEqual(titles, male_gender_search_result)
#
#         except NoSuchElementException:
#             self.fail('Not ok')
#
#     @classmethod
#     def tearDownClass(cls) -> None:
#         cls.driver.close()
#         cls.driver.quit()

class TestQualificationSearchResultCount(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = webdriver.WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        time.sleep(DELAY_SHORT)

    def test_qualification_search__when_signed_in__select_qualification_ex_one__should_pss(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        data = {
            'email': VALID_PRO_USERNAME,
            'password': VALID_PRO_PASSWORD
        }
        signin_helper(driver, data)
        job_search_helper(driver, data)
        try:
            qualification = driver.find_element_by_xpath(
                '/html/body/div[3]/div/div/div/div/div[2]/div[5]/div/button/div/div/div')
            qualification.click()
            qualification_1 = driver.find_element_by_id('bs-select-4-2')
            qualification_1.click()
            time.sleep(2)
            qualification_one_job_list = driver.find_element_by_class_name('showing-number').text
            if qualification_one_job_list != qualification_one_result and qualification_one_job_list != qualification_one_result_api:
                self.fail()
            # self.driver.execute_script("scroll(0, 0);")
            titles = []
            i = 0
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

            if titles != qualification_one_search_result and titles != qualification_one_search_result_api:
                self.fail()

            profile_btn = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[6]/button')
            profile_btn.click()
            time.sleep(1)
            sign_out_btn = driver.find_element_by_xpath('//*[@id="userNavbarMain"]/ul/li[3]/a/span')
            sign_out_btn.click()


        except NoSuchElementException:
            self.fail('Not ok')

    def test_qualification_search__when_not_signed_in___select_qualification_ex_one__should_pss(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        data = {

        }
        job_search_helper(driver, data)
        try:
            qualification = driver.find_element_by_xpath(
                '/html/body/div[3]/div/div/div/div/div[2]/div[5]/div/button/div/div/div')
            qualification.click()
            qualification_1 = driver.find_element_by_id('bs-select-4-2')
            qualification_1.click()
            time.sleep(2)
            qualification_one_job_list = driver.find_element_by_class_name('showing-number').text
            if qualification_one_job_list != qualification_one_result and qualification_one_job_list != qualification_one_result_api:
                self.fail()

            # self.driver.execute_script("scroll(0, 0);")
            titles = []
            i = 0
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
                    try:
                        signin_button = driver.find_element_by_id('signinButton')
                        pass
                    except:
                        self.fail()
                break
                time.sleep(1)

            if titles != qualification_one_search_result_10 and titles != qualification_one_search_result_10_api:
                self.fail()

        except NoSuchElementException:
            self.fail('Not ok')

    def test_qualification_search__when_signed_in__select_qualification_ex_two__should_pss(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        data = {
            'email': VALID_PRO_USERNAME,
            'password': VALID_PRO_PASSWORD
        }
        signin_helper(driver, data)
        job_search_helper(driver, data)
        try:
            qualification = driver.find_element_by_xpath(
                '/html/body/div[3]/div/div/div/div/div[2]/div[5]/div/button/div/div/div')
            qualification.click()
            qualification_2 = driver.find_element_by_id('bs-select-4-4')
            qualification_2.click()
            time.sleep(2)
            qualification_two = driver.find_element_by_class_name('showing-number').text
            self.assertEqual(qualification_two, qualification_two_result)
            self.driver.execute_script("scroll(0, 0);")
            titles = []
            i = 0
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

            self.assertEqual(titles, qualification_two_search_result)
            profile_btn = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[6]/button')
            profile_btn.click()
            time.sleep(1)
            sign_out_btn = driver.find_element_by_xpath('//*[@id="userNavbarMain"]/ul/li[3]/a/span')
            sign_out_btn.click()


        except NoSuchElementException:
            self.fail('Not ok')

    def test_qualification_search__when_not_signed_in__select_qualification_ex_two__should_pss(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        data = {

        }
        job_search_helper(driver, data)
        try:
            qualification = driver.find_element_by_xpath(
                '/html/body/div[3]/div/div/div/div/div[2]/div[5]/div/button/div/div/div')
            qualification.click()
            qualification_2 = driver.find_element_by_id('bs-select-4-4')
            qualification_2.click()
            time.sleep(2)
            qualification_two = driver.find_element_by_class_name('showing-number').text
            self.assertEqual(qualification_two, qualification_two_result)
            self.driver.execute_script("scroll(0, 0);")
            titles = []
            i = 0
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
                    try:
                        signin_button = driver.find_element_by_id('signinButton')
                        pass
                    except:
                        self.fail()
                break
                time.sleep(1)

            self.assertEqual(titles, qualification_two_search_result_10)

        except NoSuchElementException:
            self.fail('Not ok')

    def test_qualification_search__when_signed_in__select_qualification_ex_three__should_pss(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        data = {
            'email': VALID_PRO_USERNAME,
            'password': VALID_PRO_PASSWORD
        }
        signin_helper(driver, data)
        job_search_helper(driver, data)
        try:
            qualification = driver.find_element_by_xpath(
                '/html/body/div[3]/div/div/div/div/div[2]/div[5]/div/button/div/div/div')
            qualification.click()
            qualification_2 = driver.find_element_by_id('bs-select-4-3')
            qualification_2.click()
            time.sleep(2)
            qualification_three = driver.find_element_by_class_name('showing-number').text
            self.assertEqual(qualification_three, qualification_three_result)
            self.driver.execute_script("scroll(0, 0);")
            titles = []
            i = 0
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

            self.assertEqual(titles, qualification_three_search_result)
            profile_btn = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[6]/button')
            profile_btn.click()
            time.sleep(1)
            sign_out_btn = driver.find_element_by_xpath('//*[@id="userNavbarMain"]/ul/li[3]/a/span')
            sign_out_btn.click()


        except NoSuchElementException:
            self.fail('Not ok')

    def test_qualification_search__when_not_signed_in__select_qualification_ex_three__should_pss(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        data = {

        }
        job_search_helper(driver, data)
        try:
            qualification = driver.find_element_by_xpath(
                '/html/body/div[3]/div/div/div/div/div[2]/div[5]/div/button/div/div/div')
            qualification.click()
            qualification_2 = driver.find_element_by_id('bs-select-4-3')
            qualification_2.click()
            time.sleep(2)
            qualification_three = driver.find_element_by_class_name('showing-number').text
            self.assertEqual(qualification_three, qualification_three_result)
            self.driver.execute_script("scroll(0, 0);")
            titles = []
            i = 0
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

            self.assertEqual(titles, qualification_three_search_result)

        except NoSuchElementException:
            self.fail('Not ok')

    def test_qualification_search__when_select_qualification_ex_four__should_pss(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        data = {

        }
        job_search_helper(driver, data)
        try:
            qualification = driver.find_element_by_xpath(
                '/html/body/div[3]/div/div/div/div/div[2]/div[5]/div/button/div/div/div')
            qualification.click()
            qualification_2 = driver.find_element_by_id('bs-select-4-1')
            qualification_2.click()
            time.sleep(2)
            qualification_four = driver.find_element_by_class_name('showing-number').text
            if qualification_four != qualification_four_result and qualification_four != qualification_four_result_api:
                self.fail()
            # self.driver.execute_script("scroll(0, 0);")
            titles = []
            i = 0
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

            if titles != qualification_four_search_result and titles != qualification_four_search_result_api:
                self.fail()

        except NoSuchElementException:
            self.fail('Not ok')

    def test_qualification_search__when_select_qualification_ex_five__should_pss(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        data = {

        }
        job_search_helper(driver, data)
        try:
            qualification = driver.find_element_by_xpath(
                '/html/body/div[3]/div/div/div/div/div[2]/div[5]/div/button/div/div/div')
            qualification.click()
            qualification_2 = driver.find_element_by_id('bs-select-4-0')
            qualification_2.click()
            time.sleep(2)
            qualification_five = driver.find_element_by_class_name('showing-number').text

            self.assertEqual(qualification_five, qualification_five_result)
            self.driver.execute_script("scroll(0, 0);")
            titles = []
            i = 0
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

            self.assertEqual(titles, qualification_five_search_result)

        except NoSuchElementException:
            self.fail('Not ok')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


class TestFavoriteSearchResultCount(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = webdriver.WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        time.sleep(DELAY_SHORT)

    def test_job_favorite__when_click_favorite_icon_and_click_no__should_fail(self):
        driver = self.driver
        data = {

        }
        job_search_helper(driver, data)
        try:
            favorite_button = driver.find_element_by_xpath('//*[@id="job-list"]/div[2]/div[2]/div/a[3]')
            favorite_button.click()
            time.sleep(DELAY_SHORT)
            click_no = driver.find_element_by_class_name("swal2-cancel")
            click_no.click()
            time.sleep(DELAY_SHORT)
            self.assertIsNotNone(favorite_button)

        except NoSuchElementException:
            self.fail('Not ok')

    def test_job_favorite__when_click_favorite_icon_and_click_yes_without_login__should_fail(self):
        driver = self.driver
        data = {

        }
        job_search_helper(driver, data)
        try:
            favorite_button = driver.find_element_by_xpath('//*[@id="job-list"]/div[2]/div[2]/div/a[3]')
            favorite_button.click()
            time.sleep(DELAY_SHORT)
            click_no = driver.find_element_by_class_name("swal2-cancel")
            click_no.click()
            self.assertIsNotNone(favorite_button)


        except NoSuchElementException:
            self.fail('Not ok')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


class TestApplyButtonSearchResultCount(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = MAIN_URL_HOME
        cls.driver = webdriver.WebDriver(CHROME_DRIVER_LOCATION)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        time.sleep(DELAY_SHORT)

    def test_job_apply__without_signin__should_fail(self):
        driver = self.driver
        driver.get(MAIN_URL_HOME)
        data = {

        }

        job_search_helper(driver, data)

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
                        apply_now_btn.click()
                        time.sleep(1)
                        success_ok = driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button[1]')
                        success_ok.click()
                        self.fail()
                        break
                    except:
                        driver.refresh()
                        pass
                        break
            except:
                driver.refresh()
                pass

    def test_job_apply__when_signed_in__should_pass(self):
        driver = self.driver
        data = {
            "email": VALID_PRO_USERNAME,
            "password": VALID_PRO_PASSWORD
        }
        signin_helper(driver, data)
        job_search_helper(driver, data)

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
                        # apply_now_btn.click()
                        # time.sleep(DELAY_SHORT)
                        # time.sleep(DELAY_SHORT)
                        # time.sleep(DELAY_SHORT)
                        # success_ok = driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button[1]')
                        # success_ok.click()

                        driver.refresh()
                        time.sleep(DELAY_SHORT)
                        profile_btn = driver.find_element_by_xpath(
                            '/html/body/header/div[2]/div/div[2]/ul/li[6]/button')
                        profile_btn.click()
                        time.sleep(1)
                        sign_out_btn = driver.find_element_by_xpath('//*[@id="userNavbarMain"]/ul/li[3]/a/span')
                        sign_out_btn.click()
                        time.sleep(DELAY_SHORT)

                        pass
                        break
                    except:
                        self.fail()
                        break
            except:
                self.fail()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


def job_search_helper(driver, row):
    driver.get(MAIN_URL_HOME)
    time.sleep(1)
    try:
        job_page = driver.find_element_by_link_text("Jobs")
        job_page.click()
        time.sleep(5)


    except NoSuchElementException:
        return 1



if __name__ == '__main__':
    unittest.main()