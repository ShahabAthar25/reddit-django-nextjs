from django.urls import path, include
from rest_framework_nested import routers
from .views import SubredditViewSet, JoinLeaveSubredditView, RuleViewSet

router = routers.DefaultRouter()
router.register(r"", SubredditViewSet, basename="subreddit")

rules_router = routers.NestedSimpleRouter(router, r"", lookup="subreddit")
rules_router.register(r"rules", RuleViewSet, basename="subreddit-rules")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(rules_router.urls)),
    path(
        "<int:subreddit_id>/join/",
        JoinLeaveSubredditView.as_view(),
        name="join-leave-subreddit",
    ),
]
