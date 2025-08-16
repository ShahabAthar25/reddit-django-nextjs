from rest_framework import serializers
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """Serializer for retrieving and updating user details."""

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "email",
            "profile_picture",
            "bio",
            "karma_points",
            "role",
        ]
        read_only_fields = ["role", "karma_points"]
