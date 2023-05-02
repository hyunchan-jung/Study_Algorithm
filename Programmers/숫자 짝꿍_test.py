import time
import random
import importlib.util
from pathlib import Path

import pytest

module_name = Path(__file__).parent / "숫자 짝꿍.py"
spec = importlib.util.spec_from_file_location('module', module_name)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


@pytest.mark.parametrize(('X', 'Y', 'answer'), [
    ('100', '2345', '-1'),
    ('100', '203045', '0'),
    ('100', '123450', '10'),
    ('12321', '42531', '321'),
    ('5525', '1255', '552'),
])
def test_solution(X, Y, answer):
    assert module.solution(X, Y) == answer


def test_timeout():
    x = ''.join([str(random.randint(0, 9)) for _ in range(3000000)])
    y = ''.join([str(random.randint(0, 9)) for _ in range(3000000)])

    tic = time.time()
    module.solution(x, y)
    toc = time.time()

    assert toc - tic < 1
