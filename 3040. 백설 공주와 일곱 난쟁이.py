# 어느 날 광산에서 아홉 난쟁이가 돌아왔다.
# 백설공주는 이런 일이 생길 것을 대비해서,
# 사실 백설 공주는 일곱 난쟁이의 모자에 쓰여 있는 숫자의 합이 100이 되도록 적어 놓았다.
# 아홉 난쟁이의 모자에 쓰여 있는 수가 주어졌을 때, 일곱 난쟁이를 찾는 프로그램을 작성하시오.
# (아홉 개의 수 중 합이 100이 되는 일곱 개의 수를 찾으시오)

# 9 C 7 = 36개의 합

dwarf = []
dwarf_hat_sum=[]
cnt = 0
for _ in range(9):
    dwarf.append(int(input()))

for i in range(len(dwarf)):
    for j in range(i+1, len(dwarf)):
        if sum(dwarf[:i]) + sum(dwarf[i + 1:j]) + sum(dwarf[j + 1:]) == 100:    # 9 개중 2개를 제외한(7개)의 합 검사
            dwarf_hat_sum = dwarf[:i] + dwarf[i + 1:j]+ dwarf[j+1:]
for i in dwarf_hat_sum:
    print(i)