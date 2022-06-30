from FinalProject.celery import app
from django.core.mail import send_mail
from users.models import CustomUser
from FinalProject.settings import EMAIL_HOST_USER


@app.task
def send_post_spam(title, content):
    subs = CustomUser.objects.all()
    for i in subs:
        uuser = i.email
        send_mail(title, content, EMAIL_HOST_USER, [uuser])

