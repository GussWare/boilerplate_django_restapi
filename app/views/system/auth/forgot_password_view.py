from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.forms import PasswordResetForm
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.urls import reverse
from app.services.emails.auth import forgot_password_email


class ForgotPasswordView(APIView):
    """
    View for handling the forgot password functionality.
    """
    def post(self, request):
        """
        Handle the POST request for resetting the password.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            Response: The HTTP response object.

        Raises:
            None
        """
        form = PasswordResetForm(request.data)

        if form.is_valid():
            user = form.get_user()
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_url = request.build_absolute_uri(
                reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
            )
            forgot_password_email.send_email(user.email, reset_url)
            return Response({'detail': 'Password reset email sent.'}, status=200)
        
        return Response(form.errors, status=400)