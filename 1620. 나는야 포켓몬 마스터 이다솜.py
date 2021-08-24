# https://www.acmicpc.net/problem/1620
import sys
input = sys.stdin.readline

n, cmd_n = map(int, input().split())

poke_dic_num = {}
poke_dic_str = {}
for i in range(1,n+1):
    temp = input().rstrip()
    poke_dic_num[i] = temp
    poke_dic_str[temp] = i

for _ in range(cmd_n):
    cmd = input().rstrip()

    if cmd.isdigit():
        print(poke_dic_num[int(cmd)])
    else:
        print(poke_dic_str[cmd])


