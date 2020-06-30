class SingleNode:
    def __init__(self, key, next=None):
        self.key = key
        self.next = None

    def __repr__(self):
        return f"Node: key={self.key}, next={self.next.key if self.next is not None else None}"


class SinglyLinkedList:
    def __init__(self):
        self.sentinel = SingleNode(None)

    def insert(self, x):
        x.next = self.sentinel.next
        self.sentinel.next = x

    def delete(self, x):
        node = self.sentinel
        found = False
        while node and not found:
            if node.next != x:
                node = node.next
            else:
                found = True
        if not found:
            raise Exception("Node not in list")

        node.next = x.next

    def search(self, key):
        node = self.head
        found = False
        while node and not found:
            if node.key == key:
                found = True
            else:
                node = node.next
        return node if found else None

    def listit(self):
        node = self.head
        l = []
        while node:
            l.append(node.key)
            node = node.next
        return l

    def reverse(self):
        prev = None
        curr = self.head
        nex = self.head.next
        while curr:
            curr.next = prev
            prev = curr
            curr = nex
            if nex:
                nex = nex.next
        self.sentinel.next = prev

    @property
    def head(self):
        return self.sentinel.next

    def __repr__(self):
        return f"Singly linked list : {self.listit()}"

