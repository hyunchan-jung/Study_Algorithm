def solution(text, anagram, sw):
    if sw:
        answer = [''] * len(text)
        for i, j in zip(anagram, text):
            answer[i] = j
    else:
        answer = [text[i] for i in anagram]

    return ''.join(answer)
