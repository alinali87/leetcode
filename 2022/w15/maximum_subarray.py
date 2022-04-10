from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        summ = 0
        for num in nums:
            summ += num
            res = max(summ, res)
            summ = max(summ, 0)
        return res


def test():
    s = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    a = s.maxSubArray(nums)
    assert a == 6
    nums = [1]
    a = s.maxSubArray(nums)
    assert a == 1
    nums = [5, 4, -1, 7, 8]
    a = s.maxSubArray(nums)
    assert a == 23
