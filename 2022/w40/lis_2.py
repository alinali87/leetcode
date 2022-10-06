from functools import lru_cache

from utils.utils import test


class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        n = len(nums)

        @lru_cache(None)
        def dfs(index):
            if index == n:
                return float('-inf')

            res = 1
            for i in range(index + 1, n):
                if nums[index] < nums[i]:
                    res = max(res, 1 + dfs(i))
            return res

        return max(dfs(i) for i in range(n))

sol = Solution()
nums = [1,3,6,7,9,4,10,5,6]
test(sol.lengthOfLIS(nums), 6)
