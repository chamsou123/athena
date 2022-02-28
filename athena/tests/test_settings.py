import pytest

from athena.settings import get_list


@pytest.mark.parametrize(
    "text, result",
    [
        ("localhost, test, test, test, test", ["localhost", "test", "test", "test", "test"]),
        ("", TypeError)
    ]
)
def test_get_list(text, result):
    try:
        assert get_list(text) == result
    except TypeError:
        assert True
