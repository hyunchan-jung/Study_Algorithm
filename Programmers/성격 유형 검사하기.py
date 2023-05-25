def solution(survey, choices):
    scores = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

    for i in range(len(survey)):
        if choices[i] < 4:
            scores[survey[i][0]] += 4 - choices[i]
        elif choices[i] > 4:
            scores[survey[i][1]] += choices[i] - 4

    result = ''
    pairs = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]
    for pair in pairs:
        if scores[pair[0]] > scores[pair[1]]:
            result += pair[0]
        elif scores[pair[0]] < scores[pair[1]]:
            result += pair[1]
        else:
            result += min(pair[0], pair[1])

    return result
