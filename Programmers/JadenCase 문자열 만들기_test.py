import importlib.util
from pathlib import Path

import pytest

test_file_name = 'JadenCase 문자열 만들기_test.py'
file_name = test_file_name.replace('_test', '')
module_name = Path(__file__).parent / file_name
spec = importlib.util.spec_from_file_location('module', module_name)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


@pytest.mark.parametrize(('s', 'answer'), [
    ("3people unFollowed me", "3people Unfollowed Me"),
    ("for the last week", "For The Last Week"),
    ("for the last  week", "For The Last  Week"),
])
def test_solution(s, answer):
    assert module.solution(s) == answer
