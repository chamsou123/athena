import pytest

from athena.account.models import User


@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user("jhondoe@example.com", "doepassword", False, True)
    assert User.objects.all().count() == 1
    assert user.is_active
    assert user.email == "jhondoe@example.com"
    assert not (user.is_staff and user.is_superuser)


@pytest.mark.django_db
def test_create_superuser():
    user = User.objects.create_superuser("jhondoeadmin@example.com", "doeadminpassword")
    assert User.objects.all().count() == 1
    assert user.is_active and user.is_staff and user.is_superuser
    assert user.email == "jhondoeadmin@example.com"


@pytest.mark.parametrize(
    "email, first_name, last_name, full_name",
    [
        ("John@example.com", "Jhon", "Doe", "Jhon Doe"),
        ("Jhon@example.com", "", "Doe", "Doe"),
        ("Jhon@example.com", "Jhon", "", "Jhon"),
        ("", "Jhon", "Doe", "Jhon Doe"),
        ("Jhon@example.com", "", "", "Jhon@example.com"),
        ("", "", "", ""),
    ]
)
def test_get_full_name(email, first_name, last_name, full_name):
    user = User(email=email, first_name=first_name, last_name=last_name)
    assert user.get_full_name() == full_name


@pytest.mark.parametrize(
    "email, short_name",
    [
        ("John@example.com", "John@example.com"),
        ("", ""),
    ]
)
def test_short_name(email, short_name):
    user = User(email=email)
    assert user.get_short_name() == email
