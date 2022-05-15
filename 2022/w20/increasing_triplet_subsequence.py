# This solution is easy to understand but quite messy - a lot of indexing
# TODO get out of indexing

from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # pref - minimum prefixes, pref[i] = cummulative minimum for elements 0 ... i
        pref = [float('inf') for _ in nums]
        for i, num in enumerate(nums):
            pref[i] = min(pref[i - 1], num) if i > 0 else num
        # suff - maximum suffixes, suff[i] = cummulative maximum for elements i ... len(nums) - 1
        suff = [-float('inf') for _ in nums]
        for i in range(len(nums) - 1, -1, -1):
            suff[i] = max(suff[i + 1], nums[i]) if i < len(nums) - 1 else nums[i]
        # check if an element fits middle in triplet
        # it will be if it's in between minimum from the left and maximum from the right
        for i in range(1, len(nums) - 1):
            if pref[i - 1] < nums[i] < suff[i + 1]:
                return True
        # if we check all elements and do not return, there is no increasing triplet
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
