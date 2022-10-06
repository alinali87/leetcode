# TL
from typing import List
from utils.utils import test


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 10, 9, 2, 5, 7, 101
        # 10 --> l=1
        # 9 --> None, l=1
        # 2 --> None, l=1
        # 5 --> 2, l=2
        # 7 --> 5, l=3, 2, l=2 --> l=3
        # 101 --> 7, l=4, 5, l=3, 2, l=2, 9, l=2, 10, l=2 --> 4
        lis = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis[i] = max(lis[j] + 1, lis[i])
        # will I reach the end?
        # is there risk of IndexError?
        return max(lis)


sol = Solution()
nums = [1,3,6,7,9,4,10,5,6]
test(sol.lengthOfLIS(nums), 6)
