from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + root.val + self.inorderTraversal(root.right)


s = Solution()
lst = [1,None,2,3]
# TODO: f(lst) -> root: takes lst of values and returns root of a binary tree

