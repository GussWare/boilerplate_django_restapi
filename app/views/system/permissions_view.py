from rest_framework import generics
from django.contrib.auth.models import Permission
from django_filters.rest_framework import DjangoFilterBackend
from app.serializers.system.permission_serializer import PermissionSerializer
from app.libraries.custom_pagination import CustomPagination

class PermissionPagination(generics.ListAPIView):
    """
    Endpoint for listing and creating permissions.

    Attributes:
        queryset (QuerySet): The queryset of permissions.
        serializer_class (Serializer): The serializer class for permissions.
        pagination_class (Pagination): The pagination class for the endpoint.
        filter_backends (list): The list of filter backends for the endpoint.
        filterset_fields (list): The list of fields to filter permissions.

    HTTP Methods:
        GET: Retrieve a list of permissions.

    Examples:
        GET /permissions/
        GET /permissions/?name=admin  # Filter permissions by name

    """

    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
    search_fields = ['name']

class PermissionList(generics.ListAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class PermissionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer