class Node:
    def __init__(self, key, next=None, prev=None):
        self.key = key
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f"Node: key={self.key}, prev={self.prev.key}, next={self.next.key}"


class LinkedList:
    # Circular linked list
    def __init__(self):
        self.sentinel = Node(None)
        self.sentinel.next = self.sentinel  # circular
        self.sentinel.prev = self.sentinel  # circular

    def insert(self, x):
        x.next = self.sentinel.next
        self.sentinel.next.prev = x
        self.sentinel.next = x
        x.prev = self.sentinel

    def delete(self, x):
        # not checking if x is actually in the list or not
        x.next.prev = x.prev
        x.prev.next = x.next

    def search(self, key):
        node = self.sentinel
        found = False
        while node and not found:
            if node.key == key:
                found = True
            else:
                node = node.next
        return node if found else None

    @property
    def head(self):
        return self.sentinel.next

    @property
    def tail(self):
        return self.sentinel.prev

    def listit(self):
        node = self.head
        l = []
        while node != self.sentinel:
            l.append(node.key)
            node = node.next
        return l

    def reverse(self):
        node = self.sentinel
        while True:
            print(node.key)
            node.next, node.prev = node.prev, node.next
            node = node.prev  # we just interchanged
            if node == self.sentinel:
                break

    def __repr__(self):
        return f"Doubly Linked List: {self.listit()}"


dll = LinkedList()
dll.insert(Node(1))
dll.insert(Node(2))
dll.insert(Node(3))
dll.insert(Node(4))
dll.insert(Node(5))
