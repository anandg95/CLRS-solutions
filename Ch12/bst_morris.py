"""
Morris traversal for O(1) space complexity (no stack)
Reference - https://www.youtube.com/watch?v=wGXB9OWhPTg
"""
from bst_succ_pred import BST_SP, Node


class BST_M(BST_SP):
    def inorder_morris(self):
        current = self.root
        while current is not None:
            if current.left is None:
                # no left child, so visit node
                print(current.key)
                current = current.right
            else:
                # determine predecessor, if it loops back to same element, stop
                predecessor = current.left
                while predecessor.right is not None and predecessor.right != current:
                    predecessor = predecessor.right

                if predecessor.right == None:
                    predecessor.right = current  # magic
                    current = current.left
                else:
                    # loop has been formed
                    predecessor.right = None
                    print(current.key)
                    current = current.right

    def preorder_morris(self):
        current = self.root
        while current is not None:
            if current.left is None:
                print(current.key)
                current = current.right
            else:
                predecessor = current.left
                while predecessor.right is not None and predecessor.right != current:
                    predecessor = predecessor.right

                if predecessor.right == None:
                    predecessor.right = current
                    print(current.key)  # only this line has changed in fact
                    current = current.left
                else:
                    predecessor.right = None
                    current = current.right


numbers = numbers = [15, 6, 3, 4, 2, 7, 13, 9, 18, 17, 20]

bst = BST_M()
for i in numbers:
    bst.insert(Node(i))
