# n = int(input())
# li = []
# for _ in range(n):
#     li.append(input())
#
# for j in range(len(li)-1):
#     for i in range(len(li)-1-j):
#         if li[i][:li[i].index(' ')] > li[i+1][:li[i+1].index(' ')]:
#             li[i], li[i+1] = li[i+1], li[i]
# print(li)
#====================== 시간초과 ==============================
import sys
input = sys.stdin.readline

n = int(input())
member = []
for _ in range(n):
    member.append(input().split())
member.sort(key=lambda x: int(x[0]))
for mem in member:
    print(mem[0], mem[1])
