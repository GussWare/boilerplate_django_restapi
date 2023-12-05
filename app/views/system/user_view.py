from rest_framework import generics, status, pagination
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from app.serializers.system.user_serializer import UserSerializer
from rest_framework.response import Response
from app.helpers.log_helper import log_helper
from app.libraries.custom_pagination import CustomPagination

class UserPagination(generics.ListCreateAPIView):
    """
    A view for paginating and filtering User objects.

    This view provides pagination support and allows filtering of User objects based on the following fields:
    - first_name
    - last_name
    - username
    - email
    - is_active

    Attributes:
        queryset (QuerySet): A queryset of User objects.
        serializer_class (Serializer): The serializer class used to serialize User objects.
        pagination_class (Pagination): The pagination class used for paginating User objects.
        filter_backends (list): A list of filter backends used for filtering User objects.
        filterset_fields (list): The fields used for filtering User objects.

    Example:
        To paginate and filter User objects, make a GET request to this endpoint with the desired filters:

        GET /users/?first_name=John&is_active=true&page=2&page_size=10

    Pagination:
        This view supports pagination. The default pagination class is used, but you can customize it by setting the `pagination_class` attribute.

        Available query parameters for pagination:
        - page: The page number to retrieve (default: 1).
        - page_size: The number of items per page (default: 10).

    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'last_name', 'username', 'email', 'is_active']

class UserList(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be listed and created.

    Inherits from `generics.ListCreateAPIView` which provides the implementation
    for listing and creating objects.

    Attributes:
        queryset (QuerySet): The queryset of User objects to be listed.
        serializer_class (Serializer): The serializer class used for User objects.

    Example:
        To list all users, make a GET request to this endpoint.
        To create a new user, make a POST request to this endpoint with the required data.

    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retrieving, updating, and deleting a user.

    Attributes:
        queryset (QuerySet): The queryset of User objects.
        serializer_class (Serializer): The serializer class for User objects.

    HTTP Methods:
        - GET: Retrieve a user.
        - PUT: Update a user.
        - DELETE: Delete a user.

    Usage:
        GET /users/{id}/
        PUT /users/{id}/
        DELETE /users/{id}/
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserEnabled(generics.UpdateAPIView):
    """
    API endpoint that allows a user to be enabled.

    Inherits from `generics.UpdateAPIView` and provides a PUT method to enable a user.

    Attributes:
        queryset (QuerySet): The queryset of User objects.
        serializer_class (Serializer): The serializer class for User objects.

    Methods:
        put(self, request, *args, **kwargs): Handles the PUT request to enable a user.

    Examples:
        To enable a user, send a PUT request to the following URL:
        /api/users/<user_id>/enabled/

        Example Request:
        PUT /api/users/1234/enabled/

        Example Response:
        HTTP 200 OK
        {
            "message": "User enabled successfully."
        }
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def put(self, request, *args, **kwargs):
        user = self.get_object()
        # Your implementation here
        user.is_active = True
        user.save()
        return Response(status=status.HTTP_200_OK)


class UserDisabled(generics.UpdateAPIView):
    """
    API endpoint that allows a user to be disabled.

    Inherits from `generics.UpdateAPIView` and provides a `put` method
    to disable a user by setting their `is_active` attribute to False.

    Attributes:
        queryset (QuerySet): The queryset of all User objects.
        serializer_class (Serializer): The serializer class for User objects.

    Methods:
        put(request, *args, **kwargs): Updates the user's `is_active` attribute to False.

    Returns:
        Response: HTTP 200 OK response.

    Examples:
        To disable a user, send a PUT request to the endpoint with the user's ID:
        ```
        PUT /users/disable/1
        ```

        Response:
        ```
        HTTP 200 OK
        ```

    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def put(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_active = False
        user.save()
        return Response(status=status.HTTP_200_OK)
