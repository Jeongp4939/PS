# https://www.acmicpc.net/problem/1158

n, k = map(int, input().split())

arr = [i for i in range(1, n+1)]
answer = []

num = 0     # 제거될 순번

for i in range(n):
    print(arr)
    num += k-1
    if num >= len(arr):
        num %= len(arr)

    answer.append(str(arr.pop(num)))

print("<" + ", ".join(answer)[:] + ">")


# deque rotate