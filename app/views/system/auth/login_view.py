from rest_framework_simplejwt.views import TokenObtainPairView
from app.serializers.system.auth.login_serializer import LoginSerializer
from rest_framework import status


class LoginView(TokenObtainPairView):
    """
    View for handling user login and generating JWT tokens.

    Inherits from TokenObtainPairView which is a built-in view provided by the rest_framework_simplejwt library.
    Uses the LoginSerializer for validating user credentials and generating tokens.

    Attributes:
        serializer_class (class): The serializer class to be used for validating user credentials.
    """
    serializer_class = LoginSerializer
