from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    Others can only read the object.
    """
    
    def has_permission(self, request, view):
        # Allow read-only access for all users
        return request.method in ['GET', 'HEAD', 'OPTIONS']

    def has_object_permission(self, request, view, obj):
        # Allow write access only to the owner of the object
        return obj.owner == request.user or request.method in ['GET', 'HEAD', 'OPTIONS']
