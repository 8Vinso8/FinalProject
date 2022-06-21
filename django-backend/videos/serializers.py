from rest_framework import serializers
from videos.models import Video
from users import serializers


class VideoSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='author.username')
    user_id = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = Video
        fields = ['id', 'user', 'user_id', 'title', 'description', 'date', 'video', 'thumbnail', 'likes_count']


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.UserSerializer()

    class Meta:
        fields = ['id', 'body', 'video', 'user']
