# https://www.acmicpc.net/problem/2018

n = int(input())
cnt = 1     # 자기자신은 포함하므로

li = [i for i in range(1,n+1)]

# 1 ~ (n//2 + 1)