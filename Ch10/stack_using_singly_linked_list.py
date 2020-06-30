from singly_linked_list import SinglyLinkedList as LinkedList, SingleNode as Node
from stack_using_list import UnderFlowError


class Stack:
    def __init__(self):
        self.s = LinkedList()
        self.head = self.s.sentinel

    def push(self, x):
        newnode = Node(x)
        self.s.insert(newnode)

    def pop(self):
        x = self.s.head
        if x is None:
            raise UnderFlowError
        self.s.delete(self.s.head)
        return x
