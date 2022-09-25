from typing import List

from utils.utils import test


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        unique = set()
        for n in nums:
            if n != 0:
                unique.add(n)
        return len(unique)


sol = Solution()
nums = [1,5,0,3,5]
test(sol.minimumOperations(nums), 3)

nums = [0]
test(sol.minimumOperations(nums), 0)
