
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from app.serializers.system.auth.reset_password_serializer import PasswordResetSerializer

class ResetPasswordView(APIView):
    """
    API view for resetting user password.
    """

    def post(self, request):
        """
        Handle POST request to reset user password.

        Parameters:
        - request: The HTTP request object.

        Returns:
        - Response: The HTTP response object.
        """
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            user.password = make_password(serializer.validated_data['password'])
            user.save()
            return Response({'message': 'Password updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
