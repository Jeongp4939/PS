# 첫 번째 줄에는 국가의 수 N(2 ≤ N ≤ 1 000)과 비행기의 종류 M(1 ≤ M ≤ 10 000) 가 주어진다.
# 이후 M개의 줄에 a와 b 쌍들이 입력된다. a와 b를 왕복하는 비행기가 있다는 것을 의미한다. (1 ≤ a, b ≤ n; a ≠ b)
# 주어지는 비행 스케줄은 항상 연결 그래프를 이룬다.

# 테스트 케이스마다 한 줄을 출력한다.
#
# 상근이가 모든 국가를 여행하기 위해 타야 하는 비행기 종류의 최소 개수를 출력한다.

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    lst = []
    for _ in range(m):
        lst.append(list(map(int, input().split())))     #경로 입력
    print(n-1)

#=============================답만 냄========================================

