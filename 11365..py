import sys
string =[]
result = []
while True:
    string.append(sys.stdin.readline().rstrip())
    if string[len(string)-1] == 'END':
        break
for i in string[:-1]:
    result.append(''.join(list(reversed(i))))
for i in result:
    print(i)