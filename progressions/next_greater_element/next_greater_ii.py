from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [None] * length
        ans[-1] = -1
        nums += nums
        stack = [nums[-1]]
        for i in range(len(nums) - 1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if stack:
                ans[i % length] = stack[-1]
            else:
                ans[i % length] = -1
            stack.append(nums[i])
        return ans
