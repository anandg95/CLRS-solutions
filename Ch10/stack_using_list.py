"Implementing stack using python lists"


class UnderFlowError(Exception):
    pass


class OverFlowError(Exception):
    pass


class Stack:
    def __init__(self, max_size):
        self.s = []
        self.top = -1
        self.max_size = max_size

    @property
    def stack_empty(self):
        return self.top == -1

    def push(self, x):
        if self.top == self.max_size - 1:
            raise OverFlowError
        self.top += 1
        self.s.append(x)

    def pop(self):
        if self.stack_empty:
            raise UnderFlowError
        self.top -= 1
        return self.s.pop()

