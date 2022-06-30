from django.core.mail import send_mail
from users.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import PostSend
from users.tasks import send_post_spam


@receiver(post_save, sender=PostSend)
def make_post_spam(sender, instance, **kwargs):
    if instance.is_published is True:
        title = instance.title
        content = instance.content
        send_post_spam.delay(title, content)
