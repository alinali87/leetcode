from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, node, prefix, paths):
        if node.left is None and node.right is None:
            paths.append(prefix)
        for node in node.left, node.right:
            if node is not None:
                self.dfs(node, prefix + '->' + str(node.val), paths)

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        if root is not None:
            self.dfs(root, str(root.val), paths)
        return paths


def test():
    # root = [1, 2, 3, null, 5]
    node5 = TreeNode(5, None, None)
    node3 = TreeNode(3, None, None)
    node2 = TreeNode(2, None, node5)
    node1 = TreeNode(1, node2, node3)

    s = Solution()
    assert sorted(s.binaryTreePaths(node1)) == sorted(["1->3", "1->2->5"])
    nodeNone = None
    assert sorted(s.binaryTreePaths(nodeNone)) == []


