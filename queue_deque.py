from collections import deque

def run_cmd_with_queue(queue, command):
    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        if not len(queue):
            print(-1)
        else:
            print(queue.popleft())
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        print(int(not len(queue)))
    elif command[0] == 'front':
        if not len(queue):
            print(-1)
        else:
            print(queue[0])
    elif command[0] == 'back':
        if not len(queue):
            print(-1)
        else:
            print(queue[-1])

queue_obj = deque()
n = int(input())
for _ in range(n):
    cmd = input().split()
    run_cmd_with_queue(queue_obj, cmd)