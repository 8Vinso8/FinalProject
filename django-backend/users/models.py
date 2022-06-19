from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    last_name = None
    first_name = None
    email = models.EmailField(unique=True)
    avatar = models.ImageField(default='default_avatar.png', upload_to='avatars')

    def __str__(self):
        return self.username
