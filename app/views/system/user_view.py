from rest_framework import generics, status, pagination
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from app.serializers.system.user_serializer import UserSerializer
from rest_framework.response import Response
from app.helpers.log_helper import log_helper
from app.libraries.custom_pagination import CustomPagination

class UserPagination(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'last_name','username','email', 'is_active']

class UserList(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be listed and created.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows a single user to be retrieved, updated, and deleted.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserEnabled(generics.UpdateAPIView):
    """
    API endpoint that allows a user to be enabled.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def put(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_active = True
        user.save()
        return Response(status=status.HTTP_200_OK)


class UserDisabled(generics.UpdateAPIView):
    """
    API endpoint that allows a user to be disabled.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def put(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_active = False
        user.save()
        return Response(status=status.HTTP_200_OK)
