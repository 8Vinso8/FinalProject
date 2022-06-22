from django.core.mail import send_mail
from users.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from videos.models import Video
from videos.tasks import send_spam


@receiver(post_save, sender=Video)
def make_spam(sender, instance, **kwargs):
    owner = instance.user_id
    mesg = 'На канале, который вы смотрите, вышло новое видео!'
    send_spam.delay(owner, mesg)
