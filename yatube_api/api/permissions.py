from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Если пользователь не автор, то только для чтения."""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
