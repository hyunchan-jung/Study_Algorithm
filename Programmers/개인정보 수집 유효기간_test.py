import importlib.util
from pathlib import Path

import pytest

test_file_name = '개인정보 수집 유효기간_test.py'
file_name = test_file_name.replace('_test', '')
module_name = Path(__file__).parent / file_name
spec = importlib.util.spec_from_file_location('module', module_name)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


@pytest.mark.parametrize(('today', 'terms', 'privacies', 'answer'), [
    ('2022.05.19', ['A 6', 'B 12', 'C 3'], ['2021.05.02 A', '2021.07.01 B', '2022.02.19 C'], [1, 3]),
    ('2020.01.01', ['Z 3', 'D 5'], ['2019.01.01 D', '2019.11.15 Z', '2019.08.02 D', '2019.07.01 D', '2018.12.28 Z'], [1, 4, 5]),
])
def test_solution(today, terms, privacies, answer):
    assert module.solution(today, terms, privacies) == answer
