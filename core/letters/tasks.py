from core.celery import app
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


@app.task
def send_email_tasks(email):
    rendered = render_to_string('email.html')
    try:
        message = EmailMessage('Subject', rendered, settings.EMAIL_FROM, [email])
        message.content_subtype = 'html'  # this is required because there is no plain text email message
        message.send()
        print "Success"
    except Exception as e:
        print e
