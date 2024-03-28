#!/usr/bin/python3
""" Email functionality """
from flask_mail import Message
from . import mail


def send_email(to, subject, template, **kwargs):
    """ Sends email to users and admin """
    msg = Message(app.config['ECOSORTIFY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  sender=app.config['ECOSORTIFY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)
