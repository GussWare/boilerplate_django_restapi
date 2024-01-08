from rest_framework import serializers
from app.models.system.group import GroupExtended


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupExtended
        fields = ['id', 'name', 'description', 'codename', 'created_at', 'updated_at']
