import smtplib, ssl

from projectzero import config

import django_rq

def enqueue_email(receiver_email, message):
    django_rq.enqueue(send_email, receiver_email, message)

def send_email(receiver_email, message):
    # Create a secure SSL context
    context = ssl.create_default_context()
    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(config.smtp_server, config.smtp_port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.login(config.smtp_user, config.smtp_password)
        server.sendmail(config.smtp_user, receiver_email, message)
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()