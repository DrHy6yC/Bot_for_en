import pytest
from contextlib import nullcontext as not_raise

from Utils.Text_commands import detect_en_simbol


@pytest.mark.parametrize(
    "text, bool_result, expected_to_raise",
    [
        ("actyemkop", True, not_raise()),
        ("астуемкор", False, not_raise()),
        ("", False, not_raise()),
        ("0123456789+-/[],.", False, not_raise()),
        ("s йсвуъё fуектae 0.1", True, not_raise()),
        (str(), False, not_raise()),
        (int(), False, pytest.raises(TypeError)),
        (float(), False, pytest.raises(TypeError)),
        (dict(), False, pytest.raises(TypeError)),
        (list(), False, pytest.raises(TypeError)),
        (object(), False, pytest.raises(TypeError)),
    ]
)
def test_detect_en_simbol(text, bool_result, expected_to_raise):
    with expected_to_raise:
        assert detect_en_simbol(text) == bool_result


def test_detect_en_simbol_check_type():
    text = "text"
    type_func = type(detect_en_simbol(text))
    type_bool = type(True)
    assert type_func == type_bool
