from collections import deque
from typing import Optional


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
        queue.append(node.left)
        node.right = TreeNode(arr[i])
        i += 1
        queue.append(node.left)
    return root


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root, minimum, maximum):
            if not root:
                return True
            if root.val >= maximum or root.val <= minimum:
                return False
            return validate(root.left, minimum, root.val) and validate(root.right, root.val, maximum)

        return validate(root, -float('inf'), float('inf'))


def test():
    s = Solution()
    arr = [2, 1, 3]
    root = array_to_binary_tree(arr)
    ans = s.isValidBST(root)
    print(ans)
    arr2 = [5,1,4,None,None,3,6]
    root2 = array_to_binary_tree(arr2)
    ans = s.isValidBST(root2)
    print(ans)
