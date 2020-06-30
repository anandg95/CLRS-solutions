"Queue using python lists. This queue is able to enqueue in mod(max_size) fashion."
from stack_using_list import OverFlowError, UnderFlowError


class Queue:
    def __init__(self, max_size):
        self.head = self.tail = -1
        self.q = [None] * max_size
        self.max_size = max_size

    def enqueue(self, x):
        if (
            self.head == 0 and self.tail == self.max_size - 1
        ) or self.tail + 1 == self.head:
            raise OverFlowError
        if self.head == -1:
            self.head = self.tail = 0
        elif self.tail == self.max_size - 1:
            self.tail = 0
        else:
            self.tail += 1
        self.q[self.tail] = x

    def dequeue(self):
        if self.head == -1:
            raise UnderFlowError
        x = self.q[self.head]
        if self.head == self.tail:
            self.head = self.tail = -1
        elif self.head == self.max_size - 1:
            self.head = 0
        else:
            self.head += 1
        return x

    @property
    def size(self):
        if self.head == -1:
            return 0
        if self.head <= self.tail:
            return self.tail - self.head + 1
        else:
            return self.tail + (self.max_size - self.head)

    def __repr__(self):
        return f"{self.q}, head={self.head}, tail={self.tail}, size={self.size}"

