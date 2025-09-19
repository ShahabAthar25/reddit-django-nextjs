from rest_framework import serializers
from users.serializers import UserSerializer

from .models import Comment, Post


class PostSerializer(serializers.ModelSerializer):
    upvotes = serializers.SerializerMethodField()
    downvotes = serializers.SerializerMethodField()

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
            "upvotes",
            "downvotes",
        ]
        read_only_fields = ["created_by", "created_at"]

    def get_upvotes(self, obj):
        return obj.upvotes.count()

    def get_downvotes(self, obj):
        return obj.downvotes.count()


class CommentSerializer(serializers.ModelSerializer):
    upvotes = serializers.SerializerMethodField()
    downvotes = serializers.SerializerMethodField()
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

    def get_upvotes(self, obj):
        return obj.upvotes.count()

    def get_downvotes(self, obj):
        return obj.downvotes.count()
