from typing import List

from utils.utils import test


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return
        zpos = 0  # zero pos
        spos = 1  # search non-zero pos
        # Input: nums = [0,1,0,3,12]
        # Output: [1,3,12,0,0]
        # 1, 0, 0, 3, 12
        # 1, 3, 0, 0, 12
        # 1, 3, 12, 0, 0
        finished = False
        while not finished and zpos < n:
            if nums[zpos] == 0:
                while spos < n and nums[spos] == 0:
                    spos += 1
                if spos == n:
                    finished = True
                    break
                else:
                    # swap
                    nums[zpos], nums[spos] = nums[spos], nums[zpos]
            zpos += 1
            spos = max(spos, zpos + 1)


sol = Solution()
nums = [0,1,0,3,12]
sol.moveZeroes(nums)
test(nums, [1,3,12,0,0])
