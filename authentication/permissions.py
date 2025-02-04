from rest_framework.permissions import BasePermission

class IsUser(BasePermission):
    """
    Custom permission to allow only users (role='user') to view customer details.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'user'
