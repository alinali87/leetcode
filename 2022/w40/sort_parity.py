from typing import List
from utils.utils import test


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        def is_odd(num):
            if num % 2 != 0:
                return True
            return False

        n = len(nums)
        if n < 2:
            return nums
        rpos = 0  # read pos, moves left to right
        nopos = n - 1  # non-odd pos, moves right to left
        while nopos > -1 and is_odd(nums[nopos]):
            nopos -= 1
        while rpos < nopos:
            if is_odd(nums[rpos]):
                # swap
                nums[rpos], nums[nopos] = nums[nopos], nums[rpos]
                rpos += 1
                while nopos > rpos and is_odd(nums[nopos]):
                    nopos -= 1
            else:
                rpos += 1
        return nums


nums = [1,3,0,5,2]
sol = Solution()
test(sol.sortArrayByParity(nums), [0,2,1,3,5])