from rest_framework.permissions import BasePermission


class DynamicPermission(BasePermission):
    def __init__(self, *args):
        super().__init__()

        self.permissions = args

    def has_permission(self, request, view):
        for perm in self.permissions:
            if request.user.has_perm(perm):
                return True

        return False
