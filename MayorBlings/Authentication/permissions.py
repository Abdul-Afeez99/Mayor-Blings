from rest_framework.permissions import BasePermission

class IsEndUser(BasePermission):
    '''
    Permission for an individual user
    '''
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_enduser)
    
    
class IsAdmin(BasePermission):
    '''
    Permission for admin user
    '''
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_admin)