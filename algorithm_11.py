# 동전

# n, k = map(int,input().split())
# coin_list = [int(input()) for _ in range(n)]
# coin_list.reverse()
# coin_cnt = 0
#
# for coin in coin_list:
#     coin_cnt += k//coin
#     k %= coin
# print(coin_cnt)

#==============================================
# 회의실 배정

n = int(input())
time_list = []

for _ in range(n):
    time_list.append(tuple(map(int, input().split())))
time_list.sort(key=lambda x:(x[1], x[0]))

last_time = 0
cnt=0

for start, end in time_list:
    if start > last_time:
        last_time = end
        cnt += 1

print(cnt)