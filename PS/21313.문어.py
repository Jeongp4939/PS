# https://www.acmicpc.net/problem/21313
#
# 문어의 수 N(4 ≤ N ≤ 1,000)이 주어진다.
# N마리의 문어들로 만들 수 있는 길이 N의 수열 중 사전순으로 가장 앞서는 것을 출력한다.
#
# 이 때, 수열을 이루는 숫자들을 순서대로 공백으로 구분하여 출력한다.

# 연결의 수 N
# 짝수 일 땐 1,2의 반복
# 홀수 일 땐 전의 수(짝수)의 마지막에 3 한개 추가

n = int(input())
n_list = ''

if n % 2 == 0:
    for i in range(n):
        if i % 2 == 0:
            n_list += '1 '
        else:
            n_list += '2 '
else:
    for i in range(n-1):
        if i % 2 == 0:
            n_list += '1 '
        else:
            n_list += '2 '
    n_list += '3'
print(n_list)