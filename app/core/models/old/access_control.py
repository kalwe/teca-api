from tortoise import fields
from typing import List, Type

from app.core.models.user import User

class PermissionStrategy:
    """
    Base strategy class for permissions.
    """
    def can_access(self, user: 'User', resource: str) -> bool:
        raise NotImplementedError("Each strategy must implement 'can_access'.")

class AdminPermissionStrategy(PermissionStrategy):
    """
    Permission strategy for Admin users.
    """
    def can_access(self, user: 'User', resource: str) -> bool:
        return True  # Admins can access any resource

class ManagerPermissionStrategy(PermissionStrategy):
    """
    Permission strategy for Manager users.
    """
    def can_access(self, user: 'User', resource: str) -> bool:
        allowed_resources = {"employee_records", "reports"}
        return resource in allowed_resources

class EmployeePermissionStrategy(PermissionStrategy):
    """
    Permission strategy for Employee users.
    """
    def can_access(self, user: 'User', resource: str) -> bool:
        return resource == "personal_records"

class AccessControl:
    """
    A class for managing access control based on user permissions.
    Uses the Strategy pattern to allow different permission strategies.
    """
    def __init__(self, permission_strategy: PermissionStrategy):
        self.permission_strategy = permission_strategy

    def set_permission_strategy(self, permission_strategy: PermissionStrategy) -> None:
        """
        Sets the permission strategy dynamically.
        """
        self.permission_strategy = permission_strategy

    def can_access(self, user: 'User', resource: str) -> bool:
        """
        Determines if the user has permission to access the given resource.
        """
        return self.permission_strategy.can_access(user, resource)
