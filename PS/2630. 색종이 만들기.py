# https://www.acmicpc.net/problem/2630

N = int(input())
arr = []



for _ in range(N):
    arr.append(list(map(int, input().split())))

white = 0   # 하얀색 색종이의 개수
blue = 0    # 파란색 색종이의 개수

# a: 세로, b: 가로, N: 크기(size)
def colored_paper(a, b, N):
    global white, blue
    color = arr[a][b]   # color 는 처음으로 들어오는 색상 값

    for i in range(a, a+N):
        for j in range(b, b+N):
            if color != arr[i][j]:
                colored_paper(a, b, N // 2)    # 1
                colored_paper(a, b + N // 2, N // 2)    # 2
                colored_paper(a + N // 2, b, N // 2)    # 3
                colored_paper(a + N // 2, b + N // 2, N // 2)    # 4
                return

    if color == 0:
        white += 1
    else:
        blue += 1

colored_paper(0, 0, N)
print(white)
print(blue)