from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [float('inf') for _ in cost]  # how much does it cost to climb on the i-th stair
        dp[0] = 0  # one jump from the beginning cost nothing
        dp[1] = 0  # one jump over two stairs costs nothing
        for i in range(2, len(cost)):
            # there are two options to get to the i-th stair
            # first: jump from the prev = cost of prev + cost to get to the prev
            # second: jump from the second prev = cost of the second prev + cost to get there
            dp[i] = min(cost[i - 1] + dp[i - 1], cost[i - 2] + dp[i - 2])
        # to get to the top there are to options
        # first: to jump from the last stair
        # second: to jump from the second stair from the end
        return min(dp[-1] + cost[-1], dp[-2] + cost[-2])


def test(mine, expected):
    assert mine == expected, f'mine: {mine}, expected: {expected}'


sol = Solution()
cost = [10,15,20]
test(sol.minCostClimbingStairs(cost), 15)

cost = [1,100,1,1,1,100,1,1,100,1]
test(sol.minCostClimbingStairs(cost), 6)
