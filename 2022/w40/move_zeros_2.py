from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        insert_non_zero_pos = 0
        for read_pos in range(n):
            if nums[read_pos] != 0:
                nums[insert_non_zero_pos] = nums[read_pos]
                insert_non_zero_pos += 1
        while insert_non_zero_pos < n:
            nums[insert_non_zero_pos] = 0
            insert_non_zero_pos += 1
