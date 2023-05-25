import importlib.util
from pathlib import Path

import pytest

test_file_name = '햄버거 만들기_test.py'
file_name = test_file_name.replace('_test', '')
module_name = Path(__file__).parent / file_name
spec = importlib.util.spec_from_file_location('module', module_name)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


@pytest.mark.parametrize(('ingredient', 'answer'), [
    ([2,1,1,2,3,1,2,3,1], 2),
    ([1,3,2,1,2,1,3,1,2], 0),
])
def test_solution(ingredient, answer):
    assert module.solution(ingredient) == answer


def test_timeout():
    import time
    import random

    ingredient = [random.randint(1, 3) for _ in range(1000000)]

    tic = time.time()
    module.solution(ingredient)
    toc = time.time()
    exec_time = toc - tic

    assert exec_time < 0.3
