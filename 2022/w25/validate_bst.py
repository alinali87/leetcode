from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node, left_border, right_border):
            # if node is None it's a valid bst
            if node is None:
                return True
            # if node value does not fit the borders it's not a valid bst
            if node.val <= left_border or node.val >= right_border:
                return False
            # if node has children then check each child and if both are valid then the parent is also valid
            # this is equivalent to logical AND
            return check(node.left, left_border, node.val) and check(node.right, node.val, right_border)

        # call the check function with root and negative infinity and positive infinity as initial borders
        return check(root, -float('inf'), float('inf'))
