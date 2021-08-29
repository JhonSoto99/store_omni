"""
Accounts Serializers
"""

# Django RestFramework
from rest_framework import serializers

# Models
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'is_superuser',
            'is_staff',
        ]