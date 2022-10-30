from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {nums2[-1]: -1}
        stack = [nums2[-1]]
        for i in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if stack:
                d[nums2[i]] = stack[-1]
            else:
                d[nums2[i]] = -1
            stack.append(nums2[i])
        return [d[n] for n in nums1]
