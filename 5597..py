check = []
absence = []
for _ in range(28):
    check.append(int(input()))
for i in range(1, 31):
    if i not in check:
        absence.append(i)
absence.sort()
print(absence[0])
print(absence[1])
