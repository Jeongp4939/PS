class Stack:
    def __init__(self):
        self.stack_li = [0 for _ in range(10000)]
        self.cnt = 0
    def size(self):
        return self.cnt
    def empty(self):
        if self.cnt == 0:
            return 1
        return 0
    def pop(self):
        if self.cnt == 0:
            return -1
        self.cnt -= 1
        return self.stack_li[self.cnt + 1]
    def top(self):
        if self.cnt == 0:
            return -1
        return self.stack_li[self.cnt]
    def push(self, item):
        self.cnt += 1
        self.stack_li[self.cnt] = item

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

stack_a = Stack()

n=int(input())

for _ in range(n):
    command = input().split(" ")
    run_cmd_with_stack(stack_a, command)
