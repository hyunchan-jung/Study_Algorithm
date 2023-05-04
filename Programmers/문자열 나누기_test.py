import importlib.util
from pathlib import Path

import pytest

test_file_name = '문자열 나누기_test.py'
file_name = test_file_name.replace('_test', '')
module_name = Path(__file__).parent / file_name
spec = importlib.util.spec_from_file_location('module', module_name)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


@pytest.mark.parametrize(('s', 'answer'), [
    ('banana', 3),
    ('abracadabra', 6),
    ('aaabbaccccabba', 3),
])
def test_solution(s, answer):
    assert module.solution(s) == answer


def test_timeout():
    import time
    import random
    from string import ascii_lowercase

    s = ''.join(random.choice(ascii_lowercase) for _ in range(10000))

    tic = time.time()
    module.solution(s)
    toc = time.time()
    exec_time = toc - tic

    assert exec_time < 0.01
