from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def f(nums):
            n = len(nums)
            if n < 2:
                return max(nums)
            dp = [0] * n
            dp[0], dp[1] = nums[0], max(nums[0], nums[1])
            for i in range(2, n):
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
            return dp[-1]

        if len(nums) < 3:
            return max(nums)
        a = f(nums[1:])
        b = f(nums[:-1])
        return max(a, b)
