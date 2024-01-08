from rest_framework import generics, status
from rest_framework.views import APIView
from django.contrib.auth.models import Group, Permission
from app.models.system.group import GroupExtended
from django_filters.rest_framework import DjangoFilterBackend
from app.serializers.system.group_serializer import GroupSerializer
from app.libraries.custom_pagination import CustomPagination
from rest_framework.response import Response


class GroupPagination(generics.ListAPIView):
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
    queryset = GroupExtended.objects.all()
    serializer_class = GroupSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
    search_fields = ['name']

class GroupList(generics.ListAPIView):
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
    queryset = GroupExtended.objects.all()
    serializer_class = GroupSerializer

class GroupDetail(generics.RetrieveAPIView):
    """
    API endpoint for retrieving, updating, and deleting a specific user group.

    Inherits from `generics.RetrieveUpdateDestroyAPIView` which provides the default implementation
    for retrieving, updating, and deleting a model instance.

    Attributes:
        queryset (QuerySet): The queryset of all user groups.
        serializer_class (Serializer): The serializer class for serializing and deserializing user groups.
    """
    queryset = GroupExtended.objects.all()
    serializer_class = GroupSerializer

class GroupCreate(generics.CreateAPIView):
    """
    API view for creating a group.

    Inherits from `generics.CreateAPIView` which provides the implementation
    for creating an object.

    Attributes:
        queryset (QuerySet): The queryset of `Group` objects to be used for creating.
        serializer_class (Serializer): The serializer class to be used for
            serializing and deserializing `Group` objects.

    Example:
        To create a new group, make a POST request to the endpoint with the
        required data.
    """
    queryset = GroupExtended.objects.all()
    serializer_class = GroupSerializer

class GroupUpdate(generics.UpdateAPIView):
    """
    API view for updating a group.

    Inherits from `generics.UpdateAPIView` which provides the implementation
    for updating an object.

    Attributes:
        queryset (QuerySet): The queryset of `Group` objects to be used for updating.
        serializer_class (Serializer): The serializer class to be used for
            serializing and deserializing `Group` objects.

    Example:
        To update a group, make a PUT or PATCH request to the endpoint with the
        required data.
    """
    queryset = GroupExtended.objects.all()
    serializer_class = GroupSerializer

class GroupDelete(generics.DestroyAPIView):
    """
    API view for deleting a group.

    Inherits from `generics.DestroyAPIView` which provides the implementation
    for deleting an object.

    Attributes:
        queryset (QuerySet): The queryset of `Group` objects to be used for deleting.
        serializer_class (Serializer): The serializer class to be used for
            serializing and deserializing `Group` objects.

    Example:
        To delete a group, make a DELETE request to the endpoint.
    """
    queryset = GroupExtended.objects.all()
    serializer_class = GroupSerializer

class GroupPermissionsView(APIView):

    def post(self, request, group_id):
        try:
            group = GroupExtended.objects.get(pk=group_id)
        except GroupExtended.DoesNotExist:
            return Response({"error": "Group not found"}, status=status.HTTP_404_NOT_FOUND)

        permissions = request.data.get('permissions', [])

        for permission_id in permissions:
            try:
                permission = Permission.objects.get(pk=permission_id)
                group.permissions.add(permission)
            except Permission.DoesNotExist:
                return Response({"error": f"Permission with id {permission_id} does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_204_NO_CONTENT)