# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 1:
            return [-1, -1]
        l = bisect_left(nums, target)
        r = bisect_right(nums, target)
        if l == r:
            return [-1, -1]
        return [l, r - 1]


def test():
    s = Solution()
    nums = [5,7,7,8,8,10]
    target = 8
    a = s.searchRange(nums, target)
    assert a == [3, 4]
    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    a = s.searchRange(nums, target)
    assert a == [-1, -1]
    nums = []
    target = 0
    a = s.searchRange(nums, target)
    assert a == [-1, -1]
