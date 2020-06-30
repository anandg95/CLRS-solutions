from stack_using_list import OverFlowError, UnderFlowError


class Stack:
    def __init__(self, top):
        self.top = top


class TwoStacks:
    def __init__(self, max_size):
        self.s = [None] * max_size
        self.max_size = max_size
        self.P = Stack(-1)  # forward filling
        self.Q = Stack(max_size)  # reverse filling

    def push_P(self, x):
        if self.P.top == self.Q.top - 1 or self.P.top == self.max_size - 1:
            raise OverFlowError
        self.P.top += 1
        self.s[self.P.top] = x

    def push_Q(self, x):
        if self.Q.top == self.P.top + 1 or self.Q.top == 0:
            raise OverFlowError
        self.Q.top -= 1
        self.s[self.Q.top] = x

    def pop_P(self):
        if self.P.top == -1:
            raise UnderFlowError
        x = self.s[self.P.top]
        self.P.top -= 1
        return x

    def pop_Q(self):
        if self.Q.top == self.max_size:
            raise UnderFlowError
        x = self.s[self.Q.top]
        self.Q.top += 1
        return x
