from core.permissions import IsOwnerOrReadOnly
from post.models import Post
from post.serializers import PostSerializer
from rest_framework import generics, status, viewsets
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Rule, Subreddit
from .permissions import IsSubredditOwner
from .serializers import RuleSerializer, SubredditSerializer


class SubredditViewSet(viewsets.ModelViewSet):
    queryset = Subreddit.objects.all()
    serializer_class = SubredditSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class SubredditPostList(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        subreddit_id = self.kwargs["subreddit_id"]
        return Post.objects.filter(subreddit_id=subreddit_id)


class JoinLeaveSubredditView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, subreddit_id):
        try:
            subreddit = Subreddit.objects.get(id=subreddit_id)
        except Subreddit.DoesNotExist:
            return Response(
                {"error": "Subreddit not found"}, status=status.HTTP_404_NOT_FOUND
            )

        if subreddit.members.filter(id=request.user.id).exists():
            subreddit.members.remove(request.user)
            return Response(
                {"message": "Successfully left the subreddit"},
                status=status.HTTP_200_OK,
            )
        else:
            subreddit.members.add(request.user)
            return Response(
                {"message": "Successfully joined the subreddit"},
                status=status.HTTP_200_OK,
            )


class RuleViewSet(viewsets.ModelViewSet):
    serializer_class = RuleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsSubredditOwner]

    def get_queryset(self):
        return Rule.objects.filter(subreddit_id=self.kwargs["subreddit_pk"])

    def perform_create(self, serializer):
        subreddit = Subreddit.objects.get(pk=self.kwargs["subreddit_pk"])
        serializer.save(subreddit=subreddit)
