# def solution():
#     noise = list(map(int, input().split()))
#     N = int(input())
#     n = 0
#     isGood = []
#     while n < N:
#         shade = list(map(int, input().split()))
#         if ((noise[0]-shade[0])**2+(noise[1]-shade[1])**2) < noise[2]**2:
#             isGood.append('noisy')
#         else:
#             isGood.append('silent')
#         n += 1
#     for i in isGood:
#         print(i)
# solution()

a, b, R = map(int, input().split())  # split() 안에 아무것도 안들어가면 공백문자가 있을시 모두 구분
N = int(input())
n = 0
while n < N:
    x, y = map(int, input().split())
    if ((x - a) ** 2 + (y - b) ** 2) < R ** 2:
        print('noisy')
    else:
        print('silent')
    n += 1

#
# def check_sound_status(a,b,r,x,y):
#     if (x-a)**2 + (y-b)**2 >= r**2:
#         return "silent"
#     return "noisy"
#
# a, b, r = map(int, input().split())
# n = int(input())
#
# for _ in range(n):
#     x, y = map(int, input().split())
#     print(check_sound_status(a,b,r,x,y))
#