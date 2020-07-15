"Implement traversals wihtout using recursion"

from bst import BST, Node


class BST_I(BST):
    def inorder(self):
        stack = []
        current = self.root
        while True:
            if current != None:
                stack.append(current)
                current = current.left
            else:
                try:
                    current = stack.pop()
                    print(current.key)
                    current = current.right
                except:  # all done
                    break

    def preorder(self):
        stack = []
        stack.append(self.root)
        while len(stack) > 0:
            current = stack.pop()
            print(current.key)
            if current.right is not None:
                stack.append(current.right)
            if current.left is not None:
                stack.append(current.left)  # Stack is LIFO, so left pops first

    def postorder_1(self):
        """
        Postorder using 1 stack
        
        Postorder traversal is left, right, root
        1. Take a root as current
        2. Push current to stack.
        3. Check current's left child. If exsits, set current as left child. Go to 2. Else 4.
        4. Peek the topmost in stack. If topmost has a right subtree, it must be traversed first by postorder.
           Set current as right child of topmost. Go to 2.
           If there is no right child, topmost can be popped. Now peek the new topmost. If popped is the
           right child of new topmost, pop topmost, since its right has been traversed. Continue until this fails.
        """

        def peek(stack):
            try:
                topmost = stack.pop()
                stack.append(topmost)
                return topmost
            except IndexError:
                return None

        if self.root is None:
            return
        stack = []
        current = self.root
        while current != None or len(stack) != 0:
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                topmost = peek(stack)
                if topmost.right is None:
                    popped = stack.pop()
                    print(popped.key)
                    while len(stack) > 0 and popped == peek(stack).right:
                        popped = stack.pop()
                        print(popped.key)
                else:
                    current = topmost.right

    def postorder_2(self):
        """
        Postorder using 2 stacks
        There are 2 stacks S1 and S2, each of which has a function for itself:
        - S1 holds the `parent` nodes (primary stack)
        - S2 holds the `left` child and `right` child of the above `parent` node (secondary stack)
        After S2 is empty, all nodes are popped from S1 to get the post order.

        In postorder, we need nodes in order left, right, parent. Hence, they must be pushed to S1
        in order - (parent, right, left) (due to LIFO property)
        But every right, left is a parent in itself, so only the parent is pushed to S1, while children are pushed
        to S2 first in order (left, right). From S2, they are popped as `parent` which would go to S1, while children
        go to S2. By pushing in S2 as (left, right), it ensures they are popped from it in order (right, left), the
        reason for which has been explained before.        
        """
        if self.root is None:
            return
        S1, S2 = [], []
        S2.append(self.root)
        while True:
            try:
                current = S2.pop()
            except IndexError:  # underflow error
                break
            S1.append(current)
            if current.left is not None:
                S2.append(current.left)
            if current.right is not None:
                S2.append(current.right)
        while True:
            try:
                print(S1.pop().key)
            except IndexError:
                break


bst = BST_I()
numbers = [15, 6, 3, 4, 2, 7, 13, 9, 18, 17, 20]
for i in numbers:
    bst.insert(Node(i))
