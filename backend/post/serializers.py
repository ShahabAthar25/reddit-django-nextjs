from rest_framework import serializers
from users.serializers import UserSerializer

from .models import Comment, Post
from subreddits.models import Subreddit

class PostSubredditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subreddit
        fields = ["id", "name", "icon"]

class PostSerializer(serializers.ModelSerializer):
    upvotes = serializers.IntegerField(source="upvote_count", read_only=True)
    downvotes = serializers.IntegerField(source="downvote_count", read_only=True)

    created_by = UserSerializer(read_only=True)

    subreddit_id = serializers.PrimaryKeyRelatedField(
        queryset=Subreddit.objects.all(),
        source="subreddit",
        write_only=True
    )
    subreddit = PostSubredditSerializer(read_only=True)
    class Meta:
        model = Post
        fields = [
            "id",
            "created_at",
            "title",
            "description",
            "image",
            "created_by",
            "subreddit",
            "subreddit_id",
            "upvotes",
            "downvotes",
        ]
        read_only_fields = ["created_by", "created_at"]

class CommentSerializer(serializers.ModelSerializer):
    upvotes = serializers.IntegerField(read_only=True)
    downvotes = serializers.IntegerField(read_only=True)

    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = [
            "id",
            "created_by",
            "created_at",
            "text",
            "image",
            "upvotes",
            "downvotes",
        ]
        read_only_fields = ["created_by", "post", "parent"]
