import pytest
from contextlib import nullcontext as not_raise

from Utils.Other_func import get_bool_from_str


@pytest.mark.parametrize(
    "param, bool_result, expected_to_raise",
    [
        ("True", True, not_raise()),
        ("true", True, not_raise()),
        ("TRUE", True, not_raise()),
        ("FALSE", False, not_raise()),
        ("False", False, not_raise()),
        ("false", False, not_raise()),
        ("text", False, not_raise()),
        (str(), False, not_raise()),
        (int(), False, pytest.raises(AttributeError)),
        (float(), False, pytest.raises(AttributeError)),
        (dict(), False, pytest.raises(AttributeError)),
        (list(), False, pytest.raises(AttributeError)),
        (object(), False, pytest.raises(AttributeError)),
    ]
)
def test_get_bool_from_str(param, bool_result, expected_to_raise):
    with expected_to_raise:
        assert get_bool_from_str(param) == bool_result


def test_detect_en_simbol_check_type():
    text = "True"
    type_func = type(get_bool_from_str(text))
    assert type_func == bool
