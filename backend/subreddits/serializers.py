from rest_framework import serializers
from users.serializers import UserSerializer

from .models import Rule, Subreddit


class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = ["id", "subreddit", "title", "description"]
        read_only_fields = ["subreddit"]


class SubredditSerializer(serializers.ModelSerializer):
    members = serializers.SerializerMethodField()
    rules = RuleSerializer(many=True, read_only=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Subreddit
        fields = [
            "id",
            "name",
            "description",
            "banner",
            "icon",
            "created_by",
            "created_at",
            "members",
            "rules",
        ]
        read_only_fields = ["created_by", "created_at"]

    def get_members(self, obj):
        return obj.members.count()
