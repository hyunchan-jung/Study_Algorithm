import importlib.util
from pathlib import Path

import pytest

test_file_name = '최댓값과 최솟값_test.py'
file_name = test_file_name.replace('_test', '')
module_name = Path(__file__).parent / file_name
spec = importlib.util.spec_from_file_location('module', module_name)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


@pytest.mark.parametrize(('s', 'answer'), [
    ("1 2 3 4", "1 4"),
    ("-1 -2 -3 -4", "-4 -1"),
    ("-1 -1", "-1 -1"),
])
def test_solution(s, answer):
    assert module.solution(s) == answer


def test_timeout():
    import time
    import random

    s = ' '.join([str(random.randint(-100000, 100000)) for _ in range(100000)])

    tic = time.time()
    module.solution(s)
    toc = time.time()
    exec_time = toc - tic

    assert exec_time < 0.1
