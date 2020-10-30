from tests.config import SERVER_PROTOCOL, SERVER_ADDRESS

MAIN_URL = f'{SERVER_PROTOCOL}://{SERVER_ADDRESS}'
PRO_SIGNIN_URL = f'{MAIN_URL}/api/pro/signin/'
PRO_FORGOT_PASSWORD_URL = f'{MAIN_URL}/api/professional/password_reset/'
REGISTER_URL = f'{MAIN_URL}/api/professional/create_with_user/'
COM_SIGNIN_URL= f'{MAIN_URL}/api/company/signin/'
COM_CHANGED_PASSWORD_URL = f'{MAIN_URL}/api/pro/change-password/'
COM_FORGET_PASSWORD_URL = f'{MAIN_URL}/company/forgot-password/'
PRO_SEND_CREDENTIAL_URL = f'{MAIN_URL}/api/pro/credential/send-email/'
