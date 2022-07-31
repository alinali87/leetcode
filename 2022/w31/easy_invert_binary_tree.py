from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(node):
            node.left, node.right = node.right, node.left

        # add all seen nodes into the q - queue
        # just interate over all the nodes and do invert
        q = [root]
        while q:
            node = q.pop(0)
            if node:
                invert(node)
                q.extend([node.left, node.right])
        return root
