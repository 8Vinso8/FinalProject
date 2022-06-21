from rest_framework import serializers
from videos.models import Video, Comment
from users.serializers import UserSerializer


class VideoSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Video
        fields = ['id', 'user', 'user_id', 'title', 'description', 'date', 'video', 'thumbnail', 'likes_count', 'comments']


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    avatar = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False, source='user.avatar')

    class Meta:
        model = Comment
        fields = ['id', 'body', 'user', 'video', 'avatar']
