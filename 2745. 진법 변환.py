# https://www.acmicpc.net/problem/2745
#
# B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오.
#
# 10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.
#
# A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

#
# n, b = input().split()                              # n과 진법의 기준이 되는 b를 입력 받음
# a = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'          # 0~9,A~Z : 0~35 index를 가지는 문자열
# res = 0                                               # n의 10진수 표현이 될 수
#
# for i in range(len(n)):
#     res+= a.index(n[i]) * (int(b) ** (len(n) - 1 - i))      # a에서 n의 i번째 문자의 인덱스 * b(진법) * 10의 (n[i]의 자리수-1) 제곱
# print(res)                                            # 결과 값 출력
#

#==================== int()를 이용한 변환 =========================

# n, b = input().split()
# print(int(n, int(b)))

#======================== ord() =================================

# n, b = input().split()
# digit = len(n)
# res = 0
# for i in range(digit):
#     res += (ord(n[i])-55)*int(b)**(digit-i-1)
# print(res)

#===============================================================

# def to_decimal(n:list, b, res):
#     if not len(n):
#         return res
#     res += (ord(n[0])-55) * int(b) ** (len(n)-1)
#     n.pop(0)
#     return to_decimal(n, b, res)
#
# n, b = input().split()
# n = list(n)
# digit = len(n)
# res = 0
#
# print(to_decimal(n, b, res))

#=================== 강사님 코드 ===============================

# ZZZZZ 36

# 0: 36^4,
# 1: 36^3,
# 2: 36^2,
# 3: 36^1,
# 4: 36^0

# n, b = input().split()
# decimal_result = 0
#
# # char_dict = {'0': 0, '1': 1, ..., '9': 9, 'A': 10, 'B': 11, ... 'Z': 35}
# # char_map_str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#
# for i in range(len(n)):
#     pow_num = len(n)-1-i
#
#     if n[i].isnumeric():
#         num_val = int(n[i])
#     else:
#         num_val = (ord(n[i]) - ord('A') + 10)
#
#     decimal_result += int(b) ** pow_num * num_val
#
#     # decimal_result += int(b) ** pow_num * char_dict[n[i]]
#     # decimal_result += int(b) ** pow_num * char_map_str.index(n[i])
#
# print(decimal_result)
# # print(int(n, int(b)))

#======================== recursion ======================================
# 1)
# def decimal_conv(i, n, b):
#     if 1 == len(n): # 끝
#         return 0
#
#     pow_num = len(n)-1-i
#
#     if n[i].isnumeric():
#         num_val = int(n[i])
#     else:
#         num_val = (ord(n[i]) - ord('A') + 10)
#
#     return decimal_conv(i+1, n, b) + (int(b) ** pow_num) * num_val
#
# n, b = input().split()
#
# print(decimal_conv(0, n, b))

#==========================================================================

# 2)

def decimal_conv_dict(i, n, b, char_dict):
    if 1 == len(n): # 끝
        return 0

    pow_num = len(n)-1-i
    num_val = char_dict[n[i]]

    return decimal_conv_dict(i+1, n, b) + (int(b) ** pow_num) * num_val

def make_char_dict():
    char_dict = {}

    for i in range(36):
        if i < 10:
            char_dict[str(i)] = i
        else:
            # ord('A') => 65
            # chr(65) => 'A'
            # chr(ord('A')) => 'A'

            # i => 10 ~ 35
            # i-10 => 0 ~ 25
            # i-10+ord('A') => ord('A') ~ ord('A') + 25 => ord('A') ~ ord('Z')
            # chr(i-10+ord('A')) => chr(ord('A')) ~ chr(ord('Z')) => 'A' ~ 'Z'

            char_dict[chr(i - 10 + ord('A'))] = i

    return char_dict

n, b = input().split()
print(decimal_conv_dict(0, n, int(b), make_char_dict()))