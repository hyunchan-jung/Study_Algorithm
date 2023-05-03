from typing import List


def solution(babbling: List[str]) -> int:
    words = ['aya', 'ye', 'woo', 'ma']
    answer = 0

    for babble in babbling:
        for word in words:
            if word * 2 not in babble:
                babble = babble.replace(word, ' ')

        if babble.strip() == '':
            answer += 1

    return answer
