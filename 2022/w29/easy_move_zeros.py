from typing import List

from utils.utils import test


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        l, r = 0, 1
        while r < len(nums):
            if nums[l] == 0:
                if nums[r] != 0:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r += 1
                else:
                    r += 1
            else:
                l += 1
                r += 1


sol = Solution()
nums = [0,1,0,3,12]
sol.moveZeroes(nums)
test(nums, [1,3,12,0,0])

nums = [0]
sol.moveZeroes(nums)
test(nums, [0])
