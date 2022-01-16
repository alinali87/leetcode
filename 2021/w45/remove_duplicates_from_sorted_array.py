class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums):
            if nums[i] <= nums[i - 1]:
                s = i + 1
                if s >= len(nums):
                    return i
                elif nums[s] > nums[i - 1]:
                    nums[i] = nums[s]
                    i += 1
                else:
                    while s < len(nums) and nums[s] <= nums[i - 1]:
                        s += 1
                        if s >= len(nums):
                            return i
                        elif nums[s] > nums[i - 1]:
                            nums[i] = nums[s]
                            i += 1
                            if i >= len(nums):
                                return len(nums)
            else:
                i += 1
        return i
