from django.contrib.auth import get_user_model
from rest_framework import serializers

CustomUser = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Serializer for retrieving and updating user details."""

    followers = serializers.SerializerMethodField()

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
            "followers",
        ]
        read_only_fields = ["role", "karma_points"]

    def get_followers(self, obj):
        return obj.followers.count()
