from singly_linked_list import SingleNode as Node
from stack_using_list import UnderFlowError

# we will not be using the singly linked list implementation since it names the point of insertion as head.
# which could be a point of confusion


class Queue:
    def __init__(self):
        self.head = self.tail = None

    def enqueue(self, x):
        newnode = Node(x)
        if self.tail == None:
            self.head = self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode

    def dequeue(self):
        if self.head is None:
            raise UnderFlowError

        x = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = x.next
        return x

