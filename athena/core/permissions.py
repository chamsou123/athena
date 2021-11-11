from enum import Enum

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import permission_required


class BasePermissionEnum(Enum):
    @property
    def codename(self):
        return self.value.split(".")[1]


class AccountPermissions(BasePermissionEnum):
    MANAGE_USERS = "account.manage_users"
    MANAGE_STAFF = "account.manage_staff"
    IMPERSONATE_USER = "account.impersonate_user"


def split_permission_codename(permissions):
    return [permission.split(".")[1] for permission in permissions]


def permission_required(perms, requestor):
    User = get_user_model()
    if isinstance(requestor, User):
        if requestor.has_perms(perms):
            return True
    else:
        if AccountPermissions.MANAGE_STAFF in perms:
            return False
        return requestor.has_perms(perms)
    return False


def has_one_of_permissions(requestor, permissions=None):
    if not permissions:
        return True
    for perm in permissions:
        if permission_required((perm,), requestor):
            return True
    return False
