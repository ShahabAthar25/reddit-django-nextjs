from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer

from .permissions import IsOwnerOrReadOnly

CustomUser = get_user_model()

class RetrieveUpdateDestroyUserView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a user.
    """
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)

class RetrieveSpecifiedUserView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
