from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_superuser:
            return request.user == obj.creator
        else:
            return 1