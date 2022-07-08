from django.db import models
from users.models import CustomUser as User
from django_resized import ResizedImageField


class Video(models.Model):
    user = models.ForeignKey(User, related_name='videos', on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=600, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    video = models.FileField(upload_to='videos')
    thumbnail = ResizedImageField(size=[370, 210], default='default_thumbnail.jpg', upload_to='videos/thumbnails')
    likes = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.title

    def likes_count(self):
        return self.likes.count()

    class Meta:
        ordering = ['-date']


class Comment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    video = models.ForeignKey(Video, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField(blank=False)

    class Meta:
        ordering = ['-date']
