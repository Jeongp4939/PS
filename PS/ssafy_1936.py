# a, b = input().split()
# a = int(a)
# b = int(b)
#
# if a==1:
#     if b==2:
#         print("B")
#     else:
#         print("A")
# elif a==2:
#     if b==1:
#         print("A")
#     else:
#         print("B")
# else:
#     if b==1:
#         print("B")
#     else:
#         print("A")

# a = int(input())
# sum = 0
# if a > 10:
#     a = str(a)
#     for i in a:
#         sum += int(i)
# else:
#     sum = a
# print(sum)


#
# for i in range(10):
#     tc_num = int(input())
#     test_map = []
#
#     for j in range(100):
#         test_map.append(list(map(int, input().split())))
#
#     # print(test_map)
#     sum_li=[]
#     sum_d1, sum_d2 = 0, 0
#     sum_hor, sum_ver = [], []
#
#     for j in range(100):
#         sum_d1 += test_map[j][j]
#         sum_d2 += test_map[j][-1-j]
#         sum_hor.append(sum(test_map[j]))
#     for j in range(100):
#         sum_v=0
#         for k in range(100):
#             sum_v += test_map[k][j]
#         sum_ver.append(sum_v)
#
#     sum_li.append(max(sum_ver))
#     sum_li.append(max(sum_hor))
#     sum_li.append(sum_d1)
#     sum_li.append(sum_d2)
#
#     print(f'#{tc_num} {max(sum_li)}')
#

# from itertools import combinations
# tc = int(input())
# for test_case in range(1,tc+1):
#     n, k, m = map(int,input().split())
#     n_lists = []
#     result = 0
#
#
#
#     print(f'#{test_case} {result}')

# n, k, m = map(int,input().split())
# lists = list(range(1,1+n,1))
# comb_list = list(combinations(lists,k))
# result = 0
# for i in comb_list:
#     mul = 1
#     for j in range(len(i)):
#         mul *= i[j]
#     result += mul
# # result %= m
# print(result)


# '''
# from datetime import datetime
#
# today = datetime.today()
# print(today.month)
#
#
# from functools import reduce
#
# print(reduce(lambda x,y : x + y, [0, 1, 2, 3, 4]))
#
# print(reduce(lambda x,y : y + x, 'abcde'))
#
# a = {1:0, }
#
# print(type(a)); print(a)
#
#
# colwidth = 51
# rule90 = {'000':'0', '001':'1', '010':'0', '011':'1', '100':'1', '101':'0', '110':'1', '111':'0'}
#
# half = colwidth // 2
# line = '0' * half + '1' + '0' * half
# print(line)
#
# while line[1] == '0':
#     prev = line
#     line = '0' * colwidth
#     for i in range(1, colwidth - 1):
#         line = line[:i] + rule90[prev[i-1:i+2]] + line[i+1:]
#     print(line)
# '''
#
# '''
# def roll_matrix(arr, n):
#     result = [[0 for row in range(n)] for col in range(n)]
#
#     for i in range(n):
#         for j in range(n):
#             result[n - j - 1][i] = arr[i][j]
#
#     return result
#
# tc = int(input())
#
# for testcase in range(tc):
#
#     n = int(input())
#     a = []
#
#     for i in range(n):
#         a.append(list(map(int, input().split())))
#
#     roll_270 = roll_matrix(a, n)
#     roll_180 = roll_matrix(roll_270, n)
#     roll_90 = roll_matrix(roll_180, n)
#     print(f'#{testcase+1}')
#     for i in range(n):
#         temp = ""
#         for j in range(n):
#             temp += str(roll_90[i][j])
#         temp += ' '
#         for j in range(n):
#             temp += str(roll_180[i][j])
#         temp += ' '
#         for j in range(n):
#             temp += str(roll_270[i][j])
#         print(temp)
# '''
#
# '''
# def verification(arr):
#     # 가로 검증
#     for line in arr:
#         for i in range(8):
#             if line[i] in line[i+1:]: return 0
#     # 세로 검증
#     column=[0 for _ in range(9)]
#     for i in range(9):
#         for j in range(9):
#             column[j] = arr[j][i]
#         for n in range(8):
#             if column[n] in column[n+1:]: return 0
#         column=[0 for _ in range(9)]
#     # 9칸 검증
#     box = [0 for _ in range(9)]
#     for i in range(9):
#         for j in range(3):
#             for k in range(3):
#                 box[3*j+k] = arr[(i%3)*3+j][(i%3)*3+k]
#         for b in range(8):
#             if box[b] in box[b+1:]: return 0
#         box = [0 for _ in range(9)]
#     return 1
#
# tc = int(input())
#
# for testcase in range(tc):
#     result = 0
#     puzzle = []
#     for _  in range(9):
#         puzzle.append(list(map(int, input().split())))
#     result = verification(puzzle)
#
#     print(f'#{testcase+1} {result}')
# '''
#
# '''
# tc = int(input())
#
# for testcase in range(tc):
#     n = int(input())
#     print(f'#{testcase+1} {n**2}')
# '''


# 미로 크기는 16x16 (1,1) 시작 (13,13) 도착 이동 거리가 일정하므로 BFS를 이용하면 좋다

move = [(1,0),(-1,0),(0,1),(0,-1)] # 상하좌우 이동 리스트

def boundary(y,x): #경계
    if y<0 or x <0 or y>=16 or x>=16:
        return True
    return False

for _ in range(1,11):
    tc = int(input())
    y, x = 1, 1
    result = 0
    map_list = [list(map(int, list(input()))) for _ in range(16)]

    stack = [(y,x)]
    while stack:
        y, x = stack.pop()
        map_list[y][x] = 1
        for my, mx in move:
            dy = y + my
            dx = x + mx

            if boundary(dy,dx): #벽을 만나면 다른길로
                continue
            if map_list[dy][dx] == 3: #도착
                result = 1
                break
            elif not map_list[dy][dx]:
                stack.append((dy,dx))
        else:
            continue
        break

    print(f'#{tc} {result}')

