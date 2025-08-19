from django.core.cache import cache
from django.db.models import Count
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from core.permissions import IsOwnerOrReadOnly

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=False, methods=["get"])
    def trending(self, request):
        cached_trending_posts = cache.get("trending_posts")
        if cached_trending_posts:
            return Response(cached_trending_posts)

        trending_posts = Post.objects.annotate(upvote_count=Count("upvotes")).order_by(
            "-upvote_count"
        )[:20]

        serializer = self.get_serializer(trending_posts, many=True)
        cache.set("trending_posts", serializer.data, 60 * 15)  # Cache for 15 minutes
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs["post_pk"])

    def perform_create(self, serializer):
        post = Post.objects.get(pk=self.kwargs["post_pk"])
        serializer.save(created_by=self.request.user, post=post)
