from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            d = prices[i] - prices[i - 1]
            if d > 0:
                profit += d
        return profit


def test():
    s = Solution()
    prices = [0]
    profit = s.maxProfit(prices)
    print()
    print(f'if prices {repr(prices)} then profit = {profit}')
    prices = [1,2,3,3,5]
    profit = s.maxProfit(prices)
    print(f'if prices {repr(prices)} then profit = {profit}')
    prices = [7, 6, 4, 3, 1]
    profit = s.maxProfit(prices)
    print(f'if prices {repr(prices)} then profit = {profit}')
    prices = [7, 1, 5, 3, 6, 4]
    profit = s.maxProfit(prices)
    print(f'if prices {repr(prices)} then profit = {profit}')


test()