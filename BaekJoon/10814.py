from sys import stdin

age_name_list = sorted([stdin.readline().strip().split(' ') for _ in range(int(input()))], key=lambda x: int(x[0]))
for age, name in age_name_list:
    print(age, name)
