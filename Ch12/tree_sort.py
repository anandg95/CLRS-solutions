"Sorting by creating a BST, then traversing in order. Not in place"
from bst import BST, Node
import random


def tree_sort(A):
    tree = BST()
    for i in A:
        tree.insert(Node(i))

    tree.inorder(tree.root)


A = [random.randint(0, 100) for _ in range(25)]
print(A)
tree_sort(A)
