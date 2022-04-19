from typing import Optional
from collections import deque
# from ...utils.utils import array_to_binary_tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def array_to_binary_tree(arr: list[int]) -> TreeNode:
    assert len(arr) > 0, 'Array is empty! Array must contain at least one integer to build a binary tree.'
    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1
    while i < len(arr):
        node = queue.popleft()
        node.left = TreeNode(arr[i])
        i += 1
        if i == len(arr):
            break
        queue.append(node.left)
        node.right = TreeNode(arr[i])
        i += 1
        queue.append(node.left)
    return root


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maximum = 0

        def dfs(node: TreeNode):
            nonlocal maximum
            if not node:
                return -1
            left = dfs(node.left) + 1
            right = dfs(node.right) + 1
            maximum = max(maximum, left + right)
            return max(left, right)

        dfs(root)
        return maximum


root = array_to_binary_tree([1, 2])
s = Solution()
a = s.diameterOfBinaryTree(root)
print(a)
