# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        a = []
        if not root:
            return a

        k = 0
        nodes = [root]
        while nodes:
            temp = []
            a.append([])
            for node in nodes:
                a[-1].append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if k % 2 == 1:
                a[-1].reverse()
            nodes = temp
            k += 1
        return a
