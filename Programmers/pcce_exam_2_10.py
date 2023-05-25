def solution(n, board, position):
    answer = []
    for a, b in position:
        cnt = sum(map(sum, [i[0 if b == 0 else b-1:b+2] for i in board[0 if a == 0 else a-1:a+2]])) - board[a][b]
        if board[a][b]:
            answer.append(0 if cnt <= 2 or cnt >= 5 else 1)
        else:
            answer.append(1 if cnt == 2 else 0)
    return answer


assert solution(2, [[0, 1, 0],
                    [1, 1, 1],
                    [1, 1, 0]], [[1, 1]]) == [0]
