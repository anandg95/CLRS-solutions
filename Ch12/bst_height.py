from collections import deque


def height_recursive(bst, node):
    if node is None or (node.left == node.right == None):
        return 0
    lh = height_recursive(bst, node.left)
    rh = height_recursive(bst, node.right)
    return 1 + max(lh, rh)


def height_iterative(bst):
    if bst.root is None:
        return 0
    current = bst.root
    h = -1
    q = deque()
    q.appendleft(current)
    while len(q) > 0:
        size = len(q)
        while size > 0:
            current = q.pop()
            if current.left is not None:
                q.appendleft(current.left)
            if current.right is not None:
                q.appendleft(current.right)
            size -= 1
        # this while block will clear out a level from the queue, and add all elements in the next level
        h += 1
    return h

