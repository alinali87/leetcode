from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]


def test():
    s = Solution()
    nums = [1,2,3,4,5,6,7]
    k = 3
    s.rotate(nums, k)
    assert nums == [5,6,7,1,2,3,4]
    nums = [-1, -100, 3, 99]
    k = 2
    s.rotate(nums, k)
    assert nums == [3,99,-1,-100]