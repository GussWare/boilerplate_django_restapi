from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from app.serializers.system.auth.register_serializer import RegisterSerializer


class RegisterUserView(APIView):
    """
    API view for registering a new user.

    This view accepts a POST request with user data and creates a new user if the data is valid.
    If the data is invalid, it returns a response with the validation errors.

    Methods:
    - post: Handles the POST request and creates a new user if the data is valid.

    Attributes:
    - serializer: An instance of RegisterSerializer used for validating and saving user data.
    """

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
