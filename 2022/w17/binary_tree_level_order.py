

# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        prev = [root]
        curr = []
        ans = []
        ans_prep = []
        while True:
            for node in prev:
                if node:
                    ans_prep.append(node.val)
                    if node.left:
                        curr.append(node.left)
                    if node.right:
                        curr.append(node.right)
            ans.append(ans_prep)
            if not curr:
                break
            ans_prep = []
            prev = curr
            curr = []
        return ans
