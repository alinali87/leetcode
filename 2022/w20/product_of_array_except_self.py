from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1 for _ in nums]
        cumproduct = 1
        for i, num in enumerate(nums):
            ans[i] = cumproduct
            cumproduct *= num
        cumproduct = 1
        for i, num in enumerate(nums[::-1]):
            ans[len(ans) - 1 - i] *= cumproduct
            cumproduct *= num
        return ans


def test():
    s = Solution()
    nums = [1,2,3,4]
    ans = s.productExceptSelf(nums)
    assert ans == [24, 12, 8, 6]
