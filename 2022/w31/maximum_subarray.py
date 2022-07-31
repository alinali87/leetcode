from typing import List

from utils.utils import test


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # total is the maximum sum
        # cur is the current sum of subarray
        total = nums[0]
        cur = 0
        for n in nums:
            # we can continue adding new elements unless they increase the sum
            # if the current sum < element itself, it's rational to start with this element - so we get new cur
            cur = max(n, cur + n)
            # at each step we overwrite the total, if new cur is greater than total found earlier
            total = max(total, cur)
        return total


sol = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
test(sol.maxSubArray(nums), 6)

nums = [-2]
test(sol.maxSubArray(nums), -2)

nums = [-2,-1,-3]
test(sol.maxSubArray(nums), -1)

nums = [2,-3,3]
test(sol.maxSubArray(nums), 3)

nums = [2,5,3]
test(sol.maxSubArray(nums), 10)
