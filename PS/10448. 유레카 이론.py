# https://www.acmicpc.net/problem/10448

# 2 3 4 (n+1)

T = {}

T[1] = 1
for i in range(2, 46):
    T[i] = T[i-1] + i
def is_triangular(n, dic):
    for i in range(1,46):
        n_temp = n - dic[i]
        for j in range(1,46):
            if (n_temp - dic[j]) in T.values():
                return 1
    else:
        return 0
n = int(input())
num = 0
for _ in range(n):
    num = int(input())
    print(is_triangular(num, T))

