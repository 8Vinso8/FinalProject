from rest_framework import routers, serializers, viewsets
from .models import Video
from django.contrib.auth.models import User


class VideoSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    author_id = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = Video
        fields = ['id', 'author', 'author_id', 'title', 'description', 'date', 'video']


class UserSerializer(serializers.ModelSerializer):
    videos = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'videos']
