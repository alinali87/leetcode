from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        if nums[left] != val:
            left += 1
        else:
            other = nums[right]
            right -= 1
            while other == val:
                other = nums[right]
                right -= 1
            if right < left:
                return left

nums = [4,5]
solution = Solution()
ans = solution.removeElement(nums, 4)
print(ans)
print(nums)

