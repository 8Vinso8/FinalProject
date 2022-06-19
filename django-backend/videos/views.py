from rest_framework import generics, permissions
from videos import serializers
#from users.models import CustomUser as User
from videos.models import Video
from videos.permissions import IsOwnerOrReadOnly

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
