# https://www.acmicpc.net/problem/2630
#
# N = int(input())
# arr = []
#
# for _ in range(N):
#     arr.append(list(map(int, input().split())))
#
# white = 0   # 하얀색 색종이의 개수
# blue = 0    # 파란색 색종이의 개수
#
# # a: 세로, b: 가로, N: 크기(size)
# def colored_paper(a, b, N):
#     global white, blue
#     color = arr[a][b]   # color 는 처음으로 들어오는 색상 값
#
#     for i in range(a, a+N):
#         for j in range(b, b+N):
#             if color != arr[i][j]:
#                 colored_paper(a, b, N // 2)    # 1
#                 colored_paper(a, b + N // 2, N // 2)    # 2
#                 colored_paper(a + N // 2, b, N // 2)    # 3
#                 colored_paper(a + N // 2, b + N // 2, N // 2)    # 4
#                 return
#
#     if color == 0:
#         white += 1
#     else:
#         blue += 1
#
# colored_paper(0, 0, N)
# print(white)
# print(blue)


# ==================================================
# ==================================================
# recursion

# 8
# 1 1 0 0 0 0 1 1
# 1 1 0 0 0 0 1 1
# 0 0 0 0 1 1 0 0
# 0 0 0 0 1 1 0 0
# 1 0 0 0 1 1 1 1
# 0 1 0 0 1 1 1 1
# 0 0 1 1 1 1 1 1
# 0 0 1 1 1 1 1 1

def check_same_color(start_y, start_x, length, paper_map):
    for y in range(start_y, start_y + length):
        for x in range(start_x, start_x + length):
            if paper_map[y][x] != paper_map[start_y][start_x]:
                return False

    return True


def split_paper(start_y, start_x, length, paper_map):
    if check_same_color(start_y, start_x, length, paper_map):
        if paper_map[start_y][start_x] == 0:
            return [1, 0]

        return [0, 1]

    half_length = int(length / 2)
    total_paper_cnt = [0, 0]
    split_locs = [
        [start_y, start_x],
        [start_y, start_x + half_length],
        [start_y + half_length, start_x],
        [start_y + half_length, start_x + half_length]
    ]

    for y, x in split_locs:
        white_cnt, blue_cnt = split_paper(y, x, half_length, paper_map)
        total_paper_cnt[0] += white_cnt
        total_paper_cnt[1] += blue_cnt

    # split_paper(start_y, start_x, half_length, paper_map)
    # split_paper(start_y, start_x+half_length, half_length, paper_map)
    # split_paper(start_y+half_length, start_x, half_length, paper_map)
    # split_paper(start_y+half_length, start_x+half_length, half_length, paper_map)

    return total_paper_cnt


n = int(input())
paper_map = []
white_paper_cnt = 0

for _ in range(n):
    paper_map.append(list(map(int, input().split())))

for num in split_paper(0, 0, n, paper_map):
    print(num)