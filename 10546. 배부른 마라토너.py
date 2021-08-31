n = int(input())
join_dict = dict()
finish_dict = dict()

for _ in range(n):
    name = input()
    if name in join_dict:
        join_dict[name] += 1
    else:
        join_dict[name] = 1
for _ in range(n-1):
    name=input()
    if name in finish_dict:
        finish_dict[name] += 1
    else:
        finish_dict[name] = 1
for i in join_dict.keys():
    if i not in finish_dict:
        print(i)
        break
    elif join_dict[i] != finish_dict[i]:
            print(i)
            break


