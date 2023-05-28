import importlib.util
from pathlib import Path

import pytest

test_file_name = '공원 산책_test.py'
file_name = test_file_name.replace('_test', '')
module_name = Path(__file__).parent / file_name
spec = importlib.util.spec_from_file_location('module', module_name)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


@pytest.mark.parametrize(('park', 'routes', 'answer'), [
    (["SOO","OOO","OOO"], ["E 2","S 2","W 1"], [2,1]),
    (["SOO","OXX","OOO"], ["E 2","S 2","W 1"], [0,1]),
    (["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"], [0,0])
])
def test_solution(park, routes, answer):
    assert module.solution(park, routes) == answer
