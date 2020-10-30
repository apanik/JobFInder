from p7.settings_dev import *

DEBUG=True
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'p7_test',
        'USER': 'root',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode': 'traditional',
            'isolation_level': "repeatable read",
        },
        'CHARSET':'utf8',
        'COLLATION':'utf8_general_ci',
        'COLLATION_CONNECTION':'utf8_general_ci'
    }
}
SITE_URL = '127.0.0.1:8000'

