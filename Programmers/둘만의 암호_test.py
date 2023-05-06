import importlib.util
from pathlib import Path

import pytest

test_file_name = '둘만의 암호_test.py'
file_name = test_file_name.replace('_test', '')
module_name = Path(__file__).parent / file_name
spec = importlib.util.spec_from_file_location('module', module_name)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


@pytest.mark.parametrize(('s', 'skip', 'index', 'answer'), [
    ('aukks', 'wbqd', 5, 'happy'),
])
def test_solution(s, skip, index, answer):
    assert module.solution(s, skip, index) == answer
