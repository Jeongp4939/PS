# https://www.acmicpc.net/problem/1913
# 홀수인 자연수 N이 주어지면, 다음과 같이 1부터 N^2까지의 자연수를 달팽이 모양으로 N×N의 표에 채울 수 있다.
# N이 주어졌을 때, 이러한 표를 출력하는 프로그램을 작성하시오.
# 또한 N2 이하의 자연수가 하나 주어졌을 때, 그 좌표도 함께 출력하시오.
# 예를 들어 N=5인 경우 6의 좌표는 (4,3)이다.
#
# 입력
# 첫째 줄에 홀수인 자연수 N(3 ≤ N ≤ 999)이 주어진다.
# 둘째 줄에는 위치를 찾고자 하는 N2 이하의 자연수가 하나 주어진다.
#
# 출력
# N개의 줄에 걸쳐 표를 출력한다. 각 줄에 N개의 자연수를 한 칸씩 띄어서 출력하면 되며,
# 자릿수를 맞출 필요가 없다. N+1번째 줄에는 입력받은 자연수의 좌표를 나타내는 두 정수를 한 칸 띄어서 출력한다.

# 중앙값(1) 의 좌표 = (N//2, N//2)

# 방향을 바꿔가며 +1(1부터 시작) or -1(끝값부터 시작)

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

N = int(input())
n_index = int(input())

graph = [[0 for _ in range(N)] for _ in range(N)]

cnt = 1
repeat = 2
length = 1

x, y = N//2, N//2
i = 0

graph[x][y] = cnt
loc = [N//2 + 1, N//2 + 1]
while cnt < N**2:
    for _ in range(length):
        x, y = x + dx[i], y + dy[i]
        cnt += 1
        if cnt == n_index:
            loc = [x+1, y+1]
        if cnt > N**2:
            break
        graph[x][y] = cnt
    else:
        i = (i+1)%4
        repeat -= 1
    if repeat == 0:
        length += 1
        repeat = 2

for j in graph:
    print(*j)
print(*loc)