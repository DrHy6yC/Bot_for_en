import pytest
from contextlib import nullcontext as not_raise

from Utils.Text_commands import detect_en_simbol


@pytest.mark.parametrize(
    "text, bool_result, expected_to_raise",
    [
        ("actyemkop", True, not_raise()),
        ("астуемкор", False, not_raise()),
        ("", False, not_raise()),
        ("0", False, not_raise()),
        (0, False, pytest.raises(TypeError)),
        (0.1, False, pytest.raises(TypeError)),
        ("s йсвуъё fуектae 0.1", True, not_raise())
    ]
)
def test_detect_en_simbol(text, bool_result, expected_to_raise):
    with expected_to_raise:
        assert detect_en_simbol(text) == bool_result
