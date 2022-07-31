from typing import List

from utils.utils import test


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        gas = gas + gas
        cost = cost + cost
        dp = [0] * (n * 2)
        length = 0
        start = 0
        for i, g in enumerate(gas):
            delta = g - cost[i] + dp[i - 1]
            if delta < 0:
                dp[i] = 0
                length = 0
                start = i + 1
            else:
                dp[i] = delta
                length += 1
                if length >= n:
                    return start
        return -1


s = Solution()
gas = [2,3,4]
cost = [3,4,3]
test(s.canCompleteCircuit(gas, cost), -1)
