from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Subreddit
from .serializers import SubredditSerializer


class SubredditViewSet(viewsets.ModelViewSet):
    queryset = Subreddit.objects.all()
    serializer_class = SubredditSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class JoinLeaveSubredditView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, subreddit_id):
        try:
            subreddit = Subreddit.objects.get(id=subreddit_id)
        except Subreddit.DoesNotExist:
            return Response({"error": "Subreddit not found"}, status=status.HTTP_404_NOT_FOUND)

        if subreddit.members.filter(id=request.user.id).exists():
            subreddit.members.remove(request.user)
            return Response({"message": "Successfully left the subreddit"}, status=status.HTTP_200_OK)
        else:
            subreddit.members.add(request.user)
            return Response({"message": "Successfully joined the subreddit"}, status=status.HTTP_200_OK)
