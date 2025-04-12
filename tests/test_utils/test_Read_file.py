from contextlib import nullcontext as not_raise

import pytest


from Utils.Read_file import import_csv


path_test_csv: str = "/Users/denisigorevich/PycharmProjects/Bot_for_en/tests/test_.csv"
expected_result: list = [
    {'NumberQuestion': '1', 'Question': '"Doctor Who? -______"', 'Answer1': 'Harry', 'Answer2': 'Who?', 'Answer3': '...', 'Answer4': 'Vadim', 'TrueAnswer': '4'},
    {'NumberQuestion': '2', 'Question': '"How are you? -______"', 'Answer1': 'You', 'Answer2': 'I', 'Answer3': 'Vadim', 'Answer4': 'Who?', 'TrueAnswer': '2'}
]


@pytest.mark.parametrize(
    "path_csv, result, expected_to_raise",
    [
        (path_test_csv, expected_result, not_raise()),
        (str(), -1, pytest.raises(FileNotFoundError)),
        (int(), False, pytest.raises(TypeError)),
        (float(), False, pytest.raises(TypeError)),
        (dict(), False, pytest.raises(TypeError)),
        (list(), False, pytest.raises(TypeError)),
        (object(), False, pytest.raises(TypeError)),
    ]
)
def test_import_csv(path_csv, result, expected_to_raise):
    with expected_to_raise:
        assert import_csv(path_csv) == result


def test_import_csv_check_type():
    type_func = type(import_csv(path_test_csv))
    assert type_func == list
