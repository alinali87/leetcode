from functools import reduce
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if min(nums) > 0:
            return reduce(lambda x, y: x * y, nums)
        n = len(nums)
        rev = nums[::-1]
        for i in range(1, n):
            nums[i] *= nums[i - 1] or 1
            rev[i] *= rev[i - 1] or 1
        return max(nums + rev)
