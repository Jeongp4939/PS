# n = 10
# n2 = n
# print(id(n))
# print(id(n2))
# n+=5
# print(n, n2)
# print(id(n))
# print(id(n2))
#
# li=[1,2,3,[1,2]]
# li2 = li.copy()
#
# print(id(li))
# print(id(li2))
# li[3].append(1)
# print(li, li2)
#
# def func(*args, **kwargs):
#     print(args)
#
# func("testing", "optional", test="arguments", name="value")
#
# tv_size, height_ratio, width_ratio = map(int, input().split())
#
# height = ((tv_size**2 / (height_ratio**2+width_ratio**2)) * height_ratio**2)**(1/2)
# width = ((tv_size**2 / (height_ratio**2+width_ratio**2)) * width_ratio**2)**(1/2)
#
# print(int(height), int(width))
#
#
# a = input()
# b = input()
# result=[]
#
# for i in range(len(a)):
#     result.append(int(''.join(a))*int(b[-i-1]))
#
# for j in range(len(a)):
#     print(result[j])
# print(int(''.join(a))*int(''.join(b)))

#
# x = int(input())
# y = int(input())
#
# if x>0:
#     if y>0:
#         print(1)
#     else:
#         print(4)
# else:
#     if y>0:
#         print(2)
#     else:
#         print(3)

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# res = []
# for _ in range(n):
#     x, y = map(int, input().split())
#     res.append(x+y)
# for i in res:
#     print(i)

#
# n = int(input())
#
# for i in range(n):
#     x, y = map(int, input().split())
#     print(r'Case #{}: {} + {} = {}'.format(i+1, x, y, x+y))

#
# n= int(input())
# for _ in range(n):
#     score = list(map(int, input().split()))
#     avg_score = sum(score[1:])/score[0]
#
#     cnt = 0
#
#     for i in range(1, score[0]+1):
#         if score[i] > avg_score:
#             cnt += 1
#     result = cnt / score[0] * 100
#     print(f"{result:.3f}%")


#
# n ,m, k = map(int,input().split())
#
# li = list(map(int, input().split()))
# li.sort(reverse=True)
# # sum = 0
# # cnt = 1
# # for _ in range(m):
# #     for _ in range(k):
# #         if cnt < m:
# #             sum += li[0]
# #             cnt += 1
# #     if cnt < m:
# #         sum += li[1]
# #         cnt += 1
# # print(sum)
#
# print(li[1]*(m//(k+1))+li[0]*(m-(m//(k+1))))
#
# n = 100
# cnt = 0
# for i in range(2,100):

#
# n, m, k = map(int, input().split())
# a = list(map(int, input().split()))
# a.sort(reverse=True)
# # if m % k == 0:
# print(a[0]*(m-(m//(k+1))) + a[1]*(m//(k+1)))
# # elif k <= m:
# #     print(a[0]*k*(m//k) + a[1]*(m%k))


# table = 100
# 최소 2명, 최대 10명
# remain = 100 - x; remain -= x
#
# memo = {}       #중복된 연산이 필요한 경우 메모화 사용시 효율성 증가
# max_p = 10
# least = 2
# total = 100
# def table_setting(remain, sit):
#     key = str((remain, sit))
#     if key in memo:
#         return memo[key]
#     if remain < 0:      #잘못된 경우
#         return 0
#     if remain == 0:     #유효한 값
#         return 1
#     #재귀
#     count = 0
#     for i in range(sit, max_p + 1):
#         count += table_setting(remain -i, i)
#     memo[key] = count
#     return count
#
# print( table_setting(total, least) )
#

from collections import deque

n = int(input())

queue = deque(range(1, n+1))

while len(queue) > 1:

    queue.popleft()
    queue.append(queue.popleft())

if len(queue) == 1:
    print(queue[0])