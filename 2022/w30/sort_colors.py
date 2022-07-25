from typing import List

from utils.utils import test


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # zeros are on the left of l
        # twos are on the right of r
        # all the checked values are on the left of i
        # zeros and ones are on the left of i
        l, r = 0, len(nums) - 1
        i = 0
        while i <= r:
            if nums[i] == 0:
                # swap with l, after swap l stands on zero, so we need to move l forward
                # i also moves forward, because it stands on the previously seen value
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i += 1
            elif nums[i] == 2:
                # swap with r, r moves, i stands on a new value, so i does not move
                # so it's only zeros or ones on the left of i
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            elif nums[i] == 1:
                # if i stands on one just move forward
                i += 1


sol = Solution()
nums = [2,0,2,1,1,0]
out = [0,0,1,1,2,2]
sol.sortColors(nums)
test(nums, out)

nums = [2,0,1]
out = [0,1,2]
sol.sortColors(nums)
test(nums, out)
