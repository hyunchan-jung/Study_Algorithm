import importlib.util
from pathlib import Path

import pytest

test_file_name = '바탕화면 정리_test.py'
file_name = test_file_name.replace('_test', '')
module_name = Path(__file__).parent / file_name
spec = importlib.util.spec_from_file_location('module', module_name)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


@pytest.mark.parametrize(('wallpaper', 'answer'), [
    ([".#...", "..#..", "...#."], [0, 1, 3, 4]),
    (["..........", ".....#....", "......##..", "...##.....", "....#....."], [1, 3, 5, 8]),
    ([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."], [0, 0, 7, 9]),
    (["..", "#."], [1, 0, 2, 1]),
])
def test_solution(wallpaper, answer):
    assert module.solution(wallpaper) == answer


def test_timeout():
    import time
    import random

    wallpaper = [
        ''.join(random.choice('#.') for _ in range(50))
        for _ in range(50)
    ]

    tic = time.time()
    module.solution(wallpaper)
    toc = time.time()
    exec_time = toc - tic

    assert exec_time < 0.1
