from django.urls import path, include
from rest_framework_nested import routers

from .views import PostViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r"", PostViewSet, basename="post")

comments_router = routers.NestedSimpleRouter(router, r"", lookup="post")
comments_router.register(r"comments", CommentViewSet, basename="post-comments")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(comments_router.urls)),
]
