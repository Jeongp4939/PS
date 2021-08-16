# https://www.acmicpc.net/problem/18512
# 두 학생 A와 B가 일직선상의 트랙에서 같은 방향으로 멀리뛰기를 하고 있다.
# A는 한 번에 X 미터를, B는 한 번에 Y 미터를 뛴다.
# 두 학생의 시작 지점과 X, Y에 대한 정보가 주어졌을 때,
# 두 학생이 공통적으로 지나게 되는 지점 중에서 시작 지점으로부터 가장 가까운 지점을 찾는 프로그램을 작성하시오.
#
# 예를 들어 한 번에 10미터를 뛰는 A는 30의 지점에서 멀리뛰기를 시작하고,
# 한 번에 12미터를 뛰는 B는 8의 지점에서 시작한다고 가정하자.
# A가 5번의 멀리뛰기를 하고, B가 6번의 멀리뛰기를 하면
# 두 사람은 80의 지점을 공통으로 지나게 되며, 이는 두 학생의 시작 지점에서 가장 가까운 지점이다.
# ------- 입력 --------
# 첫째 줄에 두 사람이 한 번에 멀리뛰기를 하는 거리 X, Y와 시작 지점의 위치 값
# P1, P2가 각각 공백을 기준으로 구분되어 자연수로 주어진다. (1 ≤ X, Y, P1, P2 ≤ 100)
# ------- 출력 --------
# 첫째 줄에 두 학생이 공통적으로 지나는 지점 중에서 가장 가까운 지점을 출력한다.
# 단, 두 학생이 공통적으로 지나는 지점이 없다면 -1을 출력한다.

# x, y, p_x, p_y = map(int, input().split())        # x, y : 뛰는 거리, p_x, p_y : 시작 지점
#
# if x == y and (p_x % x) != (p_y % y):
#     print(-1)
#     exit()
# while True:
#     if p_x > p_y:                                 # p_x 가 p_y보다 클 때 p_y에 y를 더해줌
#         p_y += y
#     elif p_x < p_y:                               # p_y 가 p_x보다 클 때 p_x에 x를 더해줌
#         p_x += x
#
#     if p_x == p_y:                                # 두 수가 같으면 출력하고 while 종료
#         print(p_x)
#         break

#============================= 시간 초과 =====================================
#
# x, y, p_x, p_y = map(int, input().split())        # x, y : 뛰는 거리, p_x, p_y : 시작 지점
# x_list = []
# y_list = []
#
# if x == y and (p_x % x) != (p_y % y):
#     print(-1)
#     exit()
#
# for i in range(100000):
#     x_list.append(p_x + i * x)
#
# for i in range(100000):
#     y_list.append(p_y + i * y)
#
# for i in x_list:
#     if i in y_list:
#         print(i)
#         break

# ============================================================================
#
#
# x,y,p1,p2 = map(int,input().split())
# runx = set(range(p1, 10**6, x))
# runy = set(range(p2, 10**6, y))
#
# print(10**6)
# R = runx&runy
# print(min(R) if R else -1)


#=========================== 인터넷 검색 ==========================================