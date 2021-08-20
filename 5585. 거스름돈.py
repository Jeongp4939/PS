# https://www.acmicpc.net/problem/5585

# 타로는 자주 JOI잡화점에서 물건을 산다.
# JOI잡화점에는 잔돈으로 500엔, 100엔, 50엔, 10엔, 5엔, 1엔이 충분히 있고,
# 언제나 거스름돈 개수가 가장 적게 잔돈을 준다.

# 타로가 JOI잡화점에서 물건을 사고 카운터에서 1000엔 지폐를 한장 냈을 때,
# 받을 잔돈에 포함된 잔돈의 개수를 구하는 프로그램을 작성하시오.

# 입력은 한줄로 이루어져있고, 타로가 지불할 돈(1 이상 1000미만의 정수) 1개가 쓰여져있다.
# 제출할 출력 파일은 1행으로만 되어 있다. 잔돈에 포함된 매수를 출력하시오

# price = int(input())
# remain = 1000 - price
# cnt = 0
#
# while remain > 0:
#     if remain >= 500:
#         remain -= 500
#         cnt += 1
#     elif remain >= 100:
#         remain -= 100
#         cnt += 1
#     elif remain >= 50:
#         remain -= 50
#         cnt += 1
#     elif remain >= 10:
#         remain -= 10
#         cnt += 1
#     elif remain >= 5:
#         remain -= 5
#         cnt += 1
#     else:
#         remain -= 1
#         cnt += 1
# print(cnt)

#=============================================
# 1)

# n = 1000 - int(input())
# coin_list = [500, 100, 50, 10, 5, 1]
# cnt = 0
# for coin in coin_list:
#     cnt += n//coin
#     n %= coin
#
# print(cnt)

#=============================================
# 2)

def calc_coin(charge_money, i, coins_list):
    if i == len(coins_list):
        return 0

    return charge_money // coins_list[i] + calc_coin(charge_money % coins_list[i], i+1, coins_list)

coins_list = [500, 100, 50, 10, 5, 1]
charge_money = 1000 - int(input())

print(calc_coin(charge_money, 0, coins_list))