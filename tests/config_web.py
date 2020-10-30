from tests.config import SERVER_ADDRESS, SERVER_PROTOCOL

MAIN_URL_HOME = f'{SERVER_PROTOCOL}://{SERVER_ADDRESS}'
MAIN_URL = f'{SERVER_PROTOCOL}://{SERVER_ADDRESS}'
ADMIN_URL =f'{MAIN_URL}/staff'
PRO_SIGNIN_URL = f'{MAIN_URL}/professional/sign-in'
PROF_REGISTER_URL = f'{MAIN_URL}/professional/signup'
ADMIN_JOB_POST_URL = '/job/job/'
COMPANY_URL = '/job/company/'
GENDER_URL = '/job/gender/'
INDUSTRY_URL = '/job/industry/'
EXPERIENCE_URL = '/job/experience/'
CURRENCY_URL = '/job/currency/'
JOB_CATEGORY_URL = '/job/industry/'
JOB_TYPE_URL = '/job/jobtype/'
DIVISION_URL = '/location/division/'
DISTRICT_URL = '/location/district/'
QUALIFICATION_URL = '/job/qualification/'
PROFESSIONAL_URL = '/pro/professional/'
SKILL_URL = '/job/skill/'
TRENDINGKEYWORD_URL = '/job/trendingkeywords/'
TESTIMONIAL_URL = '/testimonial/testimonial/'
CAREERADVICE_URL = '/career_advice/careeradvice/'
PUBLIC_PROFILE =  f'{MAIN_URL}/pro/eef29447/'

QTYPE_URL= '/question/questiontype/'
DIFFICULTY_URL= '/question/difficulty/'
SUBJECT_URL= '/question/subject/'
TOPIC_URL= '/question/topics/'
SUB_TOPIC_URL= '/question/subtopics/'
QUESTION_URL= '/question/question/'
QUESTIONNAIRE_URL= '/questionnaire/questionnaire/'


EXAM_CATEGORY_URL= '/exam/examcategory/'
EXAM_LEVEL_URL= '/exam/examlevel/'
EXAM_URL= '/exam/exam/'


import subprocess
process = subprocess.run('whoami', stdout=subprocess.PIPE)
current_user = process.stdout.decode().strip()
import platform

if platform.system() == 'Darwin':
    CHROME_DRIVER_LOCATION = f'/Users/{current_user}/driver/chromedriver'
    TEST_IMAGE = f'/Users/{current_user}/driver/test_image.jpeg'
else:
    CHROME_DRIVER_LOCATION = f'/home/{current_user}/driver/chromedriver'
    TEST_IMAGE = f'/home/{current_user}/driver/test_image.jpeg'

DELAY_SHORT = 2
DELAY_LONG = 5
