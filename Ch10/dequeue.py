"Double ended queue"
from stack_using_list import OverFlowError, UnderFlowError


class Dequeue:
    def __init__(self, max_size):
        self.head = self.tail = -1
        self.q = [None] * max_size
        self.max_size = max_size

    def head_enqueue(self, x):
        if (self.head == 0 and self.tail == self.max_size - 1) or (
            self.head == self.tail + 1
        ):
            raise OverFlowError
        elif self.head == 0:
            self.head = self.max_size - 1
        elif self.head == -1:
            self.head = self.tail = 0
        else:
            self.head -= 1
        self.q[self.head] = x

    def tail_enqueue(self, x):
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

    def head_dequeue(self):
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

    def tail_dequeue(self):
        if self.tail == -1:
            raise UnderFlowError
        x = self.q[self.tail]
        if self.head == self.tail:
            self.head = self.tail = -1
        elif self.tail == 0:
            self.tail = self.max_size - 1
        else:
            self.tail -= 1
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
