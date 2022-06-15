from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums_sorted = sorted(nums)
        c = 1
        i = 0
        diff = 0
        first = nums_sorted[i]
        while i < len(nums_sorted):
            if diff > k:
                c += 1
                first = nums_sorted[i]
            i += 1
            if i == len(nums_sorted):
                return c
            diff = nums_sorted[i] - first

