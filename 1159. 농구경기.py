# 백준 1159. 농구 경기

import sys

input = sys.stdin.readline

n = int(input())
name = []
fst_name = []
fst_name_cnt = []
answer = ''

for _ in range(n):
    name.append(input().rstrip())  # \n
for i in range(len(name)):
    name[i] = name[i][0]

fst_name = list(set(name))
fst_name.sort()

for i in fst_name:
    fst_name_cnt.append(name.count(i))

for i in range(len(fst_name_cnt)):
    if fst_name_cnt[i] >= 5:
        answer += fst_name[i]

if not answer:
    print("PREDAJA")
else:
    print(answer)