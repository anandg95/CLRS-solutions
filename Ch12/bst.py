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

    def insert_recurive(self, node, parent, new_node):
        "Recurive version of insert()"
        if node is None:
            new_node.parent = parent
            return new_node

        if new_node.key < node.key:
            node.left = self.insert_recurive(node.left, node, new_node)
        else:
            node.right = self.insert_recurive(node.right, node, new_node)

        return node

    def delete(self, node_z):
        """
        Cases:
        1. The node is a leaf, easy-peasy, get rid of it
        2. Node has only one child, move the child to the node's position (the whole subtree figuratively)
        3. Node has 2 children. You can choose to retain the left subtree or the right subtree as such. If
           you choose to leave the left subtree as is, then discover a node from the right subtree that will
           correctly follow the BST property. The node that follows this will be the sucessor of the node to be 
           deleted (smallest node in the right subtree).
           However there is a catch. The successor could have a right subtree of its own. 
           i.  Successor is the right child of the deleted node. Here just transplant
           ii. Successor (s) is somewhere down in the right subtree of deleted node. Now where do we put its own right subtree
               and the deleted node's right subtree (of which s was a part)?
               Answer: When we move the successor, we free up the left child spot of successor's original parent.
               We move the right subtree of successor as the left subtree of successor's original parent
        Steps for (ii):
           Deleted node (Z) will have a parent (P), 2 children (L, R) and a successor (Y). Successor has a right subtree (YR). Successor has
           a parent (YP).
           - Move YR as the left subtree of YP (transplant)
           - Move Y to where Z sat. Assign Y as parent to L and R. Transplant the new Y to Z so that P becomes parent
             to Y.
        """
        if node_z.left == None:
            self.transplant(node_z, node_z.right)
        elif node_z.right == None:
            self.transplant(node_z, node_z.left)
        else:
            y = self.minimum(node_z.right)
            if y != node_z.right:
                self.transplant(y, y.right)
                y.right = node_z.right
                y.right.parent = y
            self.transplant(node_z, y)
            y.left = node_z.left
            node_z.left.parent = y

    def transplant(self, u, v):
        """Replaces the subtree rooted at `u` with the subtree rooted `v`"""
        if u.parent == None:  # u is root
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

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


# fmt: off
numbers = [50, 35, 70, 43, 45, 44, 49, 38, 32, 34, 15, 25, 10, 20, 18, 65, 90, 80, 85, 95] 
# fmt: on
sample_bst = BST()
for i in numbers:
    sample_bst.insert(Node(i))

# max height is 6
