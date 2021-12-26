class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if nums[0] == 1:
            counter = 1
        else:
            counter = 0
        max_seq = 0
        for i in range(1, len(nums)):
            if nums[i] == 0:
                max_seq = max(max_seq, counter)
                counter = 0
            else:
                counter += 1
        max_seq = max(max_seq, counter)
        return max_seq
