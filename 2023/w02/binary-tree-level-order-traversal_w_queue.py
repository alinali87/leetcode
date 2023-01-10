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
        q = deque([root])
        k = 1
        while q:
            nk = 0
            prep = []
            while k > 0:
                node = q.popleft()
                prep.append(node.val)
                if node.left:
                    q.append(node.left)
                    nk += 1
                if node.right:
                    q.append(node.right)
                    nk += 1
                k -= 1
            k = nk
            a.append(prep)
        return a
