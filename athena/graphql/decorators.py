from enum import Enum
from functools import wraps

from django.core.exceptions import PermissionDenied
from graphql import ResolveInfo

from athena.core.permissions import has_one_of_permissions
from athena.core.permissions import permission_required as core_permission_required
from athena.graphql.core.utils.utils import get_user_from_context


def context(f):
    def decorator(func):
        def wrapper(*args, **kwargs):
            info = next(arg for arg in args if isinstance(arg, ResolveInfo))
            return func(info.context, *args, **kwargs)

        return wrapper

    return decorator


def account_passes_test(test_func):
    def decorator(f):
        @wraps(f)
        @context(f)
        def wrapper(context, *args, **kwargs):
            if test_func(context):
                return f(*args, **kwargs)
            raise PermissionDenied()

        return wrapper

    return decorator


def permission_required(perm):
    def check_perms(context):
        if isinstance(perm, Enum):
            perms = (perm,)
        else:
            perms = perm

        requestor = get_user_from_context(context)
        return core_permission_required(perms, requestor)

    return account_passes_test(check_perms)


def one_of_permissions_required(perms):
    def check_perms(context):
        requestor = get_user_from_context(context)
        return has_one_of_permissions(requestor, perms)

    return account_passes_test(check_perms)
