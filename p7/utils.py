# from django.contrib.auth.models import User
# from django.contrib.auth.hashers import check_password
#
# def checkValidEmailPassword(email, password):
#     user_obj = User.objects.get(username=email)
#     status = check_password(password, user_obj.password)
#     return status
import logging
import smtplib
import uuid
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import basename
from threading import Thread

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import loader
from rest_framework.utils import json

from p7.settings_dev import *
from settings.models import Settings


def sendContactUsEmail(name, email, subject, phone, message):

    html_message = loader.render_to_string(
        'contact_us_email_content.html',
        {
            'name': name,
            'email': email,
            'subject': subject,
            'phone': phone,
            'message': message
        }
    )
    subject_text = loader.render_to_string('contact_us_email_subject.txt')

    settingsObj = Settings.objects.all().first()
    admin_email = settingsObj.admin_email

    message = ' it  means a world to us '
    recipient_list = admin_email
    return send_email(recipient_list, subject_text, html_message, settingsObj.sender_email_host, settingsObj.sender_email_port,
               settingsObj.no_reply_sender_host_user, settingsObj.no_reply_sender_host_password)


def uuid_slug_generator(instance):
    slug = str(uuid.uuid4())[:8]
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        return uuid_slug_generator(instance)
    return slug

def _send_email(to, subject, body, smtp_server, smtp_port, sender_email, sender_password, attachments, secured):
    server = None
    try:
        if secured:
            server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        else:
            server = smtplib.SMTP(smtp_server, smtp_port)

        server.ehlo()  # Can be omitted
        server.login(sender_email, sender_password)
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = to
        msg['Subject'] = subject

        # msg.attach(MIMEText(body, 'plain'))

        html = """\
        <html>
            <head></head>
            <body>
        """

        for f in attachments or []:
            with open(f, "rb") as img:
                msgImage = MIMEImage(
                    img.read(),
                    Name=basename(f)
                )
            msgImage.add_header('Content-ID', f'<{basename(f)}>')
            msg.attach(msgImage)
            html = f'<p><img src="cid:{basename(f)}" width="100%" alt="Image"></p>\r\n'


        html += body.replace('\r\n', '<br />\r\n')
        """
            </body>
        </html>
        """
        msg.attach(MIMEText(html, 'html'))

        server.sendmail(
            from_addr=sender_email,
            to_addrs=to,
            msg = msg.as_string())
    except Exception as ex:
        logging.exception(ex)
        raise
    finally:
        if server != None:
            server.quit()

def send_email(to, subject, body, smtp_server, smtp_port, sender_email, sender_password, attachments = [], secured = True):
    email_thread = Thread(target=_send_email, args=(to, subject, body, smtp_server, smtp_port, sender_email, sender_password, attachments, secured))
    email_thread.start()
