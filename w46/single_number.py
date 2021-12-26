class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = {}
        for i in range(len(nums)):
            counts[nums[i]] = counts.get(nums[i], 0) + 1
        for num, count in counts.items():
            if count == 1:
                return num
