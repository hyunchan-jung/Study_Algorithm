import importlib.util
from pathlib import Path

import pytest

test_file_name = '대충 만든 자판_test.py'
file_name = test_file_name.replace('_test', '')
module_name = Path(__file__).parent / file_name
spec = importlib.util.spec_from_file_location('module', module_name)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


@pytest.mark.parametrize(('keymap', 'targets', 'answer'), [
    (["ABACD", "BCEFD"], ["ABCD","AABB"], [9, 4]),
    (["AA"], ["B"], [-1]),
    (["AGZ", "BSSS"], ["ASA", "BGZ"], [4, 6]),
])
def test_solution(keymap, targets, answer):
    assert module.solution(keymap, targets) == answer
