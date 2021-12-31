# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        nodes = [[root]]
        ans = [[root.val]]
        empty_level = False
        while not empty_level:
            prev = nodes[-1]
            level = []
            ans_raw = []
            for node in prev:
                if node.left:
                    level.append(node.left)
                    ans_raw.append(node.left.val)
                if node.right:
                    level.append(node.right)
                    ans_raw.append(node.right.val)
            if ans_raw == []:
                empty_level = True
            else:
                nodes.append(level)
                ans.append(ans_raw)
        return ans

