from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, permissions
from . import serializers
from django.contrib.auth.models import User
from .models import Video
from .permissions import IsOwnerOrReadOnly

# Create your views here.

# redis connection
# redis = rd.Redis(host=’redis’, port=6379, db=0)


def test(request):
    return HttpResponse("This is Django")


class VideoList(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = serializers.VideoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class VideoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = serializers.VideoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
