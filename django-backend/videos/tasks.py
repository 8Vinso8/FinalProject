from FinalProject.celery import app
from django.core.mail import send_mail
from users.models import CustomUser
from FinalProject.settings import EMAIL_HOST_USER


@app.task
def send_spam(owner, title):
    subs = CustomUser.objects.get(id=owner).subscribers.all()
    name = CustomUser.objects.get(id=owner).username
    mesg = 'Здравствуйте. У пользователя ' + name + ' вышло новое видео - ' \
           + '"' + title + '"' + '. С уважением, администрация SeaVid!'
    for i in subs:
        uuser = CustomUser.objects.get(id=i.user_id).email
        send_mail('Новое видео', mesg, EMAIL_HOST_USER, [uuser])

