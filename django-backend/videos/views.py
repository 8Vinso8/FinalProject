from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from videos import serializers
from videos.models import Video, Comment
from videos.permissions import IsOwnerOrReadOnly
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter


class VideoList(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = serializers.VideoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [SearchFilter, OrderingFilter, filters.DjangoFilterBackend]
    search_fields = ['title', 'description']
    filterset_fields = ['title', 'description', 'user']
    ordering_fields = ['title', 'description', 'date']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class VideoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = serializers.VideoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class VideoSubscriptionList(generics.ListAPIView):
    permissions = [permissions.IsAuthenticated]
    serializer_class = serializers.VideoSerializer

    def get_queryset(self):
        user = self.request.user
        return Video.objects.filter(user__subscribers__user=user)




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


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
