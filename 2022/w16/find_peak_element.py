from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        left = 0
        right = len(nums) - 1
        if nums[left] > nums[left + 1]:
            return left
        if nums[right] > nums[right - 1]:
            return right
        while left <= right:
            mid = (left + right) // 2
            if nums[mid + 1] < nums[mid] and nums[mid - 1] < nums[mid]:
                return mid
            if nums[mid + 1] > nums[mid]:
                left = mid
            else:
                right = mid


s = Solution()
nums = [1,2,1,3,5,6,4]
a = s.findPeakElement(nums)
print(a)



