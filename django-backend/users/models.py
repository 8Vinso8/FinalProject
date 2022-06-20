from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    last_name = None
    first_name = None
    email = models.EmailField(unique=True)
    avatar = models.ImageField(default='default_avatar.png', upload_to='avatars')

    def subscribers_count(self):
        return self.subscribers.all().count()

    def __str__(self):
        return self.username


class UserSubscribed(models.Model):
    user = models.ForeignKey(CustomUser, related_name='subscribed', on_delete=models.CASCADE)
    subscribed_user = models.ForeignKey(CustomUser, related_name='subscribers', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'subscribed_user')
