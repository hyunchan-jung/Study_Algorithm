def solution(today, terms, privacies):
    answer = []

    year, month, day = today.split('.')
    today = (int(year) * 12 * 28) + (int(month) * 28) + int(day)

    terms = {t[:1] : int(t[2:]) * 28 for t in terms}

    for i, privacy in enumerate(privacies):
        year, month, day = privacy.split('.')
        day, term = day.split()
        p = int(year) * 12 * 28 + (int(month) * 28) + int(day)
        if p + terms[term] <= today:
            answer.append(i + 1)

    return answer
