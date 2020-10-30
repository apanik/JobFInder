import random
import string

from django.core.mail import send_mail
from django.http import HttpResponse
from django.template import loader
from django.utils.text import slugify
from rest_framework.status import HTTP_200_OK
from rest_framework.utils import json

from job import models
from p7.utils import send_email
from settings.models import Settings


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


# Unique Slug Generator
def job_slug_generator(instance, new_slug=None):
    """
    It assumes your instance has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        job_id = str(instance.job_id)
        slug = "{slug}-{uuid}".format(slug=slugify(instance.title), uuid = job_id[-8:])

    from job.models import Job
    qs_exists = Job.objects.filter(slug=slug).exists()

    if qs_exists:
        new_slug = "{slug}-{randstr}".format(slug=slug, randstr=random_string_generator(size=4))
        return job_slug_generator(instance, new_slug=new_slug)
    return slug
# Unique Slug Generator

# Favourite Job Counter
def favourite_job_counter(job):
    """
    It assumes your instance has a model with a slug field and a title character (char) field.
    """
    if job:
        from job.models import FavouriteJob
        fav_job = FavouriteJob.objects.filter(job=job).count()
        job.favorite_count = fav_job
        job.save()
# Favourite Job Counter

# Applied Job Counter
def applied_job_counter(job):
    """
    It assumes your instance has a model with a slug field and a title character (char) field.
    """
    if job:
        app_job = models.JobApplication.objects.filter(job=job).count()
        job.applied_count = app_job
        job.save()
# Applied Job Counter


def sendAccessRequestToEmail(email, company_name, phone, person_name, company_role, contact_info):
    html_message = loader.render_to_string(
        'company_access_request_content.html',
        {
            'company_name': company_name,
            'email': email,
            'phone': phone,
            'person_name' : person_name,
            'company_role' : company_role,
            'contact_info' : contact_info
        }
    )
    subject_text = "Company Requested For Access"

    settingsObj = Settings.objects.all().first()
    admin_email = settingsObj.admin_email
    recipient_list = admin_email

    send_email(recipient_list, subject_text, html_message, settingsObj.sender_email_host, settingsObj.sender_email_port,
               settingsObj.no_reply_sender_host_user, settingsObj.no_reply_sender_host_password)

    data = {
        'status': 'success',
        'code': HTTP_200_OK
    }
    return HttpResponse(json.dumps(data), content_type='application/json')

def sendVerificationRequestToEmail(email, verification_code, person_name, company_name):
    html_message = loader.render_to_string(
        'company_access_request_verification_message_content.html',
        {
            'verification_code': verification_code,
            'person_name' : person_name,
            'company_name' : company_name
        }
    )
    subject_text = "Request to access JobXprss account for company: {}".format(company_name)

    settingsObj = Settings.objects.all().first()
    admin_email = settingsObj.admin_email

    message = ' it  means a world to us '
    #email_from = EMAIL_HOST_USER
    email_from = ''
    recipient_list = email
    send_email(recipient_list, subject_text, html_message, settingsObj.sender_email_host, settingsObj.sender_email_port,
               settingsObj.no_reply_sender_host_user, settingsObj.no_reply_sender_host_password)
    # send_mail(subject_text, message, email_from, recipient_list,html_message=html_message)
    data = {
        'status': 'success',
        'code': HTTP_200_OK
    }
    return HttpResponse(json.dumps(data), content_type='application/json')