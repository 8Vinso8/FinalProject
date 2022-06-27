from FinalProject.celery import app
from django.core.mail import send_mail
from users.models import CustomUser


@app.task
def send_spam(owner, mesg):
    subs = CustomUser.objects.get(id=owner).subscribers.all()
    for i in subs:
        uuser = CustomUser.objects.get(id=i.user_id).email
        send_mail('Оповещение', mesg, 'lolbutt.noreply@gmail.com', [uuser])

