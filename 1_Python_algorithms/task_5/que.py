
class Queue:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def push(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
    
    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x
    
q = Queue(8)

q.push(1)
print(q.queue)
print(q.size)
q.push(-1)
q.push(0)
q.push(11)
q.push(34)
print(q.queue)
print(q.size)
print(q.size)
q.push(24)
q.push(44)
q.push(54)
print(q.queue)

q.pop()
print(q.queue)
q.push(84)
q.pop()
q.pop()
q.pop()
print(q.queue)

#________________________________
from collections import deque

dq = deque([1,2,3,4,5,6,7,2,3], 9)

dq.append(5)
dq.appendleft(3)
print(dq)