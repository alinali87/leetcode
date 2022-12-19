from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        m = len(l)
        ans = [True] * m
        for i in range(m):
            arr = sorted(nums[l[i]:r[i] + 1])
            d = arr[1] - arr[0]
            for k in range(2, len(arr)):
                if arr[k] - arr[k - 1] != d:
                    ans[i] = False
                    break
        return ans
