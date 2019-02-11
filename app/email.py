from flask_mail import Message
from app import mail

def send_mail(subject, sender, recepients, text_body, html_body):
    '''sends emails to registered users
    '''
    msg = Message(subject, sender, recipients, text-body, html_body)
    msg.body = text.body
    msg.html = html.body
    mail.send = (msg)


    