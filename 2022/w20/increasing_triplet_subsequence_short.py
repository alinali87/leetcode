# Beautiful solution but it's hard to understand
# The idea: if we meet a number that is greater than two previous there must be a increasing triplet
# But I'm still in a doubt that it's correct
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # naming "first" and "second" is ugly:
        # "first" and "second" are not the first and the second elements in the triplet
        first = float('inf')
        second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False


def test():
    # example 1
    s = Solution()
    nums = [1, 2, 3, 4, 5]
    a = s.increasingTriplet(nums)
    assert a is True

    # example 2
    s = Solution()
    nums = [5,4,3,2,1]
    a = s.increasingTriplet(nums)
    assert a is False

    # example 3
    s = Solution()
    nums = [2,1,5,0,4,6]
    a = s.increasingTriplet(nums)
    assert a is True

    # example 4
    s = Solution()
    nums = [20, 100, 10, 12, 5, 13]
    a = s.increasingTriplet(nums)
    assert a is True
