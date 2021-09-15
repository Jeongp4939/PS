# https://www.acmicpc.net/problem/1182

from itertools import combinations

n, s = map(int, input().split())
arr = list(map(int, input().split()))
comb_list=[]

cnt = 0

for i in range(1, len(arr)+1):
    comb_list.append(list(combinations(arr, i)))
for i in comb_list:
    for j in range(len(i)):
        if sum(i[j]) == s:
            cnt += 1
print(cnt)