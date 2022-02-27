from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, node, result):
        if node.left:
            self.helper(node.left, result)
        result.append(node.val)
        if node.right:
            self.helper(node.right, result)

    def inorderTraversal(self, root):
        if root:
            ans = []
        else:
            return []
        self.helper(root, ans)
        return ans


def test():
    # root = [1, 2, 3, 4, 5]
    node4 = TreeNode(4, None, None)
    node5 = TreeNode(5, None, None)
    node3 = TreeNode(3, None, None)
    node2 = TreeNode(2, node4, node5)
    node1 = TreeNode(1, node2, node3)

    s = Solution()

    print(s.inorderTraversal(node1))
