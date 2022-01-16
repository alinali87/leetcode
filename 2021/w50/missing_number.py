class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                return nums[i] - 1
        if nums[0] == 0:
            return len(nums)
        return 0