from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            seen[num] = i


def test():
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    a = s.twoSum(nums, target)
    assert a == [0,1]
    nums = [3, 2, 4]
    target = 6
    a = s.twoSum(nums, target)
    assert a == [1, 2]
