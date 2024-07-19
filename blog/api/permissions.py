from rest_framework import permissions
from api.models import UserStatus
class IsActive(permissions.BasePermission):
    def has_permission(self, request, view):
        if UserStatus.objects.filter(user=request.user, is_active=False).exists():
            return False 
        
        return super().has_permission(request, view)