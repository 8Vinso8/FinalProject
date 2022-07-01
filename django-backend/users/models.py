from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
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


class PostSend(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Текст поста')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Разослать')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'рассылку'
        verbose_name_plural = 'Рассылки'
        ordering = ['time_create', 'title']