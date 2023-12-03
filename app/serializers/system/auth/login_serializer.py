from django.contrib.auth import get_user_model
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = User.objects.filter(email=attrs['email']).first()

        if user and user.check_password(attrs['password']):
            refresh = RefreshToken.for_user(user)

            data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user_data': {
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email,
                }
            }

            update_last_login(None, user)
            return data

        raise serializers.ValidationError('Invalid credentials')
