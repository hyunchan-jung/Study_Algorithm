for _ in range(int(input())):
    n_list = list(map(int, input().split(' ')))[1:]
    print(f'{len([i for i in n_list if i > (sum(n_list) / len(n_list))]) / len(n_list) * 100:.3f}%')
