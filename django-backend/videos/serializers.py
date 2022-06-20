from rest_framework import serializers
from videos.models import Video
from django.contrib.auth.models import User


class VideoSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='author.username')
    user_id = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = Video
        fields = ['id', 'user', 'user_id', 'title', 'description', 'date', 'video', 'thumbnail', 'likes_count']
