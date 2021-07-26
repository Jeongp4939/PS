# import sys
# input = sys.stdin.readline
#
# n = int(input())      # 입력받을 멤버의 숫자
# li = []
# for _ in range(n):    # n 만큼의 member 를 입력 받아 리스트에 추가
#     li.append(input())
#
# for j in range(len(li)-1):
#     for i in range(len(li)-1-j):
#         if li[i][:li[i].index(' ')] > li[i+1][:li[i+1].index(' ')]:   # ' '공백을 기준으로 앞의 숫자를 비교하여 정렬
#             li[i], li[i+1] = li[i+1], li[i]
# for i in li:
#     print(i)
#====================== 시간초과 ==============================
# import sys
# input = sys.stdin.readline
#
# n = int(input())      # 입력받을 멤버의 숫자
# li = []
# for _ in range(n):    # n 만큼의 member 를 입력 받아 리스트에 추가
#     li.append(input().split())
# for j in range(len(li)-1):
#     for i in range(len(li)-1-j):
#         if li[i][0] > li[i + 1][0]:
#             li[i], li[i+1] = li[i+1], li[i]
# for i in li:
#     print(i[0], i[1])

#================================================================

import sys
input = sys.stdin.readline

n = int(input())
member = []
for _ in range(n):
    member.append(input().split())      # 멤버의 나이와 멤버의 이륾을 리스트로 받아와 리스트에 저장
member.sort(key=lambda x: int(x[0]))    # 멤버 리스트 안의 내용을 나이를 기준으로 정렬
for mem in member:
    print(mem[0], mem[1])               # 나이와 이름을 차례로 출력
