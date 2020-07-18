def successor_inorder(bst, node):
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
        return bst.minimum(node.right)
    y = node.parent
    while y is not None and y.right == node:
        node = y
        y = y.parent
    return y


def predecessor_inorder(bst, node):
    """
    Cases:
    1. Node has a left subtree - predecessor is the maximum in the left subtree (LEFT, ROOT(node))
    2. Node does not have a left subtree.  Node lies in the right subtree of its predecessor (ROOT, RIGHT(node))
        To find predecessor, keep going up till the node is a right child of its parent. Then parent node is the
        predecessor.
    """
    if node.left is not None:
        return bst.maximum(node.left)
    y = node.parent
    while y is not None and y.left == node:  # not right
        node = y
        y = y.parent
    return y


def successor_preorder(bst, node):
    """
    Cases:
    1. If node has a left child, then the left child is the successor. Else
    2. If node has a right child, then right child is the successor. Else
    3. The node is a leaf. Keep going up till the node is the left child of its parent. If the parent has a right
        child, then it becomes the successor. Else continue going up till such a node is found.
    """
    if node.left is not None:
        return node.left
    if node.right is not None:
        return node.right
    y = node.parent
    while y is not None:
        if y.right is None or y.right == node:
            node = y
            y = y.parent
        else:
            break
    return y.right if y is not None else None


def predecessor_preorder(bst, node):
    """
    Cases:
    1. If node is the left child of its parent, the predecessor of node is parent
    2. If node is the right child of its parent, predecessor is in the left subtree of its parent. This is the
        maximum in the left subtree of parent. If parent does not have a left subtree, then parent is the predecessor
    """
    if node.parent is None:  # node was root
        return None
    y = node.parent
    if y.left == None or y.left == node:
        return y
    y = y.left
    while y is not None:
        node = y
        y = y.right
    return node


def successor_postorder(bst, node):
    """
    Cases:
    1. If node is the right child of its parent, then successor is the parent
    2. If node is the left child of its parent, successor would be in right subtree of the parent. It is reahced
        by traversing left childs successively and if there is no left taking right and repeating. 
        If there is no right child, parent is the successor.
    """
    if node.parent is None:
        return None
    y = node.parent
    if y.right == None or y.right == node:
        return y
    y = y.right
    while y is not None:
        node = y
        y = y.left if y.left is not None else y.right
    return node


def predecessor_postorder(bst, node):
    """
    Cases:
    1. If node has a right child, then predecessor is the right child. Else
    2. If node has a left child, predecessor is the left child. Else
    3. Node is a leaf. Keep going up till node becomes the right child of its parent. If parent has a left child, the
        child is the successor. Else keep going up till such a node is found
    """
    if node.right is not None:
        return node.right
    if node.left is not None:
        return node.left
    y = node.parent
    while y is not None:
        if y.left == None or y.left == node:
            node = y
            y = y.parent
        else:
            break
    return y.left if y is not None else None

