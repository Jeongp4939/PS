# https://www.acmicpc.net/problem/2745
#
# B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오.
#
# 10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.
#
# A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

n, b = input().split()                              # n과 진법의 기준이 되는 b를 입력 받음
a = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'          # 0~9,A~Z : 0~35 index를 가지는 문자열
res = 0                                               # n의 10진수 표현이 될 수

for i in range(len(n)):
    res+= a.index(n[i]) * (int(b) ** (len(n) - 1 - i))      # a에서 n의 i번째 문자의 인덱스 * b(진법) * 10의 (n[i]의 자리수-1) 제곱
print(res)                                            # 결과 값 출력


