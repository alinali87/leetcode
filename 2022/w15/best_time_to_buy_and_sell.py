from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0 for _ in prices]
        for i in range(1, len(prices)):
            d = prices[i] - prices[i - 1]
            dp[i] = max(0, d, dp[i - 1] + d)
        return max(dp)
