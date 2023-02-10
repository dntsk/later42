"""Serializers for later42 app."""

from django.contrib.auth.models import Group, User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """User serializer"""

    class Meta:
        """Meta"""

        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """Group serializer"""

    class Meta:
        """Meta"""

        model = Group
        fields = ["url", "name"]
