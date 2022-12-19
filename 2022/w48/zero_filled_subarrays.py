from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        c = 0
        i = 0
        while i < n:
            while i < n and nums[i] == 0:
                c += 1
                i += 1
            ans += (1 + c) * c // 2
            c = 0
            i += 1
        return ans