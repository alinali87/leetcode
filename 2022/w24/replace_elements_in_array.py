from typing import List


class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        # nums = [1, 2, 4, 6], operations = [[1, 3], [4, 7], [6, 1]]
        # [3, 2, 7, 1]
        d = {}  # k - num, v - idx
        for i, num in enumerate(nums):
            d[num] = i
        for old_el, new_el in operations:
            idx = d[old_el]
            nums[idx] = new_el
            del d[old_el]
            d[new_el] = idx
        return nums
