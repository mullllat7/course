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
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permissions = [IsAdminUser, ]
        else:
            permissions = [IsAuthenticated]
        return [permission() for permission in permissions]


class IsTeacherOrAdminPermission(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_teacher and request.user.is_active or request.user.is_staff)