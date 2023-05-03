import time
import importlib.util
from pathlib import Path

import pytest

module_name = Path(__file__).parent / "옹알이 (2).py"
spec = importlib.util.spec_from_file_location('module', module_name)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


@pytest.mark.parametrize(('babbling', 'answer'), [
    (['aya', 'yee', 'u', 'maa'], 1),
    (['ayaye', 'uuu', 'yeye', 'yemawoo', 'ayaayaa'], 2),
    (['mayaa'], 0),
])
def test_solution(babbling, answer):
    assert module.solution(babbling) == answer
