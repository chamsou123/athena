import django_filters
from django.db.models import Q

from athena.account.models import User
from athena.graphql.account.enums import StaffMemberStatus
from athena.graphql.core.filters import EnumFilter


def filter_staff_status(qs, _, value):
    if value == StaffMemberStatus.ACTIVE:
        return qs.filter(is_staff=True, is_active=True)
    if value == StaffMemberStatus.DEACTIVATED:
        return qs.filter(is_staff=True, is_active=False)
    return qs


def filter_user_search(qs, _, value):
    if value:
        qs = qs.filter(
            Q(email__ilike=value)
            | Q(first_name__ilike=value)
            | Q(last_name__ilike=value)
        )
    return qs


class StaffUserFilter(django_filters.FilterSet):
    status = EnumFilter(input_class=StaffMemberStatus, method=filter_staff_status)
    search = django_filters.CharFilter(method=filter_user_search)

    class Meta:
        model = User
        fields = ["status", "search"]
