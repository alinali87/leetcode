from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root.left is None and root.right is None:
            return 1
        if root.left and root.right:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        if root.left:
            return self.maxDepth(root.left) + 1
        if root.right:
            return self.maxDepth(root.right) + 1

