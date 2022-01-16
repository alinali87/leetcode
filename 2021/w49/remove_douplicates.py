from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        i = 0
        d = 1
        while i < len(nums) - 1:
            if nums[i + 1] > nums[i]:
                i += 1
            else:
                d = max(i + 1, d)
                while nums[d] <= nums[i]:
                    if d == len(nums) - 1:
                        return i + 1
                    d += 1
                nums[i + 1] = nums[d]
                i += 1
        # if nums[i + 1] > nums[i]:
        #     i += 1
        return i + 1


arr = [0,0,1,1,2,2,2,3,4]
s = Solution()
k = s.removeDuplicates(arr)
