from django.contrib.auth import get_user_model
from graphene import relay

from athena.graphql.core.connection import CountableDjangoObjectType


class UserType(CountableDjangoObjectType):
    class Meta:
        description = "Represents user data."
        interfaces = [relay.Node]
        model = get_user_model()
        only_fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "is_staff",
            "date_joined",
        ]
