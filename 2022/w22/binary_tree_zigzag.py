# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Input: root = [3,9,20,null,null,15,7]
        # Output: [[3],[20,9],[15,7]]
        curr = [root]
        next_level = []
        zig = 1
        prep = deque([])
        ans = []
        while curr:
            for node in curr:
                if node:
                    if zig % 2:
                        prep.append(node.val)
                    else:
                        prep.appendleft(node.val)
                    next_level.extend([node.left, node.right])
            zig += 1
            curr = next_level
            next_level = []
            if prep:
                ans.append(prep)
            prep = deque([])
        return ans
