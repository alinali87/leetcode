from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [None for _ in nums]
        prefix = 1
        for i in range(len(nums)):
            product[i] = prefix
            prefix = prefix * nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            product[i] = product[i] * postfix
            postfix = postfix * nums[i]

        return product

def test():
    s = Solution()
    nums = [1, 2, 3, 4]
    a = s.productExceptSelf(nums)
    assert a == [24,12,8,6]
