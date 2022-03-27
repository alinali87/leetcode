from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        for i, num in enumerate(nums):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

def test():
    s = Solution()
    nums = [7, 7, 7, 7, 7, 7, 7]
    assert s.lengthOfLIS(nums) == 1
    nums = [0,1,0,3,2,3]
    assert s.lengthOfLIS(nums) == 4
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    assert s.lengthOfLIS(nums) == 4