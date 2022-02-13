from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        buffer = defaultdict(int)
        for i, num in enumerate(nums):
            if target - num in buffer:
                return [buffer[target - num], i]
            buffer[num] = i


def test():
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    assert s.twoSum(nums, target) == [0, 1]

