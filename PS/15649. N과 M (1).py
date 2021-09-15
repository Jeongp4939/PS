# https://www.acmicpc.net/problem/15649

from itertools import permutations

n, m = map(int, input().split())

arr = [i for i in range(1, n+1)]
comb_list = list(permutations(arr,m))

for i in comb_list:
    print(*i)