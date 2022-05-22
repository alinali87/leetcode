from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # you can increase the number of colors, it is important that colors encoded as 0, 1, 2 etc.
        N_COLORS = 3
        counts = [0] * N_COLORS
        for num in nums:
            counts[num] += 1
        value = 0
        i = 0
        for c in counts:
            for _ in range(c):
                nums[i] = value
                i += 1
            value += 1
