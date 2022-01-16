# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None:
            return True
        nodes = self.walkLMR(root)
        for i in range(1, len(nodes)):
            if nodes[i] <= nodes[i - 1]:
                return False
        return True
    
    def walkLMR(self, node, nodes=None) -> list:
        if nodes is None:
            nodes = []
        if node.left:
            self.walkLMR(node.left, nodes)
        nodes.append(node.val)
        if node.right:
            self.walkLMR(node.right, nodes)
        return nodes
        
