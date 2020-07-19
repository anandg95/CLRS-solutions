from math import inf
from collections import namedtuple


def lowest_common_ancestor(root, node1, node2):
    """
    Lowest common ancestor of node1 and node2 in bst
    An easy method would be store node1's path to root and then check node2's path to root.
    At any point if the path coincides with the path of node1, then that node is the LCA
    Without using auxiliary storage:
    - Start from root.
    - Check the left subtree and right subtree for node1 and node2. If node1 is in left subtree
      and node2 is in right subtree (or vice versa), then it follows that root is LCA. If both nodes lie in
      one subtree, recursively check that subtree. The point at which the 2 nodes lie in 2 different subtrees
      is the LCA
    This is code to the recursive solution
    """
    if root is None:
        return None
    if root == node1 or root == node2:  # if one of them is root, then that is the LCA
        return root
    left_lca = lowest_common_ancestor(root.left, node1, node2)
    right_lca = lowest_common_ancestor(root.right, node1, node2)

    if left_lca and right_lca:  # both nodes are in different subtrees of root
        return root
    return left_lca if left_lca else right_lca


def lca_bst(root, node1, node2):
    "Lowest common ancestor that works exclusively on a binary SEARCH tree"
    if node1.key == root.key or node2.key == root.key:
        return root
    c1 = node1.key < root.key
    c2 = node2.key > root.key
    if c1 == c2:
        return root  # they lie in different subtrees, hence root is LCA
    if c1:
        return lca_bst(root.left, node1, node2)  # both in left subtree
    else:
        return lca_bst(root.right, node1, node2)  # both in right subtree


def tree_equality(root1, root2):
    "Given the roots of 2 binary trees, verify if they are exactly similar"
    print(f"Comparing {root1} and {root2}")
    if not (root1 and root2):  # both None
        return True
    if (root1 and not root2) or (root2 and not root1):  # one is None, other is not
        return False

    return (
        (root1.key == root2.key)
        and tree_equality(root1.left, root2.left)
        and tree_equality(root1.right, root2.right)
    )


def size_of_bst(root):
    "Given the root of a binary tree, find its number of nodes"
    if root is None:
        return 0
    left_num_nodes = size_of_bst(root.left)
    right_num_nodes = size_of_bst(root.right)
    return 1 + left_num_nodes + right_num_nodes


def sum_bst(root, sum):
    """Given a binary tree and a sum, find the path from root to any leaf on the bst on which the sum of nodes
    is the given value"""
    if root is None:
        if sum == 0:
            return True
        else:
            return False

    reqd_sum = sum - root.key
    sum_from_left = sum_bst(root.left, reqd_sum)
    if sum_from_left:
        print(root)
        return True

    sum_from_right = sum_bst(root.right, reqd_sum)
    if sum_from_right:
        print(root)
        return True

    return False


def check_if_bst(root, min, max):
    """Given a binary tree, check if it follows binary search tree property
    To start off, run `check_if_bst(BT.root, -math.inf, math.inf)`"""
    if root == None:
        return True

    if root.key < min or root.key >= max:
        return False

    return check_if_bst(root.left, min, root.key) and check_if_bst(
        root.right, root.key, max
    )


LBST = namedtuple("LBST", field_names=["is_bst", "root", "num_nodes", "min", "max"])


def largest_bst_in_bt(root):
    """
    Given the root of a binary tree, find the largest subtree that follows the binary search tree property.
    Return the node which is the root of this largest bst, and also the number of nodes in it
    1. This is best done by a bottoms up approach as we need the number of nodes in the BST to determine the largest
    2. We need to check the left subtree, the right subtree for BST property and then check with the root using
       info from left and right for BST property when root is included. This is classic postorder traversal
    3. Returns - whether root its a bst, actual root of bst in subtree, size of that bst, number of nodes in it, 
        min and max of the bst
    """
    if root == None:
        return LBST(is_bst=True, root=None, num_nodes=0, min=inf, max=-inf)
        # min is used for checking if right subtrees maintains BST property. When rst is None, that is true
        # Therefore, it is set as +inf. Vice versa reasoning for max being -inf

    # postorder -- left, right, root
    left_info: LBST = largest_bst_in_bt(root.left)
    right_info: LBST = largest_bst_in_bt(root.right)
    print(root)
    print(left_info)
    print(right_info)

    if left_info.is_bst and right_info.is_bst:
        # both left and right are BST
        if left_info.max < root.key <= right_info.min:
            # adding root retains bst property
            return LBST(
                is_bst=True,
                root=root,
                num_nodes=left_info.num_nodes + right_info.num_nodes + 1,
                min=left_info.min if left_info.root is not None else root.key,
                max=right_info.max if right_info.root is not None else root.key,
            )

    larger_bst = left_info if left_info.num_nodes > right_info.num_nodes else right_info
    return LBST(
        is_bst=False,
        root=larger_bst.root,
        num_nodes=larger_bst.num_nodes,
        min=larger_bst.min,
        max=larger_bst.max,
    )
