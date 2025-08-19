from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "subreddit", "created_by", "created_at")
    list_filter = ("subreddit", "created_at")
    search_fields = ("title", "description")
    readonly_fields = ("created_at",)

    fieldsets = (
        (None, {"fields": ("title", "description", "image")}),
        ("Relations", {"fields": ("created_by", "subreddit")}),
        ("Votes", {"fields": ("upvotes", "downvotes")}),
        ("Date Information", {"fields": ("created_at",)}),
    )

    filter_horizontal = ("upvotes", "downvotes")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "created_by", "created_at")
    list_filter = ("created_at",)
    search_fields = ("text",)
    readonly_fields = ("created_at",)

    fieldsets = (
        (None, {"fields": ("text", "image")}),
        ("Relations", {"fields": ("post", "created_by")}),
        ("Votes", {"fields": ("upvotes", "downvotes")}),
        ("Date Information", {"fields": ("created_at",)}),
    )

    filter_horizontal = ("upvotes", "downvotes")
