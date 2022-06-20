from django.db import models
from django.utils import timezone
from users.models import CustomUser as User


class Video(models.Model):
    user = models.ForeignKey(User, related_name='videos', on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=600, blank=True)
    date = models.DateTimeField(default=timezone.now)
    video = models.FileField(upload_to='videos')
    thumbnail = models.ImageField(default='default_thumbnail.jpg', upload_to='videos/thumbnails')
    likes = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.title

    def likes_count(self):
        return self.likes.count()

    class Meta:
        ordering = ['-date']

