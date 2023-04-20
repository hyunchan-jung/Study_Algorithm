def solution(k, score):
    answer = []
    stack = []
    for i in score:
        stack.append(i)
        stack.sort(reverse=True)
        if len(stack) > k:
            stack.pop()
        answer.append(stack[-1])

    return answer


assert solution(3, [10, 100, 20, 150, 1, 100, 200]) == [10, 10, 10, 20, 20, 100, 100]
