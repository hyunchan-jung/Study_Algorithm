import importlib.util
from pathlib import Path

import pytest

test_file_name = '달리기 경주_test.py'
file_name = test_file_name.replace('_test', '')
module_name = Path(__file__).parent / file_name
spec = importlib.util.spec_from_file_location('module', module_name)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


@pytest.mark.parametrize(('players', 'callings', 'answer'), [
    (['mumu','soe','poe','kai','mine'], ['kai','kai','mine','mine'], ['mumu','kai','mine','soe','poe']),
])
def test_solution(players, callings, answer):
    assert module.solution(players, callings) == answer


def test_timeout():
    import time
    import random

    players = [str(i).zfill(10) for i in range(50000)]

    def get_callings():
        p = players.copy()
        players_idx = {player: i for i, player in enumerate(p)}
        callings = []
        for _ in range(1000000):
            while True:
                player = random.choice(p)
                if player != p[0]:
                    idx = players_idx[player]
                    callings.append(player)
                    break
            p[idx-1], p[idx] = p[idx], p[idx-1]
            players_idx[p[idx-1]] = idx - 1
            players_idx[p[idx]] = idx

        return callings
    callings = get_callings()

    tic = time.time()
    module.solution(players, callings)
    toc = time.time()
    exec_time = toc - tic

    assert exec_time < 0.4
