# 첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
# 왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.
# 오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.

# 첫째 줄에 큐의 크기 N과 뽑아내려고 하는 수의 개수 M이 주어진다. N은 50보다 작거나 같은 자연수이고,
# M은 N보다 작거나 같은 자연수이다. 둘째 줄에는 지민이가 뽑아내려고 하는 수의 위치가 순서대로 주어진다.
# 위치는 1보다 크거나 같고, N보다 작거나 같은 자연수이다.


from collections import deque

n, m = map(int, input().split())
cmd_list = list(map(int, input().split()))

queue = deque(range(1,n+1))
cnt = 0
for i in range(m):
    while True:
        if queue[0] == cmd_list[i]:
            queue.popleft()
            break                                # while 탈출
        else:
            if cmd_list[i] <= len(queue)//2:
                queue.append(queue.popleft())    # 왼쪽 회전
                cnt+=1
            else:
                queue.appendleft(queue.pop())    # 오른쪽 회전
                cnt+=1

print(cnt)


#==============================================================
#
# from collections import deque
#
# n, m = map(int, input().split())
# cmd_list = list(map(int, input().split()))
#
# queue = deque(range(1,n+1))
# cnt = 0
#
# for i in cmd_list:
#     while True:
#         if queue[0] == i:
#             queue.popleft()
#             break
#         else:
#             if queue.index(i) <= len(queue)//2:
#                 queue.rotate(-1)    # 왼쪽 회전
#                 cnt += 1
#             else:
#                 queue.rotate(1)     # 오른쪽 회전
#                 cnt += 1
# print(cnt)