from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def helper(self, L, R, nums, parent: Optional[TreeNode], left):
        if L > R:
            return
        mid = (L + R) // 2
        val = nums[mid]
        if val is not None:
            node = TreeNode(val)
            if left:
                parent.left = node
            else:
                parent.right = node
        self.helper(L, mid - 1, nums, node, left=True)
        self.helper(mid + 1, R, nums, node, left=False)

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        val = nums[mid]
        root = TreeNode(val)
        self.helper(left, mid - 1, nums, root, left=True)
        self.helper(mid + 1, right, nums, root, left=False)
        return root


s = Solution()
nums = [-10,-3,0,5,9]
root = s.sortedArrayToBST(nums)
