def process_stack(arr, command):
    if command[0] == 'push':
        arr.append(int(command[1]))
    elif command[0] == 'pop':
        if arr == []:
            print(-1)
        else:
            print(arr.pop(-1))
    elif command[0] == 'size':
        if arr == []:
            print(0)
        else:
            print(arr[-1]+1)
    elif command[0] == 'empty':
        if arr == []:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if arr == []:
            print(-1)
        else:
            item = arr.pop(-1)
            print(item)
            arr.append(item)


n=int(input())
stack=[]

for _ in range(n):
    command = input().split(" ")
    process_stack(stack, command)