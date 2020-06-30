from queue_using_list import Queue


class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.primary_queue = Queue(max_size)
        self.helper_queue = Queue(max_size)

    def push(self, x):
        self.primary_queue.enqueue(x)

    def pop(self):
        while self.primary_queue.size > 1:
            self.helper_queue.enqueue(self.primary_queue.dequeue())
        x = self.primary_queue.dequeue()
        self.primary_queue, self.helper_queue = self.helper_queue, self.primary_queue
        return x


s = Stack(4)
s.push(3)
s.push(10)
s.push(34)
s.push(49)
