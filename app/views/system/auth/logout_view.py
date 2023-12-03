from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

class LogoutView(APIView):
    """
    View for logging out a user by blacklisting the refresh token.

    Attributes:
        permission_classes (tuple): Tuple of permission classes required for accessing this view.
    """

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=204)
        except Exception as e:
            return Response(status=400, data={"error": "Bad request"})