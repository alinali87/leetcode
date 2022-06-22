from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # let's look at two subtrees: left and right
        # root.left will be the root1 - root of the left subtree
        # root.right will be the root2 - root of the right subtree
        def check(root1: TreeNode, root2: TreeNode):
            # if there are no subtrees then the main tree consists of one node and is symmetric
            if root1 is None and root2 is None:
                return True
            # if some of root1 or root2 does not exist then the main tree has a subtree and no symmetric one - not symmentric
            if root1 is None or root2 is None:
                return False
            # if both root1 and root2 exist let's check their values
            if root1.val != root2.val:
                return False
            return check(root1.left, root2.right) and check(root1.right, root2.left)

        return check(root.left, root.right)

