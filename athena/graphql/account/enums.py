import graphene


class StaffMemberStatus(graphene.Enum):
    ACTIVE = "active"
    DEACTIVATED = "deactivated"

    @property
    def description(self):
        if self == StaffMemberStatus.ACTIVE:
            return "User account has been activated."
        elif self == StaffMemberStatus.DEACTIVATED:
            return "User account has not been activated yet."
        return None
