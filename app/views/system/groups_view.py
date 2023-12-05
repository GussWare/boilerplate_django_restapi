from rest_framework import generics
from django.contrib.auth.models import Group
from django_filters.rest_framework import DjangoFilterBackend
from app.serializers.system.group_serializer import GroupSerializer
from app.libraries.custom_pagination import CustomPagination


class GroupPagination(generics.ListCreateAPIView):
    """
    API view for listing and creating groups.

    This view provides pagination, filtering, and serialization for the Group model.

    Supported HTTP methods:
    - GET: Retrieve a list of groups with optional filtering.
    - POST: Create a new group.

    Query Parameters:
    - name: Filter groups by name.

    Response format:
    The response is serialized using the GroupSerializer class.

    Pagination:
    The response is paginated using the CustomPagination class.

    Filtering:
    Groups can be filtered by name using the filterset_fields attribute.

    Example usage:
    GET /groups/ - Retrieve a list of all groups.
    GET /groups/?name=admin - Retrieve a list of groups with the name 'admin'.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

class GroupList(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating groups.

    Inherits from `generics.ListCreateAPIView` which provides the implementation
    for listing and creating objects.

    Attributes:
        queryset (QuerySet): The queryset of `Group` objects to be used for listing.
        serializer_class (Serializer): The serializer class to be used for
            serializing and deserializing `Group` objects.

    Example:
        To list all groups, make a GET request to the endpoint.
        To create a new group, make a POST request to the endpoint with the
        required data.

    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retrieving, updating, and deleting a specific user group.

    Inherits from `generics.RetrieveUpdateDestroyAPIView` which provides the default implementation
    for retrieving, updating, and deleting a model instance.

    Attributes:
        queryset (QuerySet): The queryset of all user groups.
        serializer_class (Serializer): The serializer class for serializing and deserializing user groups.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
