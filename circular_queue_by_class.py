# 원형 큐
# 배열의 끝 인덱스 -> 첫 인덱스 연결 : %(배열의 길이) 를 이용 인덱스를 지정
# enQueue-> 삽입(push에서 변경), deQueue -> 추출(pop에서 변경)

import sys

class Queue:
    def __init__(self, n):
        self.queue_list = [None for _ in range(n//2+1)]
        self.len = len(self.queue_list)
        self.first_idx = 0
        self.end_idx = 0

    def size(self):
        return (self.end_idx - self.first_idx)%self.len

    def enQueue(self, item):
        if self.is_full():
            return -1
        self.queue_list[self.end_idx % self.len] = item
        self.end_idx += 1
        # print(self.queue_list)

    def deQueue(self):
        if not self.size():
            return -1
        temp = self.queue_list[self.first_idx % self.len]
        self.queue_list[self.first_idx % self.len] = None
        self.first_idx += 1
        # print(self.queue_list)
        return temp

    def front(self):
        if not self.size():
            return -1
        return self.queue_list[self.first_idx  % self.len]

    def back(self):
        if not self.size():
            return -1
        return self.queue_list[(self.end_idx - 1)%self.len]

    def is_empty(self):
        if not self.size():
            return 1
        return 0

    def is_full(self):
        return self.len == self.size()


def run_cmd_with_queue(queue, command):
    if command[0] == 'enQueue':
        queue.enQueue(command[1])
    elif command[0] == 'deQueue':
        print(queue.deQueue())
    elif command[0] == 'size':
        print(queue.size())
    elif command[0] == 'empty':
        print(queue.is_empty())
    elif command[0] == 'front':
        print(queue.front())
    elif command[0] == 'back':
        print(queue.back())


n = int(input())
queue_a = Queue(n)

for _ in range(n):
    command = sys.stdin.readline().split()
    run_cmd_with_queue(queue_a, command)