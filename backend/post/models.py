from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from subreddits.models import Subreddit


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="post_images/", blank=True, null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts"
    )
    subreddit = models.ForeignKey(
        Subreddit, on_delete=models.CASCADE, related_name="posts"
    )
    upvotes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="upvoted_posts", blank=True
    )
    downvotes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="downvoted_posts", blank=True
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="post_comment"
    )
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name="replies", null=True, blank=True
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="owner_comment",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to="comment_images/", blank=True, null=True)
    upvotes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="upvoted_comments", blank=True
    )
    downvotes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="downvoted_comments", blank=True
    )

    def __str__(self):
        return f"Comment by {self.created_by} on {self.post}"
