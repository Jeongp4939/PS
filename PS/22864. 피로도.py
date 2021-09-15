# https://www.acmicpc.net/problem/22864

a, b, c, m = map(int, input().split()) # 일 -> 피로도 +A, 일 +B  /  휴식 -> 피로도 -C  / max = m
p = 0                                  # 초기 피로도 0

time = 0
work = 0

while time < 24:
    if a > m:
        break

    if p+a < m:
        p += a
        work += b
        time += 1
    else:
        p -= c
        time += 1
print(work)

