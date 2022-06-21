from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1 <= prices.length <= 3 * 10 ** 4, so we can take the first element securely
        prev = prices[0]
        profit = 0
        # let's iterate over prices and compare current price with the previous one
        # we will compare the first price with itselt and get 0 profit
        # but it's OK because we can't earch any money on the first day
        for price in prices:
            profit += max(price - prev, 0)
            # don't forget to update the previous price
            prev = price
        return profit
