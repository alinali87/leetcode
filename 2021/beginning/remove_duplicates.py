class Solution:
    def removeDuplicates(self, nums: list) -> int:
        i = 1
        limit = len(nums)
        while i < limit:
            if nums[i] == nums[i-1]:
                limit -= 1
                k = i
                while k < len(nums) - 1:
                    nums[k] = nums[k + 1]
            else:
                i += 1
        return limit


