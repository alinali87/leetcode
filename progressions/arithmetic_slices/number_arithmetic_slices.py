from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n-2):
            diff = nums[i+1] - nums[i]
            for j in range(i + 1, n):
                if nums[j] - nums[j-1] == diff:
                    if j - i + 1 >= 3:
                        ans += 1
                else:
                    break
        return ans
