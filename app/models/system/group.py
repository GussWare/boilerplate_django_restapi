from django.db import models
from django.contrib.auth.models import Group

class GroupExtended(Group):
    codename = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'auth_group_extended'