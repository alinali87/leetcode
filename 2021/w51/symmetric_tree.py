# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def walkLMR(node, nodes=None) -> list:
            if nodes is None:
                nodes = []
            if node.left:
                walkLMR(node.left, nodes)
            nodes.append(None)
            nodes.append(node.val)
            if node.right:
                walkLMR(node.right, nodes)
            nodes.append(None)
            return nodes

        def walkRML(node, nodes=None) -> list:
            if nodes is None:
                nodes = []
            if node.right:
                walkRML(node.right, nodes)
            nodes.append(None)
            nodes.append(node.val)
            if node.left:
                walkRML(node.left, nodes)
            nodes.append(None)
            return nodes

        if root.left is None and root.right is None:
            return True
        if root.left is None or root.right is None:
            return False
        nodes_left = walkLMR(root.left)
        nodes_right = walkRML(root.right)
        if len(nodes_left) != len(nodes_right):
            return False
        for i in range(len(nodes_left)):
            if nodes_left[i] != nodes_right[i]:
                return False
        return True

