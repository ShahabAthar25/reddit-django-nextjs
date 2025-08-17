from rest_framework import serializers
from .models import Subreddit, Rule


class SubredditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subreddit
        fields = ["id", "name", "description", "creator", "created_at"]
        read_only_fields = ["creator", "created_at"]


class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = ["id", "subreddit", "title", "description"]
        read_only_fields = ["subreddit"]
