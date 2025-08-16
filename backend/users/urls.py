from django.urls import path
from .views import RetrieveUpdateDestroyUserView, RetrieveSpecifiedUserView, FollowUserView

urlpatterns = [
    path('', RetrieveUpdateDestroyUserView.as_view(), name='user-detail-update-delete'),
    path('<int:pk>/', RetrieveSpecifiedUserView.as_view(), name='user-retrieve'),
    path('<int:user_id>/follow/', FollowUserView.as_view(), name='user-follow'),
]
