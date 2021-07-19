import sys
input = sys.stdin.readline

class Stack:
    def __init__(self, n):
        self.stack_list = [None for _ in range(n)]
        self.stack_size = 0
    def size(self):
        return self.stack_size
    def empty(self):
        if self.stack_size == 0:
            return 1
        return 0
    def pop(self):
        if self.stack_size == 0:
            return -1
        self.stack_size -= 1
        return self.stack_list[self.stack_size + 1]
    def top(self):
        if self.stack_size == 0:
            return -1
        return self.stack_list[self.stack_size]
    def push(self, item):
        self.stack_size += 1
        self.stack_list[self.stack_size] = item

def run_cmd_with_stack(Stack, command):
    if command[0] == 'push':
        stack_a.push(command[1])
    elif command[0] == 'pop':
        print(stack_a.pop())
    elif command[0] == 'size':
        print(stack_a.size())
    elif command[0] == 'empty':
        print(stack_a.empty())
    elif command[0] == 'top':
        print(stack_a.top())
n=int(input())

stack_a = Stack(n)

for _ in range(n):
    command = input().split()
    run_cmd_with_stack(stack_a, command)
