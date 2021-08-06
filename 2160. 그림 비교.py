# N(2≤N≤50)개의 그림이 있다.
# 각각의 그림은 5×7의 크기이고, 두 가지 색으로 되어 있다.
# 이때 두 가지의 색을 각각 ‘X’와 ‘.’으로 표현하기로 하자.
# 이러한 그림들이 주어졌을 때, 가장 비슷한 두 개의 그림을 찾아내는 프로그램을 작성하시오.
# 두 개의 그림에서 다른 칸의 개수가 가장 적을 때, 두 개의 그림이 가장 비슷하다고 하자.
# 첫째 줄에 N이 주어진다. 다음 5×N개의 줄에 7개의 문자로 각각의 그림이 주어진다.
# 첫째 줄에 가장 비슷한 두 그림의 번호를 출력한다. 그림의 번호는 입력되는 순서대로 1, 2, …, N이다.
# 번호를 출력할 때에는 작은 것을 먼저 출력한다. 입력은 항상 답이 한 가지인 경우만 주어진다.

# 2차원 리스트를 1차원 리스트로 펼친 후 비교
# li  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# li2 = [1, 3, 3, 5, 6, 6, 8, 9, 10, 10]
# li3 = [li[i]==li2[i] for i in range(len(li))]
# print(sum(li3))   # 같은 위치에 있는 원소가 같은 정도를 숫자로 표현해줌

import sys
input = sys.stdin.readline
n = int(input())
li=[]
check={}
for _ in range(n):      # 입력을 받아서 하나의 리스트로 받아줌
    color = ''
    for i in range(5):
        color += input().strip()
    li.append(list(color))
for i in range(n):
    for j in range(i+1, n):
        check[(i,j)] = sum([li[i][k]==li[j][k] for k in range(len(li[i]))])
        # 선택 된 두개의 리스트의 인덱스와 원소가 같은 수를 세어서 key 와 value 로 받아줌
print(sorted(check.items(),key=lambda x:x[1], reverse=True))
answer = sorted(check.items(),key=lambda x:x[1], reverse=True)[0][0]
print(answer[0]+1, answer[1]+1)     # 가장 비슷했던 두 리스트의 번호를 출력