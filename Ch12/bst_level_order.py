from collections import deque


def level_order_iterative(bst):
    current = bst.root
    if current is None:
        return

    q = deque()
    q.appendleft(current)
    while len(q) > 0:
        current = q.pop()
        print(current.key, end=" ")
        if current.left is not None:
            q.appendleft(current.left)
        if current.right is not None:
            q.appendleft(current.right)


def print_level(bst, root, level):
    "Print a particular level, root being level 1"
    if root is None:
        return False
    if level == 1:
        print(root.key, end=" ")
        return True
    left = print_level(bst, root.left, level - 1)
    right = print_level(bst, root.right, level - 1)
    return left or right


def level_order_recursive(bst):
    level = 1
    while print_level(bst, bst.root, level):
        level += 1
