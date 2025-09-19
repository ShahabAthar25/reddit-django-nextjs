from core.permissions import IsOwnerOrReadOnly
from django.core.cache import cache
from django.db.models import Count
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import status

from .models import Comment, Post
from .serializers import CommentSerializer, PostSerializer


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

    @action(detail=True, methods=["post"])
    def upvote(self, request, pk=None):
        post = self.get_object()
        user = self.request.user

        if post.upvotes.filter(id=user.id).exists():
            post.upvotes.remove(user)
            return Response({"msg": "upvote removed"}, status=status.HTTP_200_OK)
        else:
            post.upvotes.add(user)

            if post.downvotes.filter(id=user.id).exists():
                post.downvotes.remove(user)

            return Response({"status": "Upvoted"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"])
    def downvote(self, request, pk=None):
        post = self.get_object()
        user = self.request.user

        if post.downvotes.filter(id=user.id).exists():
            post.downvotes.remove(user)
            return Response({"msg": "Downvote removed"}, status=status.HTTP_200_OK)
        else:
            post.downvotes.add(user)

            if post.upvotes.filter(id=user.id).exists():
                post.upvotes.remove(user)

            return Response({"status": "Downvoted"}, status=status.HTTP_200_OK)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs["post_pk"])

    def perform_create(self, serializer):
        post = Post.objects.filter(id=self.kwargs["post_pk"]).first()
        parent_id = self.request.data.get("parent")

        parent = None
        if parent_id:
            parent = Comment.objects.get(id=parent_id)

        serializer.save(created_by=self.request.user, post=post, parent=parent)
