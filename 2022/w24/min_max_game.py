from typing import List


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while True:
            if len(nums) == 1:
                return nums[0]
            new_nums = []
            for i in range(len(nums) // 2):
                if i % 2 == 0:
                    new_nums.append(min(nums[2 * i], nums[2 * i + 1]))
                else:
                    new_nums.append(max(nums[2 * i], nums[2 * i + 1]))
            nums = new_nums
