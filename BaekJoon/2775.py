for _ in range(int(input())):
    k, n = [int(input()) for _ in range(2)]

    person = list(range(1, n + 1))  # 0층 n호에 사는 사람 수
    for _ in range(k):  # k층 까지 계산 반복
        for i in range(1, n):  # 1호는 계속 1명
            person[i] += person[i - 1]  # n-1호에 사는 사람수를 더함
    print(person[n - 1])
