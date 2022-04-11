from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        res = nums[0]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= res:
                left = mid + 1
            elif nums[mid] < res:
                res = nums[mid]
                right = mid - 1
        return res


def test():
    s = Solution()
    nums = [3, 4, 5, 1, 2]
    a = s.findMin(nums)
    assert a == 1
    nums = [4, 5, 6, 7, 0, 1, 2]
    a = s.findMin(nums)
    assert a == 0
    nums = [1]
    a = s.findMin(nums)
    assert a == 1
