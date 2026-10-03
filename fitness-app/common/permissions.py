from rest_framework import permissions

class IsGoalOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.profile.user == request.user