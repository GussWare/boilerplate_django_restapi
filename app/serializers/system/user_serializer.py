from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'password',
                  'username', 'email', 'is_staff', 'is_active', 'date_joined', 'last_login']
        extra_kwargs = {
            'password': {'write_only': True},
        }
