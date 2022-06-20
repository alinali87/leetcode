from typing import List


class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def min_cost(self, costs: List[List[int]]) -> int:
        # if there are no houses, the costs to paint them = 0
        if len(costs) == 0:
            return 0
        # dp stores the three best costs for painting current house in [0-color, 1-color, 2-color]
        # initially we fill dp with infinity so that real numbers replace all initial ones
        dp = [[float('inf')] * 3 for _ in costs]
        # we can choose any color for the first color
        dp[0] = costs[0]
        # let's start from the second house and check all possible combinations
        # for previous house color (prev) and current house color (curr)
        # minimum of current value in dp for current color and calculated one is the best cost
        # final answer will be the minimum of the last array in dp
        for i in range(1, len(costs)):
            for prev in range(3):
                for curr in range(3):
                    if prev != curr:
                        dp[i][curr] = min(costs[i][curr] + dp[i - 1][prev], dp[i][curr])
        return min(dp[-1])


def test():
    s = Solution()
    costs = [[14,2,11],[11,14,5],[14,3,10]]
    assert s.min_cost(costs) == 10
    costs = [[1,2,3],[1,4,6]]
    assert s.min_cost(costs) == 3


test()