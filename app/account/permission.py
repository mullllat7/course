from rest_framework.permissions import BasePermission
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
class IsActivePermission(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_active)

class IsAuthorPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.user == obj.user
        )

class PermissionMixin:
    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsAuthenticated, ]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permissions = [IsAuthenticated, ]
        else:
            permissions = []
        return [permission() for permission in permissions]
