from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubredditViewSet, JoinLeaveSubredditView

router = DefaultRouter()
router.register(r'', SubredditViewSet, basename='subreddit')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:subreddit_id>/join/', JoinLeaveSubredditView.as_view(), name='join-leave-subreddit'),
]
