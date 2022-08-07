from typing import List


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        prev = nums[-1]  # interate backwards
        res = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= prev:
                prev = nums[i]
            else:
                m = (nums[i] + prev - 1) // prev
                res += m - 1
                prev = nums[i] // m
        return res
