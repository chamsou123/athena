from django.core.exceptions import PermissionDenied

from athena.account import models
from athena.account.models import User
from athena.core.permissions import AccountPermissions
from athena.graphql.core.utils.utils import get_user_from_context, from_global_id_or_error


def _resolve_user(info, id=None, email=None):
    requester = get_user_from_context(info.context)
    if requester:
        filter_kwargs = {}
        if id:
            print(id)
            _model, filter_kwargs["pk"] = from_global_id_or_error(id, User)
        if email:
            filter_kwargs["email"] = email
        if requester.has_perms(
                [AccountPermissions.MANAGE_STAFF, AccountPermissions.MANAGE_USERS]
        ):
            return models.User.objects.filter(**filter_kwargs).first()
        if requester.has_perm(AccountPermissions.MANAGE_STAFF):
            return models.User.objects.staff().filter(**filter_kwargs).first()
    return PermissionDenied('You do not have permission to perform this action')
