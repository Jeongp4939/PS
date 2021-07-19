# class Queue:
#     def __init__(self, n):
#         self.queue_list = [None for _ in range(n)]
#         self.queue_size = 0
#
#         # self.f_idx = 0
#         # self.b_idx = 0
#
#     def size(self):
#         # self.queue_size = self.b_idx - self.f_idx
#         return self.queue_size
#
#     def empty(self):
#         if not self.queue_size:
#             return 1
#         return 0
#
#     def push(self, item):
#         self.queue_list[self.queue_size] = item
#         self.queue_size += 1
#         # self.b_idx += 1
#         # self.queue_list[self.b_idx] = item
#     def pop(self):
#         if not self.queue_size:
#             return -1
#         self.queue_size -= 1
#
#         # if not self.size():
#         #     return -1
#         # temp = self.queue_list[self.f_idx]
#         # self.f_idx += 1
#         # return temp
#         first = self.queue_list[0]
#         for i in range(len(self.queue_list)-1):
#             self.queue_list[i] = self.queue_list[i+1]
#         return first
#
#     def front(self):
#         if not self.queue_size:
#             return -1
#         # if not self.size():
#         #     return -1
#         return self.queue_list[0]   # self.queue_list[self.f_idx]
#
#     def back(self):
#         if not self.queue_size:
#             return -1
#         # if not self.size():
#         #     return -1
#         return self.queue_list[self.queue_size-1]
#         # return self.queue_list[self.b_idx]

import sys

class Queue:
    def __init__(self, n):
        self.queue_list = [None for _ in range(n)]
        self.queue_size = 0

        self.f_idx = 0
        self.b_idx = 0

    def size(self):
        self.queue_size = self.b_idx - self.f_idx
        return self.queue_size

    def empty(self):
        if not self.size():
            return 1
        return 0

    def push(self, item):
        self.queue_list[self.b_idx] = item
        self.b_idx += 1

    def pop(self):
        if not self.size():
            return -1
        temp = self.queue_list[self.f_idx]
        self.f_idx += 1
        return temp

    def front(self):
        if not self.size():
            return -1
        return self.queue_list[self.f_idx]

    def back(self):
        if not self.size():
            return -1
        return self.queue_list[self.b_idx-1]




def run_cmd_with_queue(queue, command):
    if command[0] == 'push':
        queue.push(command[1])
    elif command[0] == 'pop':
        print(queue.pop())
    elif command[0] == 'size':
        print(queue.size())
    elif command[0] == 'empty':
        print(queue.empty())
    elif command[0] == 'front':
        print(queue.front())
    elif command[0] == 'back':
        print(queue.back())


n = int(input())
queue_a = Queue(n)


for _ in range(n):
    command = sys.stdin.readline().split()
    run_cmd_with_queue(queue_a, command)