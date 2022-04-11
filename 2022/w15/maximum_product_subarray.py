from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        positive = nums[0]
        negative = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            temp = positive
            positive = max(num, temp * num, negative * num)
            negative = min(num, temp * num, negative * num)
            res = max(res, positive)
        return res


def test():
    s = Solution()
    nums = [2, 3, -2, 4]
    a = s.maxProduct(nums)
    assert a == 6
    nums = [-2, 0, -1]
    a = s.maxProduct(nums)
    assert a == 0
    nums = [-3,-1,-1]
    a = s.maxProduct(nums)
    assert a == 3
    nums = [0, 2]
    a = s.maxProduct(nums)
    assert a == 2

