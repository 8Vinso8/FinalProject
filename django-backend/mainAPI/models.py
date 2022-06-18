from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Video(models.Model):
    author = models.ForeignKey(User, related_name='videos', on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=600)
    date = models.DateTimeField(default=timezone.now)
    video = models.FileField(upload_to='videos')

    class Meta:
        ordering = ['date']
