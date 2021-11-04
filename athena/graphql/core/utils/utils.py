import binascii

import graphene
from graphql import GraphQLError


def get_user_from_context(context):
    return context.user


def from_global_id_or_error(id, only_type=None, raise_error=False):
    try:
        _type, _id = graphene.Node.from_global_id(id)
    except (binascii.Error, UnicodeDecodeError, ValueError):
        raise GraphQLError(f"Couldn't resolve id: {id}.")

    if only_type and str(_type) != str(only_type):
        if not raise_error:
            return _type, None
        raise GraphQLError(f"Must receive a {only_type} id.")
    return _type, _id
