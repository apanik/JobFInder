import requests

from tests.config import VALID_PRO_USERNAME, VALID_PRO_PASSWORD, VALID_COM_USERNAME, VALID_COM_PASSWORD, \
    VALID_STAFF_USERNAME, VALID_STAFF_PASSWORD
from tests.config_api import PRO_SIGNIN_URL, COM_SIGNIN_URL


def signin_as_staff():
    pro_signin_url = PRO_SIGNIN_URL
    json = {
        'email': VALID_STAFF_USERNAME,
        'password': VALID_STAFF_PASSWORD
    }
    resp = requests.post(pro_signin_url, json=json)
    if resp.status_code == 200:
        return resp.json()

def signin_as_pro():
    pro_signin_url = PRO_SIGNIN_URL
    json = {
        'email': VALID_PRO_USERNAME,
        'password': VALID_PRO_PASSWORD
    }
    resp = requests.post(pro_signin_url, json=json)
    if resp.status_code == 200:
        return resp.json()

def signin_as_pro_any(username,password):
    pro_signin_url = PRO_SIGNIN_URL
    json = {
        'email': username,
        'password': password
    }
    resp = requests.post(pro_signin_url, json=json)
    if resp.status_code == 200:
        return resp.json()

def signin_as_com():
    com_signin_url = COM_SIGNIN_URL
    json = {
        'email': VALID_COM_USERNAME,
        'password': VALID_COM_PASSWORD
    }
    resp = requests.post(com_signin_url, json=json)
    if resp.status_code == 200:
        return resp.json()