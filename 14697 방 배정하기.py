# 백준 14697 방 배정하기
# https://www.acmicpc.net/problem/14697
# 방의 정원 A, B, C

# a, b, c, num = map(int, input().split())
# remain = []
# remain2 = []
#
# for i in range((num+1)//c):               # num 에서 가장 큰 수 c의 배수를 뺀 리스트 생성
#     remain.append(num-c*i)
# for i in range(len(remain)):
#     for j in range(remain[i]//b):         # 위의 리스트에서 b의 배수를 뺀 리스트 생성
#         remain2.append(remain[i] - b*j)
# remain2 = list(set(remain2))              # 중복을 제거
# for i in range(len(remain2)):             # a로 나눈 나머지를 리스트로 생성
#     remain2[i] %= a
#
# if 0 in list(set(remain2)):               # a로 나누어 떨어지는 수가 있는지 검사
#     print(1)
# else:
#     print(0)
# =============== 3점 ================
def solution():                             # 모든 구문을 한번에 끝내기 위해 함수로 선언
    a, b, c, num = map(int, input().split())
    remain = []
    remain2 = []

    if num % a == 0:                        # num이 a의 배수라면 바로 정지
        return 1
    for i in range((num)//a):
        remain.append(num-a*i)              # a의 배수가 아닐 때 num에서 a의 배수를 뺀 나머지를 배열로 생성
    remain = list(set(remain))              # 계산을 줄이기 위해 중복 제거
    for i in range(len(remain)):
        for j in range(remain[i]//b):       # remain 내부에 b의 배수가 있다면 1을 반환하고 종료
            if remain[i] % b == 0:          # 없을 시 remain 각 원소에 대하여 b의 배수를 뺀 나머지를 배열로 생성
                return 1
            remain2.append(remain[i] - b*j)
    remain2 = list(set(remain2))            # 중복 제거
    for i in range(len(remain2)):           # remain2 각 원소에 대하여 c로 나눈 나머지로 변경 0이 있을 시 1 반환
        remain2[i] %= c
        if remain2[i] == 0:
            return 1
    return 0                                # 모든 조건을 만족하지 않을 때 0 반환

print(solution())