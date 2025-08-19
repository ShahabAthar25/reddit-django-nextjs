from django.urls import path

from .views import (FollowUserView, RetrieveSpecifiedUserView,
                    RetrieveUpdateDestroyUserView)

urlpatterns = [
    path(
        "me/", RetrieveUpdateDestroyUserView.as_view(), name="user-detail-update-delete"
    ),
    path("<int:pk>/", RetrieveSpecifiedUserView.as_view(), name="user-retrieve"),
    path("<int:user_id>/follow/", FollowUserView.as_view(), name="user-follow"),
]
