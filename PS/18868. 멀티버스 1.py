# https://www.acmicpc.net/problem/18868

from itertools import combinations


m, n = map(int, input().split())
space_list = []
n_list = list(range(n))

for _ in range(m):
    space_list.append(list(map(int, input().split())))

space_list_comb = list(combinations(space_list, 2))
cnt = 0

for i in space_list_comb:
    for j in n_list:
        flag = 1
        for k in n_list:
            if i[0][j] < i[0][k] and i[1][j] < i[1][k]:
                continue
            elif i[0][j] > i[0][k] and i[1][j] > i[1][k]:
                continue
            elif i[0][j] == i[0][k] and i[1][j] == i[1][k]:
                continue
            else:
                flag = 0
                break
        if flag == 0:
            break
    else:
        cnt += 1

print(cnt)
