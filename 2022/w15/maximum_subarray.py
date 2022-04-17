from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]  # store the best subarray sum found
        cum_sum = 0  # best cumulative sum with the end at current position
        for num in nums:
            cum_sum = max(cum_sum + num, num)
            res = max(cum_sum, res)
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
