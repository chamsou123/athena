from graphene_django.forms.converter import convert_form_field

from athena.graphql.core.filters import EnumFilter, ObjectTypeFilter


@convert_form_field.register(ObjectTypeFilter)
@convert_form_field.register(EnumFilter)
def convert_convert_enum(field):
    return field.input_class()
