from flask import render_template, current_app
from app.email import send_email, send_async_email


def send_welcome_mail(user):
    
    send_email(('[PitchView] Welcome to the Family'),
               sender=current_app.config['ADMINS'][0],
               recipients=[user.email],
               text_body=render_template('email/welcome_user.txt',
                                         user=user),
               html_body=render_template('email/welcome_user.html',
                                         user=user))