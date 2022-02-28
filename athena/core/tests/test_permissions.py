import pytest

from athena.core.permissions import split_permission_codename


@pytest.mark.parametrize(
    "permissions, result",
    [
        (["account.manage_users", "account.manage_staff"], [['account', 'manage_users'], ['account', 'manage_staff']]),
        ("", TypeError)
    ]
)
def test_split_permission_codename(permissions, result):
    try:
        assert split_permission_codename(permissions) == result
    except TypeError:
        assert True
