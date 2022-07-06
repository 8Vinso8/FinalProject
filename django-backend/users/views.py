from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from users import serializers
from users.models import CustomUser as User
from users.models import UserSubscribed as Subscription
from users.permissions import IsOwnerOrReadOnly
from django_filters import rest_framework as filters


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['username', 'email']


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class CurrentUser(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = serializers.UserSerializer(user)
        return Response(serializer.data)


class SubscribeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        is_subscribed = True
        try:
            record = Subscription.objects.get(user=request.user, subscribed_user=user)
        except Subscription.DoesNotExist:
            is_subscribed = False
        return Response({'is_subscribed': is_subscribed})

    def post(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.user == user:
            return Response(status.HTTP_403_FORBIDDEN)
        try:
            record = Subscription.objects.get(user=request.user, subscribed_user=user)
        except Subscription.DoesNotExist:
            Subscription.objects.create(user=request.user, subscribed_user=user)
            return Response(status.HTTP_200_OK)
        record.delete()
        return Response(status.HTTP_200_OK)
