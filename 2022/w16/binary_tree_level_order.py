# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = deque([root])
        next_level = deque([])
        ans = []
        values = []
        while level:
            node = level.popleft()
            if not node:
                continue
            values.append(node.val)
            for child in node.left, node.right:
                if child:
                    next_level.append(child)
            if not level:
                ans.append(values)
                values = []
                level = next_level
                next_level = deque([])
        return ans


def test():
    s = Solution()
    arr = [3, 9, 20, None, None, 15, 7]
    # root = array_to_binary_tree(arr)
    node7 = TreeNode(7)
    node6 = TreeNode(15)
    node3 = TreeNode(20, node6, node7)
    node2 = TreeNode(9, None, None)
    root = TreeNode(3, node2, node3)
    assert s.levelOrder(root) == [[3],[9,20],[15,7]]
    root = None
    assert s.levelOrder(root) == []
