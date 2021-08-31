from collections import deque

n = int(input())

queue = deque(range(1, n+1))

while len(queue) > 1:
    queue.popleft()                 # 한장을 버리고
    queue.append(queue.popleft())   # 한장을 뒤로 보냄

print(queue[0])
# if len(queue) == 1:   # while문에서 검사를 해서 조건을 줄 필요 없음
#     print(queue[0])