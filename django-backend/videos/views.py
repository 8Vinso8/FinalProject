from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from videos import serializers
#from users.models import CustomUser as User
from videos.models import Video, Comment
from videos.permissions import IsOwnerOrReadOnly
from django.http import JsonResponse, Http404

# redis connection
# redis = rd.Redis(host=’redis’, port=6379, db=0)


class VideoList(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = serializers.VideoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class VideoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = serializers.VideoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class LikesDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        try:
            video = Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        user = request.user
        response = user in video.likes.all()
        return Response({'is_liked': response})

    def post(self, request, pk):
        try:
            video = Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        user = request.user
        if user in video.likes.all():
            video.likes.remove(user)
            return Response(status=status.HTTP_200_OK)
        video.likes.add(user)
        return Response(status=status.HTTP_200_OK)


class CommentView(APIView):
    permissions = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        video = self.get_object(pk)
        serializer = serializers.CommentSerializer(video.comments.all(), many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        video = self.get_object(pk)
        body = request.query_params['body']
        if body:
            Comment.objects.create(user=request.user, video=video, body=request.body)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_403_FORBIDDEN)
