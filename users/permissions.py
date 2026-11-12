from rest_framework.permissions import BasePermission

from .models import CustomUser


class IsAdminOnly(BasePermission):
    """Разрешает доступ только пользователям с ролью ADMIN."""

    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.role == CustomUser.Role.ADMIN
        )


class IsUserOnly(BasePermission):
    """Разрешает доступ только пользователям с ролью USER."""

    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.role == CustomUser.Role.USER
        )
