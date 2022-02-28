import graphene as graphene

from athena.core.permissions import AccountPermissions
from athena.graphql.account.filters import StaffUserFilter
from athena.graphql.account.resolvers import _resolve_user, _resolve_staff_users
from athena.graphql.account.sorters import UserSortingInput
from athena.graphql.account.types import UserType
from athena.graphql.core.fields import FilterInputConnectionField
from athena.graphql.core.types.filter_input import FilterInputObjectType
from athena.graphql.core.validators import validate_one_of_args_is_in_query
from athena.graphql.decorators import one_of_permissions_required, permission_required


class StaffUserInput(FilterInputObjectType):
    class Meta:
        filterset_class = StaffUserFilter


class AccountQueries(graphene.ObjectType):
    me = graphene.Field(UserType, description="Return the current authenticated user")

    user = graphene.Field(
        UserType,
        id=graphene.Argument(graphene.ID, description="ID of the user."),
        email=graphene.Argument(
            graphene.String, description="Email address of the user."
        ),
        description="Look up a user by ID or email address.",
    )

    staff_users = FilterInputConnectionField(
        UserType,
        filter=StaffUserInput(description="Filtering options for staff users."),
        sort_by=UserSortingInput(description="Sort staff users."),
        description="List of athena staff users.",
    )

    @one_of_permissions_required([AccountPermissions.MANAGE_STAFF, AccountPermissions.MANAGE_USERS])
    def resolve_user(self, info, id=None, email=None):
        validate_one_of_args_is_in_query("id", id, "email", email)
        return _resolve_user(info, id, email)

    def resolve_me(self, info):
        user = info.context.user
        return user if user.is_authenticated else None

    @permission_required(AccountPermissions.MANAGE_STAFF)
    def resolve_staff_users(self, info, **kwargs):
        return _resolve_staff_users(info, **kwargs)
