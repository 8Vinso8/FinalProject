from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from . import serializers
from django.contrib.auth.models import User
from .models import Video

# Create your views here.

# redis connection
# redis = rd.Redis(host=’redis’, port=6379, db=0)


def test(request):
    return HttpResponse("This is Django")


class VideoList(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = serializers.VideoSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class VideoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = serializers.VideoSerializer
