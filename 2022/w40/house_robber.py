from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return max(nums)
        dp = [0] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        print(dp)
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        print(dp)
        return dp[-1]
