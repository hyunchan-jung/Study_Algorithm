from string import ascii_uppercase


def solution(keymap, targets):
    answer = []

    keymap_dict = {}
    for alp in ascii_uppercase:
        indices = [key.index(alp) + 1 for key in keymap if alp in key]
        if indices:
            keymap_dict[alp] = min(indices)

    for target in targets:
        if any(i not in keymap_dict for i in target):
            answer.append(-1)
        else:
            answer.append(sum([keymap_dict[i] for i in target]))

    return answer
