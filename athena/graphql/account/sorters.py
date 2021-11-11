import graphene

from athena.graphql.core.types.sort_inputs import SortInputObjectType


class UserSortField(graphene.Enum):
    FIRST_NAME = ["first_name", "last_name", "pk"]
    LAST_NAME = ["last_name", "first_name", "pk"]
    EMAIL = ["email"]

    @property
    def description(self):
        if self.name in UserSortField.__enum__._member_names_:
            sort_name = self.name.lower().replace("_", " ")
            return f"Sort users by {sort_name}."
        raise ValueError("Unsupported enum value: %s" % self.value)


class UserSortingInput(SortInputObjectType):
    class Meta:
        sort_enum = UserSortField
        type_name = "users"
