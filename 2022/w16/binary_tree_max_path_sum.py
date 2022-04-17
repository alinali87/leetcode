from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_sum = -float('inf')  # antipattern: you should not change class var, class var should be capitalized

    def findMaxSum(self, root):
        if not root:
            return 0

        l = max(self.findMaxSum(root.left), 0)
        r = max(self.findMaxSum(root.right), 0)

        self.max_sum = max(l + root.val + r, self.max_sum)

        return root.val + max(l, r)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.findMaxSum(root)
        return self.max_sum

