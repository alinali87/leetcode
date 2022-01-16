class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minimum = prices[0]
        for i in range(1, len(prices)):
            minimum = min(prices[i - 1], minimum)
            profit = max(prices[i] - minimum, profit)
        return profit
