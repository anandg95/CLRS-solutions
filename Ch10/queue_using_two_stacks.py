from stack_using_list import Stack


class Queue:
    def __init__(self, max_size):
        self.primary_stack = Stack(max_size)
        self.helper_stack = Stack(max_size)
        self.max_size = max_size

    def enqueue(self, x):
        # we will make enqueue O(1)
        self.primary_stack.push(x)

    def dequeue(self):
        """pop is heavy:
        - if helper is empty, push all elements from primary to helper.
        - pop helper
        """
        if self.helper_stack.top == -1:
            while not self.primary_stack.stack_empty:
                self.helper_stack.push(self.primary_stack.pop())
        return self.helper_stack.pop()


q = Queue(5)
q.enqueue(10)
q.enqueue(100)
q.enqueue(500)
q.enqueue(675)
q.enqueue(985)
