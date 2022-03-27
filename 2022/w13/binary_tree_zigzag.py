# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        counter = 0
        ans = [[root.val]]
        all = [[root]]
        counter += 1
        while True:
            level_all = []
            level = []
            for node in all[-1]:
                if node.left:
                    level_all.append(node.left)
                    level.append(node.left.val)
                if node.right:
                    level_all.append(node.right)
                    level.append(node.right.val)
            if not level:
                break
            all.append(level_all)
            if counter % 2 != 0:
                level = level[::-1]
            counter += 1
            ans.append(level)

        return ans


def test():
    node5 = TreeNode(7, None, None)
    node4 = TreeNode(15, None, None)
    node3 = TreeNode(20, node4, node5)
    node2 = TreeNode(9, None, None)
    node1 = TreeNode(3, node2, node3)
    s = Solution()
    a = s.zigzagLevelOrder(node1)
    print(a)


test()






