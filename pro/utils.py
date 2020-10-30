# from django.contrib.auth.models import User
# from django.contrib.auth.hashers import check_password
#
# def checkValidEmailPassword(email, password):
#     user_obj = User.objects.get(username=email)
#     status = check_password(password, user_obj.password)
#     return status
import random
import socket
import uuid
from urllib.parse import urlparse
from django.http import Http404, HttpResponse
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_401_UNAUTHORIZED,
    HTTP_200_OK,
    HTTP_404_NOT_FOUND
)
from django.db.models import Q
from django.db import IntegrityError
from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.template import loader

from p7.models import is_professional, populate_user_info
from p7.settings_dev import *

from pro.models import Professional, RecentActivity
from resources.strings_pro import *
from difflib import SequenceMatcher
from django.contrib.auth.models import User
from p7.utils import send_email
from settings.models import Settings


def sendSignupEmail(email,id, date):
    # unique_id = random.randint(100000, 999999)
    # updateExamineeVerficationCode(email, unique_id)
    id=str(id)
    date = str(date)
    activation_link = hash(id+date)
    updateProfessionalVerficationLink(email, activation_link)
    settingsObj = Settings.objects.all().first()

    data = ''
    html_message = loader.render_to_string(
        'account_activation_email.html',
        {
            'activation_url': "{}/api/professional/signup-email-verification/email={}&token={}".format(SITE_URL, email, activation_link),
            'activation_email': email,
            'subject': 'Thank you from' + data,
        }
    )
    subject_text = loader.render_to_string(
        'account_activation_email_subject.txt',
        {
            'user_name': email,
            'subject': 'Thank you from' + data,
        }
    )

    recipient_list = email
    send_email(recipient_list, subject_text, html_message, settingsObj.sender_email_host, settingsObj.sender_email_port,
               settingsObj.no_reply_sender_host_user, settingsObj.no_reply_sender_host_password)


def updateProfessionalVerficationLink(email, unique_link):
    professional = Professional.objects.get(email=email)
    professional.signup_verification_code = unique_link
    professional.save()

def job_alert_save(email):
    user = Professional.objects.get(email = email)
    user.job_alert_status = True
    user.save()

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def save_recent_activity(user_id, activity_type):
    obj = RecentActivity()
    obj.user_id = user_id
    description = {'profile_pro':'Profile Updated', 'apply_pro':'Applied job', 'apply_com':'Professional apply for this job'}
    obj.description = description[activity_type]
    obj.type = activity_type
    obj.save()