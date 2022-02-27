from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def recurse(node):
            out = []
            if node:
                out += recurse(node.left)
                out.append(node.val)
                out += recurse(node.right)
            return out

        return recurse(root)


def test():
    # root = [1, 2, 3, null, 5]
    node5 = TreeNode(5, None, None)
    node3 = TreeNode(3, None, None)
    node2 = TreeNode(2, None, node5)
    node1 = TreeNode(1, node2, node3)

    s = Solution()

    print(s.inorderTraversal(node1))


test()