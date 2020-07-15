class Node:
    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right


class BST:
    def __init__(self, root=None):
        self.root = root

    def insert(self, node):
        y = None  # will be parent for node
        x = self.root
        while x != None:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y == None:  # empty tree
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

    def delete(self, node):
        pass

    def inorder(self, node):
        if node != None:  # recursive
            self.inorder(node.left)
            print(node.key)
            self.inorder(node.right)

    def preorder(self, node):
        if node != None:
            print(node.key)
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node != None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.key)

    def search(self, k):
        current = self.root
        while current is not None:
            if k == current.key:
                return current
            if k < current.key:
                current = current.left
            else:
                current = current.right

    def minimum(self, node):  # in subtree with `node` as parent
        if node is None:
            return
        while node.left is not None:
            node = node.left
        return node

    def maximum(self, node):  # in subtree with `node` as parent
        if node is None:
            return
        while node.right is not None:
            node = node.right
        return node

    def successor(self, node):
        """
        Cases:
        1. Node has a right subtree - successor is minimum element in right subtree
        2. Node does not have a right subtree:
           i. Node is the left child of its parent - then successor = parent
           ii. Node is the right subchild of its parent - keep climbing up parent till a node becomes the left child of
              a parent. Then that parent is successor
           (i) and (ii) are implemented using similar logic. Keep parenting till it becomes a left child
        """
        if node.right is not None:
            return self.minimum(node.right)
        y = node.parent
        while y is not None and y.right == node:
            node = y
            y = y.parent
        return y

    def predecessor(self, node):
        pass


numbers = [12, 5, 2, 9, 18, 19, 15, 17]
bst = BST()
for i in numbers:
    bst.insert(Node(i))

bst.insert(Node(13))  # test
