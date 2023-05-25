import importlib.util
from pathlib import Path

import pytest

test_file_name = '성격 유형 검사하기_test.py'
file_name = test_file_name.replace('_test', '')
module_name = Path(__file__).parent / file_name
spec = importlib.util.spec_from_file_location('module', module_name)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


@pytest.mark.parametrize(('survey', 'choices', 'answer'), [
    (['AN', 'CF', 'MJ', 'RT', 'NA'], [5, 3, 2, 7, 5], 'TCMA'),
    (['TR', 'RT', 'TR'], [7, 1, 3], 'RCJA')
])
def test_solution(survey, choices, answer):
    assert module.solution(survey, choices) == answer
