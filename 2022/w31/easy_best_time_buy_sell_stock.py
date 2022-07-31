from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # bprice - buy price, r - result or say profit
        bprice = float('inf')
        r = 0
        for p in prices:
            # bprice always contains the lowest price seen
            # result is updated if diff bprice with current price gives the best profit
            r = max(r, p - bprice)
            bprice = min(bprice, p)
        return r
