from functools import lru_cache
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @lru_cache()
    def rob(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        m = 0

        if root.left:
            m += self.rob(root.left.left) + self.rob(root.left.right)

        if root.right:
            m += self.rob(root.right.left) + self.rob(root.right.right)

        return max(root.val + m, self.rob(root.left) + self.rob(root.right))
