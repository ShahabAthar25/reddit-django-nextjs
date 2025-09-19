from rest_framework import permissions

from .models import Subreddit


class IsSubredditOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if view.action == "create":
            subreddit = Subreddit.objects.get(pk=view.kwargs["subreddit_pk"])
            return subreddit.created_by == request.user
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.subreddit.created_by == request.user

