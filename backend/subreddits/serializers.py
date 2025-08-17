from rest_framework import serializers
from .models import Subreddit

class SubredditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subreddit
        fields = ['id', 'name', 'description', 'creator', 'created_at']
        read_only_fields = ['creator', 'created_at']
