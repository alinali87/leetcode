# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        a = []
        if not root:
            return a
        nodes = [root]
        while nodes:
            a.append([])
            nodes_next = []
            for node in nodes:
                a[-1].append(node.val)
                if node.left:
                    nodes_next.append(node.left)
                if node.right:
                    nodes_next.append(node.right)
            nodes = nodes_next
        return a
