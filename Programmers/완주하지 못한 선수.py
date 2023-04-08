from collections import Counter


def solution(participant, completion):
    participant_cnt = Counter(participant)

    for c in completion:
        participant_cnt[c] -= 1

    for k, v in participant_cnt.items():
        if v != 0:
            return k


assert solution(['leo', 'kiki', 'eden'], ['eden', 'kiki']) == 'leo'
assert solution(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav']) == 'mislav'
